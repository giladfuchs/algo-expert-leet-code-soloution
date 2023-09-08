def special_data_table( number_of_slots, values, find_item ) :
	####### DO NOT MODIFY BELOW #######
	myTable = MySpecialTable(number_of_slots)
	for val in values:
		myTable.add_item(val)

	return myTable.find_item(find_item)
	####### DO NOT MODIFY ABOVE #######

class MySpecialTable():
		def __init__(self, slots):
			self.slots = slots
			self.table = []
			self.create_table()

		def hash_key(self, value):
			return value% self.slots

		def create_table(self):
			for _ in range(self.slots):
				self.table.append([])

		def add_item(self, value):
			key_index = self.hash_key(value=value)
			self.table[key_index].append(value)

		def find_item(self, item):
			key_index = self.hash_key(value=item)
			return key_index if item in self.table[key_index]\
				else -1
