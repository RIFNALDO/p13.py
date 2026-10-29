import random

def get_player_move():
    """Prompt the player to input their move and validate it."""
    while True:
        move = input("Enter your move (Rock, Paper, or Scissors): ").strip().capitalize()
        if move in ["Rock", "Paper", "Scissors"]:
            return move
        print("Invalid input! Please choose Rock, Paper, or Scissors.")

def get_ai_move():
    """Generate a random move for the AI opponent."""
    moves = ["Rock", "Paper", "Scissors"]
    return random.choice(moves)

def determine_winner(player, ai):
    """Determine the outcome of the round based on RPS rules."""
    if player == ai:
        return "tie"
    elif (
        (player == "Rock" and ai == "Scissors") or 
        (player == "Scissors" and ai == "Paper") or 
        (player == "Paper" and ai == "Rock")
    ):
        return "player"
    else:
        return "ai"

def play_game():
    """Main game loop to handle multiple rounds, scores, and exit option."""
    print("=== Welcome to Rock, Paper, Scissors with AI! ===")
    
    player_score = 0
    ai_score = 0
    
    while True:
        player_move = get_player_move()
        ai_move = get_ai_move()
        
        print(f"\nYou chose: {player_move}")
        print(f"AI chose: {ai_move}")
        
        winner = determine_winner(player_move, ai_move)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("Congratulations, you win this round!")
            player_score += 1
        else:
            print("AI wins this round!")
            ai_score += 1
            
        print(f"\nScoreboard -> You: {player_score} | AI: {ai_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Final Score:")
            print(f"You: {player_score} | AI: {ai_score}")
            break

if __name__ == "__main__":
    play_game()