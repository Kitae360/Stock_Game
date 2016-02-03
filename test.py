import unittest
from stock_game import *

class Test(unittest.TestCase):
	
	def setUp(self):
		self.game = Game()	
	
	def test_show_money(self):
		self.assertEqual(5000,self.game.show_money())

	def test_show_stock(self):
		self.assertEqual({},self.game.show_player_stocks())

	def test_add_stock(self):
		self.game.add_stock_in_list("YHOO", 10)
		self.assertEqual({"YHOO": 10},self.game.show_player_stocks())

	def test_add_stock_2(self):
		self.game.add_stock_in_list("YHOO", 10)
		self.game.add_stock_in_list("NOOO", 123)
		self.assertEqual({"YHOO": 10, "NOOO": 123},self.game.show_player_stocks())

	def test_add_more_stock_in_list(self):
		self.game.add_stock_in_list("YHOO", 10)
		self.game.add_more_stock_in_list("YHOO", 14)
		self.assertEqual({"YHOO": 24},self.game.show_player_stocks())

	def test_subtract_stock(self):
		self.game.add_stock_in_list("YHOO", 10)
		self.game.subtract_stock_in_list("YHOO", 3)
		self.assertEqual({"YHOO": 7},self.game.show_player_stocks())

	def test_subtract_stock_2(self):
		self.game.add_stock_in_list("YHOO", 10)
		self.game.subtract_stock_in_list("YHOO", 3)
		self.game.subtract_stock_in_list("YHOO", 7)
		self.assertEqual({"YHOO": 0},self.game.show_player_stocks())

	def test_check_stock_in_list(self):
		self.game.add_stock_in_list("YHOO", 10)
		self.assertEqual(True,self.game.check_stock_in_list("YHOO"))
		self.assertEqual(False,self.game.check_stock_in_list("Random"))
		self.assertEqual(False,self.game.check_stock_in_list("yhoo"))

	def test_check_stock_in_NASDAQ(self):
		self.assertEqual(True,self.game.check_stock_exist_in_NASDAQ("YHOO"))
		self.assertEqual(False,self.game.check_stock_exist_in_NASDAQ("Random"))
		self.assertEqual(False,self.game.check_stock_exist_in_NASDAQ("yhoo"))

	def test_delete_list_value_zero(self):
		self.game.add_stock_in_list("YHOO", 10)
		self.game.add_stock_in_list("JKJK", 0)
		self.game.add_stock_in_list("QEWW", 2)
		self.game.delete_list_value_zero()
		self.assertEqual({"YHOO": 10, "QEWW": 2},self.game.show_player_stocks())

if __name__ == '__main__':
	unittest.main()
