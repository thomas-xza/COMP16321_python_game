#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "./lib/file-to-array.c"

char
check_range_of_chars(char *cipher_ptr, char *key_ptr, int len);

void
decrypt_message(char *cipher_ptr, char *key_ptr, int len);

int
main(int argc, char *argv[]) {

  int i, len;

  unsigned char a, b, c, result;

  unsigned char cipher[1500], key[4];

  len = 1455;

  key[3] = '\0';

  memset(cipher, 0, sizeof cipher);

  file_to_array_of_chars(&cipher[0]);

  for ( a = 97 ; a < 123 ; a++ ) {

    for ( b = 97 ; b < 123 ; b++ ) {

      for ( c = 97 ; c < 123 ; c++ ) {

	key[0] = a;

	key[1] = b;

	key[2] = c;

	result = check_range_of_chars(&cipher[0], &key[0], len);

	if ( result == 1 ) {

	  printf("potential key: %s\n", key);

	  decrypt_message(&cipher[0], &key[0], len);

	}

      }

    }

  }
  
}

char
check_range_of_chars(char *cipher_ptr, char *key_ptr, int len) {

  int i;

  unsigned char max, min, loop, decrypted;

  max = 0;

  min = 255;
  
  loop = 0;
  
  for ( i = 0 ; i < len ; i++ ) {

    decrypted = *(key_ptr + loop) ^ *(cipher_ptr + i);

    loop++;

    if ( decrypted < min ) {

      min = decrypted;

    }

    if ( decrypted > max ) {

      max = decrypted;

    }

    if ( loop == 3 ) {

      loop = 0;

    };

    /* printf("%hhu\n", cipher[i]); */

  }

  if ( max < 123 && max > 31 && min > 31 && min < 123 ) {

    return 1;

  }

  return 0;

}


void
decrypt_message(char *cipher_ptr, char *key_ptr, int len) {

  int i, ascii_sum;

  unsigned char loop, decrypted;

  loop = 0;

  ascii_sum = 0;

  for ( i = 0 ; i < len ; i++ ) {

    decrypted = *(cipher_ptr + i) ^ *(key_ptr + loop);

    ascii_sum = ascii_sum + decrypted;

    /* printf("%d XOR %c = %c\n", *(cipher_ptr + i), *(key_ptr + loop), decrypted); */

    printf("%c ", decrypted);

    loop++;

    if ( loop == 3 ) {

      loop = 0;

    };

  }

  printf("\nascii_sum:  %d\n\n", ascii_sum);

}
