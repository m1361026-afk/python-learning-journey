# Store book information
book = {
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "price": 1200,
    "available_copies": 3
}

print("Original book:")
for key, value in book.items():
    print(f"{key}: {value}")

book["price"] = 1050
book["available_copies"] = 2
book["category"] = "Programming"

if "isbn" in book:
    print(book["isbn"])
else:
    print("ISBN information is not available.")

print("Updated book:")
for key, value in book.items():
    print(f"{key}: {value}")
print(f"Number of fields: {len(book)}")