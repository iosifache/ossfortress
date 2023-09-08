#include <ctype.h>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "generate_recovery_token.h"
#include "sha256.h"

#define HEXDUMP_COLS 16

void hexdump(void *mem, unsigned int len) {
  /* https://gist.github.com/richinseattle/c527a3acb6f152796a580401057c78b4*/
  unsigned int i, j;

  for (i = 0;
       i <
       len + ((len % HEXDUMP_COLS) ? (HEXDUMP_COLS - len % HEXDUMP_COLS) : 0);
       i++) {
    if (i % HEXDUMP_COLS == 0) {
      printf("0x%06x: ", i);
    }

    if (i < len) {
      printf("%02x ", 0xFF & ((char *)mem)[i]);
    } else {
      printf("   ");
    }

    if (i % HEXDUMP_COLS == (HEXDUMP_COLS - 1)) {
      for (j = i - (HEXDUMP_COLS - 1); j <= i; j++) {
        if (j >= len) {
          putchar(' ');
        } else if (isprint(((char *)mem)[j])) {
          putchar(0xFF & ((char *)mem)[j]);
        } else {
          putchar('.');
        }
      }
      putchar('\n');
    }
  }
}

int main() {
  hexdump(generate_recovery_token("aa", 2), SHA256_BLOCK_SIZE);

  return 0;
}
