# Read the users input for lives and multiplies by character
print("\nPlease enter the number of lives.")

lives = int(input())
liv = "♥" * lives

# Read the users input for energy and multiplies by character
print("\nPlease enter the energy level.")

energy = int(input())
ene = "*" * energy

# Read the users input for shield and multiplies by character
print("\nPlease enter the shield level.")

shield = int(input())
shi = "♦" * shield

# Displays the inputs
print("\nHealth has been set.")

print("\nLives:", liv)
print("Energy:", ene)
print("Shield:", shi)