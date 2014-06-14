

try:
    screen = None
    import snack
except ImportError:
    print "Could not import snack, falling back to newt..."
    try:
        import newt as snack
        print "Could not import newt aswell, are you sure either python-snack or python-newt package is installed?"
    except ImportError:
        snack = None

import sys
from facts import TTY

class CanceledException():
    pass
    
def prepare():
    """
    Unobtrusively load snack if we're not connected via UART
    """
    global screen
    if snack and not screen:
        if not TTY.startswith("/dev/tty"):
            import atexit
            screen=snack.SnackScreen()
            atexit.register(screen.finish)
            oldexcepthook = sys.excepthook
            def newexcepthook(*args):
                screen.finish()
                oldexcepthook(*args)
            sys.excepthook = newexcepthook
		
def choice(choices, title="Select", help="Select one of following", actions=(("Ok", "ok"), ("Cancel", CanceledException()))):
    global screen
    prepare()
    choices = tuple(choices)
    MAX_HEIGHT = 20
    if screen:
        action, selected = snack.ListboxChoiceWindow(screen,
            title,
            help,
            choices,
    		buttons=actions,
    		height=MAX_HEIGHT if len(choices) > MAX_HEIGHT else -1,
    		scroll=len(choices) > MAX_HEIGHT)
        if isinstance(action, CanceledException):
            raise action
        return selected
    else:
        print
        print title
        print "=" * len(title)
        print help
        print
        for index, (title, value) in enumerate(choices):
            print "%d. %s" % (index+1, title)
        print
        while True:
            try:
                sys.stdout.write("> ")
                return choices[int(sys.stdin.readline()) - 1][1]
            except:
                print "Invalid selection, try again"

def form(fields, title="Fill fields", help="Fill following fields", actions=(("Ok", "ok"), ("Cancel", CanceledException))):
    global screen
    prepare()
    if screen:
        action, selection = snack.EntryWindow(screen,
            title,
            help,
		    fields,
		    buttons=actions)
        if isinstance(action, CanceledException):
            raise action
        return selection
    else:
        raise NotImplementedError

