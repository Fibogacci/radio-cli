#!/bin/python3

# PL
# PyRadyjko v0.1 - skrypt powstał w 2020 roku
# autor: Fibogacci
# Skrypt wymaga zainstalowanego mpv
# Działa na Linux, Termux
# Uruchamianie: python3 radio.py
# Polskie strumienie radiowe do znalezienia na stronie: http://www.emsoft.ct8.pl/strumienie.php
# Lista stacji radiowych przykładowa, dla każdego coś dobrego, można dostosować wg upodobań
#
# EN
# PyRadyjko v0.1 - script created in 2022
# author: Fibogacci
# The script requires mpv installed
# Works on Linux, Termux
# To run: python3 radio.py
# Polish radio streams can be found on: http://www.emsoft.ct8.pl/strumienie.php
# The list of radio stations is exemplary, something good for everyone, can be customized to taste

import subprocess
import sys


stacje = [ 
    ['Radio Kraków', 'http://stream3.nadaje.com:9116/radiokrakow'],
    ['Polskie Radio 24', 'http://stream3.polskieradio.pl:8080/'],
    ['Polskie Radio Jedynka', 'http://stream3.polskieradio.pl:8900/'],
    ['RDN Małopolska', 'http://stream1.dabcom.pl:8000/rdn_mpl.m3u'],
    ['Radio Alex Zakopane', 'http://srv0.streamradiowy.eu/radioalex.m3u'],
    ['Radio Maryja', 'http://51.68.135.155/listen.pls'],
]

graj = None

def clear():
    subprocess.run(['clear'])

def lista():
    print('PyRadyjko - radia internetowe\n')
    for i in range(len(stacje)):
        print('{}. {}'.format(i+1, stacje[i][0]))
    print('\nNaciśnij Q, aby wyłączyć.')

def wybierz():
    global graj
    graj = input('\nWybierz stację: ')
    if str(graj) == 'q' or str(graj) == '0':
        clear()
        sys.exit()

def wlacz():
    # radio = subprocess.Popen(['mpg123', '--quiet', stacje[int(graj)-1][1]])
    radio = subprocess.Popen(['mpv', '--really-quiet', stacje[int(graj)-1][1]])
    radio.wait()

def teraz_gra():
    print('\nTeraz gra:', stacje[int(graj)-1][0])
    wlacz()

def pyradyjko():
    while True:
        clear()
        lista()
        wybierz()
        teraz_gra()

pyradyjko()
