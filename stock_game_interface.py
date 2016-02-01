import argparse
import stock_game as game

class Interface:

	def __init__(self):
		game_1 = game.Game_Runner()
		parser = argparse.ArgumentParser()
		
		parser.add_argument(
		'-buy',
		nargs = '*', 
		help = "Requires two arguments, name of the stock and quantity")

		parser.add_argument(
		'-sell',
		nargs = '*', 
		help = "Requires two arguments, name of the stock and quantity")

		parser.add_argument(
		'-check_owned_stocks',
		nargs = '*', 
		help = "Check user's stocks. NO arguments required")

		parser.add_argument(
		'-check_NASDAQ',
		nargs = '*',
		help = "Check Stocks one the NASDAQ. One argument required: Fisrt Character of the stock")

		parser.add_argument(
		'-check_money',
		nargs = '*', 
		help = "Check money that user has. NO arguments required")

		args = parser.parse_args()
		if args.buy != None:
			list = args.buy
			if len(list) != 2:
				print "Wrong number of arguments"
			else:
		  		print game_1.buy_stock(list)

		if args.sell != None:
			list = args.sell
			if len(list) != 2:
				print "Wrong number of arguments"
			else:
		  		print game_1.sell_stock(list)

		elif args.check_owned_stocks != None:
		  	game_1.show_player_stocks()

		elif args.check_NASDAQ != None:
			list = args.check_NASDAQ
			if len(list) != 1:
				print "Wrong number of argument"
			else:
		  		game_1.show_NASDAQ(list)

		elif args.check_money != None:
		  	game_1.show_money()

Interface()
