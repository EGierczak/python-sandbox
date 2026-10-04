shopping_list = ["milk", "bread", "cucumber"]
print(shopping_list)
shopping_list.append(input("Add another product to the list: "))
print(shopping_list)
shopping_list.remove(shopping_list[0])
print(shopping_list)
shopping_list[1] = "mango"
print(shopping_list)

for number, item in enumerate(shopping_list, start=1):
    print(f"{number}. {item}")
print(f"There ane {len(shopping_list)} products on the list.")