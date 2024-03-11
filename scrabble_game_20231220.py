# File: game 2
# Purpose: players should take turns choosing numbers from 1 to 9,
#          The player who collects three numbers that add up to 15 wins.
# Author: Nouran Mahmoud Mahmoud Mohamed Elsayed Hegazy
# ID: 20231220

def check_sum15(player):
    if len(player) < 3:
        return False

    # Iterate through all combinations of three numbers
    for i in range(len(player)):   #[ 5 , 6 , 7 , 3 , 1 , 4 ] 
        for j in range(i + 1, len(player)):
            for k in range(j + 1, len(player)):
                if player[i] + player[j] + player[k] == 15:
                    return True
    return False


def check_empty(numbers):   #Checks if the list of numbers is empty.

    return not numbers   #Returns: bool: True if the list is empty, False otherwise.


def print_update(player1, player2):   #Prints the numbers chosen by each player.
    print("Player 1's numbers are:", player1)
    print("Player 2's numbers are:", player2)


def main_scrabble_game():  # Runs the Number Scrabble Game.
    try: #try/Except to prevent user from entering anything other than numbers

        while True :
            
            # Welcome message and game rules
            print("===============================================================================")
            print("----------------------- Welcome to Number Scrabble Game!-----------------------")
            print("-------------------------------------------------------------------------------")
            print("Rules:--> - Each player takes turns picking a number from the list.")
            print("- Once a number is picked, it cannot be chosen again.")
            print("- If a player picks three numbers that add up to 15, that player wins the game.")
            print("- If all numbers are used and no player gets exactly 15, the game is a draw.")
            print("===============================================================================")

            # Initiate number lists
            number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            player1 = []
            player2 = []

            while True:  # Loop until the number list is empty
                # Player 1's turn
                print("Player 1, choose a number from:", number_list)
                user1_choice = int(input("-----> "))
                
                while user1_choice not in number_list:
                    user1_choice = int(input("Player 1, Please select a valid number\n=====>"))
                    
                player1.append(user1_choice)
                number_list.remove(user1_choice)
                print_update(player1, player2)

                # Check if player 1 wins
                if check_sum15(player1):
                    print("Player 1 is the winner")
                    break
                
                is_empty = check_empty(number_list)
                if is_empty == True:
                    print_update(player1, player2)
                    print("The Game is a Draw")
                    break
                
                # Player 2's turn
                print("Player 2, choose a number from:", number_list)
                user2_choice = int(input("-----> "))
                
                while user2_choice not in number_list:
                    user2_choice = int(input("Player 2, Please select a valid number\n=====>"))
                    
                player2.append(user2_choice)
                number_list.remove(user2_choice)
                print_update(player1, player2)

                # Check if player 2 wins
                if check_sum15(player2):
                    print("Player 2 is the winner")
                    break
                
            print("Game over!")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes': # Exit Game if player diidn't choose yes 
                print("Thanks for using our Game")
                break
            print("\n==========================================================\n")


    except ValueError:
        print("Invalid input. Restart the game and enter only numbers.")

# Run the game
main_scrabble_game()

