# Below is a nested dictionary that explains how a linkes list is constructed
# Let the linked list be: 11,3,23,7
head = {"value": 11, "next": {"value": 3, "next": {"value": 23, "next": {"value": 7, "next": None}}}}

print(head["next"]["next"]["value"])

# If it were a linked list: print(my_linked_list.head.next.next.value)
