from lib.database import SessionLocal
from lib.db.models import Product, Customer, Order

def add_product_logic(name, price, stock_quantity):
    session = SessionLocal()
    try:
        product = Product(name=name, price=price, stock_quantity=stock_quantity)
        session.add(product)
        session.commit()
        return True, f" Product '{name}' added successfully!"
    except Exception as e:
        session.rollback()
        return False, f" Error adding product: {e}"
    finally:
        session.close()

def list_products_logic():
    session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return products

def update_product_logic(product_id, new_name, new_price_str, new_stock_str):
    session = SessionLocal()
    try:
        product = session.query(Product).get(product_id)

        if not product:
            return False, " Product not found."   

        if new_name:
            product.name = new_name
        if new_price_str:
            product.price = float(new_price_str)
        if new_stock_str:
            product.stock_quantity = int(new_stock_str)

        session.commit()
        return True, f" Product '{product.name}' updated successfully!"
    except ValueError:
        session.rollback()
        return False, " Invalid input. Price and stock must be numbers."
    except Exception as e:
        session.rollback()
        return False, f" Error updating product: {e}"
    finally:
        session.close()

def delete_product_logic(product_id):
    session = SessionLocal()
    try:
        product = session.query(Product).get(product_id)

        if not product:
            return False, " Product not found."

        session.delete(product)
        session.commit()
        return True, f" Product '{product.name}' deleted successfully!"
    except Exception as e:
        session.rollback()
        return False, f" Error deleting product: {e}"
    finally:
        session.close()

def add_customer_logic(name, email, phone):
    session = SessionLocal()
    try:
        customer = Customer(name=name, email=email, phone=phone)
        session.add(customer)
        session.commit()
        return True, f" Customer '{name}' added successfully!"
    except Exception as e:
        session.rollback()
        return False, f" Error adding customer: {e}"
    finally:
        session.close()

def list_customers_logic():
    session = SessionLocal()
    customers = session.query(Customer).all()
    session.close()
    return customers

def update_customer_logic(customer_id, new_name, new_email, new_phone):
    session = SessionLocal()
    try:
        customer = session.query(Customer).get(customer_id)

        if not customer:
            return False, " Customer not found."

        if new_name:
            customer.name = new_name
        if new_email:
            customer.email = new_email
        if new_phone:
            customer.phone = new_phone

        session.commit()
        return True, f" Customer '{customer.name}' updated successfully!"
    except ValueError:
        session.rollback()
        return False, " Invalid input. ID must be a number."
    except Exception as e:
        session.rollback()
        return False, f" Error updating customer: {e}"
    finally:
        session.close()

def delete_customer_logic(customer_id):
    session = SessionLocal()
    try:
        customer = session.query(Customer).get(customer_id)

        if not customer:
            return False, " Customer not found."

        session.delete(customer)
        session.commit()
        return True, f" Customer '{customer.name}' deleted successfully!"
    except Exception as e:
        session.rollback()
        return False, f" Error deleting customer: {e}"
    finally:
        session.close()

def place_order_logic(customer_email, product_name, quantity):
    session = SessionLocal()
    try:
        customer = session.query(Customer).filter_by(email=customer_email).first()
        product = session.query(Product).filter_by(name=product_name).first()

        if not customer:
            return False, " Customer not found."
        if not product:
            return False, "Product not found."
        if product.stock_quantity < quantity:
            return False, " Not enough stock available."

        order = Order(customer_id=customer.id, product_id=product.id, quantity=quantity)
        product.stock_quantity -= quantity

        session.add(order)
        session.commit()
        return True, f" Order placed successfully for {quantity} x {product.name} by {customer.name}!"
    except ValueError:
        session.rollback()
        return False, " Invalid input. Quantity must be a number."
    except Exception as e:
        session.rollback()
        return False, f" Error placing order: {e}"
    finally:
        session.close()

def view_order_history_logic(customer_email):
    session = SessionLocal()
    try:
        customer = session.query(Customer).filter_by(email=customer_email).first()

        if not customer:
            return False, " Customer not found."

        orders_data = []
        for order in customer.orders:
            product = session.query(Product).get(order.product_id)
            orders_data.append({'quantity': order.quantity, 'product_name': product.name, 'product_price': product.price})
        return True, {'customer_name': customer.name, 'orders': orders_data}
    except Exception as e:
        return False, f" Error viewing order history: {e}"
    finally:
        session.close()
