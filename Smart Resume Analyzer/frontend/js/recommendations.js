// Recommendations page – Certifications, Projects, Resume Tips

document.addEventListener("DOMContentLoaded", () => {
    const rawAnalysis = localStorage.getItem("latest_analysis_result");
    const mainEl = document.getElementById("rec-main-content");
    const noDataEl = document.getElementById("rec-no-data");

    if (!rawAnalysis) {
        if (noDataEl) noDataEl.style.display = "block";
        if (mainEl) mainEl.style.display = "none";
        return;
    }

    try {
        const data = JSON.parse(rawAnalysis);
        if (noDataEl) noDataEl.style.display = "none";
        if (mainEl) mainEl.style.display = "block";

        const sug = data.suggestions || {};
        renderCertifications(sug);
        renderProjects(sug);
        renderTips(sug);
    } catch (e) {
        console.error("Recommendations render error:", e);
    }
});

/* ── Certifications ─────────────────────────────────────────── */
function renderCertifications(sug) {
    const container = document.getElementById("rec-certs-list");
    if (!container) return;

    const certs = sug.recommended_certifications || [];

    if (certs.length === 0) {
        container.innerHTML = `
            <div style="text-align:center; padding:24px; color:var(--accent-emerald);">
                🎉 No additional certifications needed — your profile already looks strong for this role!
            </div>`;
        return;
    }

    container.innerHTML = certs.map((c, idx) => {
        const isObj = typeof c === "object" && c !== null;
        const name = isObj ? (c.certification || c.name || `Certification ${idx + 1}`) : String(c);
        const benefit = isObj ? (c.benefit || c.description || "") : "";

        return `
        <div class="rec-item">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:${benefit ? '6px' : '0'}">
                <span style="font-size:1.3rem;">🎓</span>
                <div class="rec-title" style="color:var(--accent-blue);">${name}</div>
            </div>
            ${benefit ? `<div class="rec-sub">${benefit}</div>` : ""}
        </div>`;
    }).join("");
}

/* ── Projects to Build ─────────────────────────────────────── */
function renderProjects(sug) {
    const container = document.getElementById("rec-projects-list");
    if (!container) return;

    const projs = sug.recommended_projects || [];

    if (projs.length === 0) {
        container.innerHTML = `
            <div style="text-align:center; padding:24px; color:var(--accent-emerald);">
                🎉 Your project portfolio is already strong for this role!
            </div>`;
        return;
    }

    container.innerHTML = projs.map((p, idx) => {
        const isObj = typeof p === "object" && p !== null;
        const title = isObj ? (p.title || p.name || `Project ${idx + 1}`) : String(p);
        const desc = isObj ? (p.description || p.desc || "") : "";

        return `
        <div class="rec-item">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:${desc ? '6px' : '0'}">
                <span style="font-size:1.3rem;">🛠️</span>
                <div class="rec-title" style="color:var(--accent-purple);">${title}</div>
            </div>
            ${desc ? `<div class="rec-sub">${desc}</div>` : ""}
        </div>`;
    }).join("");
}

/* ── Resume Formatting Tips ─────────────────────────────────── */
function renderTips(sug) {
    const container = document.getElementById("rec-tips-list");
    if (!container) return;

    const tips = sug.general_tips || [];

    if (tips.length === 0) {
        container.innerHTML = `
            <div style="text-align:center; padding:24px; color:var(--accent-emerald);">
                🎉 No critical formatting changes needed — your resume structure looks great!
            </div>`;
        return;
    }

    container.innerHTML = tips.map((tip, idx) => `
        <div class="tip-item">
            <div class="tip-num">${idx + 1}</div>
            <div style="font-size:0.92rem; color:var(--text-secondary); line-height:1.6;">${tip}</div>
        </div>`
    ).join("");
}
