from list_stock import existing_stocks
from list_stock import test_stocks
from yahoo_finance import Share
import re
import pickle
import os.path

class Stock_Manager(object):

	"""show list of all stocks in the NASDAQ"""
	def show_NASDAQ(self):
		stock_list = {}
		for symbol, name in existing_stocks.items():
			stock_list[name] = symbol
		return stock_list

	"""check if given stock is in the NASDAQ"""
	def check_stock_exist_in_NASDAQ(self, stock_name):
		if existing_stocks.get(stock_name) == None:
			return False
		else:
			return True

	"""returns the current value of the given stock"""
	def check_current_price_stock(self, stock_name):
 		stock = Share('{}'.format(stock_name))
 		return stock.get_price()

class Player(object):

	def __init__(self):
  		self.money = 5000
		self.player_stocks = {}
	
	"""show the stocks that user owns"""
	def show_player_stocks(self):
		return self.player_stocks

	"""show how much money""" 
	def show_money(self):
		return self.money

	"""check if given stock is in the user's stock list"""
	def check_stock_in_list(self, stock_name):
		if self.player_stocks.get(stock_name) == None:
			return False
		else:
			return True

	"""check if user owns less quantity of given name stock than the given quantity value"""
	def quantity_check(self, name, quantity):
		return int(self.player_stocks[name]) >= int(quantity)

	"""calculate the current price of the given stock at given quantity"""
	def calculate_money(self, quantity, price):
		total_price = int(quantity) * float(price)
		return total_price
	
	"""check if user has enough money to buy the given quantity of the given stock"""
	def enough_money(self, price):
		return self.money >= price

	"""add money in the user's account by price of the given stock times the quantity"""
	def add_money(self,price):
		self.money = self.money + price
		return self.money

	"""subtract money from the user's account by price of the given stock times the quantity"""
	def subtract_money(self, price):
		self.money = self.money - price
		return self.money

	"""add given quantity amount of given stock in user's stock list"""
	def add_stock_in_list(self, stock_name, quantity):
		self.player_stocks[stock_name] = quantity

	"""add given quantity amount of given stock in user's stock list when user already owns the stock"""
	def add_more_stock_in_list(self, stock_name, quantity):
		user_owns = self.player_stocks[stock_name]
		self.player_stocks[stock_name] = int(quantity) + int(user_owns)

	"""subtract given quantity amount of given stock in user's stock list"""
	def subtract_stock_in_list(self, stock_name, quantity):
		q = self.player_stocks[stock_name]
		self.player_stocks[stock_name] = int(q) - int(quantity)
	
	"""when the quantity of the stock is zero, stock gets erased from the user's stock list"""
	def delete_list_value_zero(self):
		for name, quantity in self.player_stocks.items():
			if 0 == quantity:
				self.player_stocks.pop(name, quantity)

	def player_buying(self, name, quantity, price):
		if self.check_stock_in_list(name):
			self.add_more_stock_in_list(name, quantity)
		else: self.add_stock_in_list(name, quantity)
		self.subtract_money(price)


	def player_selling(self, name, quantity, price):
		self.subtract_stock_in_list(name, quantity)
		self.delete_list_value_zero()
		self.add_money(price)

class Game_Runner(object):

	def __init__(self):
		self.stock_manager = Stock_Manager()
		if os.path.isfile('a.pickle'):
			with open('a.pickle', 'rb') as handle:
				self.player = pickle.load(handle)
		else:
			self.player = Player()

	def make_new_game(self, name):
		if os.path.isfile('{}.pickle'.format(name)):
			return "Given game name already exists"
		else:
			open("{}.pickle".format(name), 'wb')
	
	def start_game(self, name):
		return "start"
	
	def end_game(self):
		return "end"

	def show_player_stocks(self):
		return self.player.show_player_stocks()

	def show_NASDAQ(self):
		return self.stock_manager.show_NASDAQ()

	def show_money(self):
		return self.player.show_money()

	def buy_stock(self,name, quantity):
			if quantity.isdigit():
				if self.stock_manager.check_stock_exist_in_NASDAQ(name):
					price = float(self.stock_manager.check_current_price_stock(name))
					total_price = price * int(quantity)
					if self.player.show_money() >= total_price:
						self.player.player_buying(name, quantity, total_price)
						output = (self.show_money(), self.show_player_stocks())
						with open('a.pickle', 'wb') as handle:
							pickle.dump(self.player, handle)
						return output
					else: return "You do not have enough money to buy stocks"
				else: return "Given stock does not exist"
			else: return "Quantity must be an integer"

	def sell_stock(self, name, quantity):
			if quantity.isdigit():
				if self.stock_manager.check_stock_exist_in_NASDAQ(name):
					price = float(self.stock_manager.check_current_price_stock(name))
					total_price = price * int(quantity)
					if self.player.check_stock_in_list(name):
						if self.player.quantity_check(name, quantity):
							self.player.player_selling(name, quantity, total_price)
							output = (self.show_money(), self.show_player_stocks())
							with open('a.pickle', 'wb') as handle:
								pickle.dump(self.player, handle)
							return output
						else: return "You do not have enough stocks to sell"
					else: return "You do not own a given stock"
				else: return "Given stock does not exist"
			else: return "Quantity must be an integer"
