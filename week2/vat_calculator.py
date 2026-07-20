# vat_calculator.py

def calculate_vat(amount, rate=0.15):
    """Calculate VAT amount"""
    vat = amount * rate
    total = amount + vat
    return vat, total

# Test the function
amount = 2500
vat, total = calculate_vat(amount)

print(f"Amount: R{amount:.2f}")
print(f"Vat 15%: R{vat:.2f}")
print(f"Total: R{total:.2f}")
