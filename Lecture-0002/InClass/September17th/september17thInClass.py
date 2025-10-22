temp = 70
tempTomorrow = 90
tempYesterday = 59

if temp == tempYesterday:
    print("temp is same as yesterday")

if temp == tempTomorrow:
    print("temp is same as tomorrow")

if temp == tempYesterday or temp == tempTomorrow:
    print("temp is the same as tomorrow or yesterday")


if temp == tempYesterday or temp == tempTomorrow:
    if temp == tempTomorrow:
        print("temp is same as tomorrow")
    elif temp == tempYesterday:
        print("temp is same as yesterday")


itemPrice = 78.90
otherItem = 67.982
gas = 4563.123

print(f"{itemPrice:.4f}")
print(f"{otherItem:.1f}")
print(f"{gas:10.2f}")
print("{}".format(gas))