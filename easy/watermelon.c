#include <stdio.h>

int main(){
    int melon_kg;
    scanf("%d", &melon_kg);
    
    // Weight in kilo must be greater than 2 and should be even
    if (melon_kg > 2 && melon_kg % 2 == 0){
        printf("YES\n");
    }else{
        printf("NO\n");
    }
}
