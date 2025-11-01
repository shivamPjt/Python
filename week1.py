# # Q1. Write a Python program to swap two variables.
# a = 9
# b = 90
# print("a = ",a)
# print("b = ", b)
# # METHOD 1
# c=a
# a=b
# b = c

# print("After swap")
# print("a = ",a)
# print("b = ", b)

# -----------------------------------------

# # Q2. Take user input and display it back to the user.
# a = int(input("Enter a number: "));
# print(a);
# print(type(a));

# -----------------------------------------

# # Q3. Write a program to check if a number is even or odd.
# a = int(input("Enter the number: "));
# if(a%2==0):
#     print(a,"is even");
# else:
#     print(a,"is odd");

# -----------------------------------------

# # Q4. Create a program that prints the multiplication table of a given number.
# a = int(input("Enter the number: "));
# for i in range(1,11):
#     print(a ,"*", i ,"=", a*i);

# -----------------------------------------

# # Q5. Write a program to find the largest of three numbers.
# a = int(input("Enter the number: "));
# b = int(input("Enter the number: "));
# c = int(input("Enter the number: "));
# if(a>b and a>c):
#     print(a,"is greater.");
# elif(b>a and b>c):
#     print(b,"is greater.");
# else:
#     print(c,"is greater.");

# -----------------------------------------

# # Q6. Convert temperature from Celsius to Fahrenheit.
# temp = float(input("Enter the temperature in celsius: "));
# print("Temperature in Fahrenheit is:",(temp * 9/5) + 32);

# -----------------------------------------

# # Q7. Write a program to calculate the factorial of a number using a loop.
# a = int(input("Enter the number: "));
# b = 1;
# for i in range(a,0,-1):
#     b *= i;
# print("Factorial of a number:", b);

# -----------------------------------------

# # Q8. Create a program to count the number of vowels in a string.
# a = str(input("Enter a string: "));
# count = 0;
# for i in a:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i =='I' or i == 'O' or i == 'U'):
#         count += 1;
# print("Number of vowels in a string: ", count);

# -----------------------------------------

# # Q9. Write a Python script to reverse a given string.
# a = str(input("Enter a string: "));
# print(a[::-1]);

# -----------------------------------------

# # Q10. Check if a number is a palindrome.
# import math;
# a = int(input("Enter the number: "));
# b = a;
# ans = 0;
# while(b):
#     ans = (ans*10) + (b%10);
#     b = math.floor(b / 10);

# if(ans == a):
#     print(a,"is palindrome.");
# else:
#     print(a,"is not palindrome.");

# -----------------------------------------

# # Q11. Write a program to find the sum of first N natural numbers.
# a = int(input("Enter the number: "));
# sum = 0;
# for i in range(1,a+1):
#     sum += i;
# print("The sum of first N natural numbers:",sum);

# -----------------------------------------

# # Q12. Create a number guessing game.
# import random;
# print("You have 5 life...");
# print("Guess the number.... : ");
# com = random.randint(1,100);
# print(com);
# life = 4;
# while(1):
#     a = int(input("Enter the number: "));
#     if(life and a>com):
#         print("Number is Smaller...  and life is:", life);
#         life -= 1;
#     elif(life and a<com):
#         print("Number is Greater...  and life is:", life);
#         life -= 1;
#     elif(a==com):
#         print("You guessed correct🥳🥳🥳...");
#         break;
#     else:
#         print("Zero life \nYou loose...");
#         break;

# -----------------------------------------

# # Q13. Write a program to print all prime numbers between 1 and 100.
# for i in range(2,101):
#     prime = True;
#     for j in range(2,int(i**0.5)+1):
#         if(i%j==0):
#             prime = False
#             break;
#     if(prime):
#         print(i);

# -----------------------------------------

# # Q14. Check if a given year is a leap year or not.
# a = int(input("Enter a year: "));
# if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
#     print(a, "is a leap year.");
# else:
#     print(a, "is not a leap year.");

# -----------------------------------------

# Q15. Create a program to print the Fibonacci series up to N terms.

