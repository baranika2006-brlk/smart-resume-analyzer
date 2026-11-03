// Dashboard – Score & Skills page

document.addEventListener("DOMContentLoaded", () => {
    loadDashboardData();
    loadAnalysisHistory();
});

function loadDashboardData() {
    const rawAnalysis = localStorage.getItem("latest_analysis_result");
    const dashContainer = document.getElementById("dashboard-main-content");
    const noDataNotice  = document.getElementById("dashboard-no-data");

    if (!rawAnalysis) {
        if (noDataNotice)  noDataNotice.style.display  = "block";
        if (dashContainer) dashContainer.style.display = "none";
        return;
    }

    try {
        const data = JSON.parse(rawAnalysis);
        if (noDataNotice)  noDataNotice.style.display  = "none";
        if (dashContainer) dashContainer.style.display = "block";
        renderScoreSection(data);
        renderSkillsSection(data);
    } catch (e) {
        console.error("Dashboard render error:", e);
    }
}

/* ── Score & Breakdown ─────────────────────────────────────── */
function renderScoreSection(data) {
    const scoreEl   = document.getElementById("dash-score-value");
    const gradeEl   = document.getElementById("dash-score-grade");
    const roleEl    = document.getElementById("dash-target-role");
    const matchEl   = document.getElementById("dash-skill-match-pct");
    const breakdown = data.score_breakdown || {};
    const score     = data.overall_score || 0;

    if (scoreEl)  scoreEl.textContent  = score;
    if (roleEl)   roleEl.textContent   = data.job_role ? data.job_role.title : "—";
    if (matchEl)  matchEl.textContent  = `${data.skill_match_percentage || 0}%`;

    // Grade badge with colour
    if (gradeEl) {
        const grade = data.grade || "N/A";
        const colours = {
            "A+": ["#10b981","rgba(16,185,129,0.15)"], "A": ["#10b981","rgba(16,185,129,0.15)"],
            "B":  ["#6366f1","rgba(99,102,241,0.15)"],
            "C":  ["#f59e0b","rgba(245,158,11,0.15)"],
            "D":  ["#fb7185","rgba(251,113,133,0.15)"],
            "F":  ["#ef4444","rgba(239,68,68,0.15)"]
        };
        const key   = Object.keys(colours).find(k => grade.startsWith(k)) || "B";
        const [clr, bg] = colours[key];
        gradeEl.textContent = `Grade: ${grade}`;
        gradeEl.style.cssText = `background:${bg}; border:1px solid ${clr}40; color:${clr};
            display:inline-block; padding:6px 18px; border-radius:999px; font-size:0.9rem;
            font-weight:800; margin-top:10px; letter-spacing:0.5px;`;
    }

    const factors = [
        { label: "Skill Match",           key: "skill_match_score",    max: 40, colour: "var(--accent-cyan)" },
        { label: "Projects & Experience", key: "project_score",        max: 25, colour: "var(--accent-magenta)" },
        { label: "Education Relevance",   key: "education_score",      max: 15, colour: "var(--accent-emerald)" },
        { label: "Certifications",        key: "certifications_score", max: 10, colour: "var(--accent-amber)" },
        { label: "Resume Completeness",   key: "completeness_score",   max: 10, colour: "var(--accent-violet)" },
    ];

    const container = document.getElementById("dash-score-breakdown");
    if (container) {
        container.innerHTML = factors.map(f => {
            const val = breakdown[f.key] || 0;
            const pct = Math.min((val / f.max) * 100, 100);
            return `
            <div class="factor-row">
                <label>
                    <span>${f.label}</span>
                    <strong>${val} / ${f.max}</strong>
                </label>
                <div class="bar-track">
                    <div class="bar-fill" style="width:${pct}%; background:${f.colour};"></div>
                </div>
            </div>`;
        }).join("");
    }
}

/* ── Matched / Missing Skills ──────────────────────────────── */
function renderSkillsSection(data) {
    const matchedBox = document.getElementById("dash-matched-skills");
    const missingBox = document.getElementById("dash-missing-skills");

    const allMatched = [...(data.matched_skills || []), ...(data.matched_soft_skills || [])];
    const allMissing = [...(data.missing_skills || []), ...(data.missing_soft_skills || [])];

    if (matchedBox) {
        matchedBox.innerHTML = allMatched.length
            ? allMatched.map(s => `<span class="skill-badge skill-matched">✓ ${s}</span>`).join("")
            : `<span style="color:var(--text-muted); font-size:0.9rem;">No matching skills detected for this role.</span>`;
    }

    if (missingBox) {
        missingBox.innerHTML = allMissing.length
            ? allMissing.map(s => `<span class="skill-badge skill-missing">✕ ${s}</span>`).join("")
            : `<span style="color:var(--accent-emerald); font-size:0.9rem;">🎉 Perfect match — no missing skills!</span>`;
    }
}

/* ── Analysis History ──────────────────────────────────────── */
async function loadAnalysisHistory() {
    const tbody = document.getElementById("history-table-body");
    if (!tbody) return;

    const user   = getSavedUser();
    const userId = user ? user.id : "anonymous_guest";

    try {
        const res  = await fetch(`${API_BASE_URL}/dashboard/history?user_id=${userId}`, {
            credentials: "include"
        });
        const data = await res.json();

        if (res.ok && data.success) {
            const history = data.history || [];
            if (history.length === 0) {
                tbody.innerHTML = `<tr><td colspan="5" style="text-align:center; color:var(--text-muted); padding:20px;">No previous analysis records found.</td></tr>`;
                return;
            }
            tbody.innerHTML = history.map((item, idx) => {
                const dateStr = item.created_at ? new Date(item.created_at).toLocaleDateString() : "N/A";
                return `
                <tr>
                    <td>#${idx + 1}</td>
                    <td><strong>${item.job_role_title}</strong></td>
                    <td><span style="font-weight:700; color:var(--accent-blue);">${item.overall_score}/100</span></td>
                    <td>${item.skill_match_percentage}%</td>
                    <td>${dateStr}</td>
                </tr>`;
            }).join("");
        }
    } catch (e) {
        console.error("History fetch error:", e);
        tbody.innerHTML = `<tr><td colspan="5" style="text-align:center; color:var(--text-muted); padding:20px;">Could not load history — backend may be offline.</td></tr>`;
    }
}
