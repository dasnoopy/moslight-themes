## My GTK3 and GTK4 and Gnome Shell themes 

**MyAdwaita** is the current maintained **gnome-shell** theme and it works **only** with gnome version **45.x**.

![MyAdwaita GWF](https://raw.github.com/dasnoopy/moslight-themes/master/Screenshots/MyAdwaita.png)

**Installation notes:**

**Note** : MyAdwaita folder contain Gnome Shell themes **only**. 

- Download the zip file then...

*... for all users:*

- as root, copy MyAdwaita-Light and MyAdwaita-Dark folders into `/usr/share/themes`;
- open Gnome-Tweak and choose the theme.

*... for your account only:*

- copy MyAdwaita-Light and MyAdwaita-Dark folders into `~/.local/share/themes` (if it doesn't exist, create also a symbolic links in your home dir to that folder);

    `$ ln -s ~/.local/share/themes .themes`

- open Gnome-Tweak and choose the gnome-shell theme.

**Old and unsupported themes:**

* **MecOS** is a them designed **only** with for version **40.x**.

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
