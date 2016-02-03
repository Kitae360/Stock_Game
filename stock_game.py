from list_stock import existing_stocks
from yahoo_finance import Share

class Game(object):

	def __init__(self):
		self.money = 5000
		self.player_stocks = {}
		self.stock_list = existing_stocks

	#show the stocks that user owns
	def show_player_stocks(self):
		return self.player_stocks

	#show how much money 
	def show_money(self):
		return self.money

	#show list of all stocks in the NASDAQ
	def show_NASDAQ(self):
		return self.stock_list

	#check if given stock is in the user's stock list
	def check_stock_in_list(self, stock_name):
		if self.player_stocks.get(stock_name) == None:
			return False
		else:
			return True

	#check if given stock is in the NASDAQ
	def check_stock_exist_in_NASDAQ(self, stock_name):
		if self.stock_list.get(stock_name) == None:
			return False
		else:
			return True

	#check if user owns less quantity of given name stock than the given quantity value
	def quantity_check(self, name, quantity):
		return int(self.player_stocks[name]) < int(quantity)

	#returns the current value of the given stock
	def check_current_price_stock(self, stock_name):
 		stock = Share('{}'.format(stock_name))
 		return stock.get_price()

	#calculate the current price of the given stock at given quantity
	def calculate_money(self, stock_name, quantity):
		stock_price = self.check_current_price_stock(stock_name)
		total_price = int(quantity) * float(stock_price)
		return total_price
	
	#check if user has enough money to buy the given quantity of the given stock
	def enough_money(self, stock_name, quantity):
		return self.money >= self.calculate_money(stock_name, quantity)

	#add money in the user's account by price of the given stock times the quantity
	def add_money(self, stock_name, quantity):
		total_price = self.calculate_money(stock_name, quantity)
		self.money = self.money + total_price

	#subtract money from the user's account by price of the given stock times the quantity
	def subtract_money(self, stock_name, quantity):
		total_price = self.calculate_money(stock_name, quantity)
		self.money = self.money - total_price

	#add given quantity amount of given stock in user's stock list
	def add_stock_in_list(self, stock_name, quantity):
		self.player_stocks[stock_name] = quantity

	#add given quantity amount of given stock in user's stock list when user already owns the stock
	def add_more_stock_in_list(self, stock_name, quantity):
		user_owns = self.player_stocks[stock_name]
		self.player_stocks[stock_name] = int(quantity) + int(user_owns)

	#subtract given quantity amount of given stock in user's stock list
	def subtract_stock_in_list(self, stock_name, quantity):
		q = self.player_stocks[stock_name]
		self.player_stocks[stock_name] = int(q) - int(quantity)
	
	#when the quantity of the stock is zero, stock gets erased from the user's stock list
	def delete_list_value_zero(self):
		for name, quantity in self.player_stocks.items():
			if 0 == quantity:
				self.player_stocks.pop(name, quantity)

class Game_Runner(object):

	def __init__(self):
		self.game = Game()

	def show_player_stocks(self):
		print self.game.show_player_stocks()

	def show_NASDAQ(self):
		print self.game.show_NASDAQ()

	def show_money(self):
		print self.game.show_money()

	def buy_stock(self, list):
		name = list[0]
		quantity = list[1]
		if self.game.check_stock_exist_in_NASDAQ(name):
			if self.game.enough_money(name, quantity):
				if self.game.check_stock_in_list(name):
					self.game.add_more_stock_in_list(name, quantity)
				else:
					self.game.add_stock_in_list(name, quantity)
				self.game.subtract_money(name, quantity)
				self.game.show_money()
				self.game.show_player_stocks()

			else: print "You do not have enough money"
		else: print "Given stock does not exist"

	def sell_stock(self, list):
		name = list[0]
		quantity = list[1]
		if self.game.check_stock_in_list(name):
			if self.game.quantity_check(name, quantity):
				print "You do not have enough stocks"
			else:
				self.game.subtract_stock_in_list(name, quantity)
				self.game.add_money(name, quantity)
				self.game.delete_list_value_zero()
				self.game.show_money()
				self.game.show_player_stocks()
		else:
			print "You do not owne a stock with a given name"
