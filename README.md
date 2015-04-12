Mos*-themes
-----------

Simple GTK2/GTK3 and Gnome shell themes

Note:

* **Moslight** is a theme designed  **only** for Gnome 3.12: it works only with GTK2 v2.24.x and
  GTK3 v3.12.x libs.

* **Mosemite** is a theme designed **only** for Gnome 3.14: it works only with GTK2 v2.24.x and
  GTK3 v3.14.x libs

* **MosSky** is a theme designed **only** for Gnome 3.16: it works only with GTK2 v2.24.x 
  and GTK3 v3.16.x libs

To install the theme, copy it into `/usr/share/themes` (for all users)

If you copy theme in your `~/.local/share/themes`, create also a symbolic links in your home dir to
that folder

`$ ln -s ~/.local/share/themes .themes`

then use Gnome-Tweak-Tool to choose the theme.

GTK2 ENGINES REQUIREMENT
* GTK2 engine Murrine 0.98.1.1 or later.
* GTK2 pixbuf engine or the gtk(2)-engines package.

GTK3 ENGINES REQUIREMENTS:
* GTK3 engine Adwaita 3.12 (only for Moslight)
* Since GTK+ 3.14, the Adwaita theme is shipped by GTK+ itself, and does not use any engine

How to install required gtk2/3 engines:

ArchLinux:
- pacman -S gtk-engine-murrine gtk-engines gnome-themes-standard

Other distro:
Search for the engines in your distribution's repository or install the engines from source.

MosLight (GTK+3.12) :
![Moslight GWF](https://raw.github.com/dasnoopy/moslight-themes/master/Screenshots/moslight.png)

Mosemite (GTK+3.14) :
![Mosemite GWF](https://raw.github.com/dasnoopy/moslight-themes/master/Screenshots/mosemite.png)
