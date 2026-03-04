import os
import json
import copy

from ingest import generate_account_id
from extract_demo import extract_demo_info
from generate_prompt import generate_prompt
from generate_agent_spec import generate_agent_spec
from extract_onboarding import update_from_onboarding
from create_changelog import create_changelog


def run_pipeline():

    demo_folder = "data/demo_calls"
    onboarding_folder = "data/onboarding_calls"

    demo_files = os.listdir(demo_folder)

    for demo_file in demo_files:

        if not demo_file.endswith(".txt"):
            continue

        demo_path = os.path.join(demo_folder, demo_file)

        print(f"\nProcessing demo file: {demo_file}")

        with open(demo_path) as f:
            demo_transcript = f.read()

        account_id = generate_account_id()

        memo_v1 = extract_demo_info(demo_transcript, account_id)

        prompt_v1 = generate_prompt(memo_v1)

        agent_v1 = generate_agent_spec(memo_v1, prompt_v1)

        v1_dir = f"outputs/accounts/{account_id}/v1"
        os.makedirs(v1_dir, exist_ok=True)

        with open(f"{v1_dir}/memo.json", "w") as f:
            json.dump(memo_v1, f, indent=2)

        with open(f"{v1_dir}/agent_spec.json", "w") as f:
            json.dump(agent_v1, f, indent=2)

        print("v1 agent created")

        # Try to find corresponding onboarding file
        onboarding_file = demo_file.replace("demo", "onboarding")
        onboarding_path = os.path.join(onboarding_folder, onboarding_file)

        if os.path.exists(onboarding_path):

            print(f"Found onboarding file: {onboarding_file}")

            with open(onboarding_path) as f:
                onboarding_transcript = f.read()

            memo_v2 = update_from_onboarding(copy.deepcopy(memo_v1), onboarding_transcript)

            prompt_v2 = generate_prompt(memo_v2)

            agent_v2 = generate_agent_spec(memo_v2, prompt_v2)
            agent_v2["version"] = "v2"

            v2_dir = f"outputs/accounts/{account_id}/v2"
            os.makedirs(v2_dir, exist_ok=True)

            with open(f"{v2_dir}/memo.json", "w") as f:
                json.dump(memo_v2, f, indent=2)

            with open(f"{v2_dir}/agent_spec.json", "w") as f:
                json.dump(agent_v2, f, indent=2)

            changes = create_changelog(memo_v1, memo_v2)

            with open(f"outputs/accounts/{account_id}/changes.md", "w") as f:
                for change in changes:
                    f.write(change + "\n")

            print("v2 agent created with updates")

        else:
            print("No onboarding file found for this demo.")


if __name__ == "__main__":
    run_pipeline()
