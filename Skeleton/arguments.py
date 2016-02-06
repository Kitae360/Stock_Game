import formats as helper
import stock_info as yahoo_finance


def current_price_function(list):
 if len(list) != 1:
	print "Wrong number of arguments."
 else:
	name = list[0]
	price = yahoo_finance.current_price_stock(name)
	time = yahoo_finance.current_time_stock(name)
	print "Name of the stock: {}".format(name)
	print "Current price: {}".format(price)
	print "Trade Date Time: {}".format(time)

def change_of_price_function(list):
  if len(list) != 3:
	print "Wrong number of arguments"
  else:
	name = list[0]
	beginning = list[1]
	ending = list[2]
	if helper.all_integer_correct_format(beginning) and helper.all_integer_correct_format(ending):
		price_change = yahoo_finance.price_change(name, beginning, ending)
		print "Name of the stock: {}".format(name)
		print "Beginning time: {}".format(beginning)
		print "Ending time: {}".format(ending)
		print "Change of price: ${}".format(price_change)
	else:
		print "Format of the arguments is incorrect"
