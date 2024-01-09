# Fisica II

UNIVERSITA’ DEGLI STUDI DI FIRENZE \
Facolta di Ingegneria \
Corso di Laurea in Ingegneria Informatica \
[[B024251] Fisica II](https://e-l.unifi.it/course/view.php?id=31849)
___

#### Indice

- [Autoinduzione](#autoinduzione)
- 
___

#### Lavoro e Potenziale elettrostatico (conservatività del campo elettrostatico)
pag. 27

Il lavoro delle forze elettrostatiche è dato da $dW = \vec{F} \cdot d\vec{s} = q_0\vec{E} \cdot d\vec{s} = q_0 E \cos(\theta)$ con $E \cos(\theta)$ la proiezione di $\vec{E}$ su $d\vec{s}$. 

Lavoro totale $W = \int dW = \int_\gamma q_0 \vec{E} D\vec{s} = q_0 \int_\gamma \vec{E} d\vec{s}$. Per un percorso chiuso $W = \oint \vec{F} d\vec{s} = \int_{\gamma_1} \vec{F} d\vec{s} + \int_{-\gamma_2} \vec{F} d\vec{s} = \int_{\gamma_1} \vec{F} d\vec{s} - \int_{\gamma_2} \vec{F} d\vec{s} = W_1 - W_2 = q_0 \oint \vec{E} \cdot d\vec{s} = q_0 ℰ$ con ℰ detta forza elettromotrice.

In generale la f.e.m. è diversa da 0 e il campo elettrostatico non conservativo.  

___

#### Proprietà di un Conduttore in elettrostatica
pag. 1, 70

I conduttori hanno proprietà fisiche tali che buona parte delle cariche all'interno sono __libere di muoversi__ (più approssimativamente definiamo conduttori i materiali che non trattengono le cariche scambiate per strofinio). Generalmente ci si concentra sui conduttori solidi quali i metalli. 

Data un'opportuna applicazione di un campo elettrostatico è possibile far muovere ordinatamente le cariche libere all'interno del conduttore, generando una __corrente elettrica__. In elettrostatica siamo interessati a studiare il comportamento di cariche, appunto, 'statiche' pertanto il campo elettrico all'interno di un conduttore è nullo (parliamo in questi casi di __equilibrio elettrostatico__).

Questo è vero a livello macroscopico, a livello microscopico le cariche sono in continuo movimento e i nuclei degli atomi esercitano/generano un campo elettrostatico non nullo. 

L'assenza di un campo elettrico interno è:
- le cariche libere si dispongono sulla superficie del conduttore
- il potenziale elettrostatico è costante all'interno del conduttore
- il campo elettrico in un punto esterno nelle vicinanze del conduttore è perpendicolare alla superficie del conduttore e di intensità $E = \frac{\sigma}{\epsilon_0}$

La prima proprietà deriva dalla legge di Gauss:
$\Phi(E) = \oint E \cdot u_n \cdot d\Sigma = \frac{Q_int}{\epsilon_0}$ \
Prendendo una superficie completamente interna al conduttore abbiamo che il campo elettrico è nullo e quindi il flusso è nullo quindi la carica interna è nulla. Poichè la carica complessiva non è nulla allora deve essere presente una carica sulla superficie del conduttore.

La seconda proprietà dipende dalla definizione di potenziale elettrostatico: \
Dati due punti $P_1$ e $P_2$ all'interno del conduttore allora $\Delta V = V(P_2) - V(P_1) = - \int_{P_1}^{P_2} E \cdot ds = 0 \implies V(P_1) = V(P_2) = V_0$ (lo stesso vale se uno dei due punti è sulla superficie del conduttore).

La terza proprietà è una conseguenza della prima e della seconda: \
Poichè la superficie del conduttore è equipotenziale allora il campo elettrico è perpendicolare alla superficie del conduttore $E \cdot d\Sigma = \frac{dq}{\epsilon_0} = \frac{\sigma}{\epsilon_0} d\Sigma \implies E = \frac{\sigma}{\epsilon_0} \cdot u_n$ (teorema di Coulomb).

Dalle precedenti proprietà deriva poi che un conduttore sferico non influenzato da un campo elettrico esterno è equipotenziale e la carica si distribuisce uniformemente sulla superficie. 

Due o più conduttori collegati fisicamente da conduttori ideali mantegono le proprietà di conduttori isolati (avviene una ridistribuzione delle cariche).

Un conduttore con una o più cavità all'interno in equilibrio elttrostatico ha carica distribuita sempre e soltanto sulla superficie esterna.
___

#### Condensatore
pag. 76

Un sistema costituito da due conduttori tra i quali c'è induzione completa è detta condensatore.

La capacità di un condensatore è definita come $C = \frac{Q}{V}$ dove $Q$ è la carica e $V$ la differenza di potenziale tra i due conduttori. 

L'unità di misura della capacità è il ___Farad___ (F) che è pari a $[F] = \frac{[C]}{[V]} = \frac{[A][s]}{[V]} = [A][s][V]^{-1}$

Nel caso di un conduttore sferico di raggio $R_1$ al centro di un conduttore sferico cavo di raggio interno $R_2$ e raggio esterno $R_3$, se $Q$ è la carica disposta sulla superficie del conduttore interno, $-Q$ è la carica disposta sulla superficie interna del conduttore esterno e $Q$ quella sulla superficie esterna.

$E(r) = \begin{cases} \frac{Q}{4\pi\epsilon_0 r^2} & r \geq R_3 \\ 0 & R_2 \leq r \leq R_3 \\ \frac{Q}{4\pi\epsilon_0 R_3^3} \frac{R_2^3}{r^2} & R_1 \leq r \leq R_2 \\ 0 & r \leq R_1 \end{cases}, \Delta V = \frac{Q}{4\pi\epsilon_0}(\frac{1}{R_1}-\frac{1}{R_2}), C = \frac{4\pi\epsilon_0R_1R_2}{R_2 - R_1}$

Nel caso due conduttori siano posti in parallelo in modo tale che le loro armature compongano due conduttori collegati allora la capacità del sistema è la somma delle capacità dei due conduttori. 

Nel caso di condensatori in serie la carica è la stessa per entrambi i condensatori e la capacità del sistema è data da $C = \frac{C_1 C_2}{C_1 + C_2}$ ovvero il reciproco della somma dei reciproci delle capacità dei due condensatori.

Il processo di carica di un condensatore consiste in una separazione di cariche e richiede un determinato lavoro che, essendo il campo elettrostatico conservativo, dipende solo dallo stato iniziale e finale. Questa separazione può essere considerata come un trasferimento della carica dall'armatura negativa su quella positiva.

Quindi $dW = V' \cdot dq' = \frac{q'}{C}dq'$ con $V'$ la differenza di potenziale tra le due amrature in una fase intermedia del processo e $q'$ la carica $CV'$ trasferita.

$W = \int dW = \int_0^Q \frac{q'}{C}dq' = \frac{Q^2}{2C}$. Questo lavoro viene immagazzinato nel sistema sotto forma di energia potenziale elettrostatica.

$U_e = \frac{Q^2}{2C} = \frac{CV^2}{2} = \frac{QV}{2}$

In un condensatore piano il campo elettrostatico uniforme $V = E*h$, $C = \frac{\epsilon_0 \Sigma}{h}$ e $U_e = \frac{1}{2} \epsilon_0 E^2 \Sigma h = \frac{1}{2} \epsilon_0 E^2 \tau$.

Si definisce la __densità di energia elettrostatica__ come $u_e = \frac{U_e}{\tau} = \frac{1}{2} \epsilon_0 E^2$. Il fatto che la formula della densità di energia elettrostatica non contenga misure relative al condensatore ci suggerisce la sua genralità. E' dimostrabile che $dU_e = u_e \cdot d\tau = \frac{1}{2} \epsilon_0 E^2 \cdot d\tau \implies U_e = \int_\tau \frac{1}{2} \epsilon_0 E^2 \cdot d\tau$.
___

#### Legge di Ampere
pag. 177

Dato un filo indefinito in cui scorre corrente vale:\
$B \cdot ds = \frac{\mu_0 i}{2 \pi r} ds = \frac{\mu_0 i}{2 \pi} d\theta$, per un tratto finito di circonferenza possiamo quindi scrivere $\int_\gamma B \cdot ds = \frac{\mu_0 i}{2 \pi} \int_\gamma d\theta = \frac{\mu_0 i}{2 \pi} \theta$. 

Poichè il risultato dipende solo dall'angolo $\theta$ la legge continua a valere dato un qualsiasi percorso. Consideriamo ora un qualsiasi percorso chiuso che concatena la corrente: \
$\oint B \cdot ds = \frac{\mu_0 i}{2 \pi} \oint d\theta = \frac{\mu_0 i}{2 \pi} 2\pi = \mu_0 i$ (in caso il percorso non concateni la corrente allora il risultato è nullo).

L'enunciato della legge di Ampere è quindi: \
L'integrale di linea del campo magnetico $B$ lungo una linea chiusa, ovvero lua circuitazione $\Gamma (B)$ è uguale alla somma delle correnti concatenate moltiplicata per la costante $\mu_0$.

Applicando il teorema di Stokes possiamo scrivere: \
$\oint B \cdot ds = \int_\Sigma (\nabla \times B) \cdot u_n d\Sigma$ dove $\Sigma$ è una superficie qualsiasi che ha come bordo il percorso chiuso $\Gamma$. 

Attraverso la superficie $\Sigma$ passa una corrente $i$ e valendo $i = \int_\Sigma j \cdot u_n d\Sigma$ (con $j$ la densità di corrente che è diversa da 0 solo nel punto in cui il filo attraversa la superficie), allora la legge di Ampere diventa $\int_\Sigma (\nabla \times B) \cdot u_n d\Sigma = \mu_0 \int_\Sigma j \cdot u_n d\Sigma \implies \nabla \times B = \mu_0 j$. 

Questa forma della legge di Ampere è detta __forma locale__.
___

#### Legge di Faraday
pag. 203

Possiamo verificare sperimentalmente che se avviene un moto relativo tra una spira e una sorgente di campo magnetico, allora nella spira si genera una corrente __indotta__. 

Se è presente una corrente indotta allora è presente una forza elettromotrice indotta. Misurando la forza elettromotrice indotta (per mezzo ad esempio di un galvanometro) possiamo osservare che questa varia al variare del campo magnetico. 

Faraday dalle misurazioni sperimentali dedusse che $ℰ_i = - \frac{d \Phi(B)}{dt}$ detta __legge di Faraday__ o __legge di Faraday-Neumann__ o __legge di Faraday-Henry__. 

Da questo possiamo dedurre che la corrente indotta è data da $i = \frac{ℰ_i}{R} = - \frac{1}{R}\frac{d\Phi(B)}{dt}$, che però è un effetto secondario, valido solo se è presente una resistenza nel circuito.

Ricordiamo che la forza elettromotrice è il lavoro per unità di carica necessario per spostare una carica positiva da un punto ad un altro del circuito e vale: \
$ℰ_i = \oint E_i \cdot ds = - \frac{d \Phi(B)}{dt} [V]$ (altra dimostrazione che il campo elettrico indotto non è conservativo)
___

#### Autoinduzione
pag. 212

Un qualsiasi circuito elettrico produce un campo magnetico (legge di Ampere-Laplace). Il flusso del campo magnetico (con superficie $\Sigma$ una superficie qualsiasi che ha il circuito elettrico come bordo) è : \
$\Phi(B) = \int_{\Sigma} ( \oint \frac{\mu_0 i}{4 \pi} \frac{ds \times u_r }{r^2})\cdot u_n d\Sigma$

Il flusso del campo magnetico e il campo magnetico stesso sono proporzionali alla corrente che scorre nel circuito elettrico. Per questo motivo scriveremo $\Phi(B) = L i$ dove $L$ è la costante di proporzionalità che prende il nome di __coeff. di autoinduzione__ o __induttanza__ (del circuito).

L'unità di misura dell'induttanza è il ___Henry___ (H) che è pari a $[H] = \frac{[V] [s]}{[A]} = [\Omega][s]^{-1}$

Se la corrente che scorre nel circuito varia nel tempo allora anche la forza elettromotrice indotta (detta __autoinduzione__) varia nel tempo. \
La forza elettromotrice indotta è data da $ℰ_L = - \frac{d \Phi(B)}{dt} = - L \frac{d i}{dt}$ 

Dalla formula precedente possiamo ottenere una definizione alternativa di induttanza, indipendente dal circuito e dal mezzo in cui è immerso (a patto di porre come ipotesi che l'induttanza sia costante nel tempo).
___

#### Energia magnetica
pag. 216

Considerimo una spira con un generatore che genera una corrente $i$. La spira avvicinandosi ad un'altra spira induce una corrente $i'$ in quest'ultima. La potenza erogata dal generatore quando la corrente $i$ scorre nella spira è:
$P = ℰi = Ri^2 + Li\frac{di}{dt} \implies ℰi \cdot dt = Ri^2 \cdot dt + Li \cdot di$ con $ℰi \cdot dt = ℰ \cdot dq = dW$ ovvero abbiamo descritto il __bilancio energetico del circuito__.

$Ri^2 \cdot dt$ è l'energia dissipata per effetto Joule, mentre $Li \cdot di$ è l'energia spesa contro la forza elettromotrice di autoinduzione.

$W_L = \int dW_L = \int_0^i Li \cdot di = \frac{1}{2} Li^2$. Poichè il lavoro speso contro la f.e.m. di autoinduzione non dipende dal modo in cui avviene la variazione di corrente ma solo dai valori iniziali e finali possiamo parlare di __energia intrinseca della corrente__. 

Avendo legato l'induttanza alla variazione del campo magnetico possiamo vedere l'energia intrinseca della corrente in funzione del campo magnetico: \
$U_L = \frac{1}{2} Li^2 = \frac{1}{2}(\mu_0 n^2 \Sigma d) i^2 = \frac{B^2}{2\mu_0}\tau$ (quantomeno per un solenoide rettilineo indefinito di cui consideriamo il tratto d).

Si dimostra che lo stesso vale per un solenoide toroidale. Possiamo quindi identificare una __densità di energia magnetica__ pari a $u_L = \frac{B^2}{2\mu_0}$.

$U_L = \int_\tau \frac{B^2}{2\mu_0} d\tau$ 
___

