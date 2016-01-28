from list_stock import existing_stocks
from yahoo_finance import Share

class Game(object):

	def __init__(self):
		self.money = 5000
		self.player_stocks = {}
		self.stock_list = existing_stocks

	def show_player_stocks(self):
		print self.player_stocks

	def show_money(self):
		print self.money

	def show_NASDAQ(self):
		print self.stock_list

	def check_stock_in_list(self, stock_name):
		if self.player_stocks.get(stock_name) == None:
			return False
		else:
			return True

	def check_stock_exist_in_NASDAQ(self, stock_name):
		if self.stocks_list.get(stock_name) == None:
			return False
		else:
			return True

	def quantity_check(self, name, quantity):
		return self.stocks[name] > quantity

	def check_current_price_stock(self, stock_name):
 		stock = Share('{}'.format(stock_name))
 		return stock.get_price()

	def calculate_money(self, stock_name, quantity):
		stock_price = self.check_current_price_stock(stock_name)
		total_price = quantity * float(stock_price)
		return total_price

	def enough_money(self, stock_name, quantity):
		return self.money >= calculate_money(stock_name, quantity)

	def add_money(self, stock_name, quantity):
		total_price = calculate_money(self, stock_name, quantity)
		return self.money + total_price

	def subtract_money(self, stock_name, quantity):
		total_price = calculate_money(self, stock_name, quantity)
		return self.money - total_price

	def add_stock_in_list(self, stock_name, quantity):
		self.player_stocks[stock_name] = quantity

	def subtract_stock_in_list(self, stock_name, quantity):
		q = self.player_stocks[stock_name]
		self.player_stocks[stock_name] = q - quantity


class Game_Runner(object):

	def __init__(self):
		self.game = Game()

	def show_player_stocks(self):
		self.game.show_player_stocks()

	def buy_stock(self, name, quantity):
		print "buy"

	def sell_stock(self, name, quantity):
		print "sell"
		#I made helper functions(rules) in Game class. I will use them to fully build this function

	def show_NASDAQ(self):
		self.game.show_NASDAQ()

class Interaction(object):
	
	def __init__(self):
		self.game_runner = Game_Runner()
		self.options()

	def options(self):
		print "Press Number"
		answer = input("1: Check NASDAQ ")
		if answer == 1:
			self.game_runner.show_NASDAQ()

Interaction()
