from yahoo_finance import Share
from pprint import pprint

def current_price_stock(name):
 stock = Share('{}'.format(name))
 return stock.get_price()

def current_time_stock(name):
 stock = Share('{}'.format(name))
 return stock.get_trade_datetime()

def price_change(name, beginning, ending):
 stock = Share('{}'.format(name))
 history_list = stock.get_historical(beginning, ending)
 length_of_days = len(history_list)
 first_day_data = history_list[length_of_days - 1]
 last_day_data = history_list[0]
 first_day_price = first_day_data.get('Adj_Close')
 last_day_price = last_day_data.get('Adj_Close')
 fprice = float(first_day_price)
 lprice = float(last_day_price)
 return fprice - lprice

