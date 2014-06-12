
import importlib
import os
import re
import facts
from menu import choice, CanceledException

# Load plugins for configuring timezones, locales, network interfaces etc
plugins = []
for filename in os.listdir("plugins/"):
    if not filename.startswith("_") and filename.endswith(".py"):
        modname = "plugins.%s" % filename[:-3]
        print "Loading plugin:", modname
        plugins.append(importlib.import_module(modname))

# Detect board and populate main menu with platform specific options
def detect_board():
    for filename in os.listdir("boards/"):
        if not filename.startswith("_") and filename.endswith(".py"):
            mod = importlib.import_module("boards.%s" % filename[:-3])
            for obj in dir(mod):
                cls = getattr(mod, obj)
                if hasattr(cls, "match"):
                    if cls.match(facts):
                        return cls.instantiate()

board = detect_board()

MAINMENU = (
    ("Enable OpenSSH",                  NotImplemented),
    ("Disable boot to MATE desktop",    NotImplemented),
)

for plugin in plugins:
    MAINMENU += plugin.MENU_ENTRIES

MAINMENU = sorted(MAINMENU, key=lambda (k,v):k)

class RebootException(CanceledException): pass
class ShutdownException(CanceledException): pass
class ExitException(CanceledException): pass

while True:
    try:
        submenu = choice(
            MAINMENU,
            "Main menu",
            "SoC configuration utility",
            actions=(
                ("Ok", "ok"),
                ("Reboot", RebootException),
                ("Shutdown", ShutdownException),
                ("Exit", ExitException)
            )
        )
    except ExitException:
        break
    except RebootException:
        break
    except ShutdownException:
        break
    else:
        submenu()

