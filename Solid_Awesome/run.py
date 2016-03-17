from gi.repository import Gtk
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../Common')
import stock_game as stock_game
from list_stock import existing_stocks
from yahoo_finance import Share
import time
import os.path

class Dialog_Name_Warning(Gtk.Dialog):

	def __init__(self, parent):
	        Gtk.Dialog.__init__(self, "Warning", parent, 0,
		(Gtk.STOCK_OK, Gtk.ResponseType.OK))
		self.player = stock_game.Player()
		self.stock_manager = stock_game.Stock_Manager()

		self.set_default_size(100, 80)

		label = Gtk.Label("Game already exists or Cannot load")

		box = self.get_content_area()
		box.add(label)
		self.show_all()


class Current_Account(Gtk.Dialog):

	def __init__(self, parent):
		Gtk.Dialog.__init__(self, "Current Account", parent, 0,
			(Gtk.STOCK_OK, Gtk.ResponseType.OK))
		self.interface = Interface()

		self.set_default_size(300, 100)

	def get_data(self, stocks, money):
		label = Gtk.Label("Current Account:")
		stock_label = Gtk.Label("Stock(s): {}".format(stocks))
		money_label = Gtk.Label("Money: ${}".format(money))

		box = self.get_content_area()
		box.add(label)
		box.add(stock_label)
		box.add(money_label)
		self.show_all()


class Check_Price(Gtk.Dialog):

	def __init__(self, parent):
		Gtk.Dialog.__init__(self, "Stock Price", parent, 0,
			(Gtk.STOCK_OK, Gtk.ResponseType.OK))
		self.interface = Interface()

		self.set_default_size(300, 100)

	def get_data(self, name, symbol, price):
		label = Gtk.Label("Price Info:")
		name_label = Gtk.Label("Name of the Stock: {}".format(name))
		symbol_label = Gtk.Label("Symbol of the Stock: ${}".format(symbol))
		price_label = Gtk.Label("Price of the Stock: ${}".format(price))

		box = self.get_content_area()
		box.add(label)
		box.add(name_label)
		box.add(symbol_label)
		box.add(price_label)
		self.show_all()

