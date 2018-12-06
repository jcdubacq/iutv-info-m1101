#include <stdio.h>
    
int tab[6]={1,2,3,4,5,6}; /* Cette variable est globale, elle est visible de partout */
    
void print_tab(void) {
    int i;
    /* Itération en C : quatre parties
       initialisation
       test d'entrée dans la boucle
       conclusion de la boucle
       et derrière : le bloc de code à exécuter dans la boucle
    */
    for ( i=0 ; i<6 ; i=i+1 ) {
        printf("%d ",tab[i]);
    }
    printf("\n");
}
    
int doubleEntier(int a) {
    return (a+a);
}
    
int main(void) {
    /* On fait les déclarations de variable locales au début de la fonction */
    int i;
    int somme=0;
    somme = 0;
    for (i=0;i<6;i++) {
        somme = somme + tab[i];
    }
    while (somme < 100) {
        print_tab(); // Pas d'arguments
        somme = 0;
        for (i=0;i<6;i++) {
            tab[i] = doubleEntier(tab[i]); // Argument
            somme = somme + tab[i];
        }
    }
    printf("C'est bon !");
    print_tab();
    return(0);
}
    
