## My GTK3 and Gnome Shell themes 

A collection of simple GTK2/GTK3 and Gnome shell themes made in the sparetime.

**MecOS** is the current maintained theme and it works **only** for latest gnome version (current is vers. 3.38.x).

- GTK3 3.24.23 or above is required for gtk3 theme. For GTK2 and other requirements check the end of this readme..


![MosArc GWF](https://raw.github.com/dasnoopy/moslight-themes/master/Screenshots/MecOS.png)

MecOS folder contain **only** GTK2, GTK3 and Gnome Shell theme

**MecOS** is yet another osx inspired theme and it is deeply based on these others works:

- https://github.com/vinceliuice/Mojave-gtk-theme (made by https://github.com/vinceliuice)
- https://github.com/paullinuxthemer/Prof-Gnome (made by https://github.com/paullinuxthemer)
- https://github.com/paullinuxthemer/Mc-OS-themes (made by https://github.com/paullinuxthemer)

So many thanks to developers!

**Installation notes:**

- Download the zip file then...

*... for all users:*

- as root, copy MecOS and MecOS-Dark folders into `/usr/share/themes`;
- open Gnome-Tweak and choose the theme.

*... for your account only:*

- copy MecOS and MecOS-Dark folders into `~/.local/share/themes`;
- if doesn't exist, create also a symbolic links in your home dir to that folder (this is needed for the gtk2 theme);

    `$ ln -s ~/.local/share/themes .themes`

- open Gnome-Tweak and choose the theme.

**Old and unsupported themes:**

* **MosArc** is a theme designed **only** for gnome 3.34 and it was based on ARC theme (https://github.com/horst3180/Arc-theme). 
	GTK2 v2.24.x and GTK3 v3.22.x libs are required. (btw it could works also on gnome 3.36)

* **MosLight** is a theme designed  **only** for Gnome 3.12: it works only with GTK2 v2.24.x and
  GTK3 v3.12.x libs.

* **MosEmite** is a theme designed **only** for Gnome 3.14: it works only with GTK2 v2.24.x and
  GTK3 v3.14.x libs

* **MosSky** is a theme designed **only** for Gnome 3.16: it works only with GTK2 v2.24.x 
  and GTK3 v3.16.x libs

* **MosCloud** is a theme designed **only** for Gnome 3.18: it works only with GTK2 v2.24.x 
  and GTK3 v3.18.x libs

You can find these old themes also on deviantart page (http://dasnoopy.deviantart.com/)


**GTK2 ENGINES REQUIREMENT**

* GTK2 engine Murrine 0.98.1.1 or later.
* GTK2 pixbuf engine or the gtk(2)-engines package.


**How to install required gtk2/3 engines:**

*ArchLinux*:  `$pacman -S gtk-engine-murrine gtk-engines gnome-themes-standard`

*Other distro*: Search for the engines in your distribution's repository or install the engines from source.
