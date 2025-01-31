from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Text, TIMESTAMP, CheckConstraint, Index
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy_utils import EmailType

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(20))
    email = Column(EmailType, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    role = Column(String(50), CheckConstraint(
        "role IN ('Admin', 'Customer', 'Author')"))

    authorship = relationship("Author", back_populates="user")
    customer = relationship("Customer", back_populates="user")


Index("ix_users_email", User.email)
Index("ix_users_username", User.username)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    city = Column(String(100))
    goodreads_link = Column(Text)
    bank_account_number = Column(String(50))

    user = relationship("User", back_populates="authorship")
    books = relationship("Book", back_populates="author")


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    isbn = Column(String(50), unique=True, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id", ondelete="SET NULL"))
    description = Column(Text)
    units = Column(Integer, default=1)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))

    author = relationship("Author", back_populates="books")


Index("ix_books_isbn", Book.isbn)


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    subscription = Column(String(50), CheckConstraint(
        "subscription IN ('Free', 'Plus', 'Premium')"))
    subscription_end_time = Column(TIMESTAMP)
    wallet_money = Column(DECIMAL(10, 2), default=0)

    user = relationship("User", back_populates="customer")
    reservations = relationship("Reservation", back_populates="customer")


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey(
        "customers.id", ondelete="CASCADE"))
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    price = Column(DECIMAL(10, 2), nullable=False)

    customer = relationship("Customer", back_populates="reservations")


Index("ix_reservations_customer_book",
      Reservation.customer_id, Reservation.book_id)
