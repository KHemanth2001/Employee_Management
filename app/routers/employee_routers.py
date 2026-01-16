from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.employee_service import (
    add_employee,
    fetch_all_employees,
    fetch_employee_by_id,
    update_employee,
    delete_employee
)
from app.schemas.api_schemas import CreateEmployeeRequest, EmployeeListResponse, EmployeeResponse
from app.utils.auth.authenticate_user import authenticate_user


router = APIRouter(
    prefix="/api",
    tags = ["api"]
)


@router.post("/employees", status_code=status.HTTP_201_CREATED)
async def create_employee(
    request: CreateEmployeeRequest,
    auth_user=Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    """
        Creates a new employee.

        Args:
            request (CreateEmployeeRequest): Employee creation payload.
            auth_user: Authenticated user context.
            db (Session): SQLAlchemy database session.

        Returns:
            CreateEmployeeResponse: Success message.
    """
    return add_employee(db, request)


@router.get("/employees", response_model=EmployeeListResponse)
async def get_all_employees(
    department: str | None = Query(default=None),
    role: str | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    auth_user=Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    """
    Retrieves a list of employees with pagination and filtering.

    Args:
        department (str | None): Optional department filter.
        role (str | None): Optional role filter.
        page (int): Page number.
        auth_user: Authenticated user context.
        db (Session): SQLAlchemy database session.

    Returns:
        EmployeeListResponse: Paginated list of employees.
    """
    return fetch_all_employees(db, department, role, page)


@router.get("/employees/{id}", response_model=EmployeeResponse)
async def get_employee(
    id: int,
    auth_user=Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    """
    Retrieves an employee by ID.

    Args:
        id (int): Employee ID.
        auth_user: Authenticated user context.
        db (Session): SQLAlchemy database session.

    Returns:
        EmployeeResponse: Employee details.
    """
    return fetch_employee_by_id(db, id)


@router.put("/employees/{id}", response_model=EmployeeResponse)
async def update_employee_by_id(
    id: int,
    request: CreateEmployeeRequest,
    auth_user=Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    """
    Updates an employee record.

    Args:
        id (int): Employee ID.
        request (CreateEmployeeRequest): Updated employee data.
        auth_user: Authenticated user context.
        db (Session): SQLAlchemy database session.

    Returns:
        EmployeeResponse: Updated employee details.
    """
    return update_employee(db, id, request)


@router.delete("/employees/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee_by_id(
    id: int,
    auth_user=Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    """
        Deletes an employee by ID.

        Args:
            id (int): Employee ID.
            auth_user: Authenticated user context.
            db (Session): SQLAlchemy database session.

        Returns:
            None
    """
    delete_employee(db, id)
