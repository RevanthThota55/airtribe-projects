# Library Manager

A small library program for the OOP assignment. The library has books, magazines and DVDs, and members can borrow and return them. Wrong actions (like borrowing something that is already taken) give an error message instead of crashing the program.

## How to run

```
python main.py
```

On Mac/Linux use `python3 main.py`. It needs Python 3.12 or above and no extra packages.

## Files

- `models.py` - the classes (LibraryItem, Book, Magazine, DVD, Member)
- `main.py` - the demo
- `output.txt` - output from my final run

## Reflection

**1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?**

LibraryItem is abstract because nobody borrows a plain "library item", it is always a book, a magazine or a DVD, and each of them has a different late fee. Keeping it abstract means every child class has to write its own late_fee(). If DVD forgets it, the class itself still gets defined without any error, but as soon as I try to create a DVD object Python raises a TypeError saying it can't instantiate an abstract class.

**2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?**

I get an AttributeError saying the object has no attribute '__available'. This is because Python renames it to _LibraryItem__available behind the scenes, so the name I typed doesn't exist outside the class. We use is_available() because it only lets other code read the value, and the only way to change it is through mark_borrowed() and mark_returned(), so nobody can mess it up by mistake.

**3. What is the difference between LibraryItem.total_items and self.title?**

total_items is a class attribute, so there is just one copy of it and all the items share it. It goes up by 1 whenever any book, magazine or DVD is created, which is why it showed 3 in my output. self.title is an instance attribute, so every object has its own title and changing one object's title does not change the others.
