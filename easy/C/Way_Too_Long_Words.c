#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){    
    int list_num;
    scanf("%d", &list_num); // num of lines to expect

    char **words = malloc(list_num * sizeof(char *)); // allocate memory for array

    if(words == NULL){
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    for(int i = 0; i < list_num; i++){ // check for long words above 100 or below 1
        char buff[101];

        scanf("%s", buff);

        // allocate memory space for each word
        words[i] = malloc((strlen(buff) + 1) * sizeof(char));

        if(words[i] == NULL){
            fprintf(stderr, "Memory allocation failed\n");
            return 1;
        }
        
        if(strlen(buff) < 1 || strlen(buff) > 100){
            printf("Word Length must be between 1 and 100");
            return 1;
        }
        if(strlen(buff) > 10){ // check for long words above 10; abbreviate it.
            int len = strlen(buff);
            snprintf(words[i], len + 1, "%c%d%c", buff[0], len - 2, buff[len - 1]);
        }else{
            strcpy(words[i], buff); // input into array
        }    
    }

    for(int i = 0; i < list_num; i++){
        printf("%s\n",words[i]);
    }

    // free allocated memories
    for(int i = 0; i < list_num; i++){free(words[i]);}

    free(words);

    return 0;
}
