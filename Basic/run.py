import argparse
import sys
import os.path
sys.path.insert(0, '../Common')
import stock_game as stock_game

def main():
	game = stock_game.Game_Runner()
	parser = argparse.ArgumentParser()

	parser.add_argument(
	'-new',
	nargs = '*', 
	help = "Requires one argument, name of the game file")

	parser.add_argument(
	'-start',
	nargs = '*', 
	help = "Requires one argument, name of the game file")

	parser.add_argument(
	'-end',
	nargs = '*', 
	help = "No argument required. Type it to end the game")
	
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
	help = "Check Stocks one the NASDAQ. NO argument required")

	parser.add_argument(
	'-check_money',
	nargs = '*', 
	help = "Check money that user has. NO arguments required")

	args = parser.parse_args()

	if args.new != None:
		input_list = args.new
		if len(input_list) != 1:
			print "Wrong number of arguments"
		else:
			output = game.make_new_game(input_list[0])
			if isinstance(output, basestring):
				print output
			else:
				return output
			
	elif args.start != None:
		input_list = args.start
		if len(input_list) != 1:
			print "Wrong number of arguments"
		else:
			game.start_game(input_list[0])

	elif args.end != None:
		input_list = args.start
		if input_list != None:
			print "Wrong number of arguments"
		else:
			game.end_game()

	elif args.buy != None:
		input_list = args.buy
		if len(input_list) != 2:
			print "Wrong number of arguments"
		else:
			name = input_list[0]
			quantity = input_list[1]
	  		output = game.buy_stock(name, quantity)
			if isinstance(output, basestring):
				print output
			else:
				print "Player Money: {}".format(output[0])
				print "Player Stock: {}".format(output[1])
	
	elif args.sell != None:
		input_list = args.sell
		if len(input_list) != 2:
			print "Wrong number of arguments"
		else:
			name = input_list[0]
			quantity = input_list[1]
	  		output = game.sell_stock(name, quantity)
			if isinstance(output, basestring):
				print output
			else:
				print "Player Money: {}".format(output[0])
				print "Player Stock: {}".format(output[1])

	elif args.check_owned_stocks != None:
	  	print game.show_player_stocks()

	elif args.check_NASDAQ != None:
		print game.show_NASDAQ()

	elif args.check_money != None:
	  	print game.show_money()

if __name__ == "__main__":
    main()
