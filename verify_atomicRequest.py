import requests
import json

BASE_URL = "http://localhost:8013"
ENDPOINT = f"{BASE_URL}/api/atomicwork/sync-attendance"

payload = { 
    "emp_id": "E1009", # Using E1009 as E1001 might not exist or verify check
    "date": "2026-01-26",
    "status": "Working on Holiday/Weekend",
    "reason": "I am working on January 26 - Republic day",
    "approval_note": "Approved - Approved by Vijay Shankar" 
}

print(f"Sending User Payload: {json.dumps(payload, indent=2)}")
res = requests.post(ENDPOINT, json=payload)
print(f"Status: {res.status_code}")
print(f"Response: {res.text}")
