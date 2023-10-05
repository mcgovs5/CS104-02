# CS104
# Jack McGovern
# conditions.py
i = 1
while i <= 5:
    temp = int(input("Please enter the current temperature: "))
    if temp > 90:
        print("Wear Shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 32:
        print("Wear a heavy coat")
    else:
        print("Stay Inside")
    i +=1
