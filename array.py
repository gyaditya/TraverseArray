#Traversing through Array

# 1
results = ["Yes", "No", "Mabye", "No", "Mabye", "Yes", "Yes", "No", "Mabye", "Mabye"]

county = 0
countno = 0
countm = 0

for i in range (len(results)):
    if results[i] == "Yes":
        county += 1
    elif results[i] == "No":
        countno += 1
    elif results[i] == "Mabye":
        countm += 1

#2

ages = [2, 5, 23, 52, 12, 18, 23, 35, 74, 27, 44]

ofAge = 0

notOfAge = 0
for i in range(len(ages)):
    if ages[i] < 18:
        notOfAge += 1
    else:
        ofAge += 1

#3

prices = [12, 52, 1, 125, 623, 23, 74, 123, 33, 49, 25, 28, 20]

less20 = 0
more50 = 0
btwn = 0
for i in range(len(prices)):
    if prices[i] < 20:
        less20 += 1
    elif prices[i] >= 50:
        more50 += 1
    else:
        btwn += 1

for i in range(len(prices)):
    prices[i] += 2

for i in range(len(prices)):
    prices[i] *= 1.05

for i in range(len(prices)):
    prices[i] *= 0.8
