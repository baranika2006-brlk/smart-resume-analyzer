// Resume Upload & Analysis Trigger Logic

let selectedFile = null;
let availableRoles = [];

document.addEventListener("DOMContentLoaded", () => {
    loadJobRolesDropdown();

    // Drag and Drop Zone Initialization
    const dropzone = document.getElementById("resume-dropzone");
    const fileInput = document.getElementById("resume-file-input");

    if (dropzone && fileInput) {
        dropzone.addEventListener("click", () => fileInput.click());

        dropzone.addEventListener("dragover", (e) => {
            e.preventDefault();
            dropzone.classList.add("dragover");
        });

        dropzone.addEventListener("dragleave", () => {
            dropzone.classList.remove("dragover");
        });

        dropzone.addEventListener("drop", (e) => {
            e.preventDefault();
            dropzone.classList.remove("dragover");
            if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
                handleFileSelect(e.dataTransfer.files[0]);
            }
        });

        fileInput.addEventListener("change", (e) => {
            if (e.target.files && e.target.files.length > 0) {
                handleFileSelect(e.target.files[0]);
            }
        });
    }

    // Role Dropdown Change
    const roleSelect = document.getElementById("target-role-select");
    if (roleSelect) {
        roleSelect.addEventListener("change", (e) => {
            const roleId = e.target.value;
            const chosen = availableRoles.find(r => r.role_id === roleId || r.id === roleId);
            if (chosen) {
                setSelectedJobRole(chosen);
            }
        });
    }

    // Upload Form Submit
    const uploadForm = document.getElementById("upload-form");
    if (uploadForm) {
        uploadForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            
            const roleSelectEl = document.getElementById("target-role-select");
            let roleId = roleSelectEl ? roleSelectEl.value : "";

            if (!roleId) {
                const saved = getSelectedJobRole();
                if (saved) roleId = saved.role_id || saved.id;
            }

            if (!roleId && availableRoles.length > 0) {
                roleId = availableRoles[0].role_id;
            }

            if (!selectedFile) {
                showToast("Please select or drag & drop a PDF or DOCX resume file.", "error");
                return;
            }

            await submitResumeAnalysis(selectedFile, roleId);
        });
    }
});

async function loadJobRolesDropdown() {
    const roleSelect = document.getElementById("target-role-select");
    if (!roleSelect) return;

    try {
        const response = await fetch(`${API_BASE_URL}/job-roles`);
        const resData = await response.json();

        if (response.ok && resData.success) {
            availableRoles = resData.job_roles || [];
            const activeRole = getSelectedJobRole();
            const activeId = activeRole ? (activeRole.role_id || activeRole.id) : "";

            roleSelect.innerHTML = availableRoles.map(r => {
                const isSel = (r.role_id === activeId || r.id === activeId);
                return `<option value="${r.role_id}" ${isSel ? 'selected' : ''}>${r.title} (${r.category || 'Tech'})</option>`;
            }).join("");

            if (!activeRole && availableRoles.length > 0) {
                setSelectedJobRole(availableRoles[0]);
            }
        } else {
            roleSelect.innerHTML = `<option value="python-developer">Python Developer</option>`;
        }
    } catch (e) {
        console.warn("Could not fetch roles from backend, using fallback:", e);
        roleSelect.innerHTML = `
            <option value="python-developer">Python Developer</option>
            <option value="data-analyst">Data Analyst</option>
            <option value="ai-engineer">AI Engineer</option>
            <option value="cybersecurity-analyst">Cybersecurity Analyst</option>
        `;
    }
}

