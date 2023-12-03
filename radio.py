#!/bin/python3

import subprocess
import sys


stacje = [ 
    ['Radio Kraków', 'http://stream3.nadaje.com:9116/radiokrakow'],
    ['Polskie Radio 24', 'http://stream3.polskieradio.pl:8080/'],
    ['Polskie Radio Jedynka', 'http://stream3.polskieradio.pl:8900/'],
    ['RDN Małopolska', 'http://stream1.dabcom.pl:8000/rdn_mpl.m3u'],
    ['Radio Jasna Góra', 'http://online.radiojasnagora.pl:8000/rjg.m3u'],
    ['Radio Niepokalanów', 'http://88.199.169.10:8004/listen.pls'],
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
