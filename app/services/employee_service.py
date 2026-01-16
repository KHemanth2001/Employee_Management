from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.schemas.api_schemas import (
    CreateEmployeeRequest,
    CreateEmployeeResponse,
    EmployeeResponse,
    EmployeeListResponse
)
from app.repository.employee_repository import (
    add_employee_into_db,
    get_employee_by_id,
    get_all_employees,
    update_employee_by_id,
    delete_employee_by_id
)


def add_employee(session: Session, request: CreateEmployeeRequest) -> CreateEmployeeResponse:
    """
    Creates a new employee record in the database.

    Args:
        session (Session): SQLAlchemy database session.
        request (CreateEmployeeRequest): Employee creation payload.

    Returns:
        CreateEmployeeResponse: Success message after employee creation.

    Raises:
        HTTPException: If an employee with the same email already exists.
    """
    try:
        add_employee_into_db(
            session=session,
            employee_name=request.name,
            employee_email=request.email,
            employee_role=request.role,
            employee_dept=request.department
        )
        return CreateEmployeeResponse()

    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee with this email already exists"
        )


def fetch_all_employees(
    session: Session,
    department: str | None,
    role: str | None,
    page: int
) -> EmployeeListResponse:
    """
    Retrieves a paginated list of employees with optional filters.

    Args:
        session (Session): SQLAlchemy database session.
        department (str | None): Optional department filter.
        role (str | None): Optional role filter.
        page (int): Page number for pagination.

    Returns:
        EmployeeListResponse: Paginated list of employees and total count.
    """
    employees, total = get_all_employees(
        session=session,
        department=department,
        role=role,
        page=page,
        limit=10
    )
    return EmployeeListResponse(total=total, items=employees)


def fetch_employee_by_id(session: Session, employee_id: int) -> EmployeeResponse:
    """
        Retrieves an employee by their unique identifier.

        Args:
            session (Session): SQLAlchemy database session.
            employee_id (int): Employee ID.

        Returns:
            EmployeeResponse: Employee details.

        Raises:
            HTTPException: If the employee does not exist.
    """
    employee = get_employee_by_id(session, employee_id)

    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

    return employee


def update_employee(
    session: Session,
    employee_id: int,
    request: CreateEmployeeRequest
) -> EmployeeResponse:
    """
    Updates an existing employee record.

    Args:
        session (Session): SQLAlchemy database session.
        employee_id (int): Employee ID to update.
        request (CreateEmployeeRequest): Updated employee details.

    Returns:
        EmployeeResponse: Updated employee information.

    Raises:
        HTTPException: If employee does not exist or email already exists.
    """
    try:
        employee = get_employee_by_id(session, employee_id)

        if not employee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

        updated = update_employee_by_id(
            session=session,
            employee=employee,
            data=request.model_dump(exclude_unset=True)
        )
        return updated

    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee email already exists"
        )


def delete_employee(session: Session, employee_id: int) -> None:
    """
        Deletes an employee record by ID.

        Args:
            session (Session): SQLAlchemy database session.
            employee_id (int): Employee ID to delete.

        Raises:
            HTTPException: If the employee does not exist.
    """
    employee = get_employee_by_id(session, employee_id)

    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

    delete_employee_by_id(session, employee)
