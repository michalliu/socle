soc-config
==========

This is a simple yet modular SoC configuration utility, very much like
raspi-config and others alike. This one is written in Python and it aims
extendibility.

Features
--------

Preliminary support for following has been implemented

* Configure hostname
* Configure timezone
* Configure wired/wireless network interfaces on Debian
* User interface fallbacks for UART

Boards
------

Following boards will be supported

* Cubieboard2
* Cubietruck
* Raspberry Pi
* ZYBO
* Radxa

Debian jessie running on Cubietruck:

![Image of Cubietruck running soc-config](http://lauri.võsandi.com/shared/soc-config/mainmenu-cubietruck.png)

Raspbian running on Raspberry Pi:

![Image of Raspberry Pi running soc-config](http://lauri.võsandi.com/shared/soc-config/mainmenu-raspi.png)

Ubuntu 12.04 running on ZYBO:

![Image of ZYBO running soc-config](http://lauri.võsandi.com/shared/soc-config/mainmenu-cubietruck.png)

Goals
-----

* Support u-boot configuration parsing, modifying and writing
* Support platform specific configuration editing
* Support Debian adoption on SoC-s
* Compatibility with UART connections, no fancy UI there
