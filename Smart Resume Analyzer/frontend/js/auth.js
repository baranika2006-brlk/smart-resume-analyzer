// User Authentication Handling (Registration, Login)

document.addEventListener("DOMContentLoaded", () => {
    // 1. Register Form Handler
    const registerForm = document.getElementById("register-form");
    if (registerForm) {
        registerForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const name = document.getElementById("reg-name").value.trim();
            const email = document.getElementById("reg-email").value.trim();
            const password = document.getElementById("reg-password").value.trim();
            const confirmPassword = document.getElementById("reg-confirm").value.trim();

            if (!name || !email || !password) {
                showToast("Please fill in all required fields.", "error");
                return;
            }

            if (password !== confirmPassword) {
                showToast("Passwords do not match.", "error");
                return;
            }

            if (password.length < 6) {
                showToast("Password must be at least 6 characters.", "error");
                return;
            }

            const btn = registerForm.querySelector("button[type='submit']");
            const originalBtnText = btn.innerHTML;
            btn.disabled = true;
            btn.innerHTML = "Creating Account...";

            try {
                const response = await fetch(`${API_BASE_URL}/auth/register`, {
                    method: "POST",
                    credentials: "include",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ name, email, password })
                });
                const resData = await response.json();

                if (response.ok && resData.success) {
                    saveUserSession(resData.user);
                    showToast(resData.message || "Registration successful!", "success");
                    setTimeout(() => {
                        window.location.href = "job_role.html";
                    }, 1000);
                } else {
                    showToast(resData.message || "Registration failed.", "error");
                }
            } catch (err) {
                console.error(err);
                showToast("Failed to connect to backend server. Ensure Flask server is running.", "error");
            } finally {
                btn.disabled = false;
                btn.innerHTML = originalBtnText;
            }
        });
    }

    // 2. Login Form Handler
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const email = document.getElementById("login-email").value.trim();
            const password = document.getElementById("login-password").value.trim();

            if (!email || !password) {
                showToast("Please enter both email and password.", "error");
                return;
            }

            const btn = loginForm.querySelector("button[type='submit']");
            const originalBtnText = btn.innerHTML;
            btn.disabled = true;
            btn.innerHTML = "Signing in...";

            try {
                const response = await fetch(`${API_BASE_URL}/auth/login`, {
                    method: "POST",
                    credentials: "include",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ email, password })
                });
                const resData = await response.json();

                if (response.ok && resData.success) {
                    saveUserSession(resData.user);
                    showToast(resData.message || "Login successful!", "success");
                    setTimeout(() => {
                        if (resData.user.role === "admin") {
                            window.location.href = "admin.html";
                        } else {
                            window.location.href = "job_role.html";
                        }
                    }, 1000);
                } else {
                    showToast(resData.message || "Invalid credentials.", "error");
                }
            } catch (err) {
                console.error(err);
                showToast("Failed to connect to backend server.", "error");
            } finally {
                btn.disabled = false;
                btn.innerHTML = originalBtnText;
            }
        });
    }
});
