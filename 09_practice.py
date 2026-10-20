prices = {
    "Keyboard": 1200,
    "Mouse": 500,
    "Headphones": 1500
}

total = 0

for product, price in prices.items():
    total = total + price

print("Total:", total)