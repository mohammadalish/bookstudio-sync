# routers/customers.py 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import create_customer, get_customers, get_customer, update_customer, delete_customer
from schemas import CustomerBase, CustomerResponse
from typing import List

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/", response_model=CustomerResponse)
def add_customer(customer: CustomerBase, db: Session = Depends(get_db)):
    return create_customer(db, customer)

@router.get("/", response_model=List[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    return get_customers(db)

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    customer = get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer_by_id(customer_id: int, customer: CustomerBase, db: Session = Depends(get_db)):
    return update_customer(db, customer_id, customer)

@router.delete("/{customer_id}")
def remove_customer(customer_id: int, db: Session = Depends(get_db)):
    delete_customer(db, customer_id)
    return {"message": "Customer deleted successfully"}