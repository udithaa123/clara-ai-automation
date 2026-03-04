# Clara AI Automation Pipeline

## Overview

This project automates the generation of AI answering agent configurations from customer call transcripts.

The system processes two types of transcripts:

1. Demo call transcripts
2. Onboarding call transcripts

From these transcripts it extracts business rules and generates versioned agent configurations.

---

## Pipeline Architecture

Demo Transcript
↓
Extract Business Information
↓
Account Memo (v1)
↓
Generate Agent Spec (v1)

Onboarding Transcript
↓
Extract Operational Rules
↓
Update Memo (v2)
↓
Generate Agent Spec (v2)
↓
Generate Changelog

---

## Project Structure

clara-ai-automation

data/  
&nbsp;&nbsp;&nbsp;&nbsp;demo_calls/  
&nbsp;&nbsp;&nbsp;&nbsp;onboarding_calls/  

outputs/  
&nbsp;&nbsp;&nbsp;&nbsp;accounts/  

scripts/  
&nbsp;&nbsp;&nbsp;&nbsp;ingest.py  
&nbsp;&nbsp;&nbsp;&nbsp;extract_demo.py  
&nbsp;&nbsp;&nbsp;&nbsp;extract_onboarding.py  
&nbsp;&nbsp;&nbsp;&nbsp;generate_prompt.py  
&nbsp;&nbsp;&nbsp;&nbsp;generate_agent_spec.py  
&nbsp;&nbsp;&nbsp;&nbsp;create_changelog.py  
&nbsp;&nbsp;&nbsp;&nbsp;run_pipeline.py  

workflows/  
&nbsp;&nbsp;&nbsp;&nbsp;n8n_workflow.json  

requirements.txt  
README.md

---

## How to Run

Install dependencies

pip install -r requirements.txt

Run pipeline

python scripts/run_pipeline.py

---

## Output Example

outputs/accounts/

account_xxxx/

v1/  
memo.json  
agent_spec.json  

v2/  
memo.json  
agent_spec.json  

changes.md

---

## Features

• Transcript ingestion  
• Business rule extraction  
• Agent configuration generation  
• Version tracking (v1 → v2)  
• Changelog generation  
• Batch processing for multiple accounts