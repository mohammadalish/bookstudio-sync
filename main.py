from fastapi import FastAPI
from routers import users, books, customers, reservations
import models
from database import engine

app = FastAPI()

app.include_router(users.router)
app.include_router(books.router)
app.include_router(customers.router)
app.include_router(reservations.router)


@app.get("/")
def root():
    return {"message": "Here is The BookStudio API"}


models.Base.metadata.create_all(bind=engine)
