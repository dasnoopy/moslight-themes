#!/usr/bin/python3
#
# @author: Andrea Antolini (https://github.com/Dasnoopy)
# @license: GNU General Public License v3.0
# @link: https://github.com/dasnoopy/git-check


# TODO List
# tema  salvabili e richiamambili in seguito 
#

import os
import sys
import configparser
import signal

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)

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

# Function to validate
# the HTML hexadecimal color code.
def isValidHexaCode(str):
	if (str[0] != '#'):
		return False
	if (not(len(str) == 4 or len(str) == 7)):
		return False
	for i in range(1, len(str)):
		if (not((str[i] >= '0' and str[i] <= '9') or (str[i] >= 'a' and str[i] <= 'f') or (str[i] >= 'A' and str[i] <= 'F'))):
			return False
	return True

#READ Previous colors from INI file
config = configparser.ConfigParser()
config.read('COLORS.INI')
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

print (f"{colors.reset}{colors.bold}# Change accent color for gnome shell theme v44...{colors.reset}")
print (f"{colors.reset}{colors.fg.green}- new lighter and darker color MUST BE DIFFERENT!{colors.reset}")
print (f"{colors.reset}{colors.fg.green}- new colors MUST BE DIFFERENT from current colors!{colors.reset}")
print (f"{colors.reset}{colors.fg.green}- new lighter color MUST BE DIFFERENT from current darker color!{colors.reset}")
print (f"{colors.reset}{colors.fg.green}- new darker color MUST BE DIFFERENT from current lighter color!{colors.reset}")
print (f"{colors.reset}{colors.fg.green}- leave one or both colors empy to quit without further actions{colors.reset}")
print ('')
print ('❯❯ Current lighter accent color : \033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm  ' + search_lighter_color + '  \033[0m')
print ('❯❯ Current darker accent color  : \033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm  ' + search_darker_color + '  \033[0m')
print('                                    <<< >>>')
# input colors
# lighter color
while True:
	try:
		replace_lighter_color = input('❯❯ New lighter accent color     :   ')

		if replace_lighter_color == "":
			break;

		if (isValidHexaCode(replace_lighter_color)):
			rgb3 = hex_to_rgb(replace_lighter_color)
			R3 = str(rgb3[0])
			G3 = str(rgb3[1])
			B3 = str(rgb3[2])
			print(f'\033[F{colors.reset}{colors.bold}❯❯ New lighter accent color     : \033[48;2;' + R3 + ';' + G3 + ';' + B3 + 'm  ' + replace_lighter_color + '  \033[0m')
			break;
		else:
			print('Not a valid HEX color code! Colors must be in #RRGGBB format.')
	except:
		continue

#darker color
while True:
	try:
		replace_darker_color = input('❯❯ New darker accent color      :   ')

		if replace_darker_color == "":
			break;

		if (isValidHexaCode(replace_darker_color)):
			rgb4 = hex_to_rgb(replace_darker_color)
			R4 = str(rgb4[0])
			G4 = str(rgb4[1])
			B4 = str(rgb4[2])
			print(f'\033[F{colors.reset}{colors.bold}❯❯ New darker accent color      : \033[48;2;' + R4 + ';' + G4 + ';' + B4 + 'm  ' + replace_darker_color + '  \033[0m')
			break;
		else:
			print('Not a valid HEX color code! Colors must be in #RRGGBB format.')
	except:
		continue

if replace_lighter_color == '' or replace_darker_color == '':
	 exit_on_error ('- One or both invalid colors: exit!')
elif replace_lighter_color == search_darker_color:
	exit_on_error('- Unable to proceed: new lighter color is equal to current darker color!')
elif replace_darker_color == search_lighter_color:
	exit_on_error('- Unable to proceed: new darker color is equal to current ligher color!')
elif (replace_lighter_color == search_lighter_color) and (replace_darker_color == search_darker_color):
	exit_on_error('- Unable to proceed: new colors are equal to current colors!')
elif replace_lighter_color == replace_darker_color:
	exit_on_error('- Unable to proceed: new lighter and darker color are the same!')

# get shado box rgba color from ligher color
replace_rgba_color = 'rgba' + str(hex_to_rgb(replace_lighter_color)).rstrip(')')
#
print ('')
print (f'{colors.reset}{colors.fg.green}- to activate new gs colors on the fly, you must install then Unsafe Mode Menu extension.{colors.reset}')
print (f'{colors.reset}{colors.fg.green}- extension link : https://github.com/linushdot/unsafe-mode-menu.{colors.reset}')
print (f'{colors.reset}{colors.fg.green}- Otherwise you may want use gnome-tweak tool to change gs theme, as usual.{colors.reset}')
print ('')

reply = confirm_prompt("Are you sure to proceed?")
if reply == False:
	print ('Exiting without any change...')
	sys.exit(0)

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
svg1="assets/checkbox.svg"
svg2="assets/checkbox-focused.svg"
svg3="assets/toggle-on.svg"

with open(svg1, 'r', encoding='utf-8') as file:
	data = file.read()
	data = data.replace(search_lighter_color, replace_lighter_color)
with open(svg1, 'w', encoding='utf-8') as file:
	file.write(data)

with open(svg2, 'r', encoding='utf-8') as file:
	data = file.read()
	data = data.replace(search_darker_color, replace_darker_color)
with open(svg2, 'w', encoding='utf-8') as file:
	file.write(data)

with open(svg3, 'r', encoding='utf-8') as file:
	data = file.read()
	data = data.replace(search_lighter_color, replace_lighter_color)
	data = data.replace(search_darker_color, replace_darker_color)
with open(svg3, 'w', encoding='utf-8') as file:
	file.write(data)

#write INI file
config['COLORS']['hexlighter'] = replace_lighter_color
config['COLORS']['hexdarker'] = replace_darker_color
config['COLORS']['rgbalighter'] = replace_rgba_color

with open('COLORS.INI', 'w', encoding='utf-8') as configfile:
    config.write(configfile)

# apply new colors on the fly using dbus-send command (gnome v44  tested)
# gnome shell session must be in unsafe mode
# use  this extensions to temporary set gs in unsafe mode while using this script
#
#  https://github.com/linushdot/unsafe-mode-menu
#
os.system("dbus-send --session --dest=org.gnome.Shell --print-reply --type=method_call /org/gnome/Shell org.gnome.Shell.Eval string:'Main.loadTheme(); ' > /dev/null")
# final greetings
print ('')
print (f"{colors.reset}{colors.bold}# Done. Enjoy new gnome-shell colors ;-){colors.reset}")
print ('')
sys.exit(0)
