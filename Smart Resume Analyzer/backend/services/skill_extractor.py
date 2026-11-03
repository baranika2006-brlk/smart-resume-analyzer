import re
from typing import Dict, List, Any

# Predefined Skill Libraries for NLP Matching
SKILL_DATASET = {
    # Programming Languages
    "python": "Python", "java": "Java", "javascript": "JavaScript", "typescript": "TypeScript",
    "c++": "C++", "c#": "C#", "c": "C", "r": "R", "go": "Go", "golang": "Go", "php": "PHP",
    "ruby": "Ruby", "swift": "Swift", "kotlin": "Kotlin", "sql": "SQL", "html": "HTML5",
    "html5": "HTML5", "css": "CSS3", "css3": "CSS3", "bash": "Bash", "shell": "Shell",

    # Web & Backend Frameworks
    "flask": "Flask", "django": "Django", "fastapi": "FastAPI", "spring": "Spring Boot",
    "spring boot": "Spring Boot", "spring boot": "Spring Boot", "express": "Express.js",
    "express.js": "Express.js", "react": "React", "react.js": "React", "reactjs": "React",
    "vue": "Vue.js", "vue.js": "Vue.js", "angular": "Angular", "node": "Node.js",
    "node.js": "Node.js", "nodejs": "Node.js", "bootstrap": "Bootstrap", "tailwind": "Tailwind CSS",
    "rest api": "REST API", "restful api": "REST API", "restful web services": "REST API",
    "graphql": "GraphQL", "microservices": "Microservices", "websockets": "WebSockets",

    # Databases & Storage
    "mongodb": "MongoDB", "mysql": "MySQL", "postgresql": "PostgreSQL", "postgres": "PostgreSQL",
    "sqlite": "SQLite", "oracle": "Oracle DB", "redis": "Redis", "cassandra": "Cassandra",
    "dynamodb": "DynamoDB", "nosql": "NoSQL",

    # Data Science, ML & AI
    "pandas": "Pandas", "numpy": "NumPy", "scikit-learn": "Scikit-Learn", "sklearn": "Scikit-Learn",
    "tensorflow": "TensorFlow", "pytorch": "PyTorch", "keras": "Keras", "spacy": "spaCy",
    "nltk": "NLTK", "opencv": "OpenCV", "machine learning": "Machine Learning", "deep learning": "Deep Learning",
    "natural language processing": "Natural Language Processing (NLP)", "nlp": "Natural Language Processing (NLP)",
    "computer vision": "Computer Vision", "data analysis": "Data Analysis", "exploratory data analysis": "Exploratory Data Analysis (EDA)",
    "eda": "Exploratory Data Analysis (EDA)", "data visualization": "Data Visualization", "power bi": "Power BI",
    "powerbi": "Power BI", "tableau": "Tableau", "excel": "Excel", "matplotlib": "Matplotlib", "seaborn": "Seaborn",
    "statistics": "Statistics", "mlops": "MLOps", "neural networks": "Neural Networks",

    # DevOps & Tools
    "git": "Git", "github": "GitHub", "gitlab": "GitLab", "docker": "Docker",
    "kubernetes": "Kubernetes", "k8s": "Kubernetes", "aws": "AWS", "amazon web services": "AWS",
    "azure": "Azure", "gcp": "Google Cloud", "google cloud": "GCP", "jenkins": "Jenkins",
    "ci/cd": "CI/CD", "maven": "Maven", "gradle": "Gradle", "pytest": "PyTest", "junit": "JUnit",

    # Concepts & Methodologies
    "object-oriented programming": "Object-Oriented Programming (OOP)", "oop": "Object-Oriented Programming (OOP)",
    "data structures": "Data Structures", "algorithms": "Algorithms", "design patterns": "Design Patterns",
    "agile": "Agile", "scrum": "Scrum", "unit testing": "Unit Testing"
}

