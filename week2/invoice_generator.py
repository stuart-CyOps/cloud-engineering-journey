# invoice_generator.py
# Week 2 Project - Python Invoice Generator (Text Version)

from datetime import datetime

def create_invoice():
    print("=== Invoice Generator ===\n")
    
    customer = input("Enter customer name: ").strip()
    if not customer:
        customer = "Valued Customer"
    
    items = []
    total = 0.0
    
    print("\nEnter line items (type 'done' when finished):")
    
    while True:
        description = input("Item description (or 'done'): ").strip()
        if description.lower() == "done":
            break
        
        try:
            amount = float(input("Amount (R): "))
            items.append((description, amount))
            total += amount
        except ValueError:
            print("Please enter a valid number.")
    
    if not items:
        print("No items added. Exiting.")
        return
    
    vat_rate = 0.15
    vat_amount = total * vat_rate
    grand_total = total + vat_amount
    
    # Generate invoice text
    invoice_date = datetime.now().strftime("%Y-%m-%d")
    invoice_number = f"INV-{datetime.now().strftime('%Y%m%d%H%M')}"
    
    invoice_text = f"""
======================================
           TAX INVOICE
======================================
Invoice Number: {invoice_number}
Date:           {invoice_date}
Customer:       {customer}

Item Description               Amount
--------------------------------------
"""
    
    for desc, amt in items:
        invoice_text += f"{desc:<30} R {amt:>8.2f}\n"
    
    invoice_text += f"""--------------------------------------
Subtotal:                      R {total:>8.2f}
VAT (15%):                     R {vat_amount:>8.2f}
======================================
TOTAL DUE:                     R {grand_total:>8.2f}
======================================
"""
    
    # Save to file
    filename = f"{invoice_number}.txt"
    with open(filename, "w") as f:
        f.write(invoice_text)
    
    print(f"\n✅ Invoice saved as: {filename}")
    print(invoice_text)


if __name__ == "__main__":
    create_invoice()
