// Job Role Selection with Live Search and Category Filter

let allRolesList = [];
let filteredRolesList = [];
let selectedRoleObj = getSelectedJobRole();
let currentCategory = "ALL";
let currentSearchQuery = "";

document.addEventListener("DOMContentLoaded", () => {
    fetchJobRoles();

    const proceedBtn = document.getElementById("btn-proceed-upload");
    if (proceedBtn) {
        proceedBtn.addEventListener("click", () => {
            if (!selectedRoleObj) {
                showToast("Please select a target job role before proceeding.", "error");
                return;
            }
            window.location.href = "upload.html";
        });
    }

    // Search bar event listener
    const searchInput = document.getElementById("role-search-input");
    if (searchInput) {
        searchInput.addEventListener("input", (e) => {
            currentSearchQuery = e.target.value.toLowerCase().trim();
            filterAndRenderRoles();
        });
    }

    // Category button filters
    const filterBtns = document.querySelectorAll(".category-tab-btn");
    filterBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            filterBtns.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            currentCategory = btn.getAttribute("data-category") || "ALL";
            filterAndRenderRoles();
        });
    });
});

async function fetchJobRoles() {
    const rolesContainer = document.getElementById("job-roles-grid");
    if (!rolesContainer) return;

    rolesContainer.innerHTML = `
        <div style="grid-column: 1 / -1; text-align:center; padding: 40px; color:var(--text-secondary);">
            ⏳ Loading available target job roles from MongoDB...
        </div>
    `;

    try {
        const response = await fetch(`${API_BASE_URL}/job-roles`);
        const resData = await response.json();

        if (response.ok && resData.success) {
            allRolesList = resData.job_roles || [];
            filterAndRenderRoles();
        } else {
            rolesContainer.innerHTML = `<div style="color:var(--accent-rose); grid-column:1/-1; text-align:center;">Failed to load job roles from database.</div>`;
        }
    } catch (e) {
        console.error(e);
        rolesContainer.innerHTML = `
            <div style="grid-column: 1 / -1; text-align:center; padding: 40px; color:var(--accent-rose);">
                ❌ Unable to connect to backend server. Please verify the Flask backend is running on port 5000.
            </div>
        `;
    }
}

function filterAndRenderRoles() {
    filteredRolesList = allRolesList.filter(role => {
        // Category check
        const cat = (role.category || "").toLowerCase();
        let matchesCat = true;

        if (currentCategory === "Technology") {
            matchesCat = cat.includes("tech") || cat.includes("soft") || cat.includes("web") || cat.includes("frontend") || cat.includes("backend");
        } else if (currentCategory === "Security") {
            matchesCat = cat.includes("sec") || role.title.toLowerCase().includes("security") || role.title.toLowerCase().includes("hacker") || role.title.toLowerCase().includes("forensic");
        } else if (currentCategory === "AI & Data") {
            matchesCat = cat.includes("ai") || cat.includes("data") || role.title.toLowerCase().includes("ai") || role.title.toLowerCase().includes("machine learning") || role.title.toLowerCase().includes("data") || role.title.toLowerCase().includes("rpa");
        } else if (currentCategory === "Cloud & DevOps") {
            matchesCat = cat.includes("cloud") || cat.includes("devops") || role.title.toLowerCase().includes("cloud") || role.title.toLowerCase().includes("devops") || role.title.toLowerCase().includes("sre");
        } else if (currentCategory === "Mobile") {
            matchesCat = cat.includes("mob") || role.title.toLowerCase().includes("app") || role.title.toLowerCase().includes("android") || role.title.toLowerCase().includes("ios");
        } else if (currentCategory === "Management") {
            matchesCat = cat.includes("manage") || cat.includes("consult") || cat.includes("analyst") || role.title.toLowerCase().includes("manager") || role.title.toLowerCase().includes("scrum");
        }

        // Search query check
        let matchesSearch = true;
        if (currentSearchQuery) {
            const inTitle = role.title.toLowerCase().includes(currentSearchQuery);
            const inDesc = (role.description || "").toLowerCase().includes(currentSearchQuery);
            const inSkills = (role.required_skills || []).some(s => s.toLowerCase().includes(currentSearchQuery));
            matchesSearch = inTitle || inDesc || inSkills;
        }

        return matchesCat && matchesSearch;
    });

    renderJobRoleCards(filteredRolesList);
}

