# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 1:
    print("Not leap Year")
elif year % 100 == 1:
    print("Leap Year")
elif year % 400 == 1:
    print("Not leap year")
else:
    print("Leap Year")
     


