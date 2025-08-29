from lib.helpers import (
    add_product_logic,
    list_products_logic,
    update_product_logic,
    delete_product_logic,
    add_customer_logic,
    list_customers_logic,
    update_customer_logic,
    delete_customer_logic,
    place_order_logic,
    view_order_history_logic
)

def add_product():
    try:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock_quantity = int(input("Enter stock quantity: "))
        success, message = add_product_logic(name, price, stock_quantity)
        print(message)
    except ValueError:
        print(" Invalid input. Price and stock must be numbers.")

def list_products():
    products = list_products_logic()
    print("\n Available Products:")
    for p in products:
        print(f"ID: {p.id} | {p.name} | Price: ${p.price} | Stock: {p.stock_quantity}")

def update_product():
    try:
        product_id = int(input("Enter the ID of the product to update: "))
        new_name = input("Enter new name (or press Enter to skip): ")
        new_price_str = input("Enter new price (or press Enter to skip): ")
        new_stock_str = input("Enter new stock quantity (or press Enter to skip): ")
        success, message = update_product_logic(product_id, new_name, new_price_str, new_stock_str)
        print(message)
    except ValueError:
        print(" Invalid input. ID, price, and stock must be numbers.")

def delete_product():
    try:
        product_id = int(input("Enter the ID of the product to delete: "))
        confirm = input("Are you sure you want to delete this product? (y/n): ")
        if confirm.lower() == 'y':
            success, message = delete_product_logic(product_id)
            print(message)
        else:
            print(" Deletion canceled.")
    except ValueError:
        print(" Invalid input. ID must be a number.")

def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    success, message = add_customer_logic(name, email, phone)
    print(message)

def list_customers():
    customers = list_customers_logic()
    print("\n Customers:")
    for c in customers:
        print(f"ID: {c.id} | {c.name} | Email: {c.email} | Phone: {c.phone}")

def update_customer():
    try:
        customer_id = int(input("Enter the ID of the customer to update: "))
        new_name = input("Enter new name (or press Enter to skip): ")
        new_email = input("Enter new email (or press Enter to skip): ")
        new_phone = input("Enter new phone (or press Enter to skip): ")
        success, message = update_customer_logic(customer_id, new_name, new_email, new_phone)
        print(message)
    except ValueError:
        print(" Invalid input. ID must be a number.")

def delete_customer():
    try:
        customer_id = int(input("Enter the ID of the customer to delete: "))
        confirm = input("Are you sure you want to delete this customer? (y/n): ")
        if confirm.lower() == 'y':
            success, message = delete_customer_logic(customer_id)
            print(message)
        else:
            print(" Deletion canceled.")
    except ValueError:
        print(" Invalid input. ID must be a number.")

def place_order():
    try:
        customer_email = input("Enter customer email: ")
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        success, message = place_order_logic(customer_email, product_name, quantity)
        print(message)
    except ValueError:
        print(" Invalid input. Quantity must be a number.")

def view_order_history():
    customer_email = input("Enter customer email: ")
    success, result = view_order_history_logic(customer_email)
    if success:
        customer_name = result['customer_name']
        orders = result['orders']
        print(f"\n Order history for {customer_name}:")
        if orders:
            for order in orders:
                print(f"- {order['quantity']} x {order['product_name']} (Price: ${order['product_price']})")
        else:
            print(" No orders found for this customer.")
    else:
        print(result)

def main():
    while True:
        print("\n===  Online Store CLI ===")
        print("1. Add Product")
        print("2. List Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Add Customer")
        print("6. List Customers")
        print("7. Update Customer")
        print("8. Delete Customer")
        print("9. Place Order")
        print("10. View Order History")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            list_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            add_customer()
        elif choice == "6":
            list_customers()
        elif choice == "7":
            update_customer()
        elif choice == "8":
            delete_customer()
        elif choice == "9":
            place_order()
        elif choice == "10":
            view_order_history()
        elif choice == "11":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    main()
