from zambola_module import setup_game, check_number

nums, players, cuts = setup_game()

print("🎯 Zambola Game Start (First 5 cuts win!)")

while nums:
    input("Press Enter...")
    
    n = nums.pop(0)
    print("Number:", n)

    winner = check_number(players, cuts, n)

    if winner:
        print( winner, "WINS!")
        break
