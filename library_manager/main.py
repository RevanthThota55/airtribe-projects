from models import LibraryItem, Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 45)
dvd = DVD("Planet Earth", 3, 120)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

print("--- Borrowing ---")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)
except ValueError as e:
    print("Could not borrow:", e)

print("Alice has:", alice.borrowed_titles())
print("Bob has:", bob.borrowed_titles())

print()
print("--- Returning ---")
try:
    alice.return_item(dvd)
except ValueError as e:
    print("Could not return:", e)

try:
    fee = alice.return_item(book, 4)
    print("Alice returned Python 101, 4 days late. Fee: Rs", fee)
    fee = bob.return_item(magazine)
    print("Bob returned Tech Today on time. Fee: Rs", fee)
except ValueError as e:
    print("Could not return:", e)

print("Alice has:", alice.borrowed_titles())
print("Bob has:", bob.borrowed_titles())

print()
print("--- Late fees ---")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

print()
print("--- Encapsulation ---")
try:
    print(book.__available)
except AttributeError as e:
    print("Error:", e)
print("Python 101 available?", book.is_available())

print()
print("--- Abstract class ---")
try:
    x = LibraryItem("x", 1)
except TypeError as e:
    print("Error:", e)

print()
print("Total items created:", Book.total_items)
