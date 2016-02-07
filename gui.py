from gi.repository import Gtk
import matplotlib.pyplot as plt
import stock_game as stock_game
from list_stock import existing_stocks

class Transaction(Gtk.Window):

	def __init__(self):

	        Gtk.Window.__init__(self, title="Transaction")
	        self.set_size_request(200, 100)
	
	        self.timeout_id = None
	
	        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
	        self.add(vbox)

		label = Gtk.Label("Type the name of the stock")
	        vbox.pack_start(label, True, True, 0)
	
	        self.entry = Gtk.Entry()
	        self.entry.set_text("Name")
	        vbox.pack_start(self.entry, True, True, 0)
	
		label = Gtk.Label("Type the quantity of the stock")
	        vbox.pack_start(label, True, True, 0)
	
		hbox = Gtk.Box(spacing=2)
	        vbox.pack_start(hbox, True, True, 0)

		adjustment = Gtk.Adjustment(0, 0, 1000, 1, 10, 0)
		self.spinbutton = Gtk.SpinButton()
		self.spinbutton.set_adjustment(adjustment)
		hbox.pack_start(self.spinbutton, False, False, 0)
        
	        button = Gtk.Button.new_with_label("Buy")
	        button.connect("clicked", self.buy)
	        hbox.pack_start(button, True, True, 0)

	        button = Gtk.Button.new_with_mnemonic("Sell")
	        button.connect("clicked", self.sell)
	        hbox.pack_start(button, True, True, 0)
		
		self.stock_manager = stock_game.Stock_Manager()
		self.player = stock_game.Player()
	
	def buy(self, button):
		quantity = self.spinbutton.get_value_as_int()
		name = self.entry.get_text()
		if self.stock_manager.check_stock_exist_in_NASDAQ(name):
			price = float(self.stock_manager.check_current_price_stock(name))
			total_price = price * int(quantity)
			if self.player.enough_money(total_price):
				if self.player.check_stock_in_list(name):
					self.player.add_more_stock_in_list(name, quantity)
				else: 
					self.player.add_stock_in_list(name, quantity)
					self.player.subtract_money(total_price)
				dialog = Dialog_Success(self)
	        		response = dialog.run()
				dialog.destroy()
			else:
				dialog = Dialog_Money_Warning(self)
				response = dialog.run()
				dialog.destroy()
		else:
			dialog =  Dialog_Name_Warning(self)
			response = dialog.run()
			dialog.destroy()

	def sell(self, button):
		quantity = self.spinbutton.get_value_as_int()
		name = self.entry.get_text()
		if self.stock_manager.check_stock_exist_in_NASDAQ(name):
			price = float(self.stock_manager.check_current_price_stock(name))
			total_price = price * int(quantity)
			if self.player.check_stock_in_list(name):
				if self.player.quantity_check(name, quantity):
					self.player.subtract_stock_in_list(name, quantity)
					self.player.delete_list_value_zero()
					self.player.add_money(total_price)
					dialog = Dialog_Success(self)
					response = dialog.run()
					dialog.destroy()
				else:
					dialog =  Dialog_Quantity_Warning(self)
					response = dialog.run()
					dialog.destroy()
			else:
				dialog =  Dialog_No_Stock_Warning(self)
				response = dialog.run()
				dialog.destroy()
		else:
			dialog =  Dialog_Name_Warning(self)
			response = dialog.run()
			dialog.destroy()


class NASDAQ_Search(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="NASDAQ Search")
		self.game = stock_game.Stock_Manager()

		self.set_border_width(10)

		self.stock_list = []
		for name, symbol in self.game.show_NASDAQ().items():
			stock = [symbol, name]
			self.stock_list.append(stock)

		name_store = Gtk.ListStore(str, str)
		for name in self.stock_list:
			name_store.append(name)

		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

		label = Gtk.Label("NASDAQ Search")
		vbox.pack_start(label, True, True, 0)

		name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)
		name_combo.connect("changed", self.on_name_combo_changed)
		name_combo.set_entry_text_column(1)
		vbox.pack_start(name_combo, False, False, 0)
		self.add(vbox)

		button = Gtk.Button.new_with_label("Check Recent Price Graph")
		button.connect("clicked", self.draw_graph)
		vbox.pack_start(button, True, True, 0)
		self.input = ""

	def on_name_combo_changed(self, combo):
		entry = combo.get_child()
		self.input = entry.get_text()

	def draw_graph(self, button):
		graph = Graph()
		graph.make_graph(self.input)

class Graph(object):

	def __init__(self):
		self.game = stock_game.Stock_Manager()
		self.stock_list = self.game.show_NASDAQ()

	def make_graph(self, name):
		print self.stock_list[name]
		plt.plot([1,4,7,10], [21,14,44,7], 'b')
		plt.ylabel('some numbers')
		plt.xlabel('Days')
		LABELS = ["Monday", "Tuesday", "Wednesday", "Thrusday"]
		DayOfWeekOfCall = [1,4,7, 10]
		plt.xticks(DayOfWeekOfCall, LABELS)
		plt.axis([0, 15, 0, 45])
		plt.show()

