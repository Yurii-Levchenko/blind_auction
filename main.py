import art
from replit import clear
print(art.logo)

info = {"names": [],
       "bids": []}
n = 0

def filling(name, bid):
  info["names"].insert(n, name)
  info["bids"].insert(n, bid)

def calc():
  biggest_bid = max(info["bids"])
  win_index = info["bids"].index(biggest_bid)
  winner = info["names"][win_index]
  
  print(f"The winner is {winner} with a biggest bid of {biggest_bid}")

last_bid = False

while not last_bid:
  p_name = input("What's your name? ")
  p_bid = input("What's your bid? ")
  filling(p_name, p_bid)
  n += 1

  is_more = input("Is there other bidders? (yes / no) ")
  if is_more == "yes":
    clear()
  elif is_more == "no":
    last_bid = True
    clear()
    calc()