SOFT_SKILL_DATASET = {
    "problem solving": "Problem Solving",
    "communication": "Communication",
    "teamwork": "Teamwork",
    "collaboration": "Team Collaboration",
    "critical thinking": "Critical Thinking",
    "time management": "Time Management",
    "adaptability": "Adaptability",
    "analytical thinking": "Analytical Thinking",
    "analytical reasoning": "Analytical Reasoning",
    "data storytelling": "Data Storytelling",
    "attention to detail": "Attention to Detail",
    "code review": "Code Review",
    "creativity": "Creativity",
    "leadership": "Leadership",
    "business acumen": "Business Acumen",
    "task prioritization": "Task Prioritization"
}

EDUCATION_PATTERNS = [
    r'\bB\.?Tech\b', r'\bB\.?E\.?\b', r'\bM\.?Tech\b', r'\bB\.?S\.?\b', r'\bM\.?S\.?\b',
    r'\bBCA\b', r'\bMCA\b', r'\bB\.?Sc\b', r'\bM\.?Sc\b', r'\bPh\.?D\b',
    r'\bBachelor(?:\'s)?\b', r'\bMaster(?:\'s)?\b', r'\bDiploma\b',
    r'Computer Science', r'Information Technology', r'Data Science', r'Artificial Intelligence', r'Software Engineering'
]

CERTIFICATION_PATTERNS = [
    r'AWS Certified[^\n,\.]*', r'Google[^\n,\.]*Certificate', r'Microsoft Certified[^\n,\.]*',
    r'Oracle Certified[^\n,\.]*', r'PCEP[^\n,\.]*', r'PCAP[^\n,\.]*', r'TensorFlow Developer[^\n,\.]*',
    r'Spring Certified[^\n,\.]*', r'Coursera[^\n,\.]*', r'Udemy[^\n,\.]*', r'Certified[^\n,\.]*'
]

def extract_skills_nlp(resume_text: str) -> Dict[str, Any]:
    """
    Extract technical skills, soft skills, education, certifications, and project insights 
    using natural language processing and token pattern matching.
    """
    text_lower = resume_text.lower()
    
    # 1. Technical Skills Extraction
    extracted_tech_skills = set()
    for key, display_name in SKILL_DATASET.items():
        # Match as whole word / token boundary
        pattern = r'(?<![a-zA-Z0-9#\+])' + re.escape(key) + r'(?![a-zA-Z0-9#\+])'
        if re.search(pattern, text_lower):
            extracted_tech_skills.add(display_name)

    # 2. Soft Skills Extraction
    extracted_soft_skills = set()
    for key, display_name in SOFT_SKILL_DATASET.items():
        pattern = r'\b' + re.escape(key) + r'\b'
        if re.search(pattern, text_lower):
            extracted_soft_skills.add(display_name)

    # 3. Education Details
    extracted_education = []
    for pattern in EDUCATION_PATTERNS:
        matches = re.findall(pattern, resume_text, re.IGNORECASE)
        for m in matches:
            if m.strip() and m.strip() not in extracted_education:
                extracted_education.append(m.strip())

    # 4. Certifications
    extracted_certs = []
    for pattern in CERTIFICATION_PATTERNS:
        matches = re.findall(pattern, resume_text, re.IGNORECASE)
        for m in matches:
            clean_m = m.strip()
            if clean_m and len(clean_m) > 4 and clean_m not in extracted_certs:
                extracted_certs.append(clean_m)

    # 5. Project Detection
    project_mentions = len(re.findall(r'\b(?:project|developed|built|implemented|created|designed)\b', text_lower))
    has_projects_section = bool(re.search(r'\b(?:projects|personal projects|key projects|academic projects)\b', text_lower))
    estimated_projects = max(1 if has_projects_section else 0, min(project_mentions // 3, 5))

    return {
        "technical_skills": sorted(list(extracted_tech_skills)),
        "soft_skills": sorted(list(extracted_soft_skills)),
        "all_skills": sorted(list(extracted_tech_skills | extracted_soft_skills)),
        "education": extracted_education,
        "certifications": extracted_certs,
        "estimated_projects_count": estimated_projects,
        "has_projects_section": has_projects_section,
        "total_word_count": len(resume_text.split())
    }
