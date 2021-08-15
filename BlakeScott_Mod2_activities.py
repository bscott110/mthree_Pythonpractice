#Blake Scott 08/05/2021
#Activity 1 thru 4
name = input("0.What is your name?")
age = input("1.How old are you?")
bd = input("2.What is your birthdate?")
live = input("3.Where do you live?")
occ = input("4.Whats your occupation?")

ulist0 = [name, age, bd, live, occ]
print(ulist0)

color = input("5.Fav color?")
song = input("6.Fav song?")

ulist0.append(color)
ulist0.append(song)
print(ulist0)


p = int(input("Enter the number of the question that you'd like to delete."))
ulist0.pop(p)
print(ulist0)

p1 = int(input("Enter the index of the question that you'd like to update."))
update = input("Enter your new value.")
ulist0[p1] = update
print(ulist0)

#Activity 5
flname = tuple(input("First and Last name?"))
prof = tuple(input("Current Profession?"))
cadd = tuple(input("Current address?"))
padd = tuple(input("Previous address?"))

t0 = tuple(flname+prof+cadd+padd)
print(t0)

#Activity 7
ulist1 = ["this", "is", "a", "test", "list", "1", "", "hi"]
ulist2 = []
for x in ulist1:
    if len(x) >= 2:
        ulist2.append(x)

print(ulist1)
print(ulist2)

