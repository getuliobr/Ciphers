#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* xor(char* str, char* key) {
  int str_len = strlen(str);
  char* result = calloc(str_len + 1, sizeof(char));
  for (int i = 0; i < str_len; i++) {
    result[i] = str[i] ^ key[i % strlen(key)];
  }
  return result;
}

int main() {
  char* in = "Hello, world!";
  char* key = "key";
  char* encoded = xor(in, key);
  printf("encoded %s\n", encoded);
  char* decoded = xor(encoded, key);
  printf("decoded %s\n", decoded);
  free(encoded);
  free(decoded);
  return 0;
}