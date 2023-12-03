#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definicje stałych
#define MAX_STATIONS 10
#define MAX_NAME_LEN 50 
#define MAX_URL_LEN 100 

// Struktura dla stacji
typedef struct {
    char name[MAX_NAME_LEN];
    char url[MAX_URL_LEN];
} Station;

// Definicja stacji
Station stations[MAX_STATIONS] = {
    {"Radio Kraków", "http://stream3.nadaje.com:9116/radiokrakow"},
    {"Polskie Radio 24", "http://stream3.polskieradio.pl:8080/"},
    {"Polskie Radio Jedynka", "http://stream3.polskieradio.pl:8900/"},
    {"Radio RDN Małopolska", "http://stream1.dabcom.pl:8000/rdn_mpl.m3u"},
};

// Zmienna dla wybranej stacji
int selected_station = -1;

// Funkcje
void clear() {
    system("clear");
}

void list_stations() {
    printf("RadioCtacja - Radia internetowe\n\n");
    for(int i = 0; i < MAX_STATIONS; i++) {
        if(strlen(stations[i].name) > 0) {
            printf("%d. %s\n", i+1, stations[i].name);
        }
    }
    printf("\nNaciśnij Q aby zamknąć\n");
}

void select_station() {
    printf("\nWybierz stację: ");
    char input[10];
    fgets(input, 10, stdin);
    if(input[0] == 'q' || input[0] == 'Q' || input[0] == '0') {
        clear();
        exit(0);
    }
    selected_station = atoi(input) - 1;
}

void play_station() {
    printf("\nTeraz gra: %s\n", stations[selected_station].name);
    char command[300];
    sprintf(command, "mpv --really-quiet '%s'", stations[selected_station].url);
    system(command);
}

int main() {
    while(1) {
        clear();
        list_stations();
        select_station();
        play_station();
    }
    return 0;
}
