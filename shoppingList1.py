shopping = []
how_many = input("how many items of shopping do you have? ")
how_many = int(how_many)
for item_number in range(how_many):
     item = input("what is the item " + str(item_number +1) + "? ")
     shopping.append(item)

print(shopping)

for (num, item) in enumerate(shopping):
        print("item", num + 1, item)
print()
print("total List Length is ", len(shopping))