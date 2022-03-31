import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

Answer: 5 is the smallest number, 20 is the largest number.

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

Answer: 3 is the smallest number, 9 is the largest number.
        line 2 does not produce the number 4.

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

Answer: 2.5 is the smallest number, 5.5 is the largest number.

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

print(random.randint(1, 100))
