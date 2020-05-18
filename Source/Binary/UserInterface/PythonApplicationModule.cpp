/// 1.
// Add
#ifdef ENABLE_DSS_ACTIVE_EFFECT_BUTTON
	PyModule_AddIntConstant(poModule, "ENABLE_DSS_ACTIVE_EFFECT_BUTTON", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_DSS_ACTIVE_EFFECT_BUTTON", 0);
#endif