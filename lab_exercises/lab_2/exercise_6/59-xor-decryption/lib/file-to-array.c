
void file_to_array_of_chars(char *array_init_ptr);


/*  SAMPLE USAGE: initialize array and pass pocharer to it  */
  
/*  +1 element for null pointer  */

/*  static int quantity = 664579 +1; */

/*  static int quantity = 5761455 +1;  */
 
/*  int primes[quantity]; */


/* int main() { */

/*   file_to_array_of_ints(&primes[0]); */

/* } */


void file_to_array_of_chars(char *array_init_ptr) {

  FILE *numbers_file;

  char* array_ptr = array_init_ptr;

  int i = 0;

  if ((numbers_file = fopen("./lib/cipher.tx", "r"))) {

    while ( fscanf(numbers_file, "%hhu", array_ptr) != EOF) {

      array_ptr++;

      /* i++; */

      /* printf("%p \n\n", primes_ptr); */

    }

    fclose(numbers_file);

    *array_ptr = '\0';

    printf("read numbers from file, to %p \n", array_init_ptr);

    /* for ( primes_ptr = array_init_ptr ; *primes_ptr != '\0'; primes_ptr++ ) { */

    /*   printf("%d\n", *primes_ptr); */

    /* } */

  }

}
