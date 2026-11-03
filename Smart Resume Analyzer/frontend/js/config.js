// Dynamic API Configuration & Global Utilities
function getApiBaseUrl() {
    if (typeof window !== "undefined" && window.location) {
        const protocol = window.location.protocol.startsWith("http") ? window.location.protocol : "http:";
        const hostname = window.location.hostname || "127.0.0.1";
        // If frontend is accessed directly via Flask port (5000)
        if (window.location.port === "5000") {
            return `${protocol}//${hostname}:5000/api`;
        }
        // If frontend is accessed via any other port (5500, etc.) or file://
        return `${protocol}//${hostname}:5000/api`;
    }
    return "http://127.0.0.1:5000/api";
}
const API_BASE_URL = getApiBaseUrl();

// Toast Notification Helper
function showToast(message, type = "info") {
    let container = document.getElementById("toast-container");
    if (!container) {
        container = document.createElement("div");
        container.id = "toast-container";
        document.body.appendChild(container);
    }

    const toast = document.createElement("div");
    toast.className = `toast toast-${type}`;
    
    let icon = "ℹ️";
    if (type === "success") icon = "✅";
    if (type === "error") icon = "⚠️";

    toast.innerHTML = `<span>${icon}</span> <div>${message}</div>`;
    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = "0";
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

// User Session Storage Helpers
function getSavedUser() {
    try {
        const data = localStorage.getItem("smart_resume_user");
        return data ? JSON.parse(data) : null;
    } catch (e) {
        return null;
    }
}

function saveUserSession(user) {
    localStorage.setItem("smart_resume_user", JSON.stringify(user));
}

function clearUserSession() {
    localStorage.removeItem("smart_resume_user");
    localStorage.removeItem("selected_job_role");
    localStorage.removeItem("latest_analysis_result");
}

function getSelectedJobRole() {
    try {
        const data = localStorage.getItem("selected_job_role");
        return data ? JSON.parse(data) : null;
    } catch (e) {
        return null;
    }
}

function setSelectedJobRole(role) {
    localStorage.setItem("selected_job_role", JSON.stringify(role));
}

// Update Top Navigation Bar dynamically based on logged in status
function renderNavigation() {
    const navLinksContainer = document.getElementById("nav-user-area");
    if (!navLinksContainer) return;

    const user = getSavedUser();
    if (user) {
        const isAdmin = user.role === "admin";
        navLinksContainer.innerHTML = `
            <div class="user-badge">
                <div class="user-avatar">${user.name.charAt(0).toUpperCase()}</div>
                <span style="font-size:0.9rem; font-weight:600; color:var(--text-primary);">${user.name}</span>
            </div>
            ${isAdmin ? `<a href="admin.html" class="nav-link" style="color:var(--accent-primary);">⚙️ Admin</a>` : ''}
            <button onclick="handleGlobalLogout()" class="btn btn-secondary btn-sm">Logout</button>
        `;
    } else {
        navLinksContainer.innerHTML = `
            <a href="login.html" class="nav-link">Login</a>
            <a href="register.html" class="btn btn-primary btn-sm">Get Started</a>
        `;
    }
}

async function handleGlobalLogout() {
    try {
        await fetch(`${API_BASE_URL}/auth/logout`, { method: "POST" });
    } catch (e) {}
    clearUserSession();
    showToast("Logged out successfully.", "info");
    setTimeout(() => {
        window.location.href = "index.html";
    }, 800);
}

document.addEventListener("DOMContentLoaded", renderNavigation);