function handleFileSelect(file) {
    const ext = file.name.split('.').pop().toLowerCase();
    if (ext !== 'pdf' && ext !== 'docx' && ext !== 'txt') {
        showToast("Invalid file format. Only PDF, DOCX, and TXT files are supported.", "error");
        return;
    }

    if (file.size > 5 * 1024 * 1024) {
        showToast("File size exceeds 5 MB limit. Please select a smaller document.", "error");
        return;
    }

    selectedFile = file;

    const filePreview = document.getElementById("file-preview");
    if (filePreview) {
        const sizeKB = (file.size / 1024).toFixed(1);
        filePreview.style.display = "block";
        filePreview.innerHTML = `
            <div style="background: rgba(30, 41, 59, 0.9); border: 1px solid var(--accent-blue); padding: 16px 20px; border-radius: var(--radius-md); display:flex; justify-content:space-between; align-items:center;">
                <div style="display:flex; align-items:center; gap:14px;">
                    <div style="font-size:2rem;">📄</div>
                    <div>
                        <div style="font-weight:700; color:var(--text-primary);">${file.name}</div>
                        <div style="font-size:0.85rem; color:var(--text-secondary);">${ext.toUpperCase()} File • ${sizeKB} KB</div>
                    </div>
                </div>
                <button type="button" onclick="clearSelectedFile()" class="btn btn-secondary btn-sm" style="color:var(--accent-rose);">Remove</button>
            </div>
        `;
    }
}

function clearSelectedFile() {
    selectedFile = null;
    const fileInput = document.getElementById("resume-file-input");
    if (fileInput) fileInput.value = "";

    const filePreview = document.getElementById("file-preview");
    if (filePreview) {
        filePreview.style.display = "none";
        filePreview.innerHTML = "";
    }
}

async function submitResumeAnalysis(file, roleId) {
    const progressContainer = document.getElementById("analysis-progress");
    const submitBtn = document.getElementById("btn-analyze-submit");

    if (submitBtn) submitBtn.disabled = true;

    if (progressContainer) {
        progressContainer.style.display = "block";
        progressContainer.innerHTML = `
            <div class="card" style="text-align:center; padding:30px;">
                <div style="font-size:2.5rem; margin-bottom:12px;" class="spinning-loader">⚙️</div>
                <h3 style="margin-bottom:8px;">Analyzing Resume & Calculating Score...</h3>
                <p style="color:var(--text-secondary); font-size:0.9rem;">Extracting document text • Running NLP Skill Matching • Generating Weighted Score</p>
                <div style="width:100%; background:rgba(255,255,255,0.1); height:8px; border-radius:4px; margin-top:20px; overflow:hidden;">
                    <div id="progress-bar-inner" style="width:30%; height:100%; background:var(--gradient-primary); transition: width 0.5s;"></div>
                </div>
            </div>
        `;
    }

    const formData = new FormData();
    formData.append("resume_file", file);
    formData.append("role_id", roleId);

    const user = getSavedUser();
    if (user && user.id) {
        formData.append("user_id", user.id);
    }

    try {
        const progressBar = document.getElementById("progress-bar-inner");
        if (progressBar) progressBar.style.width = "65%";

        const response = await fetch(`${API_BASE_URL}/resume/analyze`, {
            method: "POST",
            credentials: "include",
            body: formData
        });

        if (progressBar) progressBar.style.width = "90%";

        const resData = await response.json();

        if (response.ok && resData.success) {
            if (progressBar) progressBar.style.width = "100%";
            
            // Save analysis result locally for instant score dashboard rendering
            localStorage.setItem("latest_analysis_result", JSON.stringify(resData));
            showToast("Resume analysis complete! Redirecting to Score & Skills...", "success");

            setTimeout(() => {
                window.location.href = "score.html";
            }, 600);
        } else {
            showToast(resData.message || "Failed to analyze resume.", "error");
            if (progressContainer) progressContainer.style.display = "none";
        }
    } catch (e) {
        console.error("Resume analysis network error:", e);
        showToast("Error connecting to server. Please verify the Flask backend is active on port 5000.", "error");
        if (progressContainer) progressContainer.style.display = "none";
    } finally {
        if (submitBtn) submitBtn.disabled = false;
    }
}
