from typing import Dict, Any

def calculate_resume_score(analysis_result: Dict[str, Any], extracted_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate overall resume score out of 100 based on weighted metrics:
    - Skill Match Percentage: 40 points max
    - Projects & Practical Experience: 25 points max
    - Education Quality & Relevance: 15 points max
    - Professional Certifications: 10 points max
    - Resume Completeness & Length: 10 points max
    """
    # 1. Skill Match Score (0 - 40)
    match_pct = analysis_result.get("skill_match_percentage", 0)
    skill_score = (match_pct / 100.0) * 40.0

    # 2. Projects Score (0 - 25)
    est_projects = extracted_data.get("estimated_projects_count", 0)
    has_proj_sec = extracted_data.get("has_projects_section", False)
    if est_projects >= 3 or (has_proj_sec and est_projects >= 2):
        project_score = 25.0
    elif est_projects == 2 or has_proj_sec:
        project_score = 18.0
    elif est_projects == 1:
        project_score = 12.0
    else:
        project_score = 5.0

    # 3. Education Score (0 - 15)
    edu_list = extracted_data.get("education", [])
    if len(edu_list) >= 2:
        education_score = 15.0
    elif len(edu_list) == 1:
        education_score = 12.0
    else:
        education_score = 6.0

    # 4. Certifications Score (0 - 10)
    certs = extracted_data.get("certifications", [])
    if len(certs) >= 2:
        cert_score = 10.0
    elif len(certs) == 1:
        cert_score = 7.0
    else:
        cert_score = 2.0

    # 5. Completeness & Length Score (0 - 10)
    word_count = extracted_data.get("total_word_count", 0)
    if 250 <= word_count <= 1200:
        completeness_score = 10.0
    elif 150 <= word_count < 250 or 1200 < word_count <= 2000:
        completeness_score = 7.0
    else:
        completeness_score = 4.0

    total_score = round(skill_score + project_score + education_score + cert_score + completeness_score, 1)
    final_overall = min(100.0, max(0.0, total_score))

    # Rating Level
    if final_overall >= 85:
        grade = "Excellent (Interview Ready)"
    elif final_overall >= 70:
        grade = "Good (Competitive Profile)"
    elif final_overall >= 50:
        grade = "Average (Needs Targeted Skills)"
    else:
        grade = "Needs Significant Improvement"

    return {
        "overall_score": final_overall,
        "grade": grade,
        "breakdown": {
            "skill_match_score": round(skill_score, 1),
            "project_score": round(project_score, 1),
            "education_score": round(education_score, 1),
            "certifications_score": round(cert_score, 1),
            "completeness_score": round(completeness_score, 1)
        }
    }
