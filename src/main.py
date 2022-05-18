# TODO: Add AI/Algorythm Handling (minmax)
# TODO: GUI Refining
# TODO: SQLite DB with Save Functionality (Own menu/page?)
# TODO: Game Modes
# TODO: Game Rules per mode (Own menu/page?)
# TODO: Alpha/Beta Pruning (AI/Algorythmic Optimizations)
# TODO: Ability to sideload different algorythms (single file with dynamic loading?)

# OPTIONAL TODO: Fucking online multiplayer cuz why not

# EXTERNAL TODO: Documentation

from windows.mainWindow import mainWindow
from windows.versionWindow import versionWindow

mW = mainWindow()
vW = versionWindow(mW)

mW.launch()
