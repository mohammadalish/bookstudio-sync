from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import User, Book, Customer, Reservation
from schemas import UserCreate, BookBase, CustomerBase, ReservationBase
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def create_book(db: Session, book: BookBase):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session):
    return db.query(Book).all()


def create_customer(db: Session, customer: CustomerBase):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_customers(db: Session):
    return db.query(Customer).all()


def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()


def update_customer(db: Session, customer_id: int, customer_data: CustomerBase):
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        raise ValueError("Customer not found")
    for key, value in customer_data.dict().items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def delete_customer(db: Session, customer_id: int):
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        raise ValueError("Customer not found")
    db.delete(db_customer)
    db.commit()


def create_reservation(db: Session, reservation: ReservationBase):
    try:
        # Check if the book exists and has available units
        book = db.query(Book).filter(
            Book.id == reservation.book_id).with_for_update().first()
        if not book:
            raise ValueError("Book not found")
        if book.units < 1:
            raise ValueError("Book is out of stock")

        # Check if the customer exists
        customer = db.query(Customer).filter(
            Customer.id == reservation.customer_id).first()
        if not customer:
            raise ValueError("Customer not found")

        # Update book units and create reservation
        book.units -= 1
        new_reservation = Reservation(**reservation.dict())
        db.add(new_reservation)
        db.commit()
        db.refresh(new_reservation)
        return new_reservation
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Reservation failed: {e}")
        raise ValueError("Reservation failed due to database constraints")


def get_reservations(db: Session):
    return db.query(Reservation).all()


def get_reservation(db: Session, reservation_id: int):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()


def delete_reservation(db: Session, reservation_id: int):
    db_reservation = get_reservation(db, reservation_id)
    if not db_reservation:
        raise ValueError("Reservation not found")
    db.delete(db_reservation)
    db.commit()