function renderJobRoleCards(roles) {
    const rolesContainer = document.getElementById("job-roles-grid");
    if (!rolesContainer) return;

    if (!roles || roles.length === 0) {
        rolesContainer.innerHTML = `
            <div style="grid-column: 1/-1; text-align:center; padding: 40px; color:var(--text-secondary);">
                <div style="font-size:2.5rem; margin-bottom:10px;">🔍</div>
                <h3>No matching job roles found</h3>
                <p style="margin-top:6px;">Try clearing your search query or selecting "All Roles".</p>
            </div>
        `;
        return;
    }

    rolesContainer.innerHTML = roles.map(role => {
        const isSelected = selectedRoleObj && (selectedRoleObj.role_id === role.role_id || selectedRoleObj.id === role.id);
        const skillPills = (role.required_skills || []).slice(0, 6).map(s => 
            `<span class="skill-badge skill-req">${s}</span>`
        ).join("");

        return `
            <div class="role-card ${isSelected ? 'selected' : ''}" onclick="selectRoleCard('${role.role_id}')">
                <div>
                    <div style="font-size: 0.8rem; color: var(--accent-blue); text-transform: uppercase; font-weight: 700; margin-bottom: 6px;">
                        ${role.category || 'Technology'}
                    </div>
                    <h3 style="font-size: 1.3rem; margin-bottom: 10px;">${role.title}</h3>
                    <p style="color: var(--text-secondary); font-size: 0.88rem; margin-bottom: 16px; min-height: 44px; line-height:1.5;">
                        ${role.description}
                    </p>
                    <div style="margin-bottom: 16px;">
                        <div style="font-size: 0.78rem; font-weight:700; color: var(--text-muted); margin-bottom: 6px; letter-spacing:0.5px;">REQUIRED SKILLS:</div>
                        <div>${skillPills} ${role.required_skills.length > 6 ? `<span style="font-size:0.75rem; color:var(--text-muted);">+${role.required_skills.length - 6} more</span>` : ''}</div>
                    </div>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--border-color); padding-top:14px; margin-top:10px;">
                    <span style="font-size:0.8rem; color:var(--text-muted);">Level: ${role.experience_level || 'Entry / Mid'}</span>
                    <button class="btn btn-sm ${isSelected ? 'btn-primary' : 'btn-secondary'}">
                        ${isSelected ? 'Selected' : 'Select Role'}
                    </button>
                </div>
            </div>
        `;
    }).join("");

    updateSelectedRoleNotice();
}

function selectRoleCard(roleId) {
    const role = allRolesList.find(r => r.role_id === roleId || r.id === roleId);
    if (role) {
        selectedRoleObj = role;
        setSelectedJobRole(role);
        renderJobRoleCards(filteredRolesList);
        showToast(`Selected target role: ${role.title}`, "success");
    }
}

function updateSelectedRoleNotice() {
    const notice = document.getElementById("selected-role-notice");
    if (!notice) return;

    if (selectedRoleObj) {
        notice.innerHTML = `
            <div style="background: rgba(56, 189, 248, 0.1); border:1px solid var(--border-glow); padding:16px 24px; border-radius: var(--radius-md); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
                <div>
                    <span style="color:var(--text-secondary); font-size:0.9rem;">Currently Selected Target Role:</span>
                    <strong style="color:var(--accent-blue); margin-left: 8px; font-size:1.1rem;">${selectedRoleObj.title}</strong>
                </div>
                <a href="upload.html" class="btn btn-primary btn-sm">Proceed to Upload Resume →</a>
            </div>
        `;
    } else {
        notice.innerHTML = ``;
    }
}
