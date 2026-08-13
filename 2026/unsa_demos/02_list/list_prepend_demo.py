values_with_insert = [20, 30]
values_with_insert.insert(0, 10)

print("list.insert(0, 10)")
print(values_with_insert)
print()

values_with_prepend = [20, 30]
result = values_with_prepend.prepend(10)

print("list.prepend(10)")
print(values_with_prepend)
print("Return value:", result)
print()

print("Same result:", values_with_insert == values_with_prepend)
