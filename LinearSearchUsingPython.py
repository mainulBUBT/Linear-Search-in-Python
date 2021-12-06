def LinearSearch(search_number, Items):
    for i in range(len(Items)):
        if Items[i] == search_number:
            return i;

    return -1


Items = [10, 20, 5, 8]
search_number = int(input("Enter data to search: "))
result = LinearSearch(search_number, Items)

if result == -1:
    print("Not Value in List. ")
else:
    print("Found in Index: ", result)
