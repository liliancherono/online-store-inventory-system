from ..database import Base, engine, SessionLocal
from .models import Customer, Product, Order

def seed():
    # Reset database
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    db = SessionLocal()

    # Add customers
    alice = Customer(name="Alice Johnson", email="alice@example.com", phone="123456789")
    bob = Customer(name="Bob Smith", email="bob@example.com", phone="987654321")
    db.add_all([alice, bob])
    db.commit()

    # Add products
    laptop = Product(name="Laptop", price=1200.00, stock_quantity=10)
    mouse = Product(name="Mouse", price=25.00, stock_quantity=50)
    keyboard = Product(name="Keyboard", price=75.00, stock_quantity=30)
    db.add_all([laptop, mouse, keyboard])
    db.commit()

    # Add orders (single product per order in your current design)
    order1 = Order(customer_id=alice.id, product_id=laptop.id, quantity=1)
    order2 = Order(customer_id=alice.id, product_id=mouse.id, quantity=2)
    order3 = Order(customer_id=bob.id, product_id=keyboard.id, quantity=1)

    db.add_all([order1, order2, order3])
    db.commit()

    db.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()
