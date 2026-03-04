def update_from_onboarding(memo, transcript):

    if "dispatch" in transcript.lower():
        memo["emergency_routing_rules"] = ["transfer to dispatch"]

    if "servicetrade" in transcript.lower():
        memo["integration_constraints"] = [
            "never create sprinkler jobs in ServiceTrade"
        ]

    return memo
