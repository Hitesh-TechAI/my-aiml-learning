## Day 2 – Strings & Conditional Statements

### String
String is a data type that stores a series of characters.

### Multiline Strings
Multiline strings are possible in Python using triple quotes:
''' '''
or
""" """

Escape sequence `\n` is used to insert a new line inside a string.

---

### Operations on String
1. Concatenation
2. Length of string using `len()`

---

### Indexing
- Helps access individual characters
- Index starts from 0
- Strings are immutable (cannot be modified)

---

### Slicing
Accessing a part of a string.

Examples:
- `str[:4]` → same as `str[0:4]`
- `str[1:]` → from index 1 to end
- `str[1:4]` → index 1 to 3 (4 excluded)

Negative indexing is supported (starts from -1).

---

### String Functions
- `str.endswith("er")`
- `str.capitalize()` → returns new string
- `str.replace(old, new)`
- `str.find(word)` → returns index or -1
- `str.count(word)`

---

### Conditional Statements

#### if-elif-else
```python
if condition:
    statement1
elif condition:
    statement2
else:
    statementN