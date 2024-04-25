#!/usr/bin/python3
#
# @author: Andrea Antolini (https://github.com/Dasnoopy)
# @license: GNU General Public License v3.0
# @link: https://github.com/dasnoopy/moslight-themes


# TODO List
# tema  salvabili e richiamambili in seguito 
#

import os
import sys
import configparser

class colors:
	reset = '\033[0m'
	bold = '\033[01m'
	disable = '\033[02m'
	underline = '\033[04m'
	reverse = '\033[07m'
	strikethrough = '\033[09m'
	invisible = '\033[08m'

	class fg:
		black = '\033[30m'
		red = '\033[31m'
		green = '\033[32m'
		orange = '\033[33m'
		blue = '\033[34m'
		purple = '\033[35m'
		cyan = '\033[36m'
		lightgrey = '\033[37m'
		darkgrey = '\033[90m'
		lightred = '\033[91m'
		lightgreen = '\033[92m'
		yellow = '\033[93m'
		lightblue = '\033[94m'
		pink = '\033[95m'
		lightcyan = '\033[96m'

	class bg:
		black = '\033[40m'
		red = '\033[41m'
		green = '\033[42m'
		orange = '\033[43m'
		blue = '\033[44m'
		purple = '\033[45m'
		cyan = '\033[46m'
		lightgrey = '\033[47m'

def exit_on_error(message: str):
	print('')
	print (f"{colors.reset}{colors.fg.yellow}{message}{colors.reset}")
	print('')
	sys.exit(1)

def confirm_prompt(question: str) -> bool:
    reply = None
    while reply not in ("y", "n"):
        reply = input(f"{question} (y/n): ").casefold()
    return (reply == "y")

def hex_to_rgb(hexa):
	hexa = hexa.lstrip('#')
	return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))

# Just a small function to write the ini file
def write_file():
	config.write(open(iniFname, 'w', encoding='utf-8'))

# clean screen and welcome message
os.system('clear')
# define some variables
iniFname = 'colors.ini'
config = configparser.ConfigParser()

# if ini file is missing, create it with some default colors(from gnome HIG palette)
if not os.path.exists(iniFname):
	config['COLORS'] = {'hexlighter': '#3584e4', 'hexdarker': '#478fe6', 'rgbalighter': 'rgba(53, 132, 228,'}
	write_file()
	
# Read ini file...
config.read(iniFname)
search_lighter_color = config['COLORS']['hexlighter']
search_darker_color = config['COLORS']['hexdarker']
search_rgba_color = config['COLORS']['rgbalighter'] 

rgb1 = hex_to_rgb(search_lighter_color)
rgb2 = hex_to_rgb(search_darker_color)

R1 = str(rgb1[0])
G1 = str(rgb1[1])
B1 = str(rgb1[2])

R2 = str(rgb2[0])
G2 = str(rgb2[1])
B2 = str(rgb2[2])

print (f"{colors.reset}{colors.bold}{colors.fg.orange}❯❯ Change accent color for gnome shell and gtk4.css version 46.x{colors.reset}")
print ('')
print ('❯❯ Current color schema   : \033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm      \033[0m' '\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm      ' + '\033[0m')
print ('')

flatred         = '#e5383b','#ba181b' #1
flatorange      = '#e2711d','#cc5803' #2
flatyellow      = '#ffcd02','#ffa800' #3
flatsand        = '#f0dfb4','#d5c395' #4
flatnavyblue    = '#44475a','#282a36' #5
flatblack       = '#2d2d2d','#262626' #6
flatmagenta     = '#ce4993','#6a0d83' #7
flatteal        = '#607d8b','#4d646f' #8
flatskyblue     = '#3584e4','#1a5fb4' #9
flatgreen       = '#2dcc70','#27ae61' #10
flatmint        = '#1bbc9b','#16a086' #11
flatwhite       = '#ecf0f1','#bec3c7' #12
flatgray        = '#95a5a5','#7e8c8d' #13
flatforestgreen = '#9fc162','#396c2f' #14
flatpurple      = '#745dc5','#5b48a2' #15
flatbrown       = '#986a44','#63452c' #16
flatplum        = '#5e335e','#4f2b4f' #17
flatwatermelon  = '#ef727a','#d95459' #18
flatlime        = '#a5c63b','#8fb021' #19
flatpink        = '#f47cc3','#d45b9e' #20
flatmaroon      = '#79302a','#662722' #21
flatcoffee      = '#a28671','#8e725d' #22
flatpowderblue  = '#778da9','#415a77' #23
flatblue        = '#5165a2','#384c81' #24

colors_matrix = [[flatred,flatorange,flatyellow,flatsand],
				 [flatnavyblue,flatblack,flatmagenta,flatteal],
				 [flatskyblue,flatgreen,flatmint,flatwhite],
				 [flatgray,flatforestgreen,flatpurple,flatbrown],
				 [flatplum,flatwatermelon,flatlime,flatpink],
				 [flatmaroon,flatcoffee,flatpowderblue,flatblue]]
				
