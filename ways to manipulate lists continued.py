cowherd = ["Daisy", "Milkshake", "Ermintrude", "Ermintrude"]
print(cowherd)
birthyears = [1993, 2001, 2008]
print("")
#find length of a list
result = len(cowherd)
print("The cow herd contains", result, " cows.")
#find specific value in the list
cowName = "Ermintrude"
result = cowherd.count(cowName)
if result >1 :
    print("Too many cows called " + cowName)
else:
    print("Only one cow called " + cowName)
print("")
#appending 2 lists
cowHerd2 = ["Lucy", "Mathilde", "Buttercup"]
print(cowherd)
print(cowHerd2)
cowherd.append(cowHerd2)
print(cowherd)
print("")
#sorting lists
bigHerd = ["Lucy", "Mathilde", "Buttercup", "Daisy", "Milkshake", "Ermintrude"]
print(bigHerd)
bigHerd.sort()
print(bigHerd)
print("")
#reverse sorting lists
print(bigHerd)
bigHerd.reverse()
print(bigHerd) 