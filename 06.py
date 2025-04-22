# Shopping list

errand_day = input("When are you going shopping? ")

number_of_items = input("How many items are you buying? ")

shoppingList = []

print("What are you buying?")

for i in range(1,int(number_of_items)+1):   
    item = input(" Add item: ")
    shoppingList.append(item)

print("\n")
print("You will be going shopping on", errand_day, "to buy: ")
print(shoppingList)