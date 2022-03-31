"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: When input is not a number.

2. When will a ZeroDivisionError occur?
Answer: When denominator input is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Use "while" loop. Display "denominator cannot divide by zero!" behind line 18
"""

valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator(denominator cannot divide by zero!): "))
        fraction = numerator / denominator
        print(fraction)
        valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

print("Finished.")