colors_list = [flatred,flatorange,flatyellow,flatsand,flatnavyblue,flatblack,
               flatmagenta,flatteal,flatskyblue,flatgreen,flatmint,flatwhite,
               flatgray,flatforestgreen,flatpurple,flatbrown,flatplum,flatwatermelon,
               flatlime,flatpink,flatmaroon,flatcoffee,flatpowderblue,flatblue]

def print_matrix_with_indices(matrix):
    index = 1
    # Loop over each row
    for i in range(len(matrix)):
        # Loop over each column in the current row
        for j in range(len(matrix[i])):
            # Print element at row i, column j
            rgb1 = hex_to_rgb(matrix[i][j][0])
            rgb2 = hex_to_rgb(matrix[i][j][1])
            R1 = str(rgb1[0])
            G1 = str(rgb1[1])
            B1 = str(rgb1[2])
            R2 = str(rgb2[0])
            G2 = str(rgb2[1])
            B2 = str(rgb2[2])
            print (f" {index:>2}"') \033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm      \033[0m' '\033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm      \033[0m', end=' ')
            index += 1
        # Print a new line after each row
        print()

# Test the function with our matrix
print_matrix_with_indices(colors_matrix)
print('')

x = ''
n = 24

while not (x.isdigit() and int(x) in range(1, n + 1)):
    x = input(f'❯❯ Choose a new color schema (1 to {n}): ')

replace_lighter_color = (colors_list[int(x)-1])[0]
replace_darker_color  = (colors_list[int(x)-1])[1]

# some checks
if replace_lighter_color == '' or replace_darker_color == '':
	 exit_on_error ('❯❯ No news colors defined: exit!')
elif replace_lighter_color == search_darker_color:
	exit_on_error('❯❯ Unable to proceed: new lighter color is equal to current darker color!')
elif replace_darker_color == search_lighter_color:
	exit_on_error('❯❯ Unable to proceed: new darker color is equal to current ligher color!')
elif replace_lighter_color == replace_darker_color:
	exit_on_error('❯❯ Unable to proceed: new lighter and darker color are the same!')
elif replace_lighter_color == search_lighter_color and replace_darker_color == search_darker_color:
	exit_on_error('❯❯ Nothing to change : current and new color schema are equal!')



# get shadow-box rgba color from ligher color
replace_rgba_color = 'rgba' + str(hex_to_rgb(replace_lighter_color)).rstrip(')') +','

reply = confirm_prompt("❯❯ Are you sure to proceed?")
if reply == False:
	exit_on_error('❯❯ Exit without do any change!')

# Opening our text file in read only
# mode using the open() function
with open(r'gnome-shell.css', 'r', encoding='utf-8') as file:
	data = file.read()
	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_lighter_color, replace_lighter_color)
	data = data.replace(search_darker_color, replace_darker_color)
	data = data.replace(search_rgba_color, replace_rgba_color)

# Opening our text file in write only
# mode to write the replaced content
with open(r'gnome-shell.css', 'w', encoding='utf-8') as file:
	file.write(data)

#update also asset/svgs
svg="toggle-on.svg"

with open(svg, 'r', encoding='utf-8') as file:
	data = file.read()
	data = data.replace(search_lighter_color, replace_lighter_color)
with open(svg, 'w', encoding='utf-8') as file:
	file.write(data)
	
#update also /home/andrea/.config/gtk-4.0/gtk.css
css="/home/andrea/.config/gtk-4.0/gtk.css"

with open(css, 'r', encoding='utf-8') as file:
	data = file.read()
	data = data.replace(search_lighter_color, replace_lighter_color)
	data = data.replace(search_darker_color, replace_darker_color)
with open(css, 'w', encoding='utf-8') as file:
	file.write(data)
	

#write INI file with new colors
config['COLORS']['hexlighter'] = replace_lighter_color
config['COLORS']['hexdarker'] = replace_darker_color
config['COLORS']['rgbalighter'] = replace_rgba_color
write_file()

# apply new colors on the fly using dbus-send command (gnome v46  tested)
# gnome shell session must be in unsafe mode
# use  this extensions to temporary set gs in unsafe mode while using this script
#
#  https://github.com/linushdot/unsafe-mode-menu
#
os.system("dbus-send --session --dest=org.gnome.Shell --print-reply --type=method_call /org/gnome/Shell org.gnome.Shell.Eval string:'Main.loadTheme(); ' > /dev/null")
# final greetings
print ('')
print (f"{colors.reset}{colors.bold}{colors.fg.orange}❯❯ Done. Enjoy your new gnome-shell accent color ;-){colors.reset}")
print ('')

sys.exit(0)
