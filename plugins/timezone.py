
import os
import pytz
from menu import choice
from atomic import AtomicWrite

def reconfigure_timezone():
    """
    Yeah we could have simply issued dpkg-reconfigure tzdata, but where's the fun in that?
    Well this one should be pretty platform agnostic and should work over the UART aswell.
    """
    
    superset = sorted(set([j.split("/", 1)[0] for j in pytz.all_timezones if "/" in j]))
            
    superselection = choice([(j,j) for j in superset],
        "Reconfigure timezone",
        "Please select geographic area in which this machine is located:")
        
    superselection += "/"

    subset = sorted([j[len(superselection):] for j in pytz.all_timezones if j.startswith(superselection)])

    subselection = choice([(j,j) for j in subset],
        "Reconfigure timezone",
        "Please select the city or region corresponding to your timezone:")
        
    with AtomicWrite("/etc/timezone") as fh:
        fh.write(superselection + subselection + "\n")

    # Update /etc/localtime symlink
    if os.path.exists("/etc/localtime.part"):
        os.unlink("/etc/localtime.part")
    os.symlink("/usr/share/zoneinfo/" + superselection + subselection, "/etc/localtime.part")
    os.rename("/etc/localtime.part", "/etc/localtime")

MENU_ENTRIES = (
    ("Set timezone", reconfigure_timezone),
)
