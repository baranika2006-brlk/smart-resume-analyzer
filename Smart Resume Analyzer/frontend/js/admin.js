// Admin Panel Logic

document.addEventListener("DOMContentLoaded", () => {
    loadAdminStats();
    loadAdminUsers();
    loadAdminJobRoles();
    loadAdminResumes();

    // Add Job Role Form Listener
    const addRoleForm = document.getElementById("admin-add-role-form");
    if (addRoleForm) {
        addRoleForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const title = document.getElementById("role-title").value.trim();
            const category = document.getElementById("role-category").value.trim();
            const desc = document.getElementById("role-desc").value.trim();
            const reqSkillsStr = document.getElementById("role-req-skills").value.trim();
            const softSkillsStr = document.getElementById("role-soft-skills").value.trim();
            const certsStr = document.getElementById("role-certs").value.trim();
            const projectsStr = document.getElementById("role-projects").value.trim();

            if (!title || !reqSkillsStr) {
                showToast("Role title and required skills are mandatory.", "error");
                return;
            }

            const payload = {
                title: title,
                category: category || "Technology",
                description: desc,
                required_skills: reqSkillsStr.split(",").map(s => s.trim()).filter(Boolean),
                soft_skills: softSkillsStr.split(",").map(s => s.trim()).filter(Boolean),
                recommended_certifications: certsStr.split(",").map(s => s.trim()).filter(Boolean),
                suggested_projects: projectsStr.split(",").map(s => s.trim()).filter(Boolean)
            };

            try {
                const response = await fetch(`${API_BASE_URL}/admin/job-roles`, {
                    method: "POST",
                    credentials: "include",
                    headers: { 
                        "Content-Type": "application/json",
                        "X-Admin-Access": "AdminSecret2026"
                    },
                    body: JSON.stringify(payload)
                });
                const resData = await response.json();

                if (response.ok && resData.success) {
                    showToast(resData.message || "Job role saved successfully!", "success");
                    addRoleForm.reset();
                    loadAdminJobRoles();
                    loadAdminStats();
                } else {
                    showToast(resData.message || "Failed to save job role.", "error");
                }
            } catch (err) {
                console.error(err);
                showToast("Error saving job role.", "error");
            }
        });
    }
});

async function loadAdminStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/admin/stats`, {
            credentials: "include",
            headers: { "X-Admin-Access": "AdminSecret2026" }
        });
        const resData = await response.json();

        if (response.ok && resData.success) {
            const stats = resData.stats;
            document.getElementById("adm-stat-users").textContent = stats.total_users || 0;
            document.getElementById("adm-stat-roles").textContent = stats.total_job_roles || 0;
            document.getElementById("adm-stat-resumes").textContent = stats.total_resumes || 0;
            document.getElementById("adm-stat-analyses").textContent = stats.total_analyses || 0;
            document.getElementById("adm-stat-score").textContent = `${stats.avg_platform_score || 0}/100`;
        }
    } catch (e) {
        console.error("Admin stats error:", e);
    }
}

async function loadAdminUsers() {
    const tableBody = document.getElementById("adm-users-table-body");
    if (!tableBody) return;

    try {
        const response = await fetch(`${API_BASE_URL}/admin/users`, {
            credentials: "include",
            headers: { "X-Admin-Access": "AdminSecret2026" }
        });
        const resData = await response.json();

        if (response.ok && resData.success) {
            const users = resData.users || [];
            if (users.length === 0) {
                tableBody.innerHTML = `<tr><td colspan="5" style="text-align:center; color:var(--text-muted);">No users found.</td></tr>`;
                return;
            }

            tableBody.innerHTML = users.map(u => `
                <tr>
                    <td><strong>${u.name}</strong></td>
                    <td>${u.email}</td>
                    <td><span class="skill-badge ${u.role === 'admin' ? 'skill-req' : 'skill-matched'}">${u.role}</span></td>
                    <td>${u.created_at ? new Date(u.created_at).toLocaleDateString() : 'N/A'}</td>
                    <td>
                        ${u.role !== 'admin' ? `<button onclick="deleteUserRecord('${u.id}')" class="btn btn-danger btn-sm">Delete</button>` : '<span style="color:var(--text-muted); font-size:0.8rem;">Protected</span>'}
                    </td>
                </tr>
            `).join("");
        }
    } catch (e) {
        console.error("Admin users error:", e);
    }
}

async function deleteUserRecord(userId) {
    if (!confirm("Are you sure you want to delete this user?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/admin/users/${userId}`, {
            method: "DELETE",
            credentials: "include",
            headers: { "X-Admin-Access": "AdminSecret2026" }
        });
        const resData = await response.json();

        if (response.ok && resData.success) {
            showToast("User account deleted.", "success");
            loadAdminUsers();
            loadAdminStats();
        } else {
            showToast(resData.message || "Failed to delete user.", "error");
        }
    } catch (e) {
        console.error(e);
        showToast("Error deleting user.", "error");
    }
}

