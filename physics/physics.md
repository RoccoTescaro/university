# Fisica II

UNIVERSITA’ DEGLI STUDI DI FIRENZE \
Facolta di Ingegneria \
Corso di Laurea in Ingegneria Informatica \
[[B024251] Fisica II](https://e-l.unifi.it/course/view.php?id=31849)
___

#### Indice

- [Lavoro e Potenziale elettrostatico (conservatività del campo elettrostatico)](#lavoro-e-potenziale-elettrostatico-conservatività-del-campo-elettrostatico)
- [Rotore del campo elettrostatico](#rotore-del-campo-elettrostatico)
- [Dipolo elettrico](#dipolo-elettrico)
- [Legge/Teorema di Gauss](#leggeteorema-di-gauss)
- [Proprietà di un Conduttore in elettrostatica](#proprietà-di-un-conduttore-in-elettrostatica)
- [Condensatore](#condensatore)
- [Corrente elettrica e legge di Ohm](#corrente-elettrica-e-legge-di-ohm)
- [Forza di Lorentz e effetto Hall](#forza-di-lorentz-e-effetto-hall)
- [Moto di una particella in un campo magnetico uniforme](#moto-di-una-particella-in-un-campo-magnetico-uniforme)
- [Legge di Ampere](#legge-di-ampere)
- [Legge di Faraday](#legge-di-faraday)
- [Generatore di corrente (continua e alternata)](#generatore-di-corrente-continua-e-alternata)
- [Autoinduzione](#autoinduzione)
- [Energia magnetica](#energia-magnetica)
- [Legge di Ampere-Maxwell](#legge-di-ampere-maxwell)
- [Equazioni di Maxwell](#equazioni-di-maxwell)
___

#### Lavoro e Potenziale elettrostatico (conservatività del campo elettrostatico)
pag. 27

Il lavoro delle forze elettrostatiche è dato da $dW = \vec{F} \cdot d\vec{s} = q_0\vec{E} \cdot d\vec{s} = q_0 E \cos(\theta) d\vec{s}$ con $E \cos(\theta)$ la proiezione di $\vec{E}$ su $d\vec{s}$. 

Lavoro totale $W = \int dW = \int_\gamma q_0 \vec{E} d\vec{s} = q_0 \int_\gamma \vec{E} d\vec{s}$. Per un percorso chiuso $W = \oint \vec{F} d\vec{s} = \int_{\gamma_1} \vec{F} d\vec{s} + \int_{-\gamma_2} \vec{F} d\vec{s} = \int_{\gamma_1} \vec{F} d\vec{s} - \int_{\gamma_2} \vec{F} d\vec{s} = W_1 - W_2 = q_0 \oint \vec{E} \cdot d\vec{s} = q_0 ℰ$ misurato in ___joule___ $[J]$ con ℰ detta forza elettromotrice misurata in ___volt___ $[V]$.

In generale la f.e.m. è diversa da 0 e il campo elettrico non conservativo.  

Chiamiamo __differenza di potenziale elettrostatico__ $\Delta V$ la grandezza definita da $\Delta V = V(B) - V(A) = -\int_A^B \vec{E} \cdot d\vec{s}$ (misurata anch'essa in volt).\
Chiamiamo __potenziale eletrico__ $V$ la grandezza definita da $V(r) = - \int_\infty^r \vec{E} \cdot d\vec{s}$ dato dal fatto che con $r \to \infty$ il campo elettrostatico e la forza a cui è soggetta una carica sono pressochè nulle.

Consideriamo ora però il caso del campo generato da una carica puntiforme.\
Vale $dW = q_0\vec{E} \cdot d\vec{s} = \frac{q_0q}{4\pi\epsilon_0}\frac{\vec{u_r} \cdot d\vec{s}}{r^2} = \frac{q_0q}{4\pi\epsilon_0}\frac{dr}{r^2} \implies \int dW = \int_{r_1}^{r_2} \frac{q_0q}{4\pi\epsilon_0}\frac{dr}{r^2} = \frac{q_0q}{4\pi\epsilon_0}(\frac{1}{r_1} - \frac{1}{r_2}) = q_0\frac{q}{4\pi\epsilon_0}[-(\frac{1}{r_2} - \frac{1}{r_1})] = -q_0 \Delta V = \Delta U_e$ con $\Delta V$ la differenza di __potenziale__ tra i due punti e $\Delta U_e$ la differenza di __energia potenziale elettrostatica__ (entrambi definiti a meno di una costante additiva).

Come ci accorgiamo il lavoro non dipende dal percorso scelto ma dal campo elettrostatico nel punto iniziale e finale, di fatto se consideriamo $V(A) - V(A) = 0$. Questo ci suggerisce che il campo elettrostatico è conservativo. I risultati si possono infatti estendere ad un sistema discreto di cariche grazie al principio di sovrapposizione e ad un sistema continuo sempre per il principio di linearità degli integrali.
___

#### Rotore del campo elettrostatico
pag. 45

Grazie al teorema di Strokes vale che la circuitazione di un campo vettoriale (come ad esempio $\vec{E}$) lungo un circuito $\gamma$, è uguale al flusso del rotore del campo attraverso una qualsiasi superficie $\Sigma$ che abbia come bordo il circuito $\gamma$:\
$\oint_\gamma \vec{E} \cdot d\vec{s} = \int_\Sigma \nabla \times \vec{E} \cdot \vec{u_n} d\Sigma$.

Per campi elttrostatici vale che $\nabla \times \vec{E} = 0$ (dato che $\vec{E}$ è conservativo) e si dice che il campo elettrostatico è __irrotazionale__.
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

Consideriamo ora un dipolo inmmerso in un campo uniforme $\vec{E}$. Sulle due cariche agiscono due forze uguali e opposte $\vec{F_1} = q\vec{E}$ e $\vec{F_2} = -q\vec{E} = -\vec{F_1}$. Calcoliamo il __momento torcente__ delle due forze: \
$\vec{M} = \vec{r_1} \times \vec{F_1} + \vec{r_2} \times \vec{F_2} = (\vec{r_2}-\vec{r_1}) \times \vec{F_1} = qd\vec{u_d} \times \vec{E} = \vec{p} \times \vec{E}$\
Tale momento tende a far ruotare $\vec{p}$ in modo che si allinei con $\vec{E}$ fino a raggiungere una posizione di equilibrio.

Quando il campo $\vec{E}$ non è uniforme, oltre ad un momento torcente, agisce anche una forza $\vec{F}$ in quanto le due cariche sono soggette a intensità di campo diverse. Consideriamo un caso semplice in cui $\vec{E}$ parallelo al dipolo e crescente al crescere di $x$. Le due cariche sono soggetti a campi diversi $E_1$ e $E_2$ con $E_2 \approx E_1 + \frac{\delta E}{\delta x} d$ (in particolare per d piccolo).\
La forza complessiva sul dipolo sarà $F = qE_2 - qE_1 = q \frac{\delta E}{\delta x} d = p\frac{\delta E}{\delta x}$.\
Si vede quindi, che il dipolo si muove dove il campo elettrico è più intenso se $p$ è positivo e viceversa.
___

#### Legge/Teorema di Gauss
pag. 56, 190

Il flusso di un qualsiasi campo vettoriale è definito come $\Phi(\vec{F}) = \int_\Sigma \vec{F} \cdot \vec{u_n} d\Sigma$ con $\Sigma$ una superficie qualsiasi e $\vec{u_n}$ il versore normale alla superficie (con superficie chiusa è convenzione orientare la normale verso l'esterno). 

Se vale che òa forza tra due cariche è inversamente proporzionale al quadrato della distanza allora vale la legge di Gauss:
> il flusso del campo elettrostatico $\vec{E}$ prodotto da un sistema di cariche attraverso una superficie chiusa è uguale alla somma algebrica delle cariche interne alla superficie, diviso $\epsilon_0$.

$\Phi(\vec{E}) = \int_\Sigma \vec{E} \cdot \vec{u_n} d\Sigma = \frac{Q_{int}}{\epsilon_0}$

La legge non dipende da come sono distribuite le cariche all'interno della superficie, fintanto che siano all'interno, questo vuol dire che la legge vale anche per un sistema di cariche continue.

Dimostrazione:\
$d\Phi(\vec{E}) = \frac{q}{4\pi\epsilon_0} \frac{\vec{u_r} \cdot \vec{u_n}}{r^2} d\Sigma = \frac{q}{4\pi\epsilon_0} \frac{d\Sigma \cos\theta}{r^2}$, con $d\Sigma \cos\theta$ l'area proiettata della superficie infinitesima $d\Sigma$ sulla superficie sferica di raggio $r$ centrata sulla carica $q$.\
Indichiamo con $d\Omega$ l'angolo solido infinitesimo sotteso da $d\Sigma$ ovvero $d\Sigma \cos\theta/r^2$.\
$\Phi(\vec{E}) = \int_\Sigma \vec{E} \cdot \vec{u_n} d\Sigma = \frac{q}{4\pi\epsilon_0} \int_\Sigma d\Omega = \frac{q}{4\pi\epsilon_0} \Omega$.

Distinguiamo due casi:
- quando la carica è completamente interna alla superficie 
- quando la carica è completamente esterna alla superficie

Nel primo caso $\Omega = 4\pi$ e quindi $\Phi(\vec{E}) = \frac{q}{4\pi\epsilon_0} 4\pi = \frac{q}{\epsilon_0}$\
Nel secondo caso l'angolo solido definisce due superfici con normale opposta e quindi il flusso entrante (quando l'angolo tra $vec{E}$ e $\vec{u_n}$ è maggiore di 90°) e il flusso uscente (angolo minore di 90°) sono uguali, pertanto il flusso risultante è nullo.\
Per il principio di sovrapposizione l'enunciato può essere esteso a un sistema discreto di cariche e a un sistema continuo di cariche.

Esiste una forma differenziale della legge di Gauss detta __teorema della divergenza__ o __legge locale di Gauss__: \
$\Phi(\vec{E}) = \oint_\Sigma \vec{E} \cdot \vec{u_n} d\Sigma = \int_\tau \nabla \cdot \vec{E} d\tau = \frac{1}{\epsilon_0}\int_\tau \rho d\tau$\
$\implies \nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$.

$\nabla \cdot \vec{E} = \frac{\delta E_x}{\delta x} + \frac{\delta E_y}{\delta y} + \frac{\delta E_z}{\delta z}$\
poichè vale $E = - \nabla V$ allora $- \nabla \cdot \vec{E} = \nabla \cdot \nabla V = \nabla^2 V = \frac{\delta^2 V}{\delta^2 x} + \frac{\delta^2 V}{\delta^2 y} + \frac{\delta^2 V}{\delta^2 z} = - \frac{\rho}{\epsilon_0}$\
Questa formulazione che mette in relazione potenziale e densità di carica è detta __equazione di Poisson__.

La nozione di flusso è applicabile anche al campo magnetico, in questo caso però data la proprietà del campo magnetico, che le linee di campo sono chiuse, ogni linea di campo che entra in una superficie deve uscirne e quindi il flusso è sempre nullo. Si parla in questo caso di __legge di Gauss per il campo magnetico__.\
$\oint \vec{B} \cdot \vec{u_n} d\Sigma = \nabla \cdot \vec{B} = 0$
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

Nel caso di un conduttore sferico di raggio $R_1$ al centro di un conduttore sferico cavo di raggio interno $R_2$ ($R_2 > R_1$) e raggio esterno $R_3$, se $Q$ è la carica disposta sulla superficie del conduttore interno, $-Q$ è la carica disposta sulla superficie interna del conduttore esterno e $Q$ quella sulla superficie esterna.

$E(r) = \begin{cases} \frac{Q}{4\pi\epsilon_0 r^2} & r \geq R_3 \\ 0 & R_2 \leq r \leq R_3 \\ \frac{Q}{4\pi\epsilon_0 R_3^3} \frac{R_2^3}{r^2} & R_1 \leq r \leq R_2 \\ 0 & r \leq R_1 \end{cases}, \space\space\space \Delta V = \frac{Q}{4\pi\epsilon_0}(\frac{1}{R_1}-\frac{1}{R_2}), \space\space\space C = \frac{4\pi\epsilon_0R_1R_2}{R_2 - R_1}$

Nel caso due conduttori siano posti in parallelo in modo tale che le loro armature compongano due conduttori collegati allora la capacità del sistema è la somma delle capacità dei due conduttori. 

Nel caso di condensatori in serie la carica è la stessa per entrambi i condensatori e la capacità del sistema è data da $C = \frac{C_1 C_2}{C_1 + C_2}$ ovvero il reciproco della somma dei reciproci delle capacità dei due condensatori.

Il processo di carica di un condensatore consiste in una separazione di cariche e richiede un determinato lavoro che, essendo il campo elettrostatico conservativo, dipende solo dallo stato iniziale e finale. Questa separazione può essere considerata come un trasferimento della carica dall'armatura negativa su quella positiva.

Quindi $dW = V' \cdot dq' = \frac{q'}{C}dq'$ con $V'$ la differenza di potenziale tra le due armature in una fase intermedia del processo e $q'$ la carica $CV'$ trasferita.

$W = \int dW = \int_0^Q \frac{q'}{C}dq' = \frac{Q^2}{2C}$. Questo lavoro viene immagazzinato nel sistema sotto forma di energia potenziale elettrostatica.

$U_e = \frac{Q^2}{2C} = \frac{CV^2}{2} = \frac{QV}{2}$

In un condensatore piano il campo elettrostatico uniforme $V = E*h$, $C = \frac{\epsilon_0 \Sigma}{h}$ e $U_e = \frac{1}{2} \epsilon_0 E^2 \Sigma h = \frac{1}{2} \epsilon_0 E^2 \tau$.

Si definisce la __densità di energia elettrostatica__ come $u_e = \frac{U_e}{\tau} = \frac{1}{2} \epsilon_0 E^2$. Il fatto che la formula della densità di energia elettrostatica non contenga misure relative al condensatore ci suggerisce la sua generalità. E' dimostrabile che $dU_e = u_e \cdot d\tau = \frac{1}{2} \epsilon_0 E^2 \cdot d\tau \implies U_e = \int_\tau \frac{1}{2} \epsilon_0 E^2 \cdot d\tau$.
___

#### Corrente elettrica e legge di Ohm
pag. 107, 110

Supponiamo che in una certa regione di un conduttore ci siano $n$ cariche elementari $e$ per unità di volume e che sia presente un campo elettrico $\vec{E}$. Queste cariche sono allora soggette ad una forza elettrica $\vec{F} = e\vec{E}$ e si muovono con velocità $\vec{v}$ detta __velocità di deriva__. \
Data una superficie $\Sigma$ definiamo l'__intensità di corrente media__ come $i = \frac{\Delta q}{\Delta t}$ con $\Delta q$ la carica che attraversa la superficie $\Sigma$ in un intervallo di tempo $\Delta t$.\
Chiamiamo __intensità di corrente istantanea__ $i = \lim_{\Delta t \to 0} \frac{\Delta q}{\Delta t} = \frac{dq}{dt}$.

Vogliamo mettere in relazione l'intensità di corrente e la velocità di deriva. Prendiamo quindi in considerazione la superficie infinitesima $d\Sigma$ la cui normale forma un angolo $\theta$ con il campo elettrico ( e quindi con la velocità di deriva).\
Le cariche percorrono una distanza $d\vec{s} = \vec{v}dt$ in un tempo $dt$ e quindi la carica complessiva che attraversa la superficie infinitesima è quella contenuta nel volume infinitesimo $d\tau = vdt d\Sigma \cos\theta \implies dq = n e d\tau = n e vdt d\Sigma \cos\theta \implies di = n e v d\Sigma \cos\theta$.

Chiamiamo __densita di corrente__ $\vec{j} = n e \vec{v}$ e quindi $di = \vec{j} \cdot \vec{u_n} d\Sigma \implies i = \int_\Sigma \vec{j} \cdot \vec{u_n} d\Sigma$.

Da notare come per cariche negative sia la carica che la velocità di deriva siano negative e quindi la densità di corrente sia positiva (convenzionalmente come verso della corrente si considera quello di cariche positive ovvero da punti con potenziale maggiore a punti con potenziale minore).

Dato un conduttore il cui volume è delimitato da due superfici $\Sigma_1$ e $\Sigma_2$, se si suppone che all'interno del conduttore non vari la carica, allora la corrente che scorre attraverso la superficie $\Sigma_1$ è uguale a quella che scorre attraverso la superficie $\Sigma_2$. Questa condizione è detta di __stazionarietà__ si parla quindi di __corrente stazionaria__: in condizioni stazionarie l'intensità di corrente è costante attraverso ogni sezione del conduttore.

In un conduttore in cui scorre corrente stazionaria si verifica che la densità di corrente è proporzionale al campo elettrico e la costante di proporzionalità è detta __conduttività elettrica__ $\sigma$. Questa relazione di proporzionalità è detta __legge di Ohm__ ed è porvata sperimentalmente $\vec{j} = \sigma \vec{E}$. \
La legge di Ohm è spesso scritta nella forma $\vec{E} = \rho \vec{j}$ con $\rho$ detta __resistività elettrica__ e $\rho = \frac{1}{\sigma}$.

Prendiamo in considerazione un conduttore metallico generico, tra campo elettrico e differenza di potenziale vale $\Delta V = \int_A^B \vec{E} \cdot d\vec{s} = \int_A^B \rho \vec{j} \cdot d\vec{s} = \int_A^B \rho \frac{i}{d\Sigma} \vec{u_n} \cdot d\vec{s} = i \int_A^B \rho \frac{d\vec{s}}{d\Sigma} \cdot \vec{u_n}$.\
Quando il conduttore ha forma cilindrica ad esempio vale $\Delta V = i \rho \frac{l}{\Sigma}$ con $l$ la lunghezza del conduttore e $\Sigma$ la sua sezione.\
Chiamiamo __resistenza elettrica__ $R = \int_A^B \rho \frac{d\vec{s}}{d\Sigma} \cdot \vec{u_n} \implies \Delta V = Ri$ detta legge di Ohm per i conduttori metallici. 
___

#### Forza di Lorentz e effetto Hall
pag. 145, 153

Consideriamo una particella di massa $m$ e carica $q$ immersa in un campo magnetico $\vec{B}$. Se la carica è ferma rispetto alla sorgente del campo magnetico, allora non è soggetta a nessuna forza. Se invece la carica si muove allora è soggetta ad una forza detta __forza di Lorentz per il campo magnetico__ (a volte abbreviata semplicemente con forza di Lorentz) $\vec{F} = q\vec{v} \times \vec{B}$.

Lungo uno spostamento l'energia cinetica della particella non varia poichè la forza di Lorentz non compie lavoro sulla stessa. Quando una particella casica si muove in un campo magnetico, la sua velocità cambia di direzione ma non di modulo.

Quando è presente anche un campo elettrico oltre a quello magnetico, la __forza di Lorentz__ indica la forza complessiva che agisce sulla particella e dipende quindi da entrambi i campi: $\vec{F} = q_0(\vec{E} + \vec{v}\times\vec{B})$ (non vale più il discorso sul lavoro e sull'energia cinetica).

Consideriamo ora una lamina rettangolare di spessore $h$ e larghezza $l$ immersa in un campo magnetico $\vec{B}$ uniforme e costante. Sulla lamina agisce una forza di Lorentz $\vec{F} = q\vec{v} \times \vec{B}$ che tende a spostare le cariche verso un lato della lamina. Questo spostamento di cariche genera un campo elettrico $\vec{E}$ che tende a contrastare la forza di Lorentz.

$\vec{j} = \frac{i}{hl}\vec{u_l} = n e \vec{v}$ con $n$ il numero di cariche libere per unità di volume e $e$ la carica elementare.\ 
$\vec{F} = e\vec{v}\times\vec{B} \implies \vec{E_H} = \frac{\vec{F}}{e} = \vec{v} \times \vec{B} = \frac{\vec{j}}{ne} \times \vec{B}$

Si parla in questi casi di __campo elettromotore__ (ovvero campo elettrico di origine magnetica). $E_H$ non è conservativo.

Grazie alle formule di Hall è possibile costruire un sonda detta __sonda di Hall__. Lo spostamento di cariche a causa del campo elttromotore genera una differenza di potenziale tra i due lati della lamina. Misurando questa differenza di potenziale è possibile misurare l'intensità del campo magnetico:\
$ℰ_H = \int_0^h \vec{E_H} \cdot d\vec{z} = \vec{E_H} \cdot h\vec{u_z} = E_H h = \frac{j B h}{n e} = \frac{i B}{n e l}$

Ora misurando $ℰ_H$ per un campo $B$ noto è possibile stabilire una costante di proporzionalità che ci permette di calcolare campo magnetico qualsiasi.
___

#### Leggi di Laplace e di J.B.Biot-F.Savart

La seconda legge di Laplace si verifica sperimentalmente e afferma che la forza esercitata da un campo magnetico su una spira in cui scorre corrente è:\
$\vec{F} = \int_\gamma i d\vec{s} \times \vec{B}$ con $\gamma$ il percorso della spira e $i$ l'intensità di corrente che scorre nella spira.

La prima legge di Laplace afferma invece che:\
$d\vec{B} = \frac{\mu_0}{4\pi} \frac{i d\vec{s} \times \vec{u_r}}{r^2}$ con $r$ la distanza tra il punto in cui si calcola il campo e il punto in cui scorre la corrente.

Sia $R$ la distanza minima (perpendicolare alla spira lineare) tra il punto in cui si calcola il campo e il punto in cui scorre la corrente, allora $r = \frac{R}{\sin \theta}$ (con $\theta$ l'angolo compreso fra $d\vec{s}$ e $\vec{u_r}$) e $d\vec{s} = \frac{Rd\theta}{\sin^2\theta}$ allora per la prima legge di Laplace vale:\
$d\vec{B} = \frac{\mu_0}{4\pi} \frac{i \frac{Rd\theta}{\sin^2\theta} \sin\theta}{\frac{R^2}{\sin^2\theta}} \vec{u_\phi} = \frac{\mu_0}{4\pi} \frac{i \sin \theta d\theta}{R} \vec{u_\phi}$ con $\vec{u_\phi}$ il versore tangente alla circonferenza di raggio $R$ centrata nel punto in cui scorre la corrente e contenente il punto in cui si calcola il campo.

$\frac{B} = \int_0^\infty \frac{\mu_0}{4\pi} \frac{i \sin \theta d\theta}{R} \vec{u_\phi} = \frac{\mu_0 i}{2 \pi} \frac{1}{R} \vec{u_\phi}$  detta __legge di Biot-Savart__.
___

#### Moto di una particella in un campo magnetico uniforme
pag. 156

Data una carica che si muove con velocità $\vec{v}$ in un campo magnetico $\vec{B}$ formando un angolo $\theta$ qualsiasi, possiamo scomporre $\vec{v}$ in due componenti: \
$\vec{v_\parallel} = ||\vec{v}||\cos\theta$ parallela a $\vec{B}$ e $\vec{v_\perp} = ||\vec{v}||\sin\theta$ perpendicolare a $\vec{B}$. \
La forza di Lorentz che agisce sulla particella $\vec{F} = q\vec{v}\times\vec{B} = q(\vec{v_\parallel} + \vec{v_\perp})\times\vec{B} = q\vec{v_\perp}\times\vec{B}$

Abbiamo quindi per un piano ortogonale a $\vec{B}$ un moto circolare uniforme con velocità $\vec{v_\perp}$ e raggio $r = \frac{mv_\perp}{qB} = \frac{mv\sin\theta}{qB}$.\
Per un piano parallelo a $\vec{B}$ invece abbiamo un moto rettilineo uniforme con velocità $\vec{v_\parallel}$.\
Questo tipo di moto è detto __moto elicoidale uniforme__.

La particella si sposta di una distanza $p = v_\parallel T = \frac{2\pi m v \cos\theta}{qB}$ detta __passo dell'elica__.

Queste tipi di conoscenze sono utili per la costruzione di __spettrometri di massa__, strumenti che permettono di determinare la massa di una particella carica (quindi ad esempio separare isotopi di uno stesso elemento).
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

La legge di Faraday può essere scritta anche nella forma differenziale: \
$\oint E_i \cdot ds = \int_\Sigma (\nabla \times E_i) \cdot u_n d\Sigma = - \frac{d \Phi(B)}{dt} \implies \nabla \times E_i = - \frac{d B}{dt}$\
detta appunto __forma locale__ della legge di Faraday.
___

#### Generatore di corrente (continua e alternata)
pag. 209

Consideriamo un circuito elettrico in cui è presente una resistenza esterna $R$, $r$ la resistenza della sbarretta mobile, immerso in un campo magnetico $B$ perpendicolare al piano della sbarretta e uniforme in tutto il circuito. Siccome manteniamo con velocità $\vec{v}$ costante della sbarretta, nel circuito compare la forza elettromotrice $ℰ_i = -vBl$ ($l$ lunghezza della sbarretta) e circola una corrente $i = \frac{ℰ_i}{R+r} = \frac{vBl}{R+r}$. Quindi sulla sbarretta agisce la forza di Lorentz $F = il \times B = - \frac{B^2 l^2}{R+r}\vec{v}$ che rallenta la sbarretta. Questa forza è detta __resistenza di attrito elettromagnetico__.

Per mantenere la velocità costante della sbarretta è necessario applicare una forza di eguale modulo e direzione opposta spendendo una potenza $P = F \cdot v = \frac{B^2 l^2}{R+r} v^2 = ℰ_i i$. Il sistema può essere considerato come un __generatore__ in cui la potenza erogata $P = ℰ_i i$ proviene da un'azione meccanica esterna.

Possiamo invece costruire un generatore di corrente alternata considerando una spira rettangolare immersa in un campo magnetico uniforme e costante che ruota con velocità costante $\omega$ attorno ad un asse perpendicolare al piano della spira. \
$\Phi(B) = \int_\Sigma B \cdot u_n d\Sigma = B\Sigma \cos\theta = B\Sigma\cos(\omega t) \implies ℰ_i = - \frac{d \Phi(B)}{dt} = B\Sigma\omega\sin(\omega t)$\
Dunque la corrente indotta è $i = \frac{ℰ_i}{R} = \frac{B\Sigma\omega\sin(\omega t)}{R}$ che ha andamento sinusoidale.\
Mentre per la potenza erogata vale $P = ℰ_i i = \frac{B^2\Sigma^2\omega^2\sin^2(\omega t)}{R}$, con media $\bar{P} = \frac{B^2\Sigma^2\omega^2}{2R}$, la stessa che si otterrebbe con un generatore di corrente continua e $ℰ_{eff} = \frac{B^2\Sigma^2\omega^2}{\sqrt{2}}$.
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

#### Legge di Ampere-Maxwell
pag. 221

Abbiamo già trattato la condizione di stazionarietà della corrente. Consideriamo ora un circuito in cui il generatore sta caricando un condensatore piano. Fissato il circuito $\gamma$ intorno ad un lato della spira, che definisce una superficie $\Sigma_1$ data da una sezione perpendicolare al lato della spira definita dal circuito, e $\Sigma_2$ che passa fra le due armature del condensatore. La corrente che passa attraverso $\Sigma_1$ è $i(t)$ mentre quella che passa attraverso $\Sigma_2$ è 0 (non c'è corrente nella parte di circuito aperto).\
In questo caso viene meno la condizione di stazionarietà.

La carica che si accumula su una superficie del condensatore genera per induzione un accumulo di carica nella superficie opposta, portando a definire una corrente detta __corrente di spostamento__ legata alla variazione del campo elettrico $i_s = \epsilon_0\frac{d\Phi(\vec{E})}{dt}$.

Possiamo riscrivere quindi la legge di Ampere come $\oint \vec{B} \cdot d\vec{s} = \mu_0 (i_{conc} + \epsilon_0 \frac{d\Phi(\vec{E})}{dt})$. Questa è la __legge di Ampere-Maxwell__.

E' importante notare come questa forma della legge di Ampere pone in relazione il campo magnetico con la variazione del campo elettrico. Mentre per la legge di Faraday abbiamo una relazione simmetrica tra campo elettrico e variazione del campo magnetico.
___

#### Equazioni di Maxwell
pag. 223, 262

Ci è utile spesso in fisica modellare eventi fisici periodici come funzioni sinusoidali (___onde___). Queste onde possono propagarsi attraverso e per mezzo di materia (in questo caso si parla di onde meccaniche) o attraverso e per mezzo di campi (come ad esempio le onde elettromagnetiche). Per semplificare questi oggetti matematici si riducono le funzioni onda a due variabili, una spaziale e una temporale: $\vec{E}(x,t)$ e $\vec{B}(x,t)$. Si parla in questo caso di __onde piane__.

L'esistenza di onde piane fu prevista da Maxwell che riuscì a raggruppare le leggi di Gauss, Ampere e Faraday in quattro equazioni differenziali che descrivono il comportamento di un campo elettromagnetico. Queste equazioni sono dette __equazioni di Maxwell__ (in forma integrale):\
$\oint \vec{E} \cdot d\Sigma = \frac{Q_{int}}{\epsilon_0}$\
$\oint \vec{B} \cdot d\Sigma = 0$\
$\oint \vec{E} \cdot ds = - \frac{d \Phi(B)}{dt}$\
$\oint \vec{B} \cdot ds = \mu_0 i + \mu_0 \epsilon_0 \frac{d \Phi(E)}{dt}$

Le analoghe formule in forma locale sono:
- Per il teorema della divergenza possiamo riscrivere le prime due equazioni come:\
    $\qquad \nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0} \qquad\qquad\text{ , }\qquad\qquad \nabla \cdot \vec{B} = 0$\
    vedi [Legge/Teorema di Gauss](#leggeteorema-di-gauss)

- Per il teorema di Stokes possiamo riscrivere le ultime due equazioni come:\
    $\qquad \nabla \times \vec{E} = 0 \qquad\qquad\text{ , }\qquad\qquad \nabla \times \vec{B} = \mu_0 \vec{j}$\
    vedi [Rotore del campo ellttrostatico](#rotore-del-campo-elettrostatico) e [Legge di Ampere](#legge-di-ampere)\
    tuttavia queste valgono per casi particolari, estese dai campi variabili nel tempo con la [forma locale legge di Faraday](#legge-di-faraday) e con la [legge di Ampere-Maxwell](#legge-di-ampere-maxwell):\
    $\qquad \nabla \times \vec{E} = - \frac{d \vec{B}}{dt} \qquad\qquad\text{ , }\qquad\qquad \nabla \times \vec{B} = \mu_0 \vec{j} + \mu_0 \epsilon_0 \frac{d \vec{E}}{dt}$

L'ipotesi di onda piana vuol dire che si cerca una soluzione in cui i campi $\vec{E}$ e $\vec{B}$ non variano per le variabili $y$ e $z$ vale a dire che $\delta/\delta y$ e $\delta/\delta z$ sono nulle.\
Dalle equazioni di Maxwell in forma locale possiamo ricavare che:
$\nabla \cdot \vec{E} = 0 \implies \frac{\delta E_x}{\delta x} = 0$\
$\nabla \cdot \vec{B} = 0 \implies \frac{\delta B_x}{\delta x} = 0$\
$\nabla \times \vec{E} = - \frac{\delta \vec{B}}{\delta t} = - \frac{\delta B_x}{\delta t} \vec{u_x} - \frac{\delta B_y}{\delta t} \vec{u_y} - \frac{\delta B_z}{\delta t} \vec{u_z} = 0\vec{u_x} - \frac{\delta E_z}{\delta x}\vec{u_y} + \frac{\delta E_y}{\delta x}\vec{u_z}$\
$\nabla \times \vec{B} = \mu_0 \epsilon_0 \frac{\delta \vec{E}}{\delta t} = \mu_0 \epsilon_0 (\frac{\delta E_x}{\delta t} \vec{u_x} + \frac{\delta E_y}{\delta t} \vec{u_y} + \frac{\delta E_z}{\delta t} \vec{u_z}) = \mu_0 \epsilon_0 ( 0\vec{u_x} - \frac{1}{\mu_0 \epsilon_0} \frac{\delta B_z}{\delta x}\vec{u_y} + \frac{1}{\mu_0 \epsilon_0} \frac{\delta B_y}{\delta x}\vec{u_z})$

In queste relazioni possiamo vedere come sia $\vec{E}$ che $\vec{B}$ siano costanti rispetto a $x$ e $t$ (la loro derivata rispetto a $x$ e $t$ è nulla).\