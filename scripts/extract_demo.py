import re

def extract_demo_info(transcript, account_id):

    services = []
    emergencies = []
    questions = []

    # Detect services
    service_keywords = ["electrical", "sprinkler", "alarm", "hvac", "inspection"]
    for s in service_keywords:
        if s in transcript.lower():
            services.append(s)

    # Detect emergencies
    if "outage" in transcript.lower():
        emergencies.append("power outage")

    if "spark" in transcript.lower():
        emergencies.append("electrical sparks")

    if "leak" in transcript.lower():
        emergencies.append("sprinkler leak")

    memo = {
        "account_id": account_id,
        "company_name": "Unknown",
        "services_supported": services,
        "emergency_definition": emergencies,
        "business_hours": None,
        "questions_or_unknowns": questions,
        "notes": "Generated from demo transcript"
    }

    return memo
