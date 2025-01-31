# routers/reservations.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import create_reservation, get_reservations, get_reservation, delete_reservation
from schemas import ReservationBase, ReservationResponse
from typing import List

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)


@router.post("/", response_model=ReservationResponse)
def add_reservation(reservation: ReservationBase, db: Session = Depends(get_db)):
    return create_reservation(db, reservation)


@router.get("/", response_model=List[ReservationResponse])
def list_reservations(db: Session = Depends(get_db)):
    return get_reservations(db)


@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation_by_id(reservation_id: int, db: Session = Depends(get_db)):
    reservation = get_reservation(db, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation


@router.delete("/{reservation_id}")
def remove_reservation(reservation_id: int, db: Session = Depends(get_db)):
    delete_reservation(db, reservation_id)
    return {"message": "Reservation deleted successfully"}
