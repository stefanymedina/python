# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!
total_donations = 0

# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
for v in donations.values():
    total_donations += v


print(total_donations)  

#other function that you can use is sum example:

total = sum(donation for donation in donations.values())
print(f"total with function sum={total}")