async function loadAdminJobRoles() {
    const listContainer = document.getElementById("adm-roles-list");
    if (!listContainer) return;

    try {
        const response = await fetch(`${API_BASE_URL}/job-roles`, {
            credentials: "include"
        });
        const resData = await response.json();

        if (response.ok && resData.success) {
            const roles = resData.job_roles || [];
            listContainer.innerHTML = roles.map(r => `
                <div style="background:rgba(15,23,42,0.6); border:1px solid var(--border-color); padding:16px 20px; border-radius:var(--radius-md); margin-bottom:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <strong style="font-size:1.05rem; color:var(--text-primary);">${r.title}</strong>
                        <span style="font-size:0.8rem; color:var(--accent-blue); margin-left:10px;">(${r.category})</span>
                        <div style="margin-top:6px;">
                            ${(r.required_skills || []).slice(0, 5).map(s => `<span class="skill-badge skill-req">${s}</span>`).join("")}
                        </div>
                    </div>
                    <button onclick="deleteJobRoleRecord('${r.role_id || r.id}')" class="btn btn-danger btn-sm">Delete</button>
                </div>
            `).join("");
        }
    } catch (e) {
        console.error("Admin job roles error:", e);
    }
}

async function deleteJobRoleRecord(roleId) {
    if (!confirm("Are you sure you want to delete this job role?")) return;

    try {
        const response = await fetch(`${API_BASE_URL}/admin/job-roles/${roleId}`, {
            method: "DELETE",
            credentials: "include",
            headers: { "X-Admin-Access": "AdminSecret2026" }
        });
        const resData = await response.json();

        if (response.ok && resData.success) {
            showToast("Job role deleted.", "success");
            loadAdminJobRoles();
            loadAdminStats();
        } else {
            showToast(resData.message || "Failed to delete job role.", "error");
        }
    } catch (e) {
        showToast("Error deleting job role.", "error");
    }
}

async function loadAdminResumes() {
    const tableBody = document.getElementById("adm-resumes-table-body");
    if (!tableBody) return;

    try {
        const response = await fetch(`${API_BASE_URL}/admin/resumes`, {
            credentials: "include",
            headers: { "X-Admin-Access": "AdminSecret2026" }
        });
        const resData = await response.json();

        if (response.ok && resData.success) {
            const resumes = resData.resumes || [];
            if (resumes.length === 0) {
                tableBody.innerHTML = `<tr><td colspan="4" style="text-align:center; color:var(--text-muted);">No uploaded resume records found.</td></tr>`;
                return;
            }

            tableBody.innerHTML = resumes.map(r => `
                <tr>
                    <td><strong>${r.filename}</strong></td>
                    <td>${r.file_size_kb} KB</td>
                    <td>${r.user_id}</td>
                    <td>${r.upload_date ? new Date(r.upload_date).toLocaleString() : 'N/A'}</td>
                </tr>
            `).join("");
        }
    } catch (e) {
        console.error("Admin resumes error:", e);
    }
}
