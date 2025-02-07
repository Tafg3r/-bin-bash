/* writer.c - Writes a string to a file and logs using syslog */
#include <stdio.h>
#include <stdlib.h>
#include <syslog.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        syslog(LOG_ERR, "Usage: %s <file_path> <text>", argv[0]);
        fprintf(stderr, "Usage: %s <file_path> <text>\n", argv[0]);
        return 1;
    }

    const char *file_path = argv[1];
    const char *text = argv[2];

    FILE *file = fopen(file_path, "w");
    if (!file) {
        syslog(LOG_ERR, "Error opening file: %s", file_path);
        perror("Error opening file");
        return 1;
    }

    fprintf(file, "%s", text);
    fclose(file);

    syslog(LOG_DEBUG, "Writing %s to %s", text, file_path);
    return 0;
}

// Makefile

CC=gcc
CFLAGS=-Wall -Werror
CROSS_COMPILE ?=

writer: writer.c
	$(CROSS_COMPILE)$(CC) $(CFLAGS) -o writer writer.c

clean:
	rm -f writer

