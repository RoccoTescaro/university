# Intelligenza Artificiale 

UNIVERSITA’ DEGLI STUDI DI FIRENZE \
Facolta di Ingegneria \
Corso di Laurea in Ingegneria Informatica \
[[B003725] Intelligenza Artificiale](https://ai.dinfo.unifi.it/teaching/ai_2023.html)
___

Professore : [Paolo Frasconi](paolo.frasconi@pm.me) \
Textbook : [Artificial Intelligence: A Modern Approach](<!-- #TODO -->) (4th Edition)
___

Il corso corrente si concentra un alcune delle tecniche più importanti dell'Intelligenza Artificiale, con particolare attenzione alle G.O.F.A.I. (Good Old Fashioned Artificial Intelligence) e alle tecniche di Machine Learning. In particolare vedremo alcune tecniche simboliche, problemi di ricerca (eg. pathfinding), problemi di soddisfacimento di vincoli, problemi di rappresentazione della conoscienza e ragionamento, ecc. Inoltre vedremo alcune tecniche di Machine Learning, come le reti neurali, le reti bayesiane, il reinforcement learning, ecc.  <!-- #TODO -->
___

##### Indice: <!-- #TODO -->
- 
- 
- 
___

#### Rapporto intelligenza artificiale e intelligenza umana

|                    | Think | Act |
| ------------------ | ----- | --- |
|   __like Humans__  |   no  |  no |
|__with Rationality__|   no  | yes |

__Razionalità__: in termini semplici "fare la cosa giusta", vale a dire massimizzare il risultato _atteso_ ( il risultato reale può essere diverso da quello atteso, ma la scelta è stata fatta sulla base di quello che si pensava fosse il risultato migliore, ambiente potrebbe essere non deterministico o non osservabile). Il risultato atteso dipende dalla conoscenza dell'agente, dalle azioni che può eseguire e dal modo in cui le azioni influenzano lo stato del mondo, e dall'obiettivo che gli viene posto (quest ultimo in particolare non facile da modellare).

Questo modello, paradigma di razionalità, è così ampiamente accettato che viene spesso chiamato _"the standard model"_. Uno dei problemi di questo modello è che non è sempre possibile o facile allineare l'obiettivo dell'agente con quello dell'umano, questo problema è detto _"value alignment problem"_. Ad esempio se si vuole costruire un agente che deve guidare una macchina, l'obiettivo dell'agente è quello di portare il passeggero a destinazione, ma se per fare ciò deve superare un semaforo rosso, l'obiettivo dell'agente non è allineato con quello dell'umano, che è quello di non superare il semaforo rosso. Questo problema è particolarmente importante ed è causa principale dello scetticismo verso l'Intelligenza Artificiale[^1]. 

[^1]: Vedi intervista a [Geoffrey Hinton](https://youtu.be/qpoRO378qRY?si=UE93Z4cKHS5RbcRc). 

Un concetto ulteriore che non indagheremo in profondità è quello di _razionalità limitata_ che dipende quindi da tempo o risorse limitate.
___

#### Agente e Ambiente

![RapportoAgenteAmbiente](..\Immagini\rapportoAgenteAmbiente.png) \
La rappresentazione non è di tipo insiemistico ma relazionale, l'agente e l'ambiente vanno sempre intesi come due entità distinte. E' tuttavia possibile che in un ambiente multiagente, un agente dipenda dagli altri e quindi li percepisca e agisca su di loro come parte dell'ambiente. 

__Agente__: qualcosa che percepisce l'ambiente tramite sensori e agisce su di esso tramite attuatori. \
__Percezione__: ciò che viene percepito dall'agente tramite sensori. \
__Sequenza di Percezioni__: la storia completa di ciò che l'agente ha percepito fino ad un certo momento \
__Funzione agente__: mappa da sequenze di percezioni a azioni (in alcuni casi anche da sequenze di percezioni a sequenze di azioni). La funzione agente è un oggetto matematico di cardinalità infinita e pertanto non implementabile fisicamente (in generale). La funzione agente determina il passaggio di stato quindi questo dipende esclusivamente dalla sequenza di percezioni e la base di conoscienze (caratteristica dei sistemi causali)e in certi casi in forma ancora più restrittiva, vale la legge di Markov, quindi il passaggio di stato dipende esclusivamente dallo stato precedente.\
__Programma agente__: implementazione fisica della funzione agente (non per mezzo di una mappa, ma tramite un algoritmo).

__Misura di prestazione__: criterio che determina il successo dell'agente data una sequenza di stati dell'ambiente (quindi la desiderabilità di una certa sequenza di azioni). Come introdotto precedentemente la misura di prestazione non è necessariamente ottima, ma è quella che l'agente ritiene ottima sulla base della sua conoscenza e obiettivo. \
__Agente Razionale__: agente che sceglie l'azione che massimizza la misura di prestazione, data la sequenza di percezioni fino a quel momento e la base di conoscienze. 

__Ambiente__: ciò che circonda l'agente, ha diverse caratteristiche che possono variare molto da problema a problema (la definizione varia quindi molto e quella che segue è informale, più simile ad una lista di caratteristiche):

<div style="position: absolute; border-left: 1px solid #000; height: 7vh; margin: 0 0;"> </div>

- __Completamente osservabile__ : l'agente può vedere lo stato dell'ambiente in ogni momento.
- __Parzialmente osservabile__ : l'agente può vedere solo una parte dello stato dell'ambiente in ogni momento.

<div style="position: absolute; border-left: 1px solid #000; height: 7vh; margin: 0 0;"> </div>

- __Agente singolo__ : un solo agente opera nell'ambiente.
- __Multiagente__ : più agenti operano nell'ambiente (in questo caso il problema può essere cooperativo o competitivo).

<div style="position: absolute; border-left: 1px solid #000; height: 7vh; margin: 0 0;"> </div>

- __Deterministico__ : l'effetto delle azioni è determinato dallo stato attuale dell'ambiente.
- __Non deterministico__ : l'effetto delle azioni è non determinato dallo stato attuale dell'ambiente.

<div style="position: absolute; border-left: 1px solid #000; height: 7vh; margin: 0 0;"> </div>

- __Episodico__ : le azioni dell'agente non dipendono dalle azioni precedenti.
- __Sequenziale__ : le azioni dell'agente dipendono dalle azioni precedenti.

<div style="position: absolute; border-left: 1px solid #000; height: 7vh; margin: 0 0;"> </div>

- __Statico__ : l'ambiente non cambia mentre l'agente sta pensando.
- __Dinamico__ : l'ambiente cambia mentre l'agente sta pensando.

<div style="position: absolute; border-left: 1px solid #000; height: 7vh; margin: 0 0;"> </div>

- __Discreto__ : l'ambiente ha un numero di stati assumibili discreto (la nozione di discreto può essere applicata anche al numero di azioni e percezioni).
- __Continuo__ : l'ambiente ha un numero di stati assumibili continuo.

<div style="position: absolute; border-left: 1px solid #000; height: 7vh; margin: 0 0;"> </div>

- __Conosciuto__ : l'agente conosce le regole dell'ambiente.
- __Sconosciuto__ : l'agente non conosce le regole dell'ambiente.
