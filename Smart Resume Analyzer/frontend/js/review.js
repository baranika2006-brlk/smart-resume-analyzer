// Rating & Review Handling

let selectedStarRating = 5;

document.addEventListener("DOMContentLoaded", () => {
    initStarRatingSelector();
    fetchReviewsFeed();

    const reviewForm = document.getElementById("review-form");
    if (reviewForm) {
        reviewForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const comment = document.getElementById("review-comment").value.trim();
            const userNameInput = document.getElementById("review-username");
            const userName = userNameInput ? userNameInput.value.trim() : "";

            if (!comment) {
                showToast("Please enter a feedback comment.", "error");
                return;
            }

            const btn = reviewForm.querySelector("button[type='submit']");
            btn.disabled = true;

            try {
                const user = getSavedUser();
                const response = await fetch(`${API_BASE_URL}/reviews`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        rating: selectedStarRating,
                        comment: comment,
                        user_name: userName || (user ? user.name : "Anonymous")
                    })
                });

                const resData = await response.json();
                if (response.ok && resData.success) {
                    showToast(resData.message || "Thank you for your feedback!", "success");
                    document.getElementById("review-comment").value = "";
                    fetchReviewsFeed();
                } else {
                    showToast(resData.message || "Failed to submit review.", "error");
                }
            } catch (err) {
                console.error(err);
                showToast("Error connecting to server.", "error");
            } finally {
                btn.disabled = false;
            }
        });
    }
});

function initStarRatingSelector() {
    const stars = document.querySelectorAll(".star-rating-input span");
    stars.forEach((star, index) => {
        star.addEventListener("click", () => {
            selectedStarRating = index + 1;
            updateStarDisplay(selectedStarRating);
        });

        star.addEventListener("mouseover", () => {
            updateStarDisplay(index + 1);
        });
    });

    const starContainer = document.querySelector(".star-rating-input");
    if (starContainer) {
        starContainer.addEventListener("mouseleave", () => {
            updateStarDisplay(selectedStarRating);
        });
    }
}

function updateStarDisplay(rating) {
    const stars = document.querySelectorAll(".star-rating-input span");
    stars.forEach((star, index) => {
        if (index < rating) {
            star.style.color = "#f59e0b";
        } else {
            star.style.color = "rgba(255,255,255,0.2)";
        }
    });
}

async function fetchReviewsFeed() {
    const feedContainer = document.getElementById("reviews-feed");
    const avgRatingVal = document.getElementById("avg-rating-display");
    const totalReviewsVal = document.getElementById("total-reviews-count");

    if (!feedContainer) return;

    try {
        const response = await fetch(`${API_BASE_URL}/reviews`);
        const resData = await response.json();

        if (response.ok && resData.success) {
            const reviews = resData.reviews || [];
            if (avgRatingVal) avgRatingVal.textContent = resData.average_rating || "5.0";
            if (totalReviewsVal) totalReviewsVal.textContent = resData.total_reviews || reviews.length;

            if (reviews.length === 0) {
                feedContainer.innerHTML = `<div style="text-align:center; color:var(--text-muted); padding:30px;">Be the first user to leave a review!</div>`;
                return;
            }

            feedContainer.innerHTML = reviews.map(r => {
                const starsHtml = "★".repeat(r.rating) + "☆".repeat(5 - r.rating);
                const dateStr = r.created_at ? new Date(r.created_at).toLocaleDateString() : "Recently";
                return `
                    <div class="card" style="padding:20px; margin-bottom:16px;">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                            <div style="display:flex; align-items:center; gap:10px;">
                                <div class="user-avatar" style="width:28px; height:28px; font-size:0.75rem;">
                                    ${r.user_name.charAt(0).toUpperCase()}
                                </div>
                                <strong style="color:var(--text-primary); font-size:0.95rem;">${r.user_name}</strong>
                            </div>
                            <span style="color:#f59e0b; font-size:1.1rem;">${starsHtml}</span>
                        </div>
                        <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:8px;">"${r.comment}"</p>
                        <div style="font-size:0.75rem; color:var(--text-muted); text-align:right;">${dateStr}</div>
                    </div>
                `;
            }).join("");
        }
    } catch (e) {
        console.error("Fetch reviews error:", e);
    }
}
