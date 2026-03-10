# jobs_data.py
"""
Futuristic Backend Data Model for Job Risk Analysis
- Designed for integration with FastAPI or similar frameworks
- Ready for MongoDB or other NoSQL/SQL storage
"""

from typing import List, Dict

jobs = [
    {
        "title": "Receptionist",
        "industry": "Administrative",
        "tasks": ["Greet visitors", "Answer phones", "Schedule appointments"],
        "risk_score": 85,
        "timeline_years": "2-5",
        "tags": ["high risk", "customer-facing"],
        "sources": ["OECD AI risk series", "McKinsey 2023"],
        "notes": "Automatable with chatbots, scheduling apps, and IVR systems."
    },
    {
        "title": "Data Entry Clerk",
        "industry": "Administrative",
        "tasks": ["Transcribe data", "Enter information into systems"],
        "risk_score": 92,
        "timeline_years": "1-3",
        "tags": ["very high risk"],
        "sources": ["Industry reports"],
        "notes": "OCR and AI-assisted data extraction reduce manual input."
    },
    {
        "title": "Accounts Payable Clerk",
        "industry": "Finance",
        "tasks": ["Process invoices", "Vendor communication", "Reconcile gl entries"],
        "risk_score": 60,
        "timeline_years": "3-7",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "Automation possible for routing and matching invoices."
    },
    {
        "title": "Credit Analyst",
        "industry": "Finance",
        "tasks": ["Assess credit risk", "Review financial statements", "Prepare risk reports"],
        "risk_score": 40,
        "timeline_years": "5-10",
        "tags": ["lower risk"],
        "sources": ["Industry reports"],
        "notes": "AI may assist analysis but judgment remains important."
    },
    {
        "title": "Bank Teller",
        "industry": "Finance",
        "tasks": ["Cash handling", "Customer service", "Balance cash drawer"],
        "risk_score": 65,
        "timeline_years": "3-7",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "Self-service kiosks and ATMs change workflow."
    },
    {
        "title": "Retail Cashier",
        "industry": "Retail",
        "tasks": ["Process transactions", "Assist customers", "Stock checks"],
        "risk_score": 70,
        "timeline_years": "2-5",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "POS automation and self-checkout impact roles."
    },
    {
        "title": "Warehouse Picker",
        "industry": "Logistics",
        "tasks": ["Locate items", "Prepare orders", "Label shipments"],
        "risk_score": 75,
        "timeline_years": "1-3",
        "tags": ["high risk"],
        "sources": ["Industry reports"],
        "notes": "Automation with robotics and AGV systems."
    },
    {
        "title": "Delivery Driver",
        "industry": "Transportation",
        "tasks": ["Deliver goods", "Update delivery status", "Customer communication"],
        "risk_score": 65,
        "timeline_years": "3-7",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "Route optimization and autonomous delivery are advancing."
    },
    {
        "title": "Truck Dispatcher",
        "industry": "Transportation",
        "tasks": ["Plan routes", "Coordinate drivers", "Track shipments"],
        "risk_score": 55,
        "timeline_years": "4-8",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "AI routing and scheduling reduce manual planning."
    },
    {
        "title": "Customer Support Representative",
        "industry": "IT/Tech",
        "tasks": ["Answer tickets", "Resolve issues", "Escalate complex problems"],
        "risk_score": 40,
        "timeline_years": "5-10",
        "tags": ["low to moderate risk"],
        "sources": ["Industry reports"],
        "notes": "Chatbots handle common queries; humans handle complex cases."
    },
    {
        "title": "Technical Support Specialist",
        "industry": "IT/Tech",
        "tasks": ["Diagnose technical problems", "Provide solutions", "Document cases"],
        "risk_score": 50,
        "timeline_years": "4-8",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "AI assists diagnosis but requires domain expertise."
    },
    {
        "title": "Software Developer",
        "industry": "IT/Tech",
        "tasks": ["Write code", "Review requirements", "Test software"],
        "risk_score": 30,
        "timeline_years": "5-15",
        "tags": ["low risk"],
        "sources": ["OECD AI risk", "WEF reports"],
        "notes": "Automation assists repetitive coding tasks but core design remains human-driven."
    },
    {
        "title": "Data Scientist",
        "industry": "IT/Tech",
        "tasks": ["Model development", "Data wrangling", "Experimentation"],
        "risk_score": 35,
        "timeline_years": "5-10",
        "tags": ["low to moderate risk"],
        "sources": ["Industry reports"],
        "notes": "Automation handles data prep; creativity in modeling stays valuable."
    },
    {
        "title": "Teacher / Tutor",
        "industry": "Education",
        "tasks": ["Deliver lessons", "Assess assignments", "Provide feedback"],
        "risk_score": 40,
        "timeline_years": "5-15",
        "tags": ["low to moderate risk"],
        "sources": ["Education technology analyses"],
        "notes": "AI tutors can assist but classroom interaction remains essential."
    },
    {
        "title": "Administrative Assistant",
        "industry": "Administrative",
        "tasks": ["Calendar management", "Document prep", "Travel arrangements"],
        "risk_score": 68,
        "timeline_years": "3-7",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "RPA and AI-assisted planning reduce routine tasks."
    },
    {
        "title": "Paralegal",
        "industry": "Legal",
        "tasks": ["Research", "Draft documents", "Case management"],
        "risk_score": 45,
        "timeline_years": "5-10",
        "tags": ["low to moderate risk"],
        "sources": ["Legal tech reports"],
        "notes": "AI can draft first-pass documents; lawyers add nuance."
    },
    {
        "title": "Parliamentary / Policy Analyst",
        "industry": "Public Sector",
        "tasks": ["Policy research", "Data analysis", "Reporting"],
        "risk_score": 50,
        "timeline_years": "5-15",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "AI supports data synthesis; human judgment essential for recommendations."
    },
    {
        "title": "Journalist / News Reporter",
        "industry": "Media/Arts",
        "tasks": ["Research", "Write articles", "Fact-check"],
        "risk_score": 55,
        "timeline_years": "5-10",
        "tags": ["moderate risk"],
        "sources": ["Media technology analyses"],
        "notes": "AI can draft, but investigative storytelling requires human insight."
    },
    {
        "title": "Graphic Designer",
        "industry": "Media/Arts",
        "tasks": ["Create visuals", "Collaborate with teams", "Prepare assets"],
        "risk_score": 60,
        "timeline_years": "3-7",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "AI-assisted design tools speed up tasks but creativity remains key."
    },
    {
        "title": "Real Estate Agent",
        "industry": "Real Estate",
        "tasks": ["List properties", "Showings", "Negotiate deals"],
        "risk_score": 40,
        "timeline_years": "5-10",
        "tags": ["low risk"],
        "sources": ["Industry reports"],
        "notes": "AI aids market analysis; human negotiation and relationships matter."
    },
    {
        "title": "Security Guard",
        "industry": "Security",
        "tasks": ["Patrol", "Monitor systems", "Incident response"],
        "risk_score": 45,
        "timeline_years": "5-10",
        "tags": ["low to moderate risk"],
        "sources": ["Security tech analyses"],
        "notes": "Automations and sensors reduce routine patrols; judgment still needed for incidents."
    },
    {
        "title": "Construction Laborer",
        "industry": "Construction",
        "tasks": ["Site prep", "Operate tools", "Assist trades"],
        "risk_score": 40,
        "timeline_years": "5-15",
        "tags": ["low risk"],
        "sources": ["Industry reports"],
        "notes": "Robotics and automation change some workflows; skilled trades persist."
    },
    {
        "title": "Maintenance Technician",
        "industry": "Manufacturing",
        "tasks": ["Repair equipment", "Perform preventive maintenance", "Diagnostics"],
        "risk_score": 50,
        "timeline_years": "4-8",
        "tags": ["moderate risk"],
        "sources": ["Industry reports"],
        "notes": "AI-assisted diagnostics reduce downtime; hands-on skills remain essential."
    },
    {
        "title": "Quality Inspector",
        "industry": "Manufacturing",
        "tasks": ["Inspect products", "Record defects", "Report"],
        "risk_score": 70,
        "timeline_years": "2-5",
        "tags": ["high risk"],
        "sources": ["Industry reports"],
        "notes": "Vision systems and robotics can automate inspection tasks."
    },
    {
        "title": "HR Generalist",
        "industry": "Other",
        "tasks": ["Recruitment", "Employee relations", "Benefits admin"],
        "risk_score": 50,
        "timeline_years": "5-10",
        "tags": ["moderate risk"],
        "sources": ["HR tech analyses"],
        "notes": "AI supports screening and onboarding; nuanced people management remains human."
    }
]

# Example function for future API integration
def get_jobs_by_risk(min_risk: int = 0) -> List[Dict]:
    """Return jobs with risk_score >= min_risk"""
    return [job for job in jobs if job["risk_score"] >= min_risk]

# Example function for filtering by industry
def get_jobs_by_industry(industry: str) -> List[Dict]:
    """Return jobs matching the industry"""
    return [job for job in jobs if job["industry"].lower() == industry.lower()]

# Example function for futuristic search (by tag)
def get_jobs_by_tag(tag: str) -> List[Dict]:
    """Return jobs containing the tag"""
    return [job for job in jobs if tag.lower() in [t.lower() for t in job["tags"]]]

# Ready for API integration, database storage, and advanced filtering
