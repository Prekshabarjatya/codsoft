from random import choice
# Function to get the user's choice
print("Welcome to the classic Rock, Paper, Scissors!. You have 5 chances in this game.")
def get_user_choice():
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_input
# Function to get the computer's choice
def get_computer_choice():
    return choice(["rock", "paper", "scissors"])
# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"  
    return "You lose!"
# Main function to run the game multiple trials
def play_game(num_trials=1):
    for _ in range(num_trials):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")        
        result = determine_winner(user_choice, computer_choice)
        print(result)
if __name__ == "__main__":
    play_game(num_trials=5)

