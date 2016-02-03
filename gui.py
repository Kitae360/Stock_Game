from gi.repository import Gtk
import matplotlib.pyplot as plt
import stock_game as game

class ListWindow(Gtk.Window):

    def __init__(self):
	rules = game.Game()
        Gtk.Window.__init__(self, title="Find NASDAQ")
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.set_border_width(10)

	label = Gtk.Label("Type the first letter of the stock")
	a = label.get_text()
	vbox.pack_start(label, True, True, 0)

	self.entry = Gtk.Entry()
	self.entry.set_text("Name")
	vbox.pack_start(self.entry, True, True, 0)

        List = rules.show_NASDAQ("{}".format(a))
        Name = Gtk.ComboBoxText()
        Name.set_entry_text_column(0)
        Name.connect("changed", self.name_changed)
        for part in List:
        	Name.append_text(part)

        vbox.pack_start(Name, False, False, 0)

        self.add(vbox)

    def name_changed(self, part):
        text = part.get_active_text()
        if text != None:
            print("Selected: name=%s" % text)

class Dialog_Success(Gtk.Dialog):

    def __init__(self, parent):
	Gtk.Dialog.__init__(self, "Success", parent, 0,
		(Gtk.STOCK_OK, Gtk.ResponseType.OK,
		Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

	self.set_default_size(100, 80)

	label = Gtk.Label("Transaction is successfully done")

	box = self.get_content_area()
	box.add(label)
	self.show_all()

class Dialog_Warning(Gtk.Dialog):

	def __init__(self, parent):
	        Gtk.Dialog.__init__(self, "Warning", parent, 0,
		(Gtk.STOCK_OK, Gtk.ResponseType.OK,
		Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

		self.set_default_size(100, 80)

		label = Gtk.Label("This transaction is not possible")

		box = self.get_content_area()
		box.add(label)
		self.show_all()

class Graph(object):

	def __init__(self):
		plt.plot([1,4,7,10], [21,14,44,7], 'b')
		plt.ylabel('some numbers')
		plt.xlabel('Days')
		LABELS = ["Monday", "Tuesday", "Wednesday", "Thrusday"]
		DayOfWeekOfCall = [1,4,7, 10]
		plt.xticks(DayOfWeekOfCall, LABELS)
		plt.axis([0, 15, 0, 45])
		plt.show()

class Window(Gtk.Window):

	def __init__(self):
		rules = game.Game()
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
	
		label = Gtk.Label("Type the name of the stock")
	        vbox.pack_start(label, True, True, 0)
	
	        self.entry = Gtk.Entry()
	        self.entry.set_text("Name")
	        vbox.pack_start(self.entry, True, True, 0)
	
		label = Gtk.Label("Type the quantity of the stock")
	        vbox.pack_start(label, True, True, 0)
	
	        self.entry = Gtk.Entry()
	        self.entry.set_text("Quantity")
	        vbox.pack_start(self.entry, True, True, 0)
	
	        hbox = Gtk.Box(spacing=6)
	        vbox.pack_start(hbox, True, True, 0)
	        
	        button = Gtk.Button.new_with_label("Buy")
	        button.connect("clicked", self.buy)
	        hbox.pack_start(button, True, True, 0)
	
	        button = Gtk.Button.new_with_mnemonic("Sell")
	        button.connect("clicked", self.sell)
	        hbox.pack_start(button, True, True, 0)

	        button = Gtk.Button.new_with_mnemonic("Find NASDAQ")
	        button.connect("clicked", self.nasdaq)
	        hbox.pack_start(button, True, True, 0)

	        button = Gtk.Button.new_with_mnemonic("Check NASDAQ Graph")
	        button.connect("clicked", self.nasdaq_graph)
	        hbox.pack_start(button, True, True, 0)
	
	def buy(self, button):
	        dialog = Dialog_Warning(self)
	        response = dialog.run()
		dialog.destroy()

	def sell(self, button):
	        dialog = Dialog_Success(self)
	        response = dialog.run()
		dialog.destroy()

	def nasdaq(self, button):
		win = ListWindow()
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	def nasdaq_graph(self, button):
		Graph()

	def switch_control(self, switch, gparam):
	        if switch.get_active():
	        	state = "on"
	        else:
	        	state = "off"

win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
