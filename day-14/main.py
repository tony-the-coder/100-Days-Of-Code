# Import needed files for the game
from art import logo, vs
from game_data import data
import random

"""Format data to match the example"""


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_answer, a_follower_count, b_follower_count):
    """Check if answer is correct when comparing A and B"""
    if a_follower_count > b_follower_count:
        return user_answer == "a"
    else:
        return user_answer == "b"


# Display Art Import
print(logo)
score = 0
game_should_continue = True
account_a = random.choice(data)
account_b = random.choice(data)


"""Using a while loop to continue the game until the user gets the answer incorrect"""


while game_should_continue:
    # Random choice from data

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask the user for their guess

    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # Check if answer is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(user_answer, a_follower_count, b_follower_count)

    # Keep track of count of correct guess
    if is_correct:
        score += 1
        print(f"You are correct! Your current score is {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
