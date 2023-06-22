#!/usr/bin/python3
#
# @author: Andrea Antolini (https://github.com/Dasnoopy)
# @license: GNU General Public License v3.0
# @link: https://github.com/dasnoopy/git-check


# TODO List
# gracefull interupt ctrl+c
# modificare anche svg
# tema  salvabili e richiamambili in seguito 

import os
import sys
import configparser

# from gi.repository import Gio

# SCHEMA = 'org.gnome.shell.extensions.user-theme'
# KEY = 'name'

# def change_theme(theme):
#     gsettings = Gio.Settings.new(SCHEMA)
#     gsettings.set_string(KEY, theme)
#     gsettings.apply()

def hex_to_rgb(hexa):
	hexa = hexa.lstrip('#')
	return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))

# python program for the above approach

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


# creating a variable and storing the text
# that we want to search
R1 = str(rgb1[0])
G1 = str(rgb1[1])
B1 = str(rgb1[2])

R2 = str(rgb2[0])
G2 = str(rgb2[1])
B2 = str(rgb2[2])

# creating a variable and storing the text
# that we want to add
print('\033[38;2;146;255;12mChange accent color for gnome shell theme v44...!\033[0m')
print('')
print('❯❯ Current lighter accent color : \033[48;2;' + R1 + ';' + G1 + ';' + B1 + 'm  ' + search_lighter_color + '  \033[0m')
print('❯❯ Current darker accent color  : \033[48;2;' + R2 + ';' + G2 + ';' + B2 + 'm  ' + search_darker_color + '  \033[0m')
print('')


# input colors
#lighter color
while True:
	try:
		replace_lighter_color = input('Enter new lighter accent color  :   ') 
		rgb3 = hex_to_rgb(replace_lighter_color)
		R3 = str(rgb3[0])
		G3 = str(rgb3[1])
		B3 = str(rgb3[2])
		print('\033[F❯❯ New lighter accent color     : \033[48;2;' + R3 + ';' + G3 + ';' + B3 + 'm  ' + replace_lighter_color + '  \033[0m')
		if (isValidHexaCode(replace_lighter_color)):
			break;
		else:
			print('Not a valid HEX color code! Colors must be in #RRGGBB format.')
	except:
		continue

#darker color
while True:
	try:
		replace_darker_color = input('Enter new darker accent color   :   ') 
		rgb4 = hex_to_rgb(replace_darker_color)
		R4 = str(rgb4[0])
		G4 = str(rgb4[1])
		B4 = str(rgb4[2])
		print('\033[F❯❯ New darker accent color      : \033[48;2;' + R4 + ';' + G4 + ';' + B4 + 'm  ' + replace_darker_color + '  \033[0m')
		if (isValidHexaCode(replace_darker_color)):
			break;
		else:
			print('Not a valid HEX color code! Colors must be in #RRGGBB format.')
	except:
		continue

print('')
input("Press Enter to continue and apply new colors...")

# get shado box rgba color from ligher color
replace_rgba_color = 'rgba' + str(hex_to_rgb(replace_lighter_color)).rstrip(')')
#
# print (replace_lighter_color)
# print (replace_darker_color)
# print (replace_rgba_color)
# sys.exit (0)

# Opening our text file in read only
# mode using the open() function
with open(r'gnome-shell.css', 'r', encoding='utf-8') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()
	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_lighter_color, replace_lighter_color)
	data = data.replace(search_darker_color, replace_darker_color)
	data = data.replace(search_rgba_color, replace_rgba_color)

# Opening our text file in write only
# mode to write the replaced content
with open(r'gnome-shell.css', 'w', encoding='utf-8') as file:

	# Writing the replaced data in our
	# text file
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
print('\033[38;2;146;255;12mDone. Enjoy new gnome-shell colors ;-)\033[0m')
print ('')
sys.exit(0)
