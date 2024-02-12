from replit import clear
import art


def add_bids(name, bid_amount):
    bids[name] = bid_amount


#HINT: You can call clear() to clear the output in the console.
more_player = "Yes"
print(art.logo)
bids = {}
higest_bid = 0
higest_bidder = ""
while more_player != "No":
    name = input("What is your name?")
    bid_amount = int(input("How much do you want to bid?"))
    add_bids(name, bid_amount)
    more_player = input("Is there any more bider (Yes/No)?")
    clear()
for biders in bids:
  if bids[biders] > higest_bid:
    higest_bid = bids[biders]
    higest_bidder = biders
print(f"The higest bid is {higest_bid}$ by {higest_bidder}")
