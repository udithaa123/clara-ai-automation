import uuid

def generate_account_id():
    return "account_" + str(uuid.uuid4())[:8]
