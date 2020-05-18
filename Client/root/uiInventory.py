''' 1. '''
# Search
		self.DSSButton = None

# Add below
		if app.ENABLE_DSS_ACTIVE_EFFECT_BUTTON:
			self.DSSButtonEffect = None

''' 2. '''
# Search
	def ClickDSSButton(self):
		self.interface.ToggleDragonSoulWindow()

# Add below
	if app.ENABLE_DSS_ACTIVE_EFFECT_BUTTON:
		def UseDSSButtonEffect(self, enable):
			if self.DSSButton:
				DSSButtonEffect = ui.SlotWindow()
				DSSButtonEffect.AddFlag("attach")
				DSSButtonEffect.SetParent(self.DSSButton)
				DSSButtonEffect.SetPosition(3.2, 0)

				DSSButtonEffect.AppendSlot(0, 0, 0, 32, 32)
				DSSButtonEffect.SetRenderSlot(0)
				DSSButtonEffect.RefreshSlot()

				if enable == True:
					DSSButtonEffect.ActivateSlot(0)
					DSSButtonEffect.Show()
				else:
					DSSButtonEffect.DeactivateSlot(0)
					DSSButtonEffect.Hide()
				self.DSSButtonEffect = DSSButtonEffect