class Dialog_Success(Gtk.Dialog):

	def __init__(self, parent):
		Gtk.Dialog.__init__(self, "Success", parent, 0,
			(Gtk.STOCK_OK, Gtk.ResponseType.OK))
		self.player = stock_game.Player()

		self.set_default_size(100, 80)
		
		stocks = self.player.show_player_stocks()
		money = self.player.show_money()
		label = Gtk.Label("Transaction was successfully done")
		space = Gtk.Label("")
		label_2 = Gtk.Label("Current Account:")
		stock_label = Gtk.Label("Stock(s): {}".format(stocks))
		money_label = Gtk.Label("Money: ${}".format(money))

		box = self.get_content_area()
		box.add(label)
		box.add(space)
		box.add(label_2)
		box.add(stock_label)
		box.add(money_label)
		self.show_all()


class Dialog_Name_Warning(Gtk.Dialog):

	def __init__(self, parent):
	        Gtk.Dialog.__init__(self, "Warning", parent, 0,
		(Gtk.STOCK_OK, Gtk.ResponseType.OK))
		self.player = stock_game.Player()
		self.stock_manager = stock_game.Stock_Manager()

		self.set_default_size(100, 80)

		label = Gtk.Label("Given stock name does not exist in the NASDAQ")

		box = self.get_content_area()
		box.add(label)
		self.show_all()

class Dialog_Quantity_Warning(Gtk.Dialog):

	def __init__(self, parent):
	        Gtk.Dialog.__init__(self, "Warning", parent, 0,
		(Gtk.STOCK_OK, Gtk.ResponseType.OK))
		self.player = stock_game.Player()
		self.stock_manager = stock_game.Stock_Manager()

		self.set_default_size(100, 80)

		label = Gtk.Label("You do not have enough stocks to sell")

		box = self.get_content_area()
		box.add(label)
		self.show_all()

class Dialog_No_Stock_Warning(Gtk.Dialog):

	def __init__(self, parent):
	        Gtk.Dialog.__init__(self, "Warning", parent, 0,
		(Gtk.STOCK_OK, Gtk.ResponseType.OK))
		self.player = stock_game.Player()
		self.stock_manager = stock_game.Stock_Manager()

		self.set_default_size(100, 80)

		label = Gtk.Label("You do not own a given stock")

		box = self.get_content_area()
		box.add(label)
		self.show_all()

class Dialog_Money_Warning(Gtk.Dialog):

	def __init__(self, parent):
	        Gtk.Dialog.__init__(self, "Warning", parent, 0,
		(Gtk.STOCK_OK, Gtk.ResponseType.OK))
		self.player = stock_game.Player()
		self.stock_manager = stock_game.Stock_Manager()

		self.set_default_size(100, 80)

		label = Gtk.Label("You do not have enough money")

		box = self.get_content_area()
		box.add(label)
		self.show_all()

class Check_Account(Gtk.Dialog):

	def __init__(self, parent):
		Gtk.Dialog.__init__(self, "Player Account", parent, 0,
			(Gtk.STOCK_OK, Gtk.ResponseType.OK))
		self.player = stock_game.Player()

		self.set_default_size(100, 80)
		
		stocks = self.player.show_player_stocks()
		money = self.player.show_money()
		label = Gtk.Label("Current Account:")
		stock_label = Gtk.Label("Stock(s): {}".format(stocks))
		money_label = Gtk.Label("Money: ${}".format(money))

		box = self.get_content_area()
		box.add(label)
		box.add(stock_label)
		box.add(money_label)
		self.show_all()

class Window(Gtk.Window):

	def __init__(self):

	        Gtk.Window.__init__(self, title="Stock Game")
	        self.set_size_request(200, 100)
	
	        self.timeout_id = None
	
	        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
	        self.add(vbox)

		label = Gtk.Label("Hard Mode")
	        vbox.pack_start(label, True, True, 0)
	
	        switch = Gtk.Switch()
	        switch.connect("notify::active", self.switch_control)
	        switch.set_active(False)
        	vbox.pack_start(switch, True, True, 0)
	
	        hbox = Gtk.Box(spacing=6)
	        vbox.pack_start(hbox, True, True, 0)
	        
	        button = Gtk.Button.new_with_label("Transaction")
	        button.connect("clicked", self.transaction)
	        hbox.pack_start(button, True, True, 0)

	        button = Gtk.Button.new_with_mnemonic("Check Account")
	        button.connect("clicked", self.check_account)
	        hbox.pack_start(button, True, True, 0)

	        button = Gtk.Button.new_with_mnemonic("Search NASDAQ")
	        button.connect("clicked", self.search_nasdaq)
	        hbox.pack_start(button, True, True, 0)

		self.hard_mode = False
	
	def transaction(self, button):
		win = Transaction()
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	def check_account(self, button):
	        dialog = Check_Account(self)
	        response = dialog.run()
		dialog.destroy()

	def search_nasdaq(self, button):
		win = NASDAQ_Search()
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	def switch_control(self, switch, gparam):
	        if switch.get_active():
	        	self.hard_mode = True
	        else:
	        	self.hard_mode = False

win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
