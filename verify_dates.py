import requests
import json

BASE_URL = "http://localhost:8013"
ENDPOINT = f"{BASE_URL}/api/atomicwork/sync-attendance"

def test_date(date_str):
    payload = {
        "emp_id": "E1005",
        "date": date_str,
        "status": "PRESENT",
        "reason": f"Test Date {date_str}",
        "approval_note": "Date Format Check"
    }
    print(f"\nSending Date: {date_str}")
    res = requests.post(ENDPOINT, json=payload)
    print(f"Status: {res.status_code}")
    print(f"Response: {res.text}")

dates_to_test = [
    "2026-01-27",    # Standard YYYY-MM-DD
    "28-01-2026",    # DD-MM-YYYY (User request)
    "29/01/2026",    # Slash DD/MM/YYYY
    "Jan 30, 2026"  # Text format
]

for d in dates_to_test:
    test_date(d)