class MyWindow(Gtk.Window):

	def __init__(self):

		self.game = stock_game.Game_Runner()
		self.interface = Interface()

		self.stock_list = []
		self.stock_dic = self.game.show_NASDAQ()
		for name, symbol in self.game.show_NASDAQ().items():
			stock = [symbol, name]
			self.stock_list.append(stock)

		self.name_store = Gtk.ListStore(str, str)
		for name in self.stock_list:
			self.name_store.append(name)

	        Gtk.Window.__init__(self, title="Stock Game")
	        self.set_size_request(300, 300)
	
	        self.timeout_id = None
	
	        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
	        self.add(self.vbox)
		self.start_page()

		self.hard_mode = False

	def start_page(self):

		self.label = Gtk.Label("Stock Investing Simulation Game")
	        self.vbox.pack_start(self.label, True, True, 0)
	
	        self.hbox = Gtk.Box(spacing=6)
	        self.vbox.pack_start(self.hbox, True, True, 0)

	        self.new_game_button = Gtk.Button.new_with_label("New Game")
	        self.new_game_button.connect("clicked", self.new_game)
	        self.vbox.pack_start(self.new_game_button, True, True, 0)

	        self.load_game_button = Gtk.Button.new_with_label("Load Game")
	        self.load_game_button.connect("clicked", self.load_game)
	        self.vbox.pack_start(self.load_game_button, True, True, 0)

	def new_game(self, new_game_button):
		self.vbox.remove(self.label)
		self.vbox.remove(self.new_game_button)
		self.vbox.remove(self.load_game_button)

		self.label = Gtk.Label("Type the name of the new game:")
	        self.vbox.pack_start(self.label, True, True, 0)

		self.entry = Gtk.Entry()
		self.entry.set_text("New Game")
		self.vbox.pack_start(self.entry, True, True, 0)

	        self.new_start_game_button = Gtk.Button.new_with_label("Start Game")
	        self.new_start_game_button.connect("clicked", self.new_start_game)
	        self.vbox.pack_start(self.new_start_game_button, True, True, 0)

	        self.back_to_start_button = Gtk.Button.new_with_label("Go Back")
	        self.back_to_start_button.connect("clicked", self.back_to_start_new)
	        self.vbox.pack_start(self.back_to_start_button, True, True, 0)

		win.show_all()

	def load_game(self, load_game_button):
		self.vbox.remove(self.label)
		self.vbox.remove(self.new_game_button)
		self.vbox.remove(self.load_game_button)

		self.label = Gtk.Label("Type the name of the game to load:")
	        self.vbox.pack_start(self.label, True, True, 0)

		self.entry = Gtk.Entry()
		self.entry.set_text("Load Game")
		self.vbox.pack_start(self.entry, True, True, 0)

	        self.load_start_game_button = Gtk.Button.new_with_label("Start Game")
	        self.load_start_game_button.connect("clicked", self.load_start_game)
	        self.vbox.pack_start(self.load_start_game_button, True, True, 0)

	        self.back_to_start_button = Gtk.Button.new_with_label("Go Back")
	        self.back_to_start_button.connect("clicked", self.back_to_start_load)
	        self.vbox.pack_start(self.back_to_start_button, True, True, 0)

		win.show_all()

	def back_to_start_new(self, back_to_start_button):
		self.vbox.remove(self.label)
		self.vbox.remove(self.entry)
		self.vbox.remove(self.new_start_game_button)
		self.vbox.remove(self.back_to_start_button)

		self.start_page()
		win.show_all()

	def back_to_start_load(self, back_to_start_button):
		self.vbox.remove(self.label)
		self.vbox.remove(self.entry)
		self.vbox.remove(self.load_start_game_button)
		self.vbox.remove(self.back_to_start_button)

		self.start_page()
		win.show_all()

	def new_start_game(self, new_start_game_button):
		self.game_name = self.entry.get_text()
		if self.interface.new_game(self.game_name):
			dialog = Dialog_Name_Warning(self)
	        	response = dialog.run()
			dialog.destroy()
		else:
			self.vbox.remove(self.label)
			self.vbox.remove(self.entry)
			self.vbox.remove(self.new_start_game_button)
			self.vbox.remove(self.back_to_start_button)
			self.game_main_menu()


	def load_start_game(self, load_start_game_button):
		self.game_name = self.entry.get_text()
		if self.interface.new_game(self.game_name):
			self.interface.dump(self.game_name)
			self.vbox.remove(self.label)
			self.vbox.remove(self.entry)
			self.vbox.remove(self.load_start_game_button)
			self.vbox.remove(self.back_to_start_button)
			self.game_main_menu()
		else:
			dialog = Dialog_Name_Warning(self)
	        	response = dialog.run()
			dialog.destroy()


	def game_main_menu(self):
		self.label = Gtk.Label("Select The Activity You Want")
	        self.vbox.pack_start(self.label, True, True, 0)

	        self.button1 = Gtk.Button.new_with_label("Transaction")
	        self.button1.connect("clicked", self.transaction)
	        self.vbox.pack_start(self.button1, True, True, 0)

	        self.button2 = Gtk.Button.new_with_mnemonic("Check Account")
	        self.button2.connect("clicked", self.check_account)
	        self.vbox.pack_start(self.button2, True, True, 0)

	        self.button3 = Gtk.Button.new_with_mnemonic("Search NASDAQ")
	        self.button3.connect("clicked", self.search_nasdaq)
	        self.vbox.pack_start(self.button3, True, True, 0)

	        self.button4 = Gtk.Button.new_with_mnemonic("Save & Quit")
	        self.button4.connect("clicked", self.save_quit)
	        self.vbox.pack_start(self.button4, True, True, 0)

		win.show_all()

	def transaction(self, button):
		self.vbox.remove(self.label)
		self.vbox.remove(self.button1)
		self.vbox.remove(self.button2)
		self.vbox.remove(self.button3)
		self.vbox.remove(self.button4)

		self.label = Gtk.Label("Type the name of the stock")
	        self.vbox.pack_start(self.label, True, True, 0)

		self.name_combo = Gtk.ComboBox.new_with_model_and_entry(self.name_store)
		self.name_combo.connect("changed", self.on_name_combo_changed)
		self.name_combo.set_entry_text_column(1)
		self.vbox.pack_start(self.name_combo, False, False, 0)

		self.label2 = Gtk.Label("Type the quantity of the stock")
	        self.vbox.pack_start(self.label2, True, True, 0)

		self.adjustment = Gtk.Adjustment(0, 0, 1000, 1, 10, 0)
		self.spinbutton = Gtk.SpinButton()
		self.spinbutton.set_adjustment(self.adjustment)
		self.vbox.pack_start(self.spinbutton, False, False, 0)

	        self.button = Gtk.Button.new_with_label("Buy")
	        self.button.connect("clicked", self.buy)
	        self.vbox.pack_start(self.button, True, True, 0)

	        self.button2 = Gtk.Button.new_with_mnemonic("Sell")
	        self.button2.connect("clicked", self.sell)
	        self.vbox.pack_start(self.button2, True, True, 0)

	        self.button3 = Gtk.Button.new_with_mnemonic("Go Back")
	        self.button3.connect("clicked", self.go_to_main_menu)
	        self.vbox.pack_start(self.button3, True, True, 0)

		win.show_all()

	def check_account(self, button):
		stocks = self.interface.player_stock()
		money = self.interface.player_money()
		dialog = Current_Account(self)
		dialog.get_data(stocks, money)
		response = dialog.run()
		dialog.destroy()

	def search_nasdaq(self, button):
		self.vbox.remove(self.label)
		self.vbox.remove(self.button1)
		self.vbox.remove(self.button2)
		self.vbox.remove(self.button3)
		self.vbox.remove(self.button4)

		self.label = Gtk.Label("Type the Name & Click The Action You Want")
	        self.vbox.pack_start(self.label, True, True, 0)

		self.name_combo = Gtk.ComboBox.new_with_model_and_entry(self.name_store)
		self.name_combo.connect("changed", self.on_name_combo_changed)
		self.name_combo.set_entry_text_column(1)
		self.vbox.pack_start(self.name_combo, False, False, 0)

	        self.button = Gtk.Button.new_with_label("Check Current Price")
	        self.button.connect("clicked", self.current_price)
	        self.vbox.pack_start(self.button, True, True, 0)

	        self.button2 = Gtk.Button.new_with_mnemonic("Check Price Graph")
	        self.button2.connect("clicked", self.price_graph)
	        self.vbox.pack_start(self.button2, True, True, 0)

	        self.button3 = Gtk.Button.new_with_mnemonic("Go Back")
	        self.button3.connect("clicked", self.go_to_main_menu2)
	        self.vbox.pack_start(self.button3, True, True, 0)

		win.show_all()

	def save_quit(self, button):
		self.interface.save(self.game_name)
		self.vbox.remove(self.label)
		self.vbox.remove(self.button1)
		self.vbox.remove(self.button2)
		self.vbox.remove(self.button3)
		self.vbox.remove(self.button4)
		self.start_page()
		win.show_all()
		
	def buy(self, button):
		stock_quantity = self.spinbutton.get_value_as_int()
		stock_name = self.name_combo.get_child().get_text()
		stock_symbol = self.stock_dic.get(stock_name)
		output = self.interface.buy(stock_symbol, stock_quantity)
		if output != False:
			stocks = output[0]
			money = output[1]

			dialog = Current_Account(self)
			dialog.get_data(stocks, money)
			response = dialog.run()
			dialog.destroy()

	def sell(self, button):
		stock_quantity = self.spinbutton.get_value_as_int()
		stock_name = self.name_combo.get_child().get_text()
		stock_symbol = self.stock_dic.get(stock_name)
		output = self.interface.sell(stock_symbol, stock_quantity)
		if output != False:
			stocks = output[0]
			money = output[1]

			dialog = Current_Account(self)
			dialog.get_data(stocks, money)
			response = dialog.run()
			dialog.destroy()

	def go_to_main_menu(self, button):
		self.vbox.remove(self.label)
		self.vbox.remove(self.label2)
		self.vbox.remove(self.button)
		self.vbox.remove(self.button2)
		self.vbox.remove(self.button3)
		self.vbox.remove(self.name_combo)
		self.vbox.remove(self.spinbutton)
		self.game_main_menu()
		win.show_all()

	def go_to_main_menu2(self, button):
		self.vbox.remove(self.label)
		self.vbox.remove(self.button)
		self.vbox.remove(self.button2)
		self.vbox.remove(self.button3)
		self.vbox.remove(self.name_combo)
		self.game_main_menu()
		win.show_all()

	def current_price(self, button):
		stock_name = self.name_combo.get_child().get_text()
		stock_symbol = self.stock_dic.get(stock_name)
		price = self.interface.stock_price(stock_symbol)
	        dialog = Check_Price(self)
		dialog.get_data(stock_name, stock_symbol, price)
	        response = dialog.run()
		dialog.destroy()

	def price_graph(self, button):
		stock_name = self.name_combo.get_child().get_text()
		stock_symbol = self.stock_dic.get(stock_name)

	def on_name_combo_changed(self, combo):
		entry = combo.get_child()
		self.stock_name = entry.get_text()


class Interface(object):
	
	def __init__(self):

		self.game = stock_game.Game_Runner()

	def new_game(self, name):
		return self.game.new_game(name)
	
	def buy(self, name, quantity):
		try:
			return self.game.buy_stock(name, quantity)
		except Exception as e:
			return False

	def sell(self, name, quantity):
		try:
			return self.game.sell_stock(name, quantity)
		except Exception as e:
			return False

	def save(self, file_name):
		try:
			self.game.save_game(file_name)
		except Exception as e:
			return type(e).__name__
	
	def dump(self, file_name):
		try:
			self.game.dump(file_name)
		except Exception as e:
			return type(e).__name__

	def player_stock(self):
		return self.game.show_player_stocks()

	def player_money(self):
		return self.game.show_money()

	def stock_price(self, name):
		try:
			return self.game.check_price(name)
		except Exception as e:
			return type(e).__name__


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
