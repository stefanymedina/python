class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration


#when I Define the function counter inside this are the method _iter_
# and when I use a for internal that call the  __iter__ method and the print use the __next__


for x in Counter(50,70): #--> in this moment we call the method iter
	print(x) #--> in this moment we call the method next