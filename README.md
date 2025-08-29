# Online Store Inventory System

This project is a command-line interface (CLI) application for managing a simple online store's inventory, customers, and orders.

## Features

*   **Product Management**: Add new products to the inventory and view a list of all available products with their prices and stock levels.
*   **Customer Management**: Add new customers to the system and view a list of all registered customers.
*   **Order Processing**: Place new orders for customers, which automatically updates product stock quantities.
*   **Order History**: View the complete order history for any customer to track their past purchases.

## Technologies Used

*   Python
*   SQLAlchemy
*   Alembic (for database migrations)
*   pipenv (for package and environment management)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd online-store-inventory-system
    ```

2.  **Install dependencies:**
    Make sure you have `pipenv` installed, then run:
    ```bash
    pipenv install
    ```

## Database Setup

The project uses Alembic to manage database migrations. To set up your database, run the following command to apply the existing migrations:

```bash
pipenv run alembic upgrade head
```
This will create the `online_store.db` file with all the necessary tables.

## Usage

To run the application, execute the following command:

```bash
pipenv run python cli.py
```

You will be presented with a menu of options to interact with the application:

```
===  Online Store CLI ===
1. Add Product
2. List Products
3. Add Customer
4. List Customers
5. Place Order
6. View Order History
7. Exit
```

Follow the on-screen prompts to use the desired feature.

## Project Structure

*   `cli.py`: The main entry point of the application. It contains the user interface logic and menu.
*   `lib/database.py`: Configures the SQLAlchemy database connection.
*   `lib/db/models.py`: Defines the database schema using SQLAlchemy ORM (Product, Customer, Order tables).
*   `lib/db/migrations/`: Contains the Alembic migration scripts for the database.
*   `Pipfile`: Specifies the project's dependencies for `pipenv`.
*   `online_store.db`: The SQLite database file (created after running migrations).