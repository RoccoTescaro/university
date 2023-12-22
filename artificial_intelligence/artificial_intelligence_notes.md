# Intelligenza Artificiale 

UNIVERSITA’ DEGLI STUDI DI FIRENZE \
Facolta di Ingegneria \
Corso di Laurea in Ingegneria Informatica \
[[B003725] Intelligenza Artificiale](https://ai.dinfo.unifi.it/teaching/ai_2023.html)
___

Professore : [Paolo Frasconi](paolo.frasconi@pm.me) \
Textbook : [Artificial Intelligence: A Modern Approach](<!-- #TODO -->) (4th Edition)
___

##### Indice: <!-- #TODO -->
- [Introduzione al corso](#introduzione-al-corso)
- [Rapporto intelligenza artificiale e intelligenza umana](#rapporto-intelligenza-artificiale-e-intelligenza-umana)
- [Agente e Ambiente](#agente-e-ambiente)
- [Problemi di Ricerca](#problemi-di-ricerca)
- [Algoritmi di Ricerca](#algoritmi-di-ricerca)
___

#### Introduzione al corso

Il corso corrente si concentra un alcune delle tecniche più importanti dell'Intelligenza Artificiale, con particolare attenzione alle __G.O.F.A.I.__ (Good Old Fashioned Artificial Intelligence) e alle tecniche di Machine Learning. In particolare vedremo alcune tecniche simboliche, problemi di ricerca (eg. pathfinding), problemi di soddisfacimento di vincoli, problemi di rappresentazione della conoscienza e ragionamento, ecc. Inoltre vedremo alcune tecniche di Machine Learning, come le reti neurali, le reti bayesiane, il reinforcement learning, ecc.  

Nel passato, in qualità di umani ci siamo sempre interrogati su come il nostro cervello funziona, come percepisce il mondo circostante e la natura della nostra coscienza. Con la nascita di questa nuova disciplina/campo di studio, l'intelligenza artificiale, siamo passati a porci nuovi obbiettivi, ovvero ricreare, simulare, quello che accade biologicamente nei nostri cervelli.

Il campo dell'ai è in un periodo di massimo sviluppo, investendo il mercato e le società di ricerca e sviluppo che ci investono i bilioni e dei nuovi orizzonti sono stati posti alla conoscienza umana. Mentre per i campi come la fisica o la matematica, le grandi '_scoperte_'  sono state già fatte, l'intelligenza artificiale è una disciplina ancora estremamente giovane e proliferante di innovazioni.

I campi di applicazioni sono infiniti: dalla medicina alla fisica e matematica stessa (riconoscere malattie e provare teoremi ecc.).

Cosa si intende per intelligenza? non è facile da definire, molti filosofi, ingegnieri ecc ci hanno provato dando delle definzioni diverse molti hanno definito intelligente ciò chè è razionale (vale a dire in certi termini, ciò che fa la cosa giusta). Questa definizione crea, però delle dicotomie fra ciò che è '_human-like_' e che quindi in qualche modo ammette errore e '_rational_' e che quindi è matematicamente, statisticamente corretto, fra ciò che è pensiero e ragionamento. Nelle varie branche dell' a.i. si studiano metodi, algoritmi, modelli specifici per emulare, ricreare questi aspetti dell'intelligenza. 

Ormai superato ma ancora utile a delineare alcuni aspetti delle moderne a.i. è il test proposto da Turing per rispondere alla domanda: "può un computer pensare?". Quello che realmente si salva di quel test sono le macrobranche di ricerca in campo a.i. 
Per passare il test di fatto la macchina dovrebbe passare 6 tipi di test: _natural language processing_, _knowledge rappresentation_, _automated reasoning_, _machine learning_ (nel senso di estrapolazione di pattern), _computer vision_ e _robotics_.

<!-- #TODO --> complete summary cap. 1
___

#### Rapporto intelligenza artificiale e intelligenza umana

Abbiamo brevemente introdotto il concetto di agente razionale e di razionalità, ci concentreremo ora nel definirlo meglio e vedere come questo concetto viene applicato in diversi ambiti con pochi cambiamenti.

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
Definito cosa intediamo per razionalità vediamo in cosa consiste nel contesto del modello agente-ambiente. E' facile concepire che ci siano agenti che in un determinato ambiente si comportino meglio di altri, vogliamo dunque l'agente che si comporti al meglio possibile. 
Quanto effettivamente poi questo agente si comporti bene dipenderà dall'ambiente e dalle difficoltà che questi pone.

<-- #TODO --> add image
![RapportoAgenteAmbiente](..\Immagini\rapportoAgenteAmbiente.png) \
La rappresentazione non è di tipo insiemistico ma relazionale, l'agente e l'ambiente vanno sempre intesi come due entità distinte. E' tuttavia possibile che in un ambiente multiagente, un agente dipenda dagli altri e quindi li percepisca e agisca su di loro come parte dell'ambiente. 

__Agente__: qualcosa che percepisce l'ambiente tramite sensori e agisce su di esso tramite attuatori. \
__Percezione__: ciò che viene percepito dall'agente tramite sensori. \
__Sequenza di Percezioni__: la storia completa di ciò che l'agente ha percepito fino ad un certo momento \
__Funzione agente__: mappa da sequenze di percezioni a azioni (in alcuni casi anche da sequenze di percezioni a sequenze di azioni). La funzione agente è un oggetto matematico di cardinalità infinita e pertanto non implementabile fisicamente (in generale). La funzione agente determina il passaggio di stato quindi questo dipende esclusivamente dalla sequenza di percezioni e la base di conoscienze (caratteristica dei sistemi causali)e in certi casi in forma ancora più restrittiva, vale la legge di Markov, quindi il passaggio di stato dipende esclusivamente dallo stato precedente. \
__Programma agente__: implementazione fisica della funzione agente (non per mezzo di una mappa, ma tramite un algoritmo). La differenza fondamentale dalla funzione agente è che è fisico non un astrazione matematica.

Abbiamo definito lascamente che un agente razionale è l'agente che fa la cosa giusta (tralasciando il fatto che non sepre è possibile fare la cosa giusta/ non sempre si hanno le informazioni per fare la cosa giusta), proviamo ora a dare una definizione più formale.

__Misura di prestazione__: criterio che determina il successo dell'agente data una sequenza di stati dell'ambiente (quindi la desiderabilità di una certo stato dell'ambiente data una sequenza di azioni). Come introdotto precedentemente la misura di prestazione non è necessariamente ottima, ma è quella che l'agente ritiene ottima sulla base della sua conoscenza e obiettivo. Definire questa funzione obbiettivo è come stato detto in precedenza molto complesso perchè può portare l'agente a prendere decisioni inaspettate che nel peggiore dei casi potrebbero essere dannose. Di solito una buona regola per definire una misura di prestazione è definirla in accordo a ciò che si vuole ottenere piuttosto a come crediamo che l'agente dovrebbe comportarsi. \
__Agente Razionale__: agente che sceglie l'azione che massimizza la misura di prestazione, data la sequenza di percezioni fino a quel momento e la base di conoscienze. 

Bisogna distingure fra razionalità e omniscienza. Un agente omniscente conosce il reale risvolto di ogni sua azione ma spesso questo è impossibile da ottenere. Razionalità $\neq$ Perfezione. Detto ciò bisogna assicurarci di aver fatto il possibile per prendere la decisione migliore, preso azioni per modificare le pecezioni future (__Information Gathering__). Eg. prima di attraversare la strada guardare a destra e sinistra ci permette di massimizzare l'azione futura da prendere (decide se attraversare la strada o aspettare il passaggio delle macchine). Non solo l'agente deve ottenere nuove informazioni ma imparare da esse, modificando o ampliando la propria conoscenza di base. Un agente che dipende dalla propria conoscenza a priori si dice manchi di __autonomia__.

> __Domanda__: il concetto di autonomia è relativo alla conoscenza di base e ai bias che il programmatore dell'a.i. ha inserito all'interno. Lo stesso concetto puo essere applicato anche alla misura di prestazione? in altre parole può anch'essa essere soggeta a bias? e dunque c'è un modo/ esistono ai indipendenti da essa che imparano la propria misura di prestazione?

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
___

#### Problemi di Ricerca

Come è pressapocamente detto a volte è necessario all'agente per prendere decisioni razioniali, pianificare in anticipo le proprie azioni. Un agente di questo tipo è detto '_problem-solving agent_' (nel caso la rappresentazione dello stato dell'ambiente sia atomica, indivisbile) o '_planning agent_' (nel caso abbia sovrastrutture interne, rappresentazioni dello stato dell'ambiente) e la ricerca attuata dallo stesso è appunto detta '_search_'. Analizzeremo solo ambienti semplici: episodici, agente singolo, completamente osservabili, deterministici, statici, discreti e conosciuti. 

Una prima distinzione da fare è fra algoritmi di ricerca informati e non informati:
- __Informati__ : l'agente può stimare quanto è distante dall'obbiettivo
- __Non informati__ : altrimenti.

Le fasi di risoluzione del problema sono fondamentalmente 4:
- formulazione del goal
- formulazione del problema (ricrea un modello dell'ambiente in cui possa simulare le azioni da intraprendere)
- ricerca, appunto simula le varie azioni fino al raggiungimento dell'obbiettivo. Tale sequenza di azioni è _una_ soluzione.
- esecuzione

__Formalizzazione__:

Chiamiamo $P$ il __problema di ricerca__. \
Chiamiamo $P.S$ l'insieme degli __stati__ in cui l'ambiente può trovarsi. \
Chiamiamo $P.$ __$s_0$__ $ \in P.S$ lo __stato iniziale__ da cui l'agente parte. \
Chiamiamo $P.G$ l'insieme (che ha spesso cardinalità 1) degli stati obbiettivo, dei __goals__. E' utile definire una funzione, matematicamente una mappa, booleana $P$.__IS_GOAL__(s) che dato uno stato verifica che questi appartenga a $P.G$. \
Chiamiamo $P.A$ l'insieme di tutte le possibili azioni intraprendibili dato un qualsiasi stato. \
Definiamo una funzione $P$.__ACTIONS__(s) che dato uno stato resituisce l'insieme delle possibili azioni che possono essere eseguite in __s__. \
Definiamo la funzione $P$.__RESULT__($s_i$, a), detta __funzione di transizione__, la funzione che dato lo stato __$s_i$__ $ \in P.S$ e l'azione __a__ $ \in P.A$ restituisce lo stato __$s_f$__ $ \in P.S$ ottenuto applicando l'azione __a__ allo stato __$s_i$__. \
Definiamo una funzione $P$.__ACTION_COST__(s, a, s$' = P$.__RESULT__(s, a)) che restituisce un valore numerico indicativo del costo di esecuzione dell'azione __a__ dato lo stato __s__. \

> __Osservazione__: s$' = P$.__RESULT__(s, a) è completamente omissibile

Chiamiamo __percorso__ una sequenza di azioni, e __soluzione__ un percorso da __$s_0$__ a __g__ $ \in P.G$. Diciamo che una soluzione è __ottima__ se la somma dei costi dato un percorso è minima ( la minore fra i costi di tutti i percorsi possibili ). \

Lo __spazio delgi stati__ viene usato intercambiabilmente per indicare $P.S$ e il grafo con nodi $P.S$ e archi $P$.__ACTIONS__.\
___

#### Algoritmi di Ricerca

Chiamiamo __algoritmo di ricerca__ un algoritmo che dato un problema di ricerca restituisce una soluzione o uno stato di _failure_. Ci sono diversi approcci per trovare una soluzione, in questo caso analizzeremo algoritmi che imporranno un __albero di ricerca__ nel grafo dello spazio degli stati che ha radice in __$s_0$__. Rispetto allo spazio delgi stati che da premessa era discreto, l'albero di ricerca può essere potenzialmente infinito anche con uno spazio finito poichè uno stesso stato potrebbe avere percorsi diversi indietro fino allo stato iniziale. L'albero di ricerca è un grafo acicilico (per definizione) ma i percorsi che definisce possono essere ciclici (_loopy paths_). Un ciclo è un caso speciale di percorso ridondante (_redundant path_). Ci sono tre approcci per affrontare questo problema: memorizzare i nodi già visitati ed evitare di riespanderli, ignorare il problema con le dovute analisi (in molti problemi il caso di ripetere un certo percorso è molto improbabile), controllare per i cicli ma non per percorsi ridondanti. <!-- #TODO --> clarify 
Chiamiamo un algoritmo ___graph search___ se evita di riespandere i nodi già visitati. \
Chiamiamo un algoritmo ___tree search___ se non evita di riespandere i nodi già visitati. \

<figure style = "display: block; margin-left: auto; margin-right: auto; width: 50%;" >
    <img src="https://pub.mdpi-res.com/mathematics/mathematics-10-01016/article_deploy/html/images/mathematics-10-01016-g012.png?1648026344"
         alt="path in the search tree"
         width="480"
         height="480" >
    <figcaption>Se nello stato del problema non fosse rappresentato un counter per il controllo della <i>threefold repetition rule</i> l'albero di ricerca potrebbe diramarsi ripetendo all'inifinito oscillando tra due stati (se le mosse sono reversibili)</figcaption>
</figure>

Da qui in avanti se non specificato ci riferiremo a _nodi_ per intendere i _nodi_ dell'albero di ricerca.
L'insieme di nodi ottenuti dal risultato di $P$.__RESULT__($s_i$, a), $\forall$ __a__ $\in P$.__ACTIONS__($s_i$) sono detti nodi __figli__ (risultato diretto) o __successori__ (esecuzione ripetuta della funzione) di __$s_i$__, mentre __$s_i$__ è il nodo __genitore__.\    
Dopo l'esecuzione di _result_ __$s_i$__ si dice __espanso__.\ 
Un nodo ottenuto dall'esecuzione di _result_ o la radice dell'albero si dice __raggiunto__.\
L'insieme di nodi non ancora espansi si dicono __frontiera__ o ___open list___ (la frontiera separa nello spazio degli stati i nodi espansi da quelli non ancora raggiunti).\

___Best-first search___ : algoritmo di ricerca che espande il nodo che sembra più vicino al goal data una ___evaluation function___ $f$($n$). La frontiera in questo caso è implementata con una ___Priority Queue___. \
___Breadth-first search___ : algoritmo di ricerca che espande tutti i nodi della frontiera, in ordine di profondità. La frontiera in questo caso è implementata con una ___FIFO Queue___. \
___Depth-first search___ : algoritmo di ricerca che espande il nodo più profondo della frontiera. La frontiera in questo caso è implementata con una ___LIFO Queue___. \

<!-- #TODO --> add interative deepening search, bidirectional ecc.

<details>
    <summary><b>CODE</b></summary>

    ```python
        def tree_search(problem, frontier, depth = -1):
        frontier.append(node(problem.s_0))
        while frontier:
            node = frontier.pop()
            if problem.is_goal(node.s):
                return node
            if depth != -1 and node.g < depth:
                for action in problem.actions(node.s):
                    # we are considering the path cost to be 1 for all actions -> child.g = parent.g + 1
                    child = node(problem.result(node.s, action), node, action, node.g + 1) 
                    frontier.append(child)
        return None
    ```

[See full python implementations for search problems](./algorithms/search_problems.py)
</details> 

Per misurare le performance di un algoritmo di ricerca si usano quattro parametri:
- __Completezza__ : l'algoritmo trova sempre una soluzione se esiste.
- __Ottimalità__ : l'algoritmo trova sempre la soluzione ottima se esiste.
- __Complessità spaziale__ : quanti nodi vengono memorizzati in memoria.
- __Complessità temporale__ : quanti nodi vengono generati e espansi.

Complessità spaziale e temporale sono misurate in termini di __b__ (fattore di branching, numero massimo di nodi figli di un nodo), __d__ (profondità massima dell'albero per la soluzione ottima) e __m__ (il massimo numero di azioni per un qualsiasi percorso), $||P.S||$ e $||(P.S \times P.A)||$ . \

