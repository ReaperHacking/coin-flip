# random module
import random

# while loop and conditions
reflip = "Y"
while reflip == "Y":
  bet = input("Heads or Tails? (H/T): ").upper()
  if bet != "H" and bet != "T":
    print("INVALID, not H or T :/\n")
    continue

  # list to store and bot random choice and conditions
  heads_tails = ["H", "T"]
  h_or_t = random.choice(heads_tails)

  if bet == "H" and h_or_t == "H":
    print("You Win! It's Heads!\n")
  elif bet == "H" and h_or_t == "T":
    print("You Lose! It's Tails!\n")
  elif bet == "T" and h_or_t == "T":
    print("You Win! It's Tails!\n")
  elif bet == "T" and h_or_t == "H":
    print("You Lose! It's Heads!\n")

  # prompting user to retry
  reflip = input("Would you like to flip the coin again? (Y/N): \n").upper()

  # condition and message
  if reflip != "Y" and reflip != "N":
    print("INVALID NOT Y OR N TRY AGAIN :/")
    break

print("Thank you for playing! :)")



