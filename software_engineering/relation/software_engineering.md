# Ingengeria del Software

UNIVERSITA’ DEGLI STUDI DI FIRENZE \
Facolta di Ingegneria \
Corso di Laurea in Ingegneria Informatica \
[[B003372] Ingegneria del Software](https://e-l.unifi.it/course/view.php?id=31223)
___

#### Indice
- [Introduzione](#introduzione)
    - [Obiettivi del Progetto](#obiettivi-del-progetto)
    - [Elementi del progetto](#elementi-del-progetto)
    - [Estendibilità del progetto](#estendibilità-del-progetto)
- [Analisi dei requisiti](#analisi-dei-requisiti)
    - [Use Case Diagram](#use-case-diagram)
___

#### Introduzione

##### Obiettivi del Progetto
Il progetto corrente nasce con l'obiettivo di realizzare un'applicazione per la gestione di campionati Fanta-sports, in particolare di calcio. E' ormai diffusissimo il fenomeno dei campionati fanta-sports, dove i giocatori hanno la possibilità di amministrare le proprie squadre favorite e sfidarsi con altri giocatori. L'applicazione nasce appunto con l'obiettivo di fornire un servizio/strumento per l'organizzazione di campionati privati e per estensione anche pubblici.

L'applicazione permette di creare leghe private di fanta-soccer, ovvero un campionato in cui gli utenti ad invito possono creare una squadra virtuale, composta da giocatori reali, e sfidarsi, con anche la possibilità di estendere le regole del campionato personalizzandole o possibilmente collegare un proprio database all'applicazione rendendo possibile la creazione di campionati di altri sport.

Le principali funzionalità dell'applicazione sono: la possibilità di creare un campionato, di invitare altri utenti a partecipare, di avviare un'asta e comporre una squadra, di definire modalità di punteggio e regole del campionato, di visualizzare la classifica e i risultati delle partite.

##### Elementi del progetto

Il progetto è composto da:
-  __Utente giocatore__: 
    è l'utente che partecipa al campionato, partecipare all'asta, comporre e gestire la propria squadra, visualizzare la classifica e i risultati delle partite. Non può modificare creare un campionato o modificare le regole di uno esistente  (nemmeno se partecipante dello stesso).
- __Utente amministratore__:
    è l'utente che crea un campionato, invita altri utenti a partecipare, avvia l'asta, modifica le regole. Scelte le regole, l'utente amministratore non può più modificarle a campionato iniziato. Ha anche il compito di fornire il database dei giocatori (reali) e il database delle valutazioni per il calcolo del punteggio. 

##### Estendibilità del progetto

Il progetto è stato pensato per essere estendibile, in particolare per quanto riguarda la possibilità di creare campionati di altri sport.
Per fare ciò è necessario fornire un database di giocatori e un database di valutazioni per il calcolo del punteggio.

Un'altra possibilità di estensione è la possibilità di avviare leghe pubbliche, ovvero leghe il cui accesso è disponibile a tutti gli utenti 
dell'applicazione, senza quindi necessità di invito da parte dell'amministratore. A questa estensione è legata anche la possibilità di visualizzare una
classifica globale, ovvero una classifica che tiene conto di tutti i campionati pubblici attivi.

In ultima istanza è possibile estendere l'applicazione affinchè siano gestite altre regole o tipologie di campionati, idealmente non vincolare dalla regola
dell'immutabilità delle regole a campionato iniziato.
___

#### Analisi dei requisiti

##### Use Case Diagram
