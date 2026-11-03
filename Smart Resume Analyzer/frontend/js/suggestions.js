// Suggestions page – Missing skill tips + ATS keywords

document.addEventListener("DOMContentLoaded", () => {
    const rawAnalysis = localStorage.getItem("latest_analysis_result");
    const mainEl   = document.getElementById("sug-main-content");
    const noDataEl = document.getElementById("sug-no-data");

    if (!rawAnalysis) {
        if (noDataEl)  noDataEl.style.display  = "block";
        if (mainEl)    mainEl.style.display    = "none";
        return;
    }

    try {
        const data = JSON.parse(rawAnalysis);
        if (noDataEl)  noDataEl.style.display  = "none";
        if (mainEl)    mainEl.style.display    = "block";

        renderMissingSkillSuggestions(data.suggestions || {});
        renderATSKeywords(data.suggestions || {});
    } catch (e) {
        console.error("Suggestions render error:", e);
    }
});

/* ── Missing-skill learning tips ───────────────────────────── */
function renderMissingSkillSuggestions(sug) {
    const container = document.getElementById("sug-skills-list");
    if (!container) return;

    const items = sug.missing_skills_suggestions || [];

    if (items.length === 0) {
        container.innerHTML = `
            <div style="text-align:center; padding:30px; color:var(--accent-emerald);">
                <div style="font-size:2.5rem; margin-bottom:10px;">🎉</div>
                <strong>Great news!</strong> Your resume already covers all required skills for this role.
            </div>`;
        return;
    }

    container.innerHTML = items.map((item, idx) => {
        // Backend sends: {skill, recommendation, priority}
        const isObj        = typeof item === "object" && item !== null;
        const skill        = isObj ? (item.skill        || item.name   || `Skill ${idx + 1}`) : String(item);
        const recommendation = isObj ? (item.recommendation || item.how_to_learn || "")       : "";
        const priority     = isObj ? (item.priority     || "")                               : "";

        const priorityColour = priority === "High"
            ? ["#fb7185", "rgba(251,113,133,0.15)"]
            : ["#f59e0b", "rgba(245,158,11,0.15)"];

        return `
        <div class="sug-card">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:${recommendation ? '8px' : '0'}">
                <span style="background:${priorityColour[1]}; border:1px solid ${priorityColour[0]}40;
                             color:${priorityColour[0]}; border-radius:999px; padding:3px 12px; font-size:0.78rem;
                             font-weight:700; white-space:nowrap;">${priority || 'MISSING'}</span>
                <div class="sug-card-title" style="color:var(--text-primary);">${skill}</div>
            </div>
            ${recommendation ? `<div class="sug-card-sub"><strong style="color:var(--accent-blue);">How to learn:</strong> ${recommendation}</div>` : ""}
        </div>`;
    }).join("");
}

/* ── ATS Keywords ───────────────────────────────────────────── */
function renderATSKeywords(sug) {
    const container = document.getElementById("sug-keywords-wrap");
    if (!container) return;

    const keywords = sug.recommended_keywords || [];

    if (keywords.length === 0) {
        container.innerHTML = `<span style="color:var(--text-muted);">
            Your resume already contains the key ATS-relevant terms. No extra keywords needed.
        </span>`;
        return;
    }

    container.innerHTML = `
        <div style="margin-bottom:12px; color:var(--text-secondary); font-size:0.88rem;">
            Copy and naturally weave these <strong style="color:var(--text-primary);">${keywords.length} keywords</strong>
            into your resume's skills, summary, and experience sections:
        </div>
        <div style="display:flex; flex-wrap:wrap;">
            ${keywords.map(k => `<span class="ats-chip">${k}</span>`).join("")}
        </div>`;
}
