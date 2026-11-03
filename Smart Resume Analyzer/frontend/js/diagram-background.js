/**
 * Smart Resume Analyzer - Single Elegant Design Engine & Architecture Pipeline
 */

(function () {
    // ── 1. Clean Single Theme Setup ──────────────────────────────────────────
    function applySingleTheme() {
        document.documentElement.setAttribute("data-theme", "violet");
        localStorage.setItem("smart_resume_theme", "violet");
        
        // Remove any old theme switcher if present
        const oldSwitcher = document.querySelector(".theme-switcher-wrap");
        if (oldSwitcher) oldSwitcher.remove();
        
        const oldSlot = document.getElementById("theme-switcher-slot");
        if (oldSlot) oldSlot.remove();
    }

    // ── 2. Clean Background Backdrop (Static & Clean) ────────────────────────
    function injectBackground() {
        // Clean up any old canvas/grid elements
        const oldCanvas = document.getElementById("bg-diagram-canvas-container");
        if (oldCanvas) oldCanvas.remove();

        if (document.getElementById("bg-elegant-backdrop")) return;
        const backdrop = document.createElement("div");
        backdrop.id = "bg-elegant-backdrop";
        backdrop.className = "bg-elegant-backdrop";
        document.body.prepend(backdrop);
    }

    // ── 3. Interactive Architecture Pipeline Diagram Controller ───────────────
    const PIPELINE_DATA = [
        {
            title: "Multi-Format Resume Ingestion",
            badge: "STAGE 01",
            icon: "📄",
            desc: "Parses PDF and DOCX binary streams using PyPDF2 & docx2txt, sanitizing raw text and preserving structural section boundaries.",
            stats: [
                { val: "PDF / DOCX", label: "Accepted Formats" },
                { val: "5 MB", label: "Max File Size" },
                { val: "< 120ms", label: "Parsing Latency" }
            ]
        },
        {
            title: "NLP Tokenization & Skill Extraction",
            badge: "STAGE 02",
            icon: "🧠",
            desc: "Performs lemmatization, regex entity pattern extraction, and keyword vector tokenization across technical frameworks, databases, cloud, and soft skills.",
            stats: [
                { val: "150+", label: "NLP Skill Vectors" },
                { val: "100%", label: "Zero Hallucination" },
                { val: "Auto-Clean", label: "Stopword Filter" }
            ]
        },
        {
            title: "Semantic Role Benchmark Matching",
            badge: "STAGE 03",
            icon: "🎯",
            desc: "Compares extracted candidate skill tokens directly against the benchmark curriculum of 30+ curated industry roles from MongoDB.",
            stats: [
                { val: "30+ Roles", label: "Active Benchmarks" },
                { val: "Dual-Match", label: "Tech + Soft Split" },
                { val: "Categorized", label: "Domain Mapping" }
            ]
        },
        {
            title: "Weighted ATS Scoring Engine",
            badge: "STAGE 04",
            icon: "⚖️",
            desc: "Calculates normalized composite scores out of 100 with weighted metrics: 50% Core Tech, 15% Soft Skills, 20% Experience, 15% Education & AST Structure.",
            stats: [
                { val: "100 Pts", label: "Normalized Base" },
                { val: "A+ to D", label: "Letter Grade System" },
                { val: "Real-Time", label: "Instant Execution" }
            ]
        },
        {
            title: "Roadmap & Gap Recommendations",
            badge: "STAGE 05",
            icon: "🚀",
            desc: "Generates tailored learning actions, missing prerequisite courses, actionable project ideas, and industry certification targets.",
            stats: [
                { val: "Direct Gap", label: "Missing Skills" },
                { val: "Curated", label: "Course Roadmaps" },
                { val: "Resume Tips", label: "ATS Formatting" }
            ]
        }
    ];

    window.activatePipelineStep = function (index) {
        const step = PIPELINE_DATA[index];
        if (!step) return;

        document.querySelectorAll(".pipeline-step-node").forEach((el, idx) => {
            if (idx === index) el.classList.add("active");
            else el.classList.remove("active");
        });

        const panel = document.getElementById("pipeline-detail-panel");
        if (panel) {
            panel.innerHTML = `
                <div style="flex: 1; min-width: 260px;">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                        <span style="font-size: 1.6rem;">${step.icon}</span>
                        <div>
                            <span class="node-badge">${step.badge}</span>
                            <h3 style="font-size: 1.25rem;">${step.title}</h3>
                        </div>
                    </div>
                    <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.6;">${step.desc}</p>
                </div>
                <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                    ${step.stats.map(s => `
                        <div class="diagram-stat-pill">
                            <span class="diagram-stat-val">${s.val}</span>
                            <span class="diagram-stat-label">${s.label}</span>
                        </div>
                    `).join('')}
                </div>
            `;
        }
    };

    // ── 4. Lifecycle Initialization ───────────────────────────────────────────
    document.addEventListener("DOMContentLoaded", () => {
        applySingleTheme();
        injectBackground();
    });

})();
