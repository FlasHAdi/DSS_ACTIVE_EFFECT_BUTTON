''' 1. '''
# Search
	def SetDragonSoulRefineWindow(self, wndDragonSoulRefine):

# Add above
	def BindInterfaceClass(self, interface):
		from _weakref import proxy
		self.interface = proxy(interface)

''' 2. '''
# Search
	def ActivateDragonSoulByExtern(self, deck):
		self.ActivateEquipSlotWindow(deck)
		self.isActivated = True
		self.activateButton.Down()
		self.deckPageIndex = deck
		self.deckTab[deck].Down()
		self.deckTab[(deck + 1) % 2].SetUp()
		self.RefreshEquipSlotWindow()

# Add below
		if app.ENABLE_DSS_ACTIVE_EFFECT_BUTTON:
			if self.interface:
				self.interface.UseDSSButtonEffect(self.isActivated)

''' 3. '''
# Search
	def DeactivateDragonSoul(self):
		self.DeactivateEquipSlotWindow()
		self.isActivated = False
		self.activateButton.SetUp()

# Add below
		if app.ENABLE_DSS_ACTIVE_EFFECT_BUTTON:
			if self.interface:
				self.interface.UseDSSButtonEffect(self.isActivated)