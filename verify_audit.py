
import requests
import json
from datetime import date, timedelta

BASE_URL = "http://localhost:8005"
EMP_ID = "E1001"

def test_api_scenarios():
    print("=== TEST START: 3 API Scenarios ===")

    # 1. Mark Present (Attendance)
    print("\n[Scenario 1] Mark Present")
    # First, unlock system to allow working on weekend/holiday
    requests.post(f"{BASE_URL}/api/simulate", json={"state": "UNLOCK_RESTRICTION"})
    
    res = requests.post(f"{BASE_URL}/api/mark-attendance", json={"emp_id": EMP_ID})
    if res.status_code == 200:
        print("✅ Attendance Marked Successfully (after unlock)")
    else:
        print(f"⚠️ Failed: {res.text}")
    
    # Reset to normal
    requests.post(f"{BASE_URL}/api/simulate", json={"state": "NORMAL"})

    # 2. Leave Request (with Reason)
    print("\n[Scenario 2] Leave Request (HOLIDAY_EXCEPTION)")
    payload_leave = {
        "emp_id": EMP_ID,
        "request_type": "HOLIDAY_EXCEPTION",
        "date_start": str(date.today()),
        "date_end": str(date.today()),
        "current_status": "HOLIDAY",
        "desired_status": "PRESENT",
        "reason_category": "HOLIDAY_WORK",
        "reason_text": "Production Support for Release v2"
    }
    res = requests.post(f"{BASE_URL}/attendance-requests", json=payload_leave)
    if res.status_code == 201:
        req_id = res.json()['id']
        print(f"✅ Leave Request Created (ID: {req_id})")
        
        # Verify Audit
        audit = requests.get(f"{BASE_URL}/attendance-requests/{req_id}/audit").json()
        if any(a['comment'] == payload_leave['reason_text'] for a in audit):
            print("   ✅ Reason verified in Audit Log")
        else:
            print("   ❌ Reason MISSING in Audit Log")
    else:
        print(f"❌ Failed to create leave request: {res.text}")

    # 3. Unlock Request (with Reason)
    print("\n[Scenario 3] Unlock Request (Lockout Exception)")
    payload_unlock = {
        "emp_id": EMP_ID,
        "request_type": "UNLOCK",
        "date_start": str(date.today()),
        "date_end": str(date.today()),
        "reason_category": "SYSTEM_ISSUE",
        "reason_text": "Biometric scanner malfunction at Gate 1"
    }
    res = requests.post(f"{BASE_URL}/attendance-requests", json=payload_unlock)
    if res.status_code == 201:
        req_id = res.json()['id']
        print(f"✅ Unlock Request Created (ID: {req_id})")
        
        # Verify Audit
        audit = requests.get(f"{BASE_URL}/attendance-requests/{req_id}/audit").json()
        if any(a['comment'] == payload_unlock['reason_text'] for a in audit):
            print("   ✅ Reason verified in Audit Log")
        else:
            print("   ❌ Reason MISSING in Audit Log")
    else:
        print(f"❌ Failed to create unlock request: {res.text}")

if __name__ == "__main__":
    try:
        test_api_scenarios()
    except Exception as e:
        print(f"Error: {e}")

