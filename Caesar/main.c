#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* caesar(char* in, int shift) {
  int str_len = strlen(in);
  char* out = calloc(str_len + 1, sizeof(char));
  for(int i = 0; i < str_len; i++) {
    char c = in[i];
    if(c >= 'a' && c <= 'z') {
      c = (c - 'a' + shift) % 26 + 'a';
    } else if(c >= 'A' && c <= 'Z') {
      c = (c - 'A' + shift) % 26 + 'A';
    }
    out[i] = c;
  }
  return out;
}

int main() {
  char* in = "Hello, World!";
  char* out = caesar(in, 3);
  printf("%s\n", out);
}
