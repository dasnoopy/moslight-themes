Mos*-themes
-----------

Simple GTK2/GTK3 and Gnome shell themes

* **MosLight** is a theme designed  **only** for Gnome 3.12: it works only with GTK2 v2.24.x and
  GTK3 v3.12.x libs.

* **MosEmite** is a theme designed **only** for Gnome 3.14: it works only with GTK2 v2.24.x and
  GTK3 v3.14.x libs

* **MosSky** is a theme designed **only** for Gnome 3.16: it works only with GTK2 v2.24.x 
  and GTK3 v3.16.x libs

* **MosCloud** is a theme designed **only** for Gnome 3.18: it works only with GTK2 v2.24.x 
  and GTK3 v3.18.x libs

Stable versions are available on my deviantart page (http://dasnoopy.deviantart.com/)

**Just for fun:**

* **MosArc** is a GTK2/3 and gnome shell theme based on ARC theme (https://github.com/horst3180/Arc-theme) and it works for Gnome 3.24 (I don't know if it works also for previous gnome versions). GTK2 v2.24.x 
  and GTK3 v3.22.x libs are required. Noticeable changes are OSX like windows controls with reduced padding and few other minor changes.

**Some notes:**

To install the theme, copy it into `/usr/share/themes` (for all users)

If you copy theme in your `~/.local/share/themes`, create also a symbolic links in your home dir to
that folder

`$ ln -s ~/.local/share/themes .themes`

then use Gnome-Tweak-Tool to choose the theme.

**GTK2 ENGINES REQUIREMENT**
* GTK2 engine Murrine 0.98.1.1 or later.
* GTK2 pixbuf engine or the gtk(2)-engines package.

**GTK3 ENGINES REQUIREMENTS**
* GTK3 engine Adwaita 3.12 (only for Moslight)
* Since GTK+ 3.14, the Adwaita theme is shipped by GTK+ itself and it does not use any engine

How to install required gtk2/3 engines:

ArchLinux:
- pacman -S gtk-engine-murrine gtk-engines gnome-themes-standard

Other distro:
Search for the engines in your distribution's repository or install the engines from source.

**How they looks like :**
![MosSky GWF](https://raw.github.com/dasnoopy/moslight-themes/master/Screenshots/MosSky.png)

- MosArc
![MosArc GWF](https://raw.github.com/dasnoopy/moslight-themes/master/Screenshots/MosArc.png)

