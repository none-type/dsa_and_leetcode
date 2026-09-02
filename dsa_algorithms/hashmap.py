# HashMap (dict) - key-value pairs, O(1) average lookup/insert/delete

# 1. CREATE
user = {
    "id": 101,
    "name": "Alice",
    "age": 30
}
print("Initial:", user)  # {'id': 101, 'name': 'Alice', 'age': 30}

# 2. INSERT / UPDATE - O(1)
user["email"] = "alice@email.com"  # insert new
user["age"] = 31                   # update existing
print("After updates:", user)

# 3. LOOKUP - O(1)
print("Name:", user.get("name"))        # Alice
print("Phone:", user.get("phone", "N/A"))  # N/A (default)

# 4. CHECK existence - O(1)
if "id" in user:
    print("ID exists:", user["id"])  # 101

# 5. DELETE - O(1)
removed = user.pop("age")  # removes 'age'
print(f"Removed age: {removed}, now:", user)

# 6. ITERATE keys, values, items
for key, value in user.items():
    print(f"{key} -> {value}")

# 7. COUNT frequency (common use case)
text = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = {}
for item in text:
    freq[item] = freq.get(item, 0) + 1
print("Frequency:", freq)  # {'apple': 3, 'banana': 2, 'orange': 1}

# 8. DEFAULT dict (avoids key checks)
from collections import defaultdict
word_count = defaultdict(int)
for word in text:
    word_count[word] += 1
print("DefaultDict count:", dict(word_count))

# Real-world uses: caching, indexing, counting, lookup tables, database indexes