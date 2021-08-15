# Blake Scott 08/03/2021
size = input("Do you want small, medium, or large?")
if size == "small":
    size_price = float(2.0)
elif size == "medium":
    size_price = float(3.0)
elif size == "large":
    size_price = float(4.0)
else:
    print("invalid size. restart")
    quit()

type = input("Do you want brewed, espresso, or cold press?")

if type == "brewed":
    type_price = float(0.0)
elif type == "espresso":
    type_price = float(0.5)
elif type == "cold press":
    type_price = float(1.0)
else:
    print("invalid type. restart")
    quit()

flav = input("Do you want favored syrup?(yes or no)")

if flav == "yes":
    flav_type = input("Do you want hazelnut, vanilla, or caramel?")
    if flav_type == "hazelnut" or "vanilla" or "caramel":
        flav_price = float(.5)
        total = size_price + type_price + flav_price;
        print("You asked for a " + size + " cup of " + type + " coffee with " + flav_type + " syrup.")
        print("Your cup of coffee costs " + str(total))
        print("The price with a tip is " + str(total*1.15));
    else:
        print("invalid flavor type. restart")
        quit()

elif flav == "no":
    print("You asked for a " + size + " cup of " + type + " coffee")
    total = size_price + type_price;
    print("Your cup of coffee costs " + str(total))
    print("The price with a tip is " + str(total * 1.15))
else:
    print("not a yes or no. restart")
    quit()


