# **BookStudio Sync - Setup and Testing Guide**

This document provides a step-by-step guide for setting up, working on, and testing the **BookStudio Sync** repository.

## **Table of Contents**

1. [Prerequisites](#1-prerequisites)
2. [Clone the Repository](#2-clone-the-repository)
3. [Set Up the Environment](#3-set-up-the-environment)
4. [Run the Application](#4-run-the-application)
5. [Testing the Application](#5-testing-the-application)
6. [Repository Structure](#6-repository-structure)

## **1. Prerequisites**

Ensure you have the following installed on your system:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **PostgreSQL**: [Download PostgreSQL](https://www.postgresql.org/download/)
- **Git**: [Download Git](https://git-scm.com/downloads)

## **2. Clone the Repository**

1. Open your terminal or command prompt.
2. Clone the repository using Git:
   ```bash
   git clone https://github.com/mohammadalish/bookstudio-sync.git
   ```
3. Navigate to the project directory:
   ```bash
   cd bookstudio-sync
   ```

## **3. Set Up the Environment**

1. **Install Dependencies**:

   - If you don’t have Poetry, use `pip`:

     ```bash
     pip install -r requirements.txt
     ```

     Change directory to the `app/`:

     ```bash
     cd app
     ```

2. **Set Up PostgreSQL**:

   - Create a new PostgreSQL database for the project.
   - Update the `DATABASE_FULL_URL` in the `.env` file (or create one if it doesn’t exist) with your database credentials:
     ```env
     DATABASE_FULL_URL=postgresql+psycopg2://username:password@hostname:port/dbname
     ```
     Replace `username`, `password`, and `dbname` with your PostgreSQL credentials.

3. **Run Database Migrations**:

   - Use Alembic to apply database migrations:

     ```bash
     alembic init alembic
     ```

     Replace this line in the `alembic.ini` with your actual PostgreSQL full URL:

     ```bash
     sqlalchemy.url = postgresql+psycopg2://username:password@hostname:port/dbname
     ```

     then run this command in the same directory:

     ```bash
     alembic upgrade head
     ```

## **4. Run the Application**

1. Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
2. The application will be available at:
   - **API Docs**: `http://127.0.0.1:8000/docs`
   - **Redoc**: `http://127.0.0.1:8000/redoc`

## **5. Testing the Application**

1. **Test Endpoints**:

   - Use the interactive API docs (`/docs`) to test the endpoints.
   - Example:
     - Create a user: `POST /users/`
     - Create a book: `POST /books/`
     - Create a reservation: `POST /reservations/`

## **6. Repository Structure**

Here’s an overview of the repository structure:

```
📂 **BOOKSTUDIO**
│── 📂 **app**
│   ├── 📂 **routers**
│   │   ├── 📂 \_\_pycache\_\_
│   │   ├── 📄 books.py
│   │   ├── 📄 customers.py
│   │   ├── 📄 reservations.py
│   │   ├── 📄 users.py
│   ├── 📄 alembic.ini
│   ├── 📄 crud.py
│   ├── 📄 database.py
│   ├── 📄 main.py
│   ├── 📄 models.py
│   ├── 📄 schemas.py
├── 📄 .env
├── 📄 .gitignore
├── 📄 LICENSE
├── 📄 README.md
├── 📄 requirements.txt

```
