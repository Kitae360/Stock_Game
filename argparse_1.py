import argparse
import arguments as data

class Argparse:
 def __init__(self):
  parser = argparse.ArgumentParser()
  parser.add_argument(
	'-current_price',
	nargs = '*', 
	help = "show the current price and a corresponding time. Argument: Name of a stock")

  parser.add_argument(
	'-price_change',
	nargs = '*', 
	help = "show the change of the price from the beginning to the end. Arguments: Name of the stock, Beginning(YYYY-MM-DD), Ending(YYYY-MM-DD)")

  args = parser.parse_args()
  if args.current_price != None:
	list = args.current_price
  	print data.current_price_function(list)
  elif args.price_change != None:
	list = args.price_change
  	print data.change_of_price_function(list)

Argparse()
