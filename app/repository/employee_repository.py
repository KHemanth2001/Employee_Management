from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.employee import Employee


def add_employee_into_db(
    session: Session,
    employee_name: str,
    employee_email: str,
    employee_role: Optional[str],
    employee_dept: Optional[str]
) -> Employee:
    employee = Employee(
        name=employee_name,
        email=employee_email,
        role=employee_role,
        department=employee_dept
    )
    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee



def get_employee_by_id(session: Session, employee_id: int) -> Optional[Employee]:
    return session.query(Employee).filter(Employee.id == employee_id).first()


def get_all_employees(
    session: Session,
    department: Optional[str],
    role: Optional[str],
    page: int,
    limit: int
) -> tuple[list[Employee], int]:
    query = session.query(Employee)

    if department:
        query = query.filter(Employee.department == department)

    if role:
        query = query.filter(Employee.role == role)

    total = query.count()
    employees = query.offset((page - 1) * limit).limit(limit).all()
    return employees, total


def update_employee_by_id(
    session: Session,
    employee: Employee,
    data: dict
) -> Employee:
    for key, value in data.items():
        setattr(employee, key, value)

    session.commit()
    session.refresh(employee)
    return employee


def delete_employee_by_id(session: Session, employee: Employee) -> None:
    session.delete(employee)
    session.commit()
