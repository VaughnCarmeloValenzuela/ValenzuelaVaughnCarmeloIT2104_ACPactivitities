set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

union_set = set1.union(set2)

symmdiff_set1 = set2.symmetric_difference(set1)
symmdiff_set2 = set1.symmetric_difference(set2)

intersection_set1 = set1.intersection(set2)
intersection_set2 = set2.intersection(set1)

print("Set Difference")
print(difference_set1)
print(difference_set2)
print("Union of Sets")
print(union_set)
print("Symmetric Difference")
print(symmdiff_set1)
print(symmdiff_set2)
print("Set Intersection")
print(intersection_set1)
print(intersection_set2)