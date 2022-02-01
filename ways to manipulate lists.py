cowherd = ["Daisy", "Milkshake", "Ermintrude"]
print(cowherd)
birthyears = [1993, 2001, 2008]
print("")
#append to a list
cowherd.append("Mathilde")
print(cowherd)
print("")
#insert to a list
cowherd.insert(1, "Lucy")
print(cowherd)
print("")
#different ways to remove items
cowherd.remove("Milkshake")
print(cowherd)
cowherd.pop(0)
print(cowherd)
cowherd.pop()
print(cowherd)
del cowherd[1]
print(cowherd)
print("")