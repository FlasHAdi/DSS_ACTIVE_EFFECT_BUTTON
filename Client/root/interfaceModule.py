''' 1. '''
# Search
			wndDragonSoul = uiDragonSoul.DragonSoulWindow()

# Add below
			wndDragonSoul.BindInterfaceClass(self)

''' 2. '''
# Search
if __name__ == "__main__":

# Add above
	if app.ENABLE_DSS_ACTIVE_EFFECT_BUTTON:
		def UseDSSButtonEffect(self, enable):
			if self.wndInventory:
				self.wndInventory.UseDSSButtonEffect(enable)