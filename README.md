# Attendance Service (SAP Mock)

A tiny FastAPI + SQLite microservice to mock the **Attendance unlock/correction** use case.

It supports the end-to-end flow used by Atom workflows:

1) **Create request** (employee) → status `PENDING_APPROVAL`
2) **Approve / Reject** (manager) → on approve, apply updates to `attendance_records` (mock "SAP update")
3) **Confirm** request status + view audit trail

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload --port 8000
```

Open:
- API docs: http://localhost:8000/docs
- Admin UI: http://localhost:8000/admin

## Key endpoints

### Create a request
`POST /attendance-requests`

Example payload:
```json
{
  "emp_id": "E1001",
  "request_type": "CORRECT_MARKING",
  "date_start": "2025-12-25",
  "date_end": "2025-12-25",
  "current_status": "PRESENT",
  "desired_status": "LEAVE",
  "reason_category": "MISTAKE",
  "reason_text": "Marked present by mistake"
}
```

Response includes `id` + `approver_emp_id` (manager).

### Approve (and apply to SAP_MOCK)
`POST /attendance-requests/{id}/approve`

```json
{ "actor_emp_id": "M2001", "comment": "Approved" }
```

### Confirm + audit
- `GET /attendance-requests/{id}`
- `GET /attendance-requests/{id}/audit`

### Validate the applied record
`GET /attendance?emp_id=E1001&start=2025-12-25&end=2025-12-25`

## Demo seed data

On startup, the service seeds:
- Manager: `M2001`
- Employees: `E1001`, `E1002` (manager = M2001)
- Attendance records for `E1001` for last 10 days

## Notes
- This is intentionally simple and auditable.
- In real deployment, the `_apply_change` function would call SAP (or a middleware) instead of updating SQLite.
