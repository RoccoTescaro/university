# Fisica II

UNIVERSITA’ DEGLI STUDI DI FIRENZE \
Facolta di Ingegneria \
Corso di Laurea in Ingegneria Informatica \
[[B024251] Fisica II](https://e-l.unifi.it/course/view.php?id=31849)
___

#### Indice

- [Lavoro e Potenziale elettrostatico (conservatività del campo elettrostatico)](#lavoro-e-potenziale-elettrostatico-conservatività-del-campo-elettrostatico)
- [Dipolo elettrico](#dipolo-elettrico)
- [Legge/Teorema di Gauss](#leggeteorema-di-gauss)
- [Proprietà di un Conduttore in elettrostatica](#proprietà-di-un-conduttore-in-elettrostatica)
- [Condensatore](#condensatore)
- [Legge di Ampere](#legge-di-ampere)
- [Legge di Faraday](#legge-di-faraday)
- [Autoinduzione](#autoinduzione)
- [Energia magnetica](#energia-magnetica)
___

#### Lavoro e Potenziale elettrostatico (conservatività del campo elettrostatico)
pag. 27

Il lavoro delle forze elettrostatiche è dato da $dW = \vec{F} \cdot d\vec{s} = q_0\vec{E} \cdot d\vec{s} = q_0 E \cos(\theta)$ con $E \cos(\theta)$ la proiezione di $\vec{E}$ su $d\vec{s}$. 

Lavoro totale $W = \int dW = \int_\gamma q_0 \vec{E} d\vec{s} = q_0 \int_\gamma \vec{E} d\vec{s}$. Per un percorso chiuso $W = \oint \vec{F} d\vec{s} = \int_{\gamma_1} \vec{F} d\vec{s} + \int_{-\gamma_2} \vec{F} d\vec{s} = \int_{\gamma_1} \vec{F} d\vec{s} - \int_{\gamma_2} \vec{F} d\vec{s} = W_1 - W_2 = q_0 \oint \vec{E} \cdot d\vec{s} = q_0 ℰ$ misurato in ___joule___ $[J]$ con ℰ detta forza elettromotrice misurata in ___volt___ $[V]$.

In generale la f.e.m. è diversa da 0 e il campo elettrostatico non conservativo.  

Chiamiamo __differenza di potenziale elettrostatico__ $\Delta V$ la grandezza definita da $\Delta V = V(B) - V(A) = -\int_A^B \vec{E} \cdot d\vec{s}$ (misurata anch'essa in volt).\
Chiamiamo __potenziale eletrico__ $V$ la grandezza definita da $V(r) = - \int_\infty^r \vec{E} \cdot d\vec{s}$ dato dal fatto che con $r \to \infty$ il campo elettrostatico e la forza a cui è soggetta una carica sono pressochè nulle.

Consideriamo ora però il caso del campo generato da una carica puntiforme.\
Vale $dW = q_0\vec{E} \cdot d\vec{s} = \frac{q_0q}{4\pi\epsilon_0}\frac{\vec{u_r} \cdot d\vec{s}}{r^2} = \frac{q_0q}{4\pi\epsilon_0}\frac{dr}{r^2} \implies \int dW = \int_{r_1}^{r_2} \frac{q_0q}{4\pi\epsilon_0}\frac{dr}{r^2} = \frac{q_0q}{4\pi\epsilon_0}(\frac{1}{r_1} - \frac{1}{r_2}) = q_0\frac{q}{4\pi\epsilon_0}[-(\frac{1}{r_2} - \frac{1}{r_1})] = -q_0 \Delta V = \Delta U_e$ con $\Delta V$ la differenza di __potenziale__ tra i due punti e $\Delta U_e$ la differenza di __energia potenziale elettrostatica__ (entrambi definiti a meno di una costante additiva).

Come ci accorgiamo il lavoro non dipende dal percorso scelto ma dal campo elettrostatico nel punto iniziale e finale, di fatto se consideriamo $V(A) - V(A) = 0$. Questo ci suggerisce che il campo elettrostatico è conservativo. I risultati si possono infatti estendere ad un sistema discreto di cariche grazie al principio di sovrapposizione e ad un sistema continuo sempre per il principio di linearità degli integrali.
___

#### Dipolo elettrico
pag. 46

Chiamiamo dipolo un sistema di cariche costituito da due cariche di uguale modulo e segno opposto poste a distanza $d$ l'una dall'altra. \
Vale che il __momento del dipolo__ elettrico $\vec{p} = qd\vec{u_d}$ con $\vec{u_d}$ la direzione che congiunge le due cariche da quella negativa a quella positiva. 

Il potenziale elettrostatico del dipolo si usa sfruttando il principio di sovrapposizione: \
$V(P) = \frac{q}{4\pi\epsilon_0}( \frac{1}{r_1} - \frac{1}{r_2}) = \frac{q}{4\pi\epsilon_0} \frac{r_2 - r_1}{r_1 r_2}$ con $r_1$ e $r_2$ le distanze delle due cariche dal punto $P$.\
Quando la distanza $r$, tra il punto $P$ e il centro del dipolo, è $r >> d$ allora $r_2 - r_1 \approx d\cos\theta$ e $r_1r_2 \approx r^2$ quindi $V(P) = \frac{q}{4\pi\epsilon_0} \frac{r_2 - r_1}{r_1 r_2} \approx \frac{qd\cos\theta}{4\pi\epsilon_0 r^2} = \frac{\vec{p} \cdot \vec{u_r}}{4\pi\epsilon_0 r^2}$

Per quanto riguarda il campo elettrostatico invece dobbiamo scomporlo in due componenti:\
$E_r(P) = - \frac{\delta V}{\delta r} = \frac{2 ||p|| \cos\theta}{4\pi\epsilon_0 r^3}$,\
$E_\theta(P) = - \frac{1}{r} \frac{\delta V}{\delta \theta} = \frac{||p|| \sin\theta}{4\pi\epsilon_0 r^3}$\
$\implies \vec{E}(P) = E_r(P) \vec{u_r} + E_\theta(P) \vec{u_\theta} = \frac{||p||}{4\pi\epsilon_0 r^3} (2\cos\theta \vec{u_r} + \sin\theta \vec{u_\theta})$

Consideriamo ora un dipolo inmmerso in un campo uniforme $\vec{E}$. Sulle due cariche agiscono due forze uguali e opposte $\vec{F_1} = q\vec{E}$ e $\vec{F_2} = -q\vec{E} = -\vec{F_1}$. Calcoliamo il __momento torcente__ delle due forze rispetto al centro del dipolo: \
$\vec{M} = \vec{r_1} \times \vec{F_1} + \vec{r_2} \times \vec{F_2} = (\vec{r_2}-\vec{r_1}) \times \vec{F_1} = qd\vec{u_d} \times \vec{E} = \vec{p} \times \vec{E}$\
Tale momento tende a far ruotare $\vec{p}$ in modo che si allinei con $\vec{E}$ fino a raggiungere una posizione di equilibrio.

Quando il campo $\vec{E}$ non è uniforme, oltre ad un momento torcente, agisce anche una forza $\vec{F}$ in quanto le due cariche sono soggette a intensità di campo diverse. Consideriamo un caso semplice in cui $\vec{E}$ parallelo al dipolo e crescente al crescere di $x$. Le due cariche sono soggetti a campi diversi $E_1$ e $E_2$ con $E_2 \approx E_1 + \frac{\delta E}{\delta x} d$ (in particolare per d piccolo).\
La forza complessiva sul dipolo sarà $F = qE_2 - qE_1 = q \frac{\delta E}{\delta x} d = p\frac{\delta E}{\delta x}$.\
Si vede quindi, che il dipolo si muove dove il campo elettrico è più intenso se $p$ è positivo e viceversa.
___

#### Legge/Teorema di Gauss
pag. 56

Il flusso di un qualsiasi campo vettoriale è definito come $\Phi(\vec{F}) = \int_\Sigma \vec{F} \cdot \vec{u_n} d\Sigma$ con $\Sigma$ una superficie qualsiasi e $\vec{u_n}$ il versore normale alla superficie (con superficie chiusa è convenzione orientare la normale verso l'esterno). 

Se vale che òa forza tra due cariche è inversamente proporzionale al quadrato della distanza allora vale la legge di Gauss: \
> il flusso del campo elettrostatico $\vec{E}$ prodotto da un sistema di cariche attraverso una superficie chiusa è uguale alla somma algebrica delle cariche interne alla superficie, diviso $\epsilon_0$.

$\Phi(\vec{E}) = \int_\Sigma \vec{E} \cdot \vec{u_n} d\Sigma = \frac{Q_{int}}{\epsilon_0}$

La legge non dipende da come sono distribuite le cariche all'interno della superficie, fintanto che siano all'interno, questo vuol dire che la legge vale anche per un sistema di cariche continue.

Dimostrazione:
$d\Phi(\vec{E}) = \frac{q}{4\pi\epsilon_0} \frac{\vec{u_r} \cdot \vec{u_n}}{r^2} d\Sigma = \frac{q}{4\pi\epsilon_0} \frac{d\Sigma \cos\theta}{r^2}$, con $d\Sigma \cos\theta$ l'area proiettata della superficie infinitesima $d\Sigma$ sulla superficie sferica di raggio $r$ centrata sulla carica $q$.\
Indichiamo con $d\Omega$ l'angolo solido infinitesimo sotteso da $d\Sigma$ ovvero $d\Sigma \cos\theta/r^2$.\
$\Phi(\vec{E}) = \int_\Sigma \vec{E} \cdot \vec{u_n} d\Sigma = \frac{q}{4\pi\epsilon_0} \int_\Sigma d\Omega = \frac{q}{4\pi\epsilon_0} \Omega$.

Distinguiamo due casi:
- quando la carica è completamente interna alla superficie 
- quando la carica è completamente esterna alla superficie

Nel primo caso $\Omega = 4\pi$ e quindi $\Phi(\vec{E}) = \frac{q}{4\pi\epsilon_0} 4\pi = \frac{q}{\epsilon_0}$\
Nel secondo caso l'angolo solido definisce due superfici con normale opposta e quindi il flusso risultante è nullo.\
Per il principio di sovrapposizione l'enunciato può essere esteso a un sistema discreto di cariche e a un sistema continuo di cariche.

Esiste una forma differenziale della legge di Gauss detta __teorema della divergenza__ o __legge locale di Gauss__: \
$\Phi(\vec{E}) = \oint_\Sigma \vec{E} \cdot \vec{u_n} d\Sigma = \int_\tau \nabla \cdot \vec{E} d\tau = \frac{1}{\epsilon_0}\int_\tau \rho d\tau$\
$\implies \nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$.

$\nabla \cdot \vec{E} = \frac{\delta E_x}{\delta x} + \frac{\delta E_y}{\delta y} + \frac{\delta E_z}{\delta z}$\
poichè vale $E = \nabla V$ allora $\nabla \cdot \vec{E} = \nabla \cdot \nabla V = \nabla^2 V = \frac{\delta^2 V}{\delta^2 x} + \frac{\delta^2 V}{\delta^2 y} + \frac{\delta^2 V}{\delta^2 z} = - \frac{\rho}{\epsilon_0}$\
Questa formulazione è detta __equazione di Poisson__.
___

#### Proprietà di un Conduttore in elettrostatica
pag. 1, 70

I conduttori hanno proprietà fisiche tali che buona parte delle cariche all'interno sono __libere di muoversi__ (più approssimativamente definiamo conduttori i materiali che non trattengono le cariche scambiate per strofinio). Generalmente ci si concentra sui conduttori solidi quali i metalli. 

Data un'opportuna applicazione di un campo elettrostatico è possibile far muovere ordinatamente le cariche libere all'interno del conduttore, generando una __corrente elettrica__. In elettrostatica siamo interessati a studiare il comportamento di cariche, appunto, 'statiche' pertanto il campo elettrico all'interno di un conduttore è nullo (parliamo in questi casi di __equilibrio elettrostatico__). Se fosse presente un campo all'interno non nullo, avendo appunto la proprietà che le cariche libere sono libere di muoversi all'interno del conduttore, queste sarebbero soggette ad una forza elettrica e si muoverebbero, contraddicendo l'ipotesi di elettrostaticità.

Questo è vero a livello macroscopico, a livello microscopico le cariche sono in continuo movimento e i nuclei degli atomi esercitano/generano un campo elettrostatico non nullo. 

L'assenza di un campo elettrico interno implica tre altre altre proprietà dei conduttori:
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

