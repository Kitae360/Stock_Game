import matplotlib.pyplot as plt

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
