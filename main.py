def bidding_exit():
  print("You are now leaving the auction. Have a nice day!")

def item_listing():
  item_name = input("Let's list an item.\nWhat is the item?\n")
  item_price = int(input("How much is the " + item_name + "?\n"))
  print(f"The price of {item_name} is {item_price}")
  return item_price

def bidding_cycle(item_price):
  days = int(input("How many days is the item on auction?\n"))
  user_is_bidding = input("Would you like to join the bidding?\nEnter yes or no.\n")
  not_first_bid = 0
  bid = 0

  if (user_is_bidding != 'Y'):
    bidding_exit()

  while (user_is_bidding == 'Y' and bid < item_price and days >= 0):
    if (days == 0):
      print("The bidding for this item has ended. Please try again next time")
      break

    if (days == 1):
      print("Today is the last day to bid!\n")
    else:
      print(f"There are {days} days left to bid.\n")

    days = days - 1

    if (not_first_bid == 1):
      user_is_bidding = input("If you would like to continue bidding, press Y.\n")

    not_first_bid = 1

    if (user_is_bidding == 'Y'):
      bid = int(input("How much would you like to bid?\n"))

      if (bid >= item_price):
        print(f"Congratulations! You won the item.\nPlease pay {bid} to the Auction.")

    else:
      bidding_exit()

item_price = item_listing()

bidding_cycle(item_price)
  