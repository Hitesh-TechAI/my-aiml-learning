## Day 3 – Lists and Tuples

### Lists

List is a built-in data type that stores a collection of values.

- Lists are mutable
- Elements are accessed using index (same as strings)
- Length can be found using `len()`
- Slicing works same as strings
- Negative slicing is supported

### List Functions

- `len(list)`
- `list.append(element)` → adds element at end
- `list.sort()` → ascending order
- `list.sort(reverse=True)` → descending order
- `list.reverse()` → reverses list
- `list.insert(index, element)` → inserts element
- `list.remove(element)` → removes first occurrence
- `list.pop(index)` → removes element at index
- `list.pop()` → removes last element

---

### Tuples

Tuple is an immutable sequence of values.

- Defined by comma
- Parentheses are optional but recommended
- Slicing is possible

### Tuple Functions

- `tup.index(element)` → returns index of first occurrence
- `tup.count(element)` → counts occurrences
