import requests
import json

BASE_URL = "http://localhost:8014"
ENDPOINT = f"{BASE_URL}/api/atomicwork/sync-attendance"

payload = { 
    "emp_id": "E1001",
    "date": "2026-01-01",
    "status": "Cancel Leave & Mark Attendance",
    "reason": "Worked on Jan 1st, need to cancel leave and mark attendance. Proof of visit available.",
    "approval_note": "Approved - Approved by Vijay Shankar" 
}

print(f"Sending User Payload: {json.dumps(payload, indent=2)}")
res = requests.post(ENDPOINT, json=payload)
print(f"Status: {res.status_code}")
print(f"Response: {res.text}")
