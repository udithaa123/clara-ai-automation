def generate_agent_spec(memo, prompt):

    agent_spec = {
        "agent_name": "Clara AI Agent",
        "voice_style": "professional",
        "system_prompt": prompt,
        "variables": {
            "services_supported": memo["services_supported"],
            "emergency_definition": memo["emergency_definition"]
        },
        "version": "v1"
    }

    return agent_spec
