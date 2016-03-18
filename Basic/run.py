import argparse
import sys
import os.path
sys.path.insert(0, '../Common')
import stock_game as stock_game

def main():
	parser = argparse.ArgumentParser()
	
	parser.add_argument(
	'-buy',
	nargs = '*', 
	help = "Requires three arguments, symbol of the stock, quantity, game name")

	parser.add_argument(
	'-sell',
	nargs = '*', 
	help = "Requires three arguments, symbol of the stock, quantity, game name")

	parser.add_argument(
	'-check_owned_stocks',
	nargs = '*', 
	help = "Check user's stocks. Requires one argument, name of the game file")

	parser.add_argument(
	'-check_NASDAQ',
	nargs = '*',
	help = "Check Stocks one the NASDAQ. NO argument required")

	parser.add_argument(
	'-check_money',
	nargs = '*', 
	help = "Check money that user has. Requires one argument, name of the game file")

	parser.add_argument(
	'-current_price',
	nargs = '*', 
	help = "Check the price of the stock. One argument required, stock symbol")

	args = parser.parse_args()

	if args.buy != None:
		input_list = args.buy
		if len(input_list) != 3:
			print "Wrong number of arguments"
		else:
			try:
				name = input_list[0]
				quantity = input_list[1]
				file_name = input_list[2]
				game = stock_game.Game_Runner()
				game.dump(file_name)
		  		output = game.buy_stock(name, quantity)
				game.save_game(file_name)
				print "Player Money: {}".format(output[0])
				print "Player Stock: {}".format(output[1])
			except Exception as e:
				print type(e).__name__

	
	elif args.sell != None:
		input_list = args.sell
		if len(input_list) != 3:
			print "Wrong number of arguments"
		else:
			try:
				name = input_list[0]
				quantity = input_list[1]
				file_name = input_list[2]
				game = stock_game.Game_Runner()
				game.dump(file_name)
		  		output = game.sell_stock(name, quantity)
				game.save_game(file_name)
				print "Player Money: {}".format(output[0])
				print "Player Stock: {}".format(output[1])
			except Exception as e:
				print type(e).__name__

	elif args.check_owned_stocks != None:
		input_list = args.check_owned_stocks
		if len(input_list) != 1:
			print "Wrong number of arguments"
		else:
			file_name = input_list[0]
			if os.path.isfile('{}.pickle'.format(file_name)):
				game = stock_game.Game_Runner()
				game.dump(file_name)
		  		print game.show_player_stocks()
			else:
				print "Given game does not exist"

	elif args.check_NASDAQ != None:
		game = stock_game.Game_Runner()
		print game.show_NASDAQ()

	elif args.check_money != None:
		input_list = args.check_money
		if len(input_list) != 1:
			print "Wrong number of arguments"
		else:
			file_name = input_list[0]
			if os.path.isfile('{}.pickle'.format(file_name)):
				game = stock_game.Game_Runner()
				game.dump(file_name)
		  		print game.show_money()
			else:
				print "Given game does not exist"

	elif args.current_price != None:
		input_list = args.current_price
		if len(input_list) != 1:
			print "Wrong number of arguments"
		else:
			try:
				game = stock_game.Game_Runner()
				price = game.check_price(input_list[0])
				print "Stock Name: {}".format(input_list[0])
				print "Price: {}".format(price)
			except Exception as e:
				print type(e).__name__

	else:
		print "Type 'python run.py -h' to find what you can do!"

if __name__ == "__main__":
    main()
