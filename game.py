mport random
import time
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0
        self.round_count = 0
        self.player_name = ""
        self.animations = {
            'rock': [
                "    _______",
                "---'   ____)",
                "      (_____)",
                "      (_____)",
                "      (____)",
                "---.__(___)"
            ],
            'paper': [
                "    _______",
                "---'   ____)____",
                "          ______)",
                "          _______)",
                "         _______)",
                "---.__________)"
            ],
            'scissors': [
                "    _______",
                "---'   ____)____",
                "          ______)",
                "       __________)",
                "      (____)",
                "---.__(___)"
            ]
        }
        self.taunts = [
            "Is that the best you've got?",
            "I'm just warming up!",
            "You're making this too easy!",
            "I can read your mind!",
            "Let's see if you can beat that!"
        ]
        self.compliments = [
            "Nice move!",
            "You're good at this!",
            "I didn't see that coming!",
            "Well played!",
            "You're a worthy opponent!"
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_title(self):
        title = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════╗
║ {Fore.YELLOW}  ____  ___   ____ _  __   ____   _    ____  _____ {Fore.CYAN} ║
║ {Fore.YELLOW} |  _ \\/ _ \\ / ___| |/ /  |  _ \\ / \\  |  _ \\| ____| {Fore.CYAN}║
║ {Fore.YELLOW} | |_) | | | | |   | ' /   | |_) / _ \\ | |_) |  _|   {Fore.CYAN}║
║ {Fore.YELLOW} |  _ <| |_| | |___| . \\   |  __/ ___ \\|  __/| |___  {Fore.CYAN}║
║ {Fore.YELLOW} |_| \\_\\\\___/ \\____|_|\\_\\  |_| /_/   \\_\\_|   |_____| {Fore.CYAN}║
║ {Fore.YELLOW}  ____   ____ ___ ____ ____   ___  ____  ____       {Fore.CYAN}║
║ {Fore.YELLOW} / ___| / ___|_ _/ ___|/ ___| / _ \\|  _ \\/ ___|      {Fore.CYAN}║
║ {Fore.YELLOW} \\___ \\| |    | |\\___ \\\\___ \\| | | | |_) \\___ \\      {Fore.CYAN}║
║ {Fore.YELLOW}  ___) | |___ | | ___) |___) | |_| |  _ < ___) |     {Fore.CYAN}║
║ {Fore.YELLOW} |____/ \\____|___|____/|____/ \\___/|_| \\_\\____/      {Fore.CYAN}║
╚═══════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(title)

    def get_player_name(self):
        self.clear_screen()
        self.print_title()
        self.player_name = input(f"{Fore.GREEN}Enter your name, challenger: {Style.RESET_ALL}")
        if not self.player_name.strip():
            self.player_name = "Player"
        return self.player_name

    def display_animation(self, choice):
        for line in self.animations[choice]:
            print(line)
            time.sleep(0.1)

    def display_rules(self):
        self.clear_screen()
        self.print_title()
        print(f"{Fore.YELLOW}=== GAME RULES ==={Style.RESET_ALL}")
        print(f"{Fore.WHITE}• Rock crushes Scissors")
        print(f"• Scissors cuts Paper")
        print(f"• Paper covers Rock")
        print(f"\n{Fore.YELLOW}=== HOW TO PLAY ==={Style.RESET_ALL}")
        print(f"{Fore.WHITE}• Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors")
        print(f"• First to win {Fore.GREEN}5 rounds{Style.RESET_ALL} is the champion!")
        print(f"• Enter 'q' at any time to quit the game")
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

    def get_player_choice(self):
        while True:
            choice = input(f"\n{Fore.GREEN}{self.player_name}, make your move (r)ock, (p)aper, (s)cissors, or (q)uit: {Style.RESET_ALL}").lower()
            
            if choice == 'q':
                return 'quit'
            elif choice in ['r', 'rock']:
                return 'rock'
            elif choice in ['p', 'paper']:
                return 'paper'
            elif choice in ['s', 'scissors']:
                return 'scissors'
            else:
                print(f"{Fore.RED}Invalid choice! Try again.{Style.RESET_ALL}")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            return "player"
        else:
            return "computer"

    def update_score(self, winner):
        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1

    def display_score(self):
        print(f"\n{Fore.YELLOW}=== SCORE ==={Style.RESET_ALL}")
        print(f"{Fore.GREEN}{self.player_name}: {self.player_score}{Style.RESET_ALL}")
        print(f"{Fore.RED}Computer: {self.computer_score}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Round: {self.round_count}{Style.RESET_ALL}")

    def display_result(self, player_choice, computer_choice, winner):
        print(f"\n{Fore.CYAN}You chose: {player_choice.upper()}{Style.RESET_ALL}")
        self.display_animation(player_choice)
        
        print(f"\n{Fore.MAGENTA}Computer chose: {computer_choice.upper()}{Style.RESET_ALL}")
        self.display_animation(computer_choice)
        
        if winner == "tie":
            print(f"\n{Fore.YELLOW}It's a tie!{Style.RESET_ALL}")
        elif winner == "player":
            print(f"\n{Fore.GREEN}You win this round! {random.choice(self.compliments)}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}Computer wins this round! {random.choice(self.taunts)}{Style.RESET_ALL}")

    def play_round(self):
        self.round_count += 1
        self.clear_screen()
        self.print_title()
        print(f"{Fore.YELLOW}=== ROUND {self.round_count} ==={Style.RESET_ALL}")
        
        player_choice = self.get_player_choice()
        if player_choice == 'quit':
            return False
        
        print(f"\n{Fore.CYAN}Rock...{Style.RESET_ALL}")
        time.sleep(0.7)
        print(f"{Fore.CYAN}Paper...{Style.RESET_ALL}")
        time.sleep(0.7)
        print(f"{Fore.CYAN}Scissors...{Style.RESET_ALL}")
        time.sleep(0.7)
        print(f"{Fore.YELLOW}Shoot!{Style.RESET_ALL}")
        
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(player_choice, computer_choice)
        
        self.display_result(player_choice, computer_choice, winner)
        self.update_score(winner)
        self.display_score()
        
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
        return True

    def display_final_result(self):
        self.clear_screen()
        self.print_title()
        print(f"\n{Fore.YELLOW}=== FINAL SCORE ==={Style.RESET_ALL}")
        print(f"{Fore.GREEN}{self.player_name}: {self.player_score}{Style.RESET_ALL}")
        print(f"{Fore.RED}Computer: {self.computer_score}{Style.RESET_ALL}")
        
        if self.player_score > self.computer_score:
            print(f"\n{Fore.GREEN}Congratulations, {self.player_name}! You are the champion!{Style.RESET_ALL}")
        elif self.computer_score > self.player_score:
            print(f"\n{Fore.RED}The computer wins this time! Better luck next time, {self.player_name}!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}It's a tie! Great match, {self.player_name}!{Style.RESET_ALL}")

    def play_game(self):
        self.get_player_name()
        self.display_rules()
        
        game_active = True
        while game_active and self.player_score < 5 and self.computer_score < 5:
            game_active = self.play_round()
        
        if game_active:  # Only show final result if player didn't quit
            self.display_final_result()
        
        play_again = input(f"\n{Fore.CYAN}Would you like to play again? (y/n): {Style.RESET_ALL}").lower()
        if play_again == 'y':
            self.__init__()  # Reset the game
            self.play_game()
        else:
            self.clear_screen()
            print(f"{Fore.YELLOW}Thanks for playing Rock Paper Scissors! Goodbye!{Style.RESET_ALL}")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
