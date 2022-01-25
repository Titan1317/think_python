"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 7, Exercise 7-2
by Allen Downey
    Code written by Mustafa Ali.
"""

def eval_loop() -> None:
    """Iteratively prompts the user to enter a mathematical expression,
        evaluates it, and prints the value of the given expression.\n
        Enter 'done' to exit the loop."""
    while True:
        user_in = input('Enter a mathematical expression\n')
        if user_in == 'done':
            print(result)
            break
        result = eval(user_in)
        print(result)


if __name__ == '__main__':
    eval_loop()
