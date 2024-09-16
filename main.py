# Programmers: Owen and Rayan

# Course: CS151, Professor Z

# Due Date: 9/19/24

# Lab Assignment: 1

# Problem Statement: This equation is to solve the cost of a trip in miles

# Input the total miles of the trip, the miles per gallon, and the price per gallon
total_miles=int(input('Enter the total miles of trip:'))
miles_per_gallon=int(input('Enter the miles per gallon of car:'))
price_per_gallon=float(input('Enter the price per gallon:'))

# Output is the total cost of gas you have to spend
total_cost=float((total_miles/miles_per_gallon)*price_per_gallon)
print('Your total cost of the trip is',total_cost)

# Credits: Zybooks