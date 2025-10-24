def rock_paper_scissors():

    import random
    import emoji


    rock_emoji = "\U0001FAA8"
    paper_emoji = "\U0001F4C4"
    scissors_emoji = "\u2702\ufe0f"
    
    while True:

        system_choice = random.choice(['r', 'p', 's'])
        
        human_choice = input("Rock, paper or scissors? (r/p/s)").strip().lower()

        if human_choice == system_choice:
                print("Tie!") 
            
        elif human_choice not in ['r', 'p', 's']:
                print("Invalid choice! Please enter r, p, or s.\n")
                continue
            
        elif (human_choice == 'r' and system_choice == 's') or (human_choice == 'p' and system_choice == 'r') or (human_choice == 's' and system_choice == 'p'):
                print("You win")
            
        elif (human_choice == 'r' and system_choice == 'p') or (human_choice == 'p' and system_choice == 's') or (human_choice == 's' and system_choice == 'r'):
                print("You lose")

        

rock_paper_scissors()

