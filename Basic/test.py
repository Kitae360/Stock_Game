import unittest
import sys
sys.path.insert(0, '../Common')
from stock_game import *

class Test(unittest.TestCase):
	
	def setUp(self):
		self.player = Player()
		self.stock_manager = Stock_Manager()
	
	def test_show_money(self):
		self.assertEqual(5000,self.player.show_money())

	def test_show_stock(self):
		self.assertEqual({},self.player.show_player_stocks())

	def test_add_stock(self):
		self.player.add_stock_in_list("YHOO", 10)
		self.assertEqual({"YHOO": 10},self.player.show_player_stocks())

	def test_add_stock_2(self):
		self.player.add_stock_in_list("YHOO", 10)
		self.player.add_stock_in_list("NOOO", 123)
		self.assertEqual({"YHOO": 10, "NOOO": 123},self.player.show_player_stocks())

	def test_add_more_stock_in_list(self):
		self.player.add_stock_in_list("YHOO", 10)
		self.player.add_more_stock_in_list("YHOO", 14)
		self.assertEqual({"YHOO": 24},self.player.show_player_stocks())

	def test_subtract_stock(self):
		self.player.add_stock_in_list("YHOO", 10)
		self.player.subtract_stock_in_list("YHOO", 3)
		self.assertEqual({"YHOO": 7},self.player.show_player_stocks())

	def test_subtract_stock_2(self):
		self.player.add_stock_in_list("YHOO", 10)
		self.player.subtract_stock_in_list("YHOO", 3)
		self.player.subtract_stock_in_list("YHOO", 7)
		self.assertEqual({"YHOO": 0},self.player.show_player_stocks())

	def test_check_stock_in_list(self):
		self.player.add_stock_in_list("YHOO", 10)
		self.assertEqual(True,self.player.check_stock_in_list("YHOO"))
		self.assertEqual(False,self.player.check_stock_in_list("Random"))
		self.assertEqual(False,self.player.check_stock_in_list("yhoo"))

	def test_delete_list_value_zero(self):
		self.player.add_stock_in_list("YHOO", 10)
		self.player.add_stock_in_list("JKJK", 0)
		self.player.add_stock_in_list("QEWW", 2)
		self.player.delete_list_value_zero()
		self.assertEqual({"YHOO": 10, "QEWW": 2},self.player.show_player_stocks())

	def test_quantity_check(self):
		self.player.add_stock_in_list("QEWW", 2)
		self.assertEqual(False ,self.player.quantity_check("QEWW", 3))
		self.assertEqual(True ,self.player.quantity_check("QEWW", 2))
		self.assertEqual(True ,self.player.quantity_check("QEWW", 1))

	def test_calculate_money(self):
		self.assertEqual(100 ,self.player.calculate_money(20, 5))
		self.assertEqual(2846 ,self.player.calculate_money(200, 14.23))
		self.assertEqual(442.2 ,self.player.calculate_money(20, 22.11))
		self.assertEqual(60 ,self.player.calculate_money(20, 3.00))

	def test_check_stock_in_NASDAQ(self):
		self.assertEqual(True,self.stock_manager.check_stock_exist_in_NASDAQ("YHOO"))
		self.assertEqual(False,self.stock_manager.check_stock_exist_in_NASDAQ("Random"))
		self.assertEqual(False,self.stock_manager.check_stock_exist_in_NASDAQ("yhoo"))

	def test_add_money(self):
		self.assertEqual(6000 ,self.player.add_money(1000))
		self.assertEqual(6888.89 ,self.player.add_money(888.89))
		self.assertEqual(9211 ,self.player.add_money(2322.11))

	def test_subtract_money(self):
		self.assertEqual(4000 ,self.player.subtract_money(1000))
		self.assertEqual(3111.11 ,self.player.subtract_money(888.89))
		self.assertEqual(789.00 ,self.player.subtract_money(2322.11))

if __name__ == '__main__':
	unittest.main()
