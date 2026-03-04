def create_changelog(v1, v2):

    changes = []

    for key in v2:
        if key not in v1:
            changes.append(f"{key} added")

    for key in v1:
        if key in v2 and v1[key] != v2[key]:
            changes.append(f"{key} updated")

    return changes
