class AddrBookEntry(object): # class definition
	'address book entry class'
	def __init__(self, nm, ph): # define constructor
		self.name = nm # set name
		self.phone = ph # set phone#
		print 'Created instance for:', self.name
	def updatePhone(self, newph): # define method
		self.phone = newph
		print 'Updated phone# for:', self.name

job = AddrBookEntry('leng', 39383)

