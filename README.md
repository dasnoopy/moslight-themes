## My GTK3 and Gnome Shell themes 

A collection of simple GTK2/GTK3 and Gnome shell themes made in the sparetime.

**McOS** is the current maintained theme and it works **only** for Gnome 3.36.x.

- GTK3 3.24.16 or above is required for gtk3 theme. For GTK2 and other requirements check the end of this readme..


![MosArc GWF](https://raw.github.com/dasnoopy/moslight-themes/master/Screenshots/McOS.png)

McOS folder contain **only** GTK2, GTK3 and Gnome Shell theme

**McoS** is deeply inspired by these themes:

- https://github.com/vinceliuice/Mojave-gtk-theme (made by https://github.com/vinceliuice)
- https://github.com/paullinuxthemer/Prof-Gnome (made by https://github.com/paullinuxthemer)
- https://github.com/paullinuxthemer/Mc-OS-themes (made by https://github.com/paullinuxthemer)

So many thanks to their creators / maintainers!

**Old and unsupported themes:**

* **MosArc** is a theme designed **only** for gnome 3.34and it was based on ARC theme (https://github.com/horst3180/Arc-theme). 
	GTK2 v2.24.x and GTK3 v3.22.x libs are required. 

* **MosLight** is a theme designed  **only** for Gnome 3.12: it works only with GTK2 v2.24.x and
  GTK3 v3.12.x libs.

* **MosEmite** is a theme designed **only** for Gnome 3.14: it works only with GTK2 v2.24.x and
  GTK3 v3.14.x libs

* **MosSky** is a theme designed **only** for Gnome 3.16: it works only with GTK2 v2.24.x 
  and GTK3 v3.16.x libs

* **MosCloud** is a theme designed **only** for Gnome 3.18: it works only with GTK2 v2.24.x 
  and GTK3 v3.18.x libs

You can find these old themes also on deviantart page (http://dasnoopy.deviantart.com/)

**Some notes:**

* To install the theme, copy theme folder into `/usr/share/themes` (for all users)

* If you copy theme in your `~/.local/share/themes`, create also a symbolic links in your home dir to
that folder

    `$ ln -s ~/.local/share/themes .themes`

* then, use Gnome-Tweak to choose the theme.

**GTK2 ENGINES REQUIREMENT**

* GTK2 engine Murrine 0.98.1.1 or later.
* GTK2 pixbuf engine or the gtk(2)-engines package.


**How to install required gtk2/3 engines:**

*ArchLinux*:  `$pacman -S gtk-engine-murrine gtk-engines gnome-themes-standard`

*Other distro*: Search for the engines in your distribution's repository or install the engines from source.
