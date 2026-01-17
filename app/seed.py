from __future__ import annotations

from datetime import date, timedelta

from sqlalchemy import select

from .db import Base, engine, SessionLocal
from .models import Employee, AttendanceRecord, AttendanceStatus


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def seed() -> None:
    init_db()
    db = SessionLocal()
    try:
        # Seed manager
        manager = db.get(Employee, "M2001")
        if not manager:
            manager = Employee(emp_id="M2001", name="Vivek Manager", location="Hyderabad", cost_center="CC100")
            db.add(manager)

        # Seed employees
        if not db.get(Employee, "E1001"):
            db.add(Employee(emp_id="E1001", name="Asha Field", location="Hyderabad", cost_center="CC200", manager_emp_id="M2001"))
        if not db.get(Employee, "E1002"):
            db.add(Employee(emp_id="E1002", name="Rahul Field", location="Vijayawada", cost_center="CC200", manager_emp_id="M2001"))

        db.commit()

        # Seed attendance records for last 10 days for E1001 if none exist
        existing = db.execute(select(AttendanceRecord).where(AttendanceRecord.emp_id == "E1001")).scalars().first()
        if not existing:
            today = date.today()
            for i in range(1, 11):
                d = today - timedelta(days=i)
                # Skip Weekends for seed data
                if d.weekday() < 5: 
                    db.add(
                        AttendanceRecord(
                            emp_id="E1001",
                            day=d,
                            status=AttendanceStatus.PRESENT.value,
                            source_system="SAP_MOCK",
                            last_updated_by="seed",
                        )
                    )
            db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    seed()
    print("Seed complete")
