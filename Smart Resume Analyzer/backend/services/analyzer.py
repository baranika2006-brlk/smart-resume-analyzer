from typing import Dict, List, Any

def analyze_resume_against_role(extracted_data: Dict[str, Any], job_role: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compare extracted resume skills against selected job role requirements.
    Calculates matched skills, missing skills, and skill match percentage.
    """
    extracted_tech = [s.lower() for s in extracted_data.get("technical_skills", [])]
    extracted_soft = [s.lower() for s in extracted_data.get("soft_skills", [])]
    all_extracted_lower = set(extracted_tech + extracted_soft)

    required_tech = job_role.get("required_skills", [])
    required_soft = job_role.get("soft_skills", [])

    matched_tech = []
    missing_tech = []

    for req in required_tech:
        if req.lower() in all_extracted_lower:
            matched_tech.append(req)
        else:
            missing_tech.append(req)

    matched_soft = []
    missing_soft = []
    for req in required_soft:
        if req.lower() in all_extracted_lower:
            matched_soft.append(req)
        else:
            missing_soft.append(req)

    total_required = len(required_tech)
    matched_count = len(matched_tech)

    if total_required > 0:
        match_percentage = round((matched_count / total_required) * 100, 1)
    else:
        match_percentage = 100.0

    return {
        "role_id": job_role.get("role_id"),
        "job_title": job_role.get("title"),
        "required_skills": required_tech,
        "matched_skills": matched_tech,
        "missing_skills": missing_tech,
        "matched_soft_skills": matched_soft,
        "missing_soft_skills": missing_soft,
        "skill_match_percentage": match_percentage,
        "total_required_skills": total_required,
        "matched_skills_count": matched_count
    }
