import random

# Dictionary with the first Hiragana letters
Work_japanese = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so"
}

print("=" * 40)
print("     Nihongo Quiz - Try Hiragana!     ")
print("=" * 40)
print("Instructions: Look at the symbol and type the correct sound.")
print("Type 'exit' anytime to end the program.\n")

life = 3
points = 0
play = True

# Convert dictionary keys into a list for random selection
symbols = list(Work_japanese.keys())

while play:
    # Draw a random symbol
    symbol_drawn = random.choice(symbols)
    correct_answer = Work_japanese[symbol_drawn]
    
    print("-" * 20)
    print(f"❤️  Lives left: {life}")
    print(f"What is the sound of this symbol? ->  {symbol_drawn}  <-")
    
    guess = input("Your answer: ").strip().lower()
    
    if guess == 'exit':
        play = False
        print("\nEnding game!!")
    elif guess == correct_answer:
        print("🟢 Right! Good job!\n")
        points += 1
    else:
        print(f"🔴 Wrong... the correct answer is: '{correct_answer}'\n")
        life -= 1 
        
        if life == 0:
            print('💀 Game Over!')
            break
        
print("=" * 40)
print(f"Endgame! You scored {points} points.")
print("Keep practicing!")
print("=" * 40)