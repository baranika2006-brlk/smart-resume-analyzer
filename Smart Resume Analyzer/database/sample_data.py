# Predefined sample job roles and required skills for smart_resume_analyzer

SAMPLE_JOB_ROLES = [
    # ── ORIGINAL ROLES ────────────────────────────────────────────────────────
    {
        "role_id": "python-developer",
        "title": "Python Developer",
        "category": "Software Engineering",
        "description": "Responsible for developing backend logic, RESTful APIs, data processing pipelines, and integrating databases using Python frameworks.",
        "required_skills": [
            "Python", "Flask", "Django", "FastAPI", "REST API",
            "PostgreSQL", "MongoDB", "Git", "Docker", "Object-Oriented Programming (OOP)",
            "Data Structures", "Algorithms", "Unit Testing", "PyTest"
        ],
        "soft_skills": [
            "Problem Solving", "Team Collaboration", "Code Review", "Communication", "Time Management"
        ],
        "recommended_certifications": [
            "PCEP - Certified Entry-Level Python Programmer",
            "PCAP - Certified Associate in Python Programming",
            "AWS Certified Developer - Associate"
        ],
        "suggested_projects": [
            "RESTful E-Commerce Microservice API with Flask/Django",
            "Automated Web Scraper and ETL Pipeline",
            "Real-time Chat Application using WebSockets"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "java-developer",
        "title": "Java Developer",
        "category": "Enterprise Software Engineering",
        "description": "Develops enterprise-grade scalable web applications, microservices, and secure backend platforms using Java and Spring ecosystem.",
        "required_skills": [
            "Java", "Spring Boot", "Spring MVC", "Hibernate", "JPA",
            "RESTful Web Services", "Maven", "Gradle", "MySQL", "PostgreSQL",
            "Git", "JUnit", "Microservices", "Design Patterns"
        ],
        "soft_skills": [
            "Critical Thinking", "Adaptability", "Teamwork", "Problem Solving"
        ],
        "recommended_certifications": [
            "Oracle Certified Associate (OCA) Java SE 11/17 Programmer",
            "Spring Certified Professional",
            "AWS Certified Solutions Architect"
        ],
        "suggested_projects": [
            "Banking & Transaction Management System in Spring Boot",
            "Microservices Architecture with API Gateway and Eureka",
            "Employee Portal with JWT Authentication"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "data-analyst",
        "title": "Data Analyst",
        "category": "Data Science & Analytics",
        "description": "Extracts insights from structured and unstructured data, performs statistical analysis, builds SQL queries, and constructs business dashboards.",
        "required_skills": [
            "SQL", "Python", "Pandas", "NumPy", "Power BI",
            "Tableau", "Excel", "Data Visualization", "Matplotlib", "Seaborn",
            "Data Cleaning", "Statistics", "Exploratory Data Analysis (EDA)"
        ],
        "soft_skills": [
            "Analytical Thinking", "Data Storytelling", "Attention to Detail", "Business Acumen"
        ],
        "recommended_certifications": [
            "Google Data Analytics Professional Certificate",
            "Microsoft Certified: Power BI Data Analyst Associate",
            "IBM Data Analyst Professional Certificate"
        ],
        "suggested_projects": [
            "Customer Churn Prediction and Visual Dashboard",
            "Sales Insights & Revenue Trend Analysis using Power BI and SQL",
            "Exploratory Data Analysis on E-Commerce Transactions"
        ],
        "experience_level": "Entry Level"
    },
    {
        "role_id": "ai-engineer",
        "title": "AI Engineer",
        "category": "Artificial Intelligence & Machine Learning",
        "description": "Designs, trains, deploys, and optimizes Machine Learning models, Deep Learning architectures, and Natural Language Processing pipelines.",
        "required_skills": [
            "Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
            "Scikit-Learn", "Natural Language Processing (NLP)", "spaCy", "NLTK",
            "Computer Vision", "OpenCV", "Neural Networks", "Data Modeling", "MLOps"
        ],
        "soft_skills": [
            "Research Aptitude", "Complex Problem Solving", "Analytical Reasoning", "Continuous Learning"
        ],
        "recommended_certifications": [
            "TensorFlow Developer Certificate",
            "AWS Certified Machine Learning - Specialty",
            "DeepLearning.AI Machine Learning Specialization"
        ],
        "suggested_projects": [
            "Smart Resume Parsing and Automated Candidate Ranking System",
            "Sentiment Analysis on Customer Reviews using BERT/Transformers",
            "Object Detection and Recognition Web Application"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "web-developer",
        "title": "Web Developer",
        "category": "Frontend & Full Stack Development",
        "description": "Builds interactive, modern, responsive websites and client-side web interfaces with clean HTML, CSS, JavaScript, and backend integration.",
        "required_skills": [
            "HTML5", "CSS3", "JavaScript", "React", "Vue.js",
            "Node.js", "Express.js", "REST API", "Responsive Web Design",
            "Git", "Bootstrap", "Tailwind CSS", "JSON", "DOM Manipulation"
        ],
        "soft_skills": [
            "UI/UX Sensitivity", "Creativity", "Collaboration", "Task Prioritization"
        ],
        "recommended_certifications": [
            "Meta Front-End Developer Professional Certificate",
            "FreeCodeCamp Responsive Web Design Certificate",
            "AWS Certified Developer - Associate"
        ],
        "suggested_projects": [
            "Full Stack Task Management App with Kanban View",
            "Portfolio Website with Dynamic Theme Switcher and Contact Form",
            "Interactive Weather Dashboard with Third-Party API Integration"
        ],
        "experience_level": "Entry Level"
    },

    # ── NEW ROLES ─────────────────────────────────────────────────────────────
    {
        "role_id": "cybersecurity-analyst",
        "title": "Cybersecurity Analyst",
        "category": "Cybersecurity",
        "description": "Monitors, detects, investigates, and responds to security threats and vulnerabilities across enterprise networks, systems, and cloud environments.",
        "required_skills": [
            "Network Security", "SIEM", "Intrusion Detection System (IDS)", "Intrusion Prevention System (IPS)",
            "Vulnerability Assessment", "Penetration Testing", "Firewalls", "TCP/IP",
            "Python", "Bash Scripting", "Linux", "Incident Response",
            "OWASP", "Cryptography", "Risk Management"
        ],
        "soft_skills": [
            "Analytical Thinking", "Attention to Detail", "Problem Solving", "Ethical Judgment", "Communication"
        ],
        "recommended_certifications": [
            "CompTIA Security+",
            "Certified Information Systems Security Professional (CISSP)",
            "Certified Ethical Hacker (CEH)",
            "Google Cybersecurity Professional Certificate"
        ],
        "suggested_projects": [
            "Network Traffic Anomaly Detection System using Python",
            "Vulnerability Scanner and CVE Reporter Tool",
            "SIEM Dashboard for Real-Time Log Analysis"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "mlops-engineer",
        "title": "MLOps Engineer",
        "category": "Artificial Intelligence & Machine Learning",
        "description": "Bridges the gap between ML model development and production deployment by automating CI/CD pipelines for ML workflows, model monitoring, and infrastructure management.",
        "required_skills": [
            "Python", "Docker", "Kubernetes", "MLflow", "Kubeflow",
            "CI/CD Pipelines", "Git", "Apache Airflow", "AWS SageMaker",
            "Model Monitoring", "Feature Store", "Data Versioning (DVC)",
            "TensorFlow", "PyTorch", "Terraform"
        ],
        "soft_skills": [
            "Systems Thinking", "Collaboration", "Continuous Learning", "Problem Solving"
        ],
        "recommended_certifications": [
            "AWS Certified Machine Learning - Specialty",
            "Google Professional Machine Learning Engineer",
            "MLflow Certified MLOps Professional"
        ],
        "suggested_projects": [
            "End-to-End MLOps Pipeline with MLflow, Docker, and CI/CD",
            "Automated Model Retraining System with Data Drift Detection",
            "Kubernetes-based ML Model Serving Platform"
        ],
        "experience_level": "Mid Level"
    },
    {
        "role_id": "cloud-security-engineer",
        "title": "Cloud Security Engineer",
        "category": "Cloud Computing & Security",
        "description": "Designs and implements security controls, policies, and architectures for cloud environments (AWS, Azure, GCP), ensuring compliance and data protection.",
        "required_skills": [
            "AWS Security", "Azure Security", "GCP Security", "IAM",
            "Zero Trust Architecture", "Cloud Compliance (SOC2, ISO27001)", "Encryption",
            "Network Security Groups", "VPC", "SIEM", "CSPM Tools",
            "Python", "Terraform", "Incident Response"
        ],
        "soft_skills": [
            "Risk Assessment", "Attention to Detail", "Communication", "Adaptability"
        ],
        "recommended_certifications": [
            "AWS Certified Security - Specialty",
            "Microsoft Certified: Azure Security Engineer Associate",
            "Certified Cloud Security Professional (CCSP)"
        ],
        "suggested_projects": [
            "Automated Cloud Security Compliance Checker using AWS Config",
            "Zero Trust Network Access Implementation on Azure",
            "Cloud Security Posture Management (CSPM) Dashboard"
        ],
        "experience_level": "Mid to Senior Level"
    },
    {
        "role_id": "blockchain-developer",
        "title": "Blockchain Developer",
        "category": "Blockchain & Web3",
        "description": "Develops decentralized applications (dApps), smart contracts, and blockchain-based solutions using platforms like Ethereum, Solana, and Hyperledger.",
        "required_skills": [
            "Solidity", "Ethereum", "Smart Contracts", "Web3.js", "Ethers.js",
            "Truffle", "Hardhat", "IPFS", "Hyperledger Fabric",
            "JavaScript", "Python", "Cryptography", "DeFi", "NFT Standards (ERC-20, ERC-721)"
        ],
        "soft_skills": [
            "Innovation", "Problem Solving", "Attention to Detail", "Continuous Learning"
        ],
        "recommended_certifications": [
            "Certified Blockchain Developer - Ethereum (CBDE)",
            "Blockchain Council Certified Blockchain Expert",
            "Hyperledger Fabric Developer"
        ],
        "suggested_projects": [
            "Decentralized Voting System using Solidity and Ethereum",
            "NFT Marketplace with Smart Contract and MetaMask Integration",
            "Supply Chain Transparency Platform on Hyperledger Fabric"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "iot-engineer",
        "title": "IoT Engineer",
        "category": "Internet of Things",
        "description": "Designs and builds connected embedded systems, sensor networks, edge computing solutions, and cloud-integrated IoT platforms.",
        "required_skills": [
            "Embedded C", "Python", "Arduino", "Raspberry Pi", "MQTT",
            "AWS IoT", "Azure IoT Hub", "Edge Computing", "Microcontrollers",
            "Communication Protocols (I2C, SPI, UART)", "Linux", "RTOS",
            "Sensor Integration", "REST API", "Data Streaming"
        ],
        "soft_skills": [
            "Creative Problem Solving", "Hardware-Software Integration Mindset", "Analytical Thinking"
        ],
        "recommended_certifications": [
            "AWS Certified IoT Developer",
            "Microsoft Certified: Azure IoT Developer Specialty",
            "CertNexus Certified IoT Practitioner (CIoTP)"
        ],
        "suggested_projects": [
            "Smart Home Automation System with MQTT and Raspberry Pi",
            "Real-Time Air Quality Monitoring Dashboard with IoT Sensors",
            "Edge AI Object Detection on Embedded Hardware"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "site-reliability-engineer",
        "title": "Site Reliability Engineer (SRE)",
        "category": "DevOps & Cloud Infrastructure",
        "description": "Ensures high availability, scalability, and reliability of production systems by applying software engineering principles to infrastructure and operations.",
        "required_skills": [
            "Linux", "Python", "Go", "Kubernetes", "Docker",
            "Prometheus", "Grafana", "Terraform", "Ansible", "CI/CD Pipelines",
            "SLI/SLO/SLA", "Incident Management", "Load Balancing",
            "Distributed Systems", "Git"
        ],
        "soft_skills": [
            "Systems Thinking", "Crisis Management", "Communication", "Accountability"
        ],
        "recommended_certifications": [
            "Google Professional Cloud DevOps Engineer",
            "Certified Kubernetes Administrator (CKA)",
            "AWS Certified SysOps Administrator"
        ],
        "suggested_projects": [
            "Production Monitoring Stack with Prometheus, Grafana, and Alertmanager",
            "Automated Incident Response Runbook System",
            "Infrastructure as Code (IaC) with Terraform and Ansible"
        ],
        "experience_level": "Mid to Senior Level"
    },
    {
        "role_id": "devsecops-engineer",
        "title": "DevSecOps Engineer",
        "category": "DevOps & Cybersecurity",
        "description": "Integrates security practices into the DevOps pipeline, automating vulnerability scanning, compliance checks, and secure software delivery.",
        "required_skills": [
            "CI/CD Security (Jenkins, GitHub Actions)", "SAST", "DAST", "OWASP",
            "Docker Security", "Kubernetes Security", "Secret Management (Vault)",
            "Terraform", "Ansible", "Python", "Bash", "SIEM",
            "Threat Modeling", "Compliance Automation", "Git"
        ],
        "soft_skills": [
            "Security Mindset", "Collaboration", "Analytical Thinking", "Continuous Improvement"
        ],
        "recommended_certifications": [
            "Certified DevSecOps Professional (CDP)",
            "AWS Certified Security - Specialty",
            "CompTIA Security+"
        ],
        "suggested_projects": [
            "Automated SAST/DAST Security Pipeline in GitHub Actions",
            "Kubernetes Security Hardening and Policy Enforcement Tool",
            "Secret Rotation and Vault Management System"
        ],
        "experience_level": "Mid Level"
    },
    {
        "role_id": "generative-ai-engineer",
        "title": "Generative AI Engineer",
        "category": "Artificial Intelligence & Machine Learning",
        "description": "Builds and fine-tunes large language models (LLMs) and generative AI systems for text, image, and multimodal applications.",
        "required_skills": [
            "Python", "Large Language Models (LLMs)", "OpenAI API", "LangChain",
            "Hugging Face Transformers", "Prompt Engineering", "RAG (Retrieval-Augmented Generation)",
            "Vector Databases (Pinecone, Weaviate)", "Fine-Tuning", "PyTorch",
            "Embeddings", "Diffusion Models", "NLP", "API Integration"
        ],
        "soft_skills": [
            "Creativity", "Research Aptitude", "Continuous Learning", "Problem Solving"
        ],
        "recommended_certifications": [
            "DeepLearning.AI Generative AI with LLMs",
            "AWS Certified Machine Learning - Specialty",
            "Google Cloud Professional Machine Learning Engineer"
        ],
        "suggested_projects": [
            "LLM-Powered Document Q&A Chatbot with RAG and Pinecone",
            "AI Image Generation App using Stable Diffusion",
            "Automated Code Review Assistant using GPT-4 and LangChain"
        ],
        "experience_level": "Mid Level"
    },
    {
        "role_id": "rpa-developer",
        "title": "RPA Developer",
        "category": "Automation & RPA",
        "description": "Designs and implements software bots using Robotic Process Automation tools to automate repetitive business processes and workflows.",
        "required_skills": [
            "UiPath", "Automation Anywhere", "Blue Prism", "Power Automate",
            "VB.NET", "C#", "Python", "BPMN", "Workflow Design",
            "API Integration", "OCR", "SQL", "Excel Automation", "SAP Automation"
        ],
        "soft_skills": [
            "Process Analysis", "Attention to Detail", "Problem Solving", "Communication"
        ],
        "recommended_certifications": [
            "UiPath Certified RPA Developer (UiARD)",
            "Automation Anywhere Certified Advanced RPA Professional",
            "Microsoft Power Automate Certification"
        ],
        "suggested_projects": [
            "Automated Invoice Processing Bot using UiPath and OCR",
            "HR Onboarding Workflow Automation with Power Automate",
            "Web Data Scraping and Reporting Bot with Automation Anywhere"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "solutions-architect",
        "title": "Solutions Architect",
        "category": "Cloud Computing & Architecture",
        "description": "Designs scalable, secure, and cost-effective cloud and enterprise software architectures aligned with business requirements and technical constraints.",
        "required_skills": [
            "AWS", "Azure", "GCP", "Microservices Architecture", "System Design",
            "Terraform", "Kubernetes", "API Gateway", "Database Design",
            "Security Architecture", "Cost Optimization", "Load Balancing",
            "Networking", "Python", "Technical Documentation"
        ],
        "soft_skills": [
            "Strategic Thinking", "Communication", "Stakeholder Management", "Leadership", "Problem Solving"
        ],
        "recommended_certifications": [
            "AWS Certified Solutions Architect - Professional",
            "Google Professional Cloud Architect",
            "Microsoft Certified: Azure Solutions Architect Expert"
        ],
        "suggested_projects": [
            "Multi-Region Fault-Tolerant E-Commerce Architecture on AWS",
            "Event-Driven Microservices Platform with Kafka and Kubernetes",
            "Hybrid Cloud Migration Strategy and Implementation"
        ],
        "experience_level": "Senior Level"
    },
    {
        "role_id": "ui-ux-designer",
        "title": "UI/UX Designer",
        "category": "Design & User Experience",
        "description": "Creates intuitive, visually compelling user interfaces and seamless user experiences through research, wireframing, prototyping, and design systems.",
        "required_skills": [
            "Figma", "Adobe XD", "Sketch", "Prototyping", "Wireframing",
            "User Research", "Usability Testing", "Design Systems", "Typography",
            "Color Theory", "HTML5", "CSS3", "Responsive Design",
            "Accessibility (WCAG)", "Interaction Design"
        ],
        "soft_skills": [
            "Empathy", "Creativity", "Communication", "Attention to Detail", "Collaboration"
        ],
        "recommended_certifications": [
            "Google UX Design Professional Certificate",
            "Interaction Design Foundation UX Certification",
            "Adobe Certified Professional in UI/UX Design"
        ],
        "suggested_projects": [
            "End-to-End Mobile App Design with Full Figma Prototype",
            "Design System and Component Library for a SaaS Product",
            "Usability Audit and Redesign of an Existing Web Application"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "ethical-hacker",
        "title": "Ethical Hacker",
        "category": "Cybersecurity",
        "description": "Performs authorized penetration testing, red team operations, and vulnerability assessments to identify and help remediate security weaknesses.",
        "required_skills": [
            "Penetration Testing", "Kali Linux", "Metasploit", "Burp Suite", "Nmap",
            "OWASP Top 10", "Web Application Security", "Network Security",
            "Python", "Bash Scripting", "SQL Injection", "XSS", "Social Engineering",
            "Wireless Security", "Exploit Development"
        ],
        "soft_skills": [
            "Ethical Judgment", "Curiosity", "Analytical Thinking", "Attention to Detail", "Report Writing"
        ],
        "recommended_certifications": [
            "Certified Ethical Hacker (CEH)",
            "Offensive Security Certified Professional (OSCP)",
            "CompTIA PenTest+"
        ],
        "suggested_projects": [
            "Custom Vulnerability Scanner with CVE Integration",
            "Web Application Penetration Testing Lab (DVWA/OWASP WebGoat)",
            "CTF (Capture The Flag) Writeup Portfolio"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "mobile-app-developer",
        "title": "Mobile App Developer",
        "category": "Mobile Development",
        "description": "Develops cross-platform mobile applications using React Native or Flutter, integrating REST APIs, local storage, and device hardware features.",
        "required_skills": [
            "React Native", "Flutter", "Dart", "JavaScript", "TypeScript",
            "REST API Integration", "Redux", "Firebase", "SQLite",
            "Push Notifications", "App Store Deployment", "Git",
            "UI Component Design", "Performance Optimization"
        ],
        "soft_skills": [
            "Creativity", "User Empathy", "Collaboration", "Problem Solving", "Attention to Detail"
        ],
        "recommended_certifications": [
            "Meta React Native Developer Professional Certificate",
            "Google Associate Android Developer",
            "Flutter Development Bootcamp Certificate"
        ],
        "suggested_projects": [
            "Cross-Platform Fitness Tracker App with Firebase and React Native",
            "Real-Time Chat Application using Flutter and Firebase",
            "E-Commerce Mobile App with Payment Gateway Integration"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "android-developer",
        "title": "Android Developer",
        "category": "Mobile Development",
        "description": "Builds native Android applications using Kotlin and Java, following Material Design guidelines and integrating backend services.",
        "required_skills": [
            "Kotlin", "Java", "Android SDK", "Jetpack Compose", "Android Studio",
            "MVVM Architecture", "Room Database", "Retrofit", "Coroutines",
            "Firebase", "Git", "REST API", "Google Play Publishing", "Material Design"
        ],
        "soft_skills": [
            "Attention to Detail", "User-Centric Thinking", "Collaboration", "Problem Solving"
        ],
        "recommended_certifications": [
            "Google Associate Android Developer (AAD)",
            "Android Kotlin Developer Nanodegree (Udacity)",
            "Jetpack Compose Pathway (Google)"
        ],
        "suggested_projects": [
            "News Reader App with Retrofit, Coroutines, and Room DB",
            "Task Manager App using Jetpack Compose and MVVM",
            "Location-Based Service App with Google Maps API"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "ios-developer",
        "title": "iOS Developer",
        "category": "Mobile Development",
        "description": "Develops native iOS applications for iPhone and iPad using Swift and SwiftUI, following Apple Human Interface Guidelines.",
        "required_skills": [
            "Swift", "SwiftUI", "UIKit", "Xcode", "Core Data",
            "Combine Framework", "REST API Integration", "URLSession",
            "MVVM Architecture", "CocoaPods", "SPM (Swift Package Manager)",
            "Git", "TestFlight", "App Store Connect", "Push Notifications"
        ],
        "soft_skills": [
            "Creativity", "Attention to Detail", "User Empathy", "Problem Solving"
        ],
        "recommended_certifications": [
            "Apple Developer Program Certification",
            "iOS App Development with Swift (Meta Professional Certificate)",
            "SwiftUI Masterclass Certificate"
        ],
        "suggested_projects": [
            "Personal Finance Tracker App using SwiftUI and Core Data",
            "Real-Time Weather App with URLSession and Combine",
            "Social Media App with Firebase Authentication and Firestore"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "devops-engineer",
        "title": "DevOps Engineer",
        "category": "DevOps & Cloud Infrastructure",
        "description": "Implements and manages CI/CD pipelines, automates infrastructure provisioning, and ensures fast, reliable software delivery through DevOps best practices.",
        "required_skills": [
            "Docker", "Kubernetes", "Jenkins", "GitHub Actions", "GitLab CI",
            "Terraform", "Ansible", "Linux", "Bash Scripting", "Python",
            "AWS / Azure / GCP", "Prometheus", "Grafana", "Nginx", "Git"
        ],
        "soft_skills": [
            "Collaboration", "Continuous Improvement", "Systems Thinking", "Problem Solving"
        ],
        "recommended_certifications": [
            "Certified Kubernetes Administrator (CKA)",
            "AWS Certified DevOps Engineer - Professional",
            "HashiCorp Certified: Terraform Associate"
        ],
        "suggested_projects": [
            "Full CI/CD Pipeline with Jenkins, Docker, and Kubernetes",
            "Infrastructure as Code with Terraform and AWS",
            "GitOps Workflow with ArgoCD and Kubernetes"
        ],
        "experience_level": "Mid Level"
    },
    {
        "role_id": "aws-cloud-engineer",
        "title": "AWS Cloud Engineer",
        "category": "Cloud Computing & Architecture",
        "description": "Designs, deploys, and manages cloud infrastructure and services on Amazon Web Services, ensuring scalability, reliability, and cost optimization.",
        "required_skills": [
            "AWS EC2", "AWS S3", "AWS Lambda", "AWS RDS", "AWS VPC",
            "AWS IAM", "AWS CloudFormation", "Terraform", "AWS EKS",
            "AWS CloudWatch", "Route 53", "Elastic Load Balancing",
            "Python", "Bash", "Linux"
        ],
        "soft_skills": [
            "Analytical Thinking", "Cost Optimization Mindset", "Communication", "Adaptability"
        ],
        "recommended_certifications": [
            "AWS Certified Solutions Architect - Associate",
            "AWS Certified Developer - Associate",
            "AWS Certified SysOps Administrator - Associate"
        ],
        "suggested_projects": [
            "Serverless Web Application with AWS Lambda, API Gateway, and DynamoDB",
            "Multi-Tier Auto-Scaling Web Architecture on AWS",
            "AWS Cost Optimization Dashboard with CloudWatch and Lambda"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "azure-cloud-engineer",
        "title": "Azure Cloud Engineer",
        "category": "Cloud Computing & Architecture",
        "description": "Builds, deploys, and maintains cloud solutions on Microsoft Azure including VMs, containers, databases, and serverless functions.",
        "required_skills": [
            "Azure Virtual Machines", "Azure App Service", "Azure Functions",
            "Azure Kubernetes Service (AKS)", "Azure SQL", "Azure Blob Storage",
            "Azure Active Directory", "Azure DevOps", "ARM Templates",
            "Terraform", "PowerShell", "Python", "Azure Monitor", "Bicep"
        ],
        "soft_skills": [
            "Structured Thinking", "Communication", "Adaptability", "Problem Solving"
        ],
        "recommended_certifications": [
            "Microsoft Certified: Azure Administrator Associate (AZ-104)",
            "Microsoft Certified: Azure Solutions Architect Expert (AZ-305)",
            "Microsoft Certified: Azure Developer Associate (AZ-204)"
        ],
        "suggested_projects": [
            "Containerized Microservices Deployment on Azure Kubernetes Service",
            "Serverless Event-Driven Architecture using Azure Functions and Service Bus",
            "Azure Infrastructure Automation with Terraform and Azure DevOps"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "business-analyst-it",
        "title": "Business Analyst – IT",
        "category": "Business & Management",
        "description": "Bridges business needs and technology solutions by gathering requirements, analyzing processes, and translating them into detailed functional specifications.",
        "required_skills": [
            "Requirements Gathering", "Business Process Modeling (BPMN)", "Use Case Writing",
            "SQL", "Power BI", "Excel", "JIRA", "Confluence",
            "Stakeholder Management", "Gap Analysis", "User Stories",
            "Wireframing (Figma/Balsamiq)", "Agile / Scrum", "Data Analysis"
        ],
        "soft_skills": [
            "Communication", "Analytical Thinking", "Problem Solving", "Facilitation", "Negotiation"
        ],
        "recommended_certifications": [
            "IIBA Certified Business Analysis Professional (CBAP)",
            "PMI Professional in Business Analysis (PMI-PBA)",
            "Microsoft Certified: Power BI Data Analyst Associate"
        ],
        "suggested_projects": [
            "End-to-End Requirements Documentation for an E-Commerce Platform",
            "Business Process Improvement Analysis with BPMN Diagrams",
            "Stakeholder Interview Report and Product Backlog for an HR System"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "it-consultant",
        "title": "IT Consultant",
        "category": "Business & Management",
        "description": "Advises organizations on technology strategy, system selection, and digital transformation initiatives to improve business efficiency and competitiveness.",
        "required_skills": [
            "IT Strategy", "Enterprise Architecture", "Cloud Solutions",
            "ERP Systems (SAP, Oracle)", "IT Governance (ITIL, COBIT)",
            "Project Management", "Business Process Analysis", "Risk Management",
            "Data Analytics", "Cybersecurity Fundamentals", "Vendor Management",
            "SQL", "PowerPoint", "Stakeholder Engagement"
        ],
        "soft_skills": [
            "Strategic Thinking", "Communication", "Leadership", "Adaptability", "Client Relationship Management"
        ],
        "recommended_certifications": [
            "ITIL 4 Foundation",
            "AWS Certified Solutions Architect - Associate",
            "Microsoft Certified: Azure Solutions Architect Expert"
        ],
        "suggested_projects": [
            "Digital Transformation Roadmap for a Mid-Sized Retail Company",
            "ERP System Evaluation and Selection Report",
            "IT Cost Reduction Strategy and Vendor Consolidation Plan"
        ],
        "experience_level": "Mid to Senior Level"
    },
    {
        "role_id": "it-project-manager",
        "title": "IT Project Manager",
        "category": "Business & Management",
        "description": "Plans, executes, and closes IT projects on time, within scope, and on budget while managing cross-functional teams and stakeholder expectations.",
        "required_skills": [
            "Project Planning", "Risk Management", "Budgeting", "JIRA",
            "MS Project", "Agile / Scrum", "Waterfall Methodology",
            "Stakeholder Management", "Change Management", "PRINCE2",
            "PMP Methodology", "Resource Allocation", "Status Reporting", "Confluence"
        ],
        "soft_skills": [
            "Leadership", "Communication", "Negotiation", "Conflict Resolution", "Decision Making"
        ],
        "recommended_certifications": [
            "Project Management Professional (PMP)",
            "PRINCE2 Practitioner",
            "PMI Agile Certified Practitioner (PMI-ACP)"
        ],
        "suggested_projects": [
            "Full Project Plan for a Software Development Lifecycle (SDLC) Initiative",
            "Risk Register and Mitigation Plan for a Cloud Migration Project",
            "Agile Sprint Retrospective and Velocity Tracking Dashboard"
        ],
        "experience_level": "Mid to Senior Level"
    },
    {
        "role_id": "product-manager-tech",
        "title": "Product Manager – Technology",
        "category": "Business & Management",
        "description": "Owns the product vision, roadmap, and backlog for a technology product, working with engineering, design, and business teams to deliver customer value.",
        "required_skills": [
            "Product Roadmapping", "User Story Writing", "Agile / Scrum",
            "OKRs / KPIs", "Market Research", "Competitor Analysis",
            "JIRA", "Confluence", "Wireframing (Figma/Balsamiq)", "A/B Testing",
            "Data Analysis", "SQL", "Customer Discovery", "Prioritization Frameworks (RICE, MoSCoW)"
        ],
        "soft_skills": [
            "Strategic Vision", "Communication", "Empathy", "Leadership", "Decision Making"
        ],
        "recommended_certifications": [
            "Certified Scrum Product Owner (CSPO)",
            "PMI Agile Certified Practitioner (PMI-ACP)",
            "Product School - Product Management Certificate"
        ],
        "suggested_projects": [
            "Product Roadmap and MVP Definition for a B2B SaaS Platform",
            "User Research Report with Personas, Pain Points, and Opportunity Map",
            "Feature Prioritization Matrix with RICE Scoring Framework"
        ],
        "experience_level": "Mid Level"
    },
    {
        "role_id": "scrum-master",
        "title": "Scrum Master",
        "category": "Business & Management",
        "description": "Facilitates Agile Scrum ceremonies, removes team impediments, coaches the team on Scrum values, and ensures continuous delivery and improvement.",
        "required_skills": [
            "Scrum Framework", "Agile Methodologies", "Sprint Planning",
            "Retrospectives", "Daily Standups", "Backlog Grooming",
            "JIRA", "Confluence", "Kanban", "SAFe (Scaled Agile)",
            "Impediment Removal", "Stakeholder Communication", "Conflict Facilitation"
        ],
        "soft_skills": [
            "Servant Leadership", "Facilitation", "Empathy", "Communication", "Adaptability"
        ],
        "recommended_certifications": [
            "Certified ScrumMaster (CSM)",
            "Professional Scrum Master (PSM I/II)",
            "SAFe Agilist (SA)"
        ],
        "suggested_projects": [
            "Agile Transformation Plan for a Traditional Waterfall Team",
            "Team Health Check Dashboard and Continuous Improvement Tracker",
            "Sprint Velocity and Burndown Chart Analysis Report"
        ],
        "experience_level": "Entry to Mid Level"
    },
    {
        "role_id": "generative-ai-app-developer",
        "title": "Generative AI Application Developer",
        "category": "Artificial Intelligence & Machine Learning",
        "description": "Develops production-grade applications powered by Generative AI models, integrating LLMs, multimodal APIs, and intelligent agent workflows.",
        "required_skills": [
            "Python", "OpenAI API (GPT-4/GPT-4o)", "LangChain", "LlamaIndex",
            "RAG Pipelines", "Vector Databases (Pinecone, ChromaDB)", "Prompt Engineering",
            "FastAPI", "Streamlit", "Gradio", "Docker", "Git",
            "Embeddings", "Function Calling", "AI Agents (AutoGen, CrewAI)"
        ],
        "soft_skills": [
            "Creativity", "Rapid Prototyping", "Problem Solving", "Continuous Learning"
        ],
        "recommended_certifications": [
            "DeepLearning.AI Generative AI with LLMs",
            "LangChain for LLM Application Development",
            "AWS Certified Machine Learning - Specialty"
        ],
        "suggested_projects": [
            "AI-Powered PDF Knowledge Base Chatbot with RAG and LangChain",
            "Multi-Agent Research Assistant using AutoGen and GPT-4",
            "Generative AI Resume Optimizer with OpenAI API and Streamlit"
        ],
        "experience_level": "Mid Level"
    },
    {
        "role_id": "ai-automation-engineer",
        "title": "AI Automation Engineer",
        "category": "Automation & RPA",
        "description": "Combines artificial intelligence with automation frameworks to design intelligent workflows, smart bots, and decision-making automation systems.",
        "required_skills": [
            "Python", "LangChain", "OpenAI API", "UiPath", "Power Automate",
            "Apache Airflow", "REST API Integration", "Machine Learning",
            "Prompt Engineering", "NLP", "AI Agents", "Docker",
            "SQL", "Workflow Orchestration", "RPA Tools"
        ],
        "soft_skills": [
            "Process Thinking", "Innovation", "Analytical Thinking", "Collaboration"
        ],
        "recommended_certifications": [
            "UiPath Certified RPA Developer",
            "DeepLearning.AI Generative AI with LLMs",
            "AWS Certified Machine Learning - Specialty"
        ],
        "suggested_projects": [
            "AI-Driven Email Triage and Response Automation System",
            "Intelligent Document Processing Pipeline with OCR and LLM",
            "LLM-Powered Decision Automation Bot with LangChain and Power Automate"
        ],
        "experience_level": "Mid Level"
    },
    {
        "role_id": "computer-forensics-analyst",
        "title": "Computer Forensics Analyst",
        "category": "Cybersecurity",
        "description": "Investigates cybercrimes, data breaches, and digital fraud by collecting, preserving, and analyzing digital evidence from computer systems and networks.",
        "required_skills": [
            "Digital Forensics", "Autopsy", "FTK (Forensic Toolkit)", "EnCase",
            "Memory Forensics (Volatility)", "Disk Imaging", "Chain of Custody",
            "Network Forensics (Wireshark)", "Log Analysis", "Python",
            "Linux", "Malware Analysis", "Incident Response", "Legal & Compliance"
        ],
        "soft_skills": [
            "Attention to Detail", "Analytical Thinking", "Ethical Judgment", "Report Writing", "Integrity"
        ],
        "recommended_certifications": [
            "Certified Computer Examiner (CCE)",
            "GIAC Certified Forensic Examiner (GCFE)",
            "EnCase Certified Examiner (EnCE)"
        ],
        "suggested_projects": [
            "Digital Forensics Investigation Report on a Simulated Data Breach",
            "Memory Dump Analysis for Malware Detection using Volatility",
            "Network Packet Capture and Evidence Reconstruction with Wireshark"
        ],
        "experience_level": "Mid Level"
    }
]

DEFAULT_ADMIN_USER = {
    "name": "System Administrator",
    "email": "admin@smartresume.com",
    "role": "admin"
}

SAMPLE_REVIEWS = [
    {
        "user_name": "Aarav Sharma",
        "rating": 5,
        "comment": "Incredible tool! The missing skills breakdown helped me land my Python Developer interview."
    },
    {
        "user_name": "Priya Patel",
        "rating": 5,
        "comment": "Super clean interface and super fast NLP extraction. The resume score matched recruiter feedback."
    },
    {
        "user_name": "Rohan Gupta",
        "rating": 4,
        "comment": "Very accurate skill detection for Data Analyst role. Highly recommended for final year students."
    }
]
