#include <stdio.h>
#include <string.h>


struct Vehicule {
    char marque[50];
    char modele[50];
    int annee;
    char couleur[20];
    char energie[20];
};


struct Vehicule vehicules[100];
int nombreVehicules = 0;


void ajouterVehicule() {
    struct Vehicule vehicule;
    
    printf("Marque : ");
    scanf("%s", vehicule.marque);
    
    printf("Modèle : ");
    scanf("%s", vehicule.modele);
    
    printf("Année : ");
    scanf("%d", &vehicule.annee);
    
    printf("Couleur : ");
    scanf("%s", vehicule.couleur);
    
    printf("Énergie (diesel, essence, électrique) : ");
    scanf("%s", vehicule.energie);
    
    vehicules[nombreVehicules] = vehicule;
    nombreVehicules++;
    
    printf("Véhicule ajouté avec succès.\n");
}


void supprimerVehicule() {
    int index;
    
    printf("Indice du véhicule à supprimer : ");
    scanf("%d", &index);
    
    if (index >= 0 && index < nombreVehicules) {
        for (int i = index; i < nombreVehicules - 1; i++) {
            vehicules[i] = vehicules[i + 1];
        }
        
        nombreVehicules--;
        printf("Véhicule supprimé avec succès.\n");
    } else {
        printf("Indice invalide.\n");
    }
}


void modifierVehicule() {
    int index;
    
    printf("Indice du véhicule à modifier : ");
    scanf("%d", &index);
    
    if (index >= 0 && index < nombreVehicules) {
        struct Vehicule* vehicule = &vehicules[index];
        
        printf("Marque : ");
        scanf("%s", vehicule->marque);
        
        printf("Modèle : ");
        scanf("%s", vehicule->modele);
        
        printf("Année : ");
        scanf("%d", &vehicule->annee);
        
        printf("Couleur : ");
        scanf("%s", vehicule->couleur);
        
        printf("Énergie (diesel, essence, électrique) : ");
        scanf("%s", vehicule->energie);
        
        printf("Véhicule modifié avec succès.\n");
    } else {
        printf("Indice invalide.\n");
    }
}


void afficherStatistiques() {
    printf("Statistiques des véhicules :\n");
    
    
    int nombreDiesel = 0;
    int nombreEssence = 0;
    int nombreElectrique = 0;
    int nombreRouge = 0;
    int nombreBleu = 0;
    int nombreBlanc = 0;
    
    
    for (int i = 0; i < nombreVehicules; i++) {
        struct Vehicule vehicule = vehicules[i];
        
    
        if (strcmp(vehicule.energie, "diesel") == 0) {
            nombreDiesel++;
        } else if (strcmp(vehicule.energie, "essence") == 0) {
            nombreEssence++;
        } else if (strcmp(vehicule.energie, "électrique") == 0) {
            nombreElectrique++;
        }
        
        
        if (strcmp(vehicule.couleur, "rouge") == 0) {
            nombreRouge++;
        } else if (strcmp(vehicule.couleur, "bleu") == 0) {
            nombreBleu++;
        } else if (strcmp(vehicule.couleur, "blanc") == 0) {
            nombreBlanc++;
        }
        
        
    }
    
    
    printf("Nombre de véhicules diesel : %d\n", nombreDiesel);
    printf("Nombre de véhicules essence : %d\n", nombreEssence);
    printf("Nombre de véhicules électrique : %d\n", nombreElectrique);
    printf("Nombre de véhicules rouges : %d\n", nombreRouge);
    printf("Nombre de véhicules bleus : %d\n", nombreBleu);
    printf("Nombre de véhicules blancs : %d\n", nombreBlanc);
    
}


void afficherListeVehicules() {
    printf("Liste des véhicules :\n");
    
    for (int i = 0; i < nombreVehicules; i++) {
        struct Vehicule vehicule = vehicules[i];
        
        printf("Véhicule %d :\n", i + 1);
        printf("Marque : %s\n", vehicule.marque);
        printf("Modèle : %s\n", vehicule.modele);
        printf("Année : %d\n", vehicule.annee);
        printf("Couleur : %s\n", vehicule.couleur);
        printf("Énergie : %s\n", vehicule.energie);
        printf("-----------------------------\n");
    }
}


void genererStatistiquesCirculation() {
    printf("Statistiques de la circulation routière :\n");
    
    
}


void rechercherVehicule() {
    char critere[50];
    
    printf("Critère de recherche (numéro d'immatriculation, marque, modèle, année, couleur) : ");
    scanf("%s", critere);
    
    printf("Résultats de la recherche pour le critère \"%s\" :\n", critere);
    
    
}

int main() {
    int choix = 0;
    
    while (choix != 6) {
        printf("----- Menu -----\n");
        printf("1. Ajouter un véhicule\n");
        printf("2. Supprimer un véhicule\n");
        printf("3. Modifier un véhicule\n");
        printf("4. Afficher les statistiques des véhicules\n");
        printf("5. Afficher la liste complète des véhicules\n");
        printf("6. Quitter\n");
        
        printf("Choix : ");
        scanf("%d", &choix);
        
        switch (choix) {
            case 1:
                ajouterVehicule();
                break;
            case 2:
                supprimerVehicule();
                break;
            case 3:
                modifierVehicule();
                break;
            case 4:
                afficherStatistiques();
                break;
            case 5:
                afficherListeVehicules();
                break;
            case 6:
                printf("Au revoir.\n");
                break;
            default:
                printf("Choix invalide.\n");
        }
    }
    
    return 0;
}
