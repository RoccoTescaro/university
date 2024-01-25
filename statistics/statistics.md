# Statisitica

UNIVERSITA’ DEGLI STUDI DI FIRENZE \
Facolta di Ingegneria \
Corso di Laurea in Ingegneria Informatica 
<!-- #TODO -->

___

### Statistica descrittiva 

- __indici di tendenza centrale__ :
   $x_1 , x_2 , ... , x_n$ | istanze di valori assunti da una variabile statistica (_in ordine crescente_) [dette unità statistiche ?] \
   $v_1 , v_2 , ... , v_m$ | valori assunti da una variabile statistica [dette modalità]\
    __frequenza assoluta__ : $f_1, f_2, ..., f_m$ | numero di volte che si ripete un istanza di valore$x$($f_j = \sum_{x_i = v_j} 1$ )

    __frequenza relativa__ : $f_{r_i} = f_i/n$ con $i = 1, 2, ..., m$| frequenza relativa percentuale = $f_i/n*100$ % \
    __frequenza cumulata__ : $\sum_{i=1}^{j} f_i$ | somma delle frequenze assolute o _relative_ di tutti i valori minori o uguali al valore considerato $j$

    __ampiezza classi__ : $\frac{v_{\text{max}} - v_{\text{min}}}{n_{\text{classi}}}$|$v_{\text{min}} = v_1$ e $v_{\text{max}} = v_m$ in quanto ordinati

    __media campionaria__ : $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$| oppure$\bar{x} = \frac{1}{n} \sum_{i=1}^{m} v_i * f_i = \sum_{i=1}^{m} fr_i$ \
    __media di popolazione__ : $\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$| con$N =$numero totale di unità statistiche

    __mediana__ : $\tilde{x} = \begin{cases} x_{\frac{n+1}{2}} & \text{se n è dispari} \\ \frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2} & \text{se n è pari} \end{cases}$

    __quartile__ : 
   $Q_1 = \begin{cases} x_{\frac{n+1}{4}} & \text{se n è dispari} \\ \frac{x_{\frac{n}{4}} + x_{\frac{n}{4}+1}}{2} & \text{se n è pari} \end{cases}$ \
   $Q_2 = \begin{cases} x_{\frac{n+1}{2}} & \text{se n è dispari} \\ \frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2} & \text{se n è pari} \end{cases} = \tilde{x}$ \
   $Q_3 = \begin{cases} x_{\frac{3(n+1)}{4}} & \text{se n è dispari} \\ \frac{x_{\frac{3n}{4}} + x_{\frac{3n}{4}+1}}{2} & \text{se n è pari} \end{cases}$

    __outliers__ :
   $a = \text{max}(x_{\text{min}}; Q_1 - 1.5*(Q_3 - Q_1))$|$x_{\text{min}} = x_1 = v_1$in quanto ordinati \
   $b = \text{min}(x_{\text{max}}; Q_3 + 1.5*(Q_3 - Q_1))$|$x_{\text{max}} = x_n = v_m$in quanto ordinati

- __indici di variabilità__ :
    __campo di variazione__ : $x_{\text{max}} - x_{\text{min}}$|$x_{\text{max}} = x_n = v_m$e$x_{\text{min}} = x_1 = v_1$in quanto ordinati \
    __varianza campionaria__ : $s^2 = \frac{1}{n-1} \sum_{i=1}^{n}(x_i-\bar{x})^2$ \
    __varianza di popolazione__ : $\sigma^2 = \frac{1}{N} \sum_{i=1}^{N}(x_i-\mu)^2 = \mu_2 - \mu^2$ \
    __momento__ : $\mu_k = \frac{1}{N} \sum_{i=1}^{N}x_i^k$ \
    __deviazione standard__ : $\sigma = \sqrt{\sigma^2}$( dvs campionaria$s = \sqrt{s^2}$) \
    __coefficiente di variazione__ : $cv = \sigma / \mu$|$cv = s / \bar{x}$ \
    __differenza interquartile__ : $dq = Q_3 - Q_1$ \
    __covarianza__ : $cov(x,y) = \frac{1}{n-1} \sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})$ \
    __indice di correlazione__ : $r = \frac{cov(x,y)}{\sigma_x \sigma_y}$ |$r \in [-1,1]$ \
   $r = 1$correlazione positiva perfetta, \
   $r = -1$correlazione negativa perfetta, \
   $r = 0$non correlati 
___

### Probabilità

__spazio campionario__ / __evento certo__ : $\Omega^k$| insieme di tutti i possibili esiti di un esperimento ($k =$numero di esperimenti )
__evento__ : $E \subseteq \Omega^k$
__evento impossibile__ : $\bar{\Omega} = \emptyset$

algebra degli eventi : operazioni insiemistiche, quindi valgono le operazioni di unione, intersezione e complemento, le leggi di De Morgan e le proprietà commutativa, associativa e distributiva

approccio a priori : $P(E) = \frac{\text{casi favorevoli}}{\text{casi possibili}}$
approccio empirico : $P(E) = \frac{1}{n} \sum_{i=1}^{n} \mathbb{1}_{[n]}(E_i)$con$\mathbb{1}_{[n]}(E_i) = \begin{cases} 0 & \text{se } E_i \neq n \\ 1 & \text{se } E_i = n \end{cases}$

__assiomi di Kolmogorov__ :
-$P(E) \in [0, 1]$per ogni evento$E$
-$P(\Omega) = 1$e$P(\emptyset) = 0$
-$P(\bigcup_{i=1}^{m} E_i) = \sum_{i=1}^{m} P(E_i)$se$E_i \cap E_j = \emptyset$per ogni$i \neq j$[eventi mutuamente esclusivi] | m può essere infinito

$\implies P(\bar{E}) = 1 - P(E), \qquad P(E_1 \cup E_2) = P(E_1) + P(E_2) - P(E_1 \cap E_2)$

__probabilità congiunta__ : $P(E_1 \cap E_2) = P(E_2 | E_1)P(E_1) = P(E_1 | E_2)P(E_2)$
>$P(E_1 \cap E_2)$si scrive anche$P(E_1, E_2)$

__probabilità condizionata__ : $P(H|E) = \frac{P(E \cap H)}{P(E)}$| con$P(E)$[prob. marginale]$\neq 0$
__indipendenza__ : $P(E \cap H) = P(E)P(H) \implies P(E|H) = P(E), P(H|E) = P(H)$( si scrive$E \perp H$)

$\implies P(E) = P(E|H)*P(H) + P(E|\bar{H})*P(\bar{H})$(sempre vera ?)
$\implies P(E) = \sum_{i=1}^{n}P(E|H_i)*P(H_i)$(se$H_1, H_2, ..., H_n$sono eventi mutuamente esclusivi ed esaustivi ovvero$H_i \cap H_j = \emptyset$per ogni$i \neq j$e$\bigcup_{i=1}^{n} H_i = \Omega$)

__teorema di Bayes__: $P(H_i|E) = \frac{P(E|H_i)P(H_i)}{\sum_{i=1}^{n}P(E|H_i)P(H_i)}$

>$P(H|E) = \frac{P(E|H)P(H)}{P(E|H)*P(H) + P(E|\bar{H})*P(\bar{H})}$

__odds__: $O(E) = P(E)/P(\bar{E})$

>$O(H|E) = \frac{P(E|H)P(H)}{P(E|\bar{H})P(\bar{H})} \implies P(H|E) = \frac{O(H|E)}{1+O(H|E)}$

___

- __Variabili Aleatorie__:
    __funzione di ripartizione__ : 
        -$F_X(x) = P(X \leq x)$
        -$P(a < X < b) = P(X < b) - P(X < a) = F_X(b) - F_X(a)$
        - mediana$\tilde{x}$: $F_X(\tilde{x}) = \frac{1}{2}$(analogo per$Q_1$e$Q_3$)
    __valore atteso__ : 
        -$E[aX + bY + c] = aE[X] + bE[Y] + c$
        -$E[XY] = E[X]E[Y]$se$X \perp Y$
        -$E[X+Y] = E[X] + E[Y]$se$X \perp Y$
    __varianza__ :
        -$Var[aX + bY + c] = a^2Var[X] + b^2Var[Y] + 2abCov(X,Y)$con$Cov(X,Y) = 0$se$X \perp Y$
        -$Var[X] = E[X^2] - E[X]^2$
        -$Var[X+Y] = Var[X] + Var[Y]$se$X \perp Y$
        -$Var[\sum_{i=1}^{n} X_i] = \sum_{i=1}^{n} Var[X_i] + \sum_{i=1}^{n} \sum_{j \neq i} Cov[X_i, X_j]$
    __covarianza__ :
        -$Cov[X,Y] = E[(X-E[X])(Y-E[Y])] = E[XY] - E[X]E[Y]$
        -$Cov[X,X] = Var[X]$
        -$Cov[X,Y] = 0$se$X \perp Y$
        -$Cov[aX + b, cY + d] = acCov[X,Y]$
        -$Cov[X,Y] = Cov[Y,X]$
        -$Cov[\sum_{i=1}^{n} X_i, \sum_{j=1}^{m} Y_j] = \sum_{i=1}^{n} \sum_{j=1}^{m} Cov[X_i, Y_j]$
    __funzione generatrice dei momenti__ :
        -$\Phi_X(t) = E[e^{tX}]$
        -$\Phi_X^{(r)}(t) = \frac{d^r \Phi_X(t)}{dt^r} = \frac{d^r E[e^tx]}{dt^r}$per$t = 0$si ottiene il momento$r$-esimo$E[X^r]$
        - se$X \perp Y$allora$\Phi_{X+Y}(t) = \Phi_X(t)\Phi_Y(t)$
    __indipendeza__ : 
        -$P(X < a, Y < b) = P(X < a)P(Y < b) = F_X(a)F_Y(b)$
    <br>

    ||caso discreto ($X, Y \subseteq \mathbb{N}$)|caso continuo ($X, Y \subseteq \mathbb{R}$)|
    |---|---|---|
    |funzione di massa/densità di probabilità|$p_X(x) = P(X = x)$|$f_X(x) = \frac{d}{dx} F_X(x)$| 
    |funzione di ripartizione|$F_X(x) = \sum_{y \leq x} p_X(y)$<br>$\implies P(a < X < b) = \sum_{x=a}^{b} p_X(x)$|$F_X(x) = \int_{-\infty}^{x} f_X(t) dt$<br>$\implies P(a < X < b) = \int_{a}^{b} f_X(x) dx$|
    |valore atteso|$E[X] = \sum_{X} x*p_X(x)$<br>$E[g(X)] = \sum_{X} g(x)p_X(x)$<br>$\implies E[X^k] = \sum_{X} x^k p_X(x)$|$E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$<br>$E[g(X)] = \int_{-\infty}^{\infty} g(x)f_X(x) dx$<br>$\implies E[X^k] = \int_{-\infty}^{\infty} x^k f_X(x) dx$|
    |funzione di massa/densità di probabilità congiunta|$p_{XY}(x,y) = P(X = x, Y = y)$|$f_{XY}(x,y) = \frac{\partial^2}{\partial x \partial y} F_{XY}(x,y)$|
    |funzione di massa/densità di probabilità marginale (rispetto ad$X$)|$p_X(x) = \sum_{y} p_{XY}(x,y)$|$f_X(x) = \int_{-\infty}^{\infty} f_{XY}(x,y) dy$|
    |funzione di massa/densità di probabilità condizionata|$p_{X\|Y}(x\|y) = P(X = x\|Y = y) = \frac{p_{XY}(x,y)}{p_Y(y)}$ (per$p_Y(y) > 0$) |$f_{X\|Y}(x\|y) = \frac{f_{XY}(x,y)}{f_Y(y)}$ (per$f_Y(y) > 0$)|
    |funzione di ripartizione congiunta|$F_{XY}(x,y) = P(X \leq x, Y \leq y)$|$F_{XY}(x,y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f_{XY}(u,v) dv du$|
    |funzione di ripartizione marginale (rispetto ad$X$)|$F_X(x) = P(X \leq x, Y < \infty) = \sum_{Y} F_{XY}(x,y)$|$F_X(x) = \int_{-\infty}^{\infty} F_{XY}(x,y) dy$|
    |indipendeza|$p_{X,Y}(x,y) = p_X(x)p_Y(y)$|$f_{X,Y}(x,y) = f_X(x)f_Y(y)$|

    __disuguaglianza di Markov__ : $P(X \geq a) \leq \frac{E[X]}{a}$per$a > 0$e$X \geq 0$
    __disuguaglianza di Chebyshev__ : $P(|X - E[X]| \geq a) \leq \frac{Var[X]}{a^2}$per$a > 0$
    
    > per$E[X] = \mu$e$Var[X] = \sigma^2$si ha$P(|X - \mu| \geq a) \leq \frac{\sigma^2}{a^2}$(questo è il caso più comune, distribuzione normale)

    __legge debole dei grandi numeri__ : $P(|\frac{1}{n} \sum_{i=1}^{n} X_i - E[X]| \geq \epsilon) \leq \frac{Var[X]}{n\epsilon^2}$per$n \geq 1$e$\epsilon > 0$

___

- __Modelli di V.A.__ :
    - __DISCRETE__ :
        ___
        #### Bernoulli
        caso di un esperimento Bernoulliano eg. lancio di una moneta
       $X \sim Ber(p)$
       $||\Omega|| = ||X|| = 2$
       $p_X(x) = p^x(1-p)^{1-x}$con$x \in \{0,1\} \implies p_X(0) = 1-p,\qquad p_X(1) = p$
       $E[X] = p$
       $Var[X] = p(1-p) = p - p^2$
        ___
        #### Binomiale
        caso di$n$esperimenti Bernoulliani indipendenti eg. lancio di$n$monete
       $X \sim Bin(n,p)$
       $p_X(x) = \binom{n}{x} p^x(1-p)^{n-x}$con$x \in \{0,1,...,n\}$|$x =$numero di successi in$n$esperimenti
        
        >$\binom{n}{x} = \frac{n!}{x!(n-x)!}$
        >$\binom{n}{x} = \binom{n}{n-x}$,$\binom{n}{0} = \binom{n}{n} = 1$,$\binom{n}{1} = \binom{n}{n-1} = n$
        
       $E[X] = np$
       $Var[X] = np(1-p)$       
        >$Y_i \sim Ber(p), X = \sum_{i=1}^{n} Y_i \implies X \sim Bin(n,p)$
        >$X_1 \sim Bin(n_1,p), X_2 \sim Bin(n_2,p) \implies X_1 + X_2 \sim Bin(n_1 + n_2, p)$<!--#TODO check-->
        >$P(X = k+1) = \frac{p}{1-p} \frac{n-k}{k+1} P(X = k)$ [ riproducibilità ]
        ___
        #### Poisson
        caso di$n$esperimenti Bernoulliani indipendenti con$n \to \infty$e$p \to 0$con$np = \lambda$costante
       $X \sim Pois(\lambda)$
       $p_X(x) = \frac{\lambda^x}{x!}e^{-\lambda}$con$x \in \mathbb{N}$
       $\Phi_X(t) = e^{\lambda(e^t - 1)}$
       $E[X] = \lambda$
       $Var[X] = \lambda$
        >$X_1 \sim Pois(\lambda_1), X_2 \sim Pois(\lambda_2) \implies X_1 + X_2 \sim Pois(\lambda_1 + \lambda_2)$con$X_1 \perp X_2$
        >$X_i \sim Pois(\lambda_i), X = \sum_{i=1}^{n} X_i \implies X \sim Pois(\sum_i \lambda_i)$con$X_i \perp X_j$
        >$P(X = k+1) = \frac{\lambda}{k+1} P(X = k)$ [ riproducibilità ]
        ___
        #### Ipergeometrica
        caso di$n$esperimenti Bernoulliani __dipendenti__ con$n \to \infty$eg. estrazioni senza reinserimento
       $X \sim H(N,M,n)$
       $p_X(x) = \frac{\binom{N}{x}\binom{M}{n-x}}{\binom{N+M}{n}}$con$x \in \{0,1,...,n\}$
       $E[X] = \frac{nN}{N+M}$
       $Var[X] = \frac{nNM}{(N+M)^2} - \frac{n(n-1)NM}{(N+M)^2(N+M-1)}$
        ___
    - __CONTINUE__ :
        ___
        #### Uniforme
       $X \sim U(a,b)$
       $f_X(x) = \frac{1}{b-a}$con$x \in [a,b]$
       $F_X(x) = \frac{x-a}{b-a}$con$x \in [a,b] \implies P(\alpha \leq X \leq \beta) = \frac{\beta-\alpha}{b-a}$
       $E[X] = \frac{a+b}{2}$
       $Var[X] = \frac{(b-a)^2}{12}$
        >$E[X^2] = \frac{a^2+ab+b^2}{3}$
        ___
        #### Normale/Gaussiana
       $X \sim N(\mu, \sigma^2)$
       $f_X(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$con$x \in \mathbb{R}$
        >$max_{x \in \mathbb{R}} f_X(x) = f_X(\mu) = \frac{1}{\sigma\sqrt{2\pi}}$
       $\Phi_X(t) = e^{\mu t + \frac{\sigma^2 t^2}{2}}$
       $E[X] = \mu$
       $Var[X] = \sigma^2$
        >$E[X^2] = \mu^2 + \sigma^2$

        versione standardizzata : $Z = \frac{X-\mu}{\sigma} \sim N(0,1)$
        >$X \sim N(\mu,\sigma^2)$allora$Y = \alpha + \beta X \sim N(\alpha+\beta\mu,\beta^2\sigma^2) = N(0,1)$per$\alpha = -\mu/\sigma$e$\beta = 1/\sigma$
        
       $F_Z(x) = \Phi(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x}e^{\frac{z^2}{2}} dz$| non ha nulla che a vedere con la funzione generatrice dei momenti
        
        >$P_X(x < a) = P_X(\frac{x-\mu}{\sigma} < \frac{a-\mu}{\sigma}) = P_Z(z < \frac{a-\mu}{\sigma}) = \Phi(\frac{a-\mu}{\sigma})$

        caso somma di$m$v.a. normali indipendenti : $X = \sum_{i=1}^{m} X_i \sim N(\sum_{i=1}^{m} \mu_i, \sum_{i=1}^{m} \sigma_i^2)$
        con funzione generatrice dei momenti : $\Phi_X(t) = e^{\sum_{i=1}^{m} \mu_i t + \frac{1}{2}\sum_{i=1}^{m} \sigma_i^2 t^2}$
        ___
        #### Esponenziale
       $X \sim Exp(\lambda)$
       $f_X(x) = \lambda e^{-\lambda x}$con$x \in \mathbb{R}^+$
       $F_X(x) = 1 - e^{-\lambda x}$con$x \in \mathbb{R}^+$
       $\Phi_X(t) = \frac{\lambda}{\lambda - t}$con$t < \lambda$
       $E[X] = \frac{1}{\lambda}$
       $Var[X] = \frac{1}{\lambda^2}$
        >$E[X^2] = \frac{2}{\lambda^2}$

        __senza memoria__ : $P(X > s+t | X > s) = P(X > t) \implies P(X > s + t) = P(X > s)P(X > t)$
        > __con memoria__ : $P(\text{vita residua} > t) = P(\text{vita totale} > s+t | \text{vita vissuta} > s) = \frac{1-F_X(s+t)}{1-F_X(s)}$
        ___
        #### Gamma
       $X \sim \Gamma(\alpha, \lambda)$
       $f_X(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}$con$x \in \mathbb{R}^+$
        >$\Gamma(\alpha) = \int_{0}^{\infty} t^{\alpha-1} e^{-t} dt$
        >$\Gamma(\alpha+1) = \alpha \Gamma(\alpha) \implies \Gamma(\alpha) = (\alpha-1)!$con$\alpha \in \mathbb{N}$

       $\Phi_X(t) = \frac{\lambda^\alpha}{(\lambda - t)^\alpha}$
       $E[X] = \frac{\alpha}{\lambda}$
       $Var[X] = \frac{\alpha}{\lambda^2}$
        >$E[X^2] = \frac{\alpha(\alpha+1)}{\lambda^\alpha}$

        >$X_1 + X_2 \sim Gamma(\alpha_1 + \alpha_2, \lambda)$con$X_i \sim Gamma(\alpha_i, \lambda)$indipendenti [ riproducibilità ]
        ___
        #### Chi-quadro$\Chi^2$
        se$Z \sim N(0,1) \implies \Chi_1^2 \sim Z^2$
        per$Z_1, Z_2, ..., Z_n \sim N(0,1)$indipendenti$\sum_{i=1}^{n} Z_i^2 \sim \Chi_n^2$[$n$grado di libertà]
       $\Chi_n^2+\Chi_m^2 = \Chi_{n+m}^2$[ riproducibilità ]
        ___
        ####$t$di Student 
       $T_n = \frac{Z}{\sqrt{C_n/n}}$con$Z \sim N(0,1)$e$C_n \sim \Chi_n^2$
       $E[T_n] = 0$per$n \ge 2$
       $Var[T_n] = \frac{n}{n-2}$per$n \ge 3$

       $t_{\alpha,n} := P(T_n \ge t_{\alpha,n}) = \alpha$
        ___
        #### Fisher-Smedeoor
       $F_{n,m} \sim \frac{C_n/n}{C_m/m}$con$C_n \sim \Chi_n^2$e$C_m \sim \Chi_m^2$

       $f_{n,m,\alpha} := P(F_{n,m} \ge f_{n,m,\alpha}) = \alpha$
___

### Statistiche campionarie
 
 __media medie campionarie__ : $E[\bar{X}] = E[\frac{X_1+X_2+...+X_n}{n}] = \mu$con$E[X_i] = \mu$indipendenti ? 
 __varianza medie campionarie__ : $Var[\bar{X}] = Var[\frac{X_1+X_2+...+X_n}{n}] = \frac{\sigma^2}{n}$con$Var[X_i] = \sigma^2$indipendenti ?
 __teorema del limite centrale__ : $\sum_{i=1}^{n} X_i \sim N(n\mu, n\sigma^2)$con$X_i \sim N(\mu, \sigma^2)$e indipendenti (__i.i.d__)
 > con$X_i \sim Ber(p) \implies \sum_{i=1}^{n} X_i \sim N(np, np(1-p))$con$n$suff. grande 
 > __forma standardizzata__ : $\frac{(\sum_{i=1}^{n} X_i) - n\mu}{\sigma\sqrt{n}} \sim N(0,1)$
 >$\implies$con$X_i \sim Ber(p) \implies \frac{(\sum_{i=1}^{n} X_i)-np}{\sqrt{np(1-p)}} \sim N(0,1)$

__distribuzione media campionaria__ : $\bar{X} = \frac{\sum_{i=1}^{n} X_i}{n} \sim N(\mu,\frac{\sigma^2}{n})$
__varianza campionaria__ : $S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar{X})^2$
__valore atteso varianza campionaria__ : $E[S^2] = \sigma^2$
__popolazioni gaussiane__ : $\bar{X} = \frac{\sum_{i=1}^{n} X_i}{n} \sim N(\mu,\frac{\sigma^2}{n}) \implies \frac{S^2}{\sigma^2}=\frac{1}{\sigma^2(n-1)}\sum_{i=1}^{n}(X_i-\bar{X})^2 \sim \frac{\Chi_n-1^2}{n-1}$
> stimando$\sigma^2$tramite$S^2$allora$\frac{\bar{X}-\mu}{S/\sqrt{n}} \sim t_{n-1}$

___

### Inferenze parametriche

__massima verosimiglianza__ := ML (maximum likelihood)
__funzione di ML prima dell'osservazione__ : $l(x_1, x_2, ..., x_n | \theta) = \prod_{i=1}^{n} f_X(x_i | \theta)$<!-- #TODO check -->
__funzione di ML dopo l'osservazione__ : $l(\theta; x_1, x_2, ..., x_n) = \prod_{i=1}^{n} f_{X_i}(x_i | \theta)$
__stima di massima verosimiglianza__ := MLE (maximum likelihood estimation) indicato con$\hat{\theta}$è il valore di$\theta$che massimizza la funzione di MLE dopo l'osservazione

- MLE di una BERNOULLIANA __$Ber(p)$__
 $l(p; x_1, x_2, ..., x_n) = p^{\sum_{i=1}^{n} x_i} (1-p)^{n-\sum_{i=1}^{n} x_i}$
  __stima/stimatore MLE__ : $\hat{\theta} = \hat{p} = \frac{\sum_{i=1}^{n} x_i}{n} = \bar{x}$
- MLE di una POISSON __$Pois(\lambda)$__
 $l(\lambda; x_1, x_2, ..., x_n) = \frac{\lambda^{\sum_{i=1}^{n} x_i}}{\prod_{i=1}^{n} x_i!} e^{-n\lambda}$
  __stima MLE__ : $\hat{\theta} = \hat{\lambda} = \frac{\sum_{i=1}^{n} x_i}{n} = \bar{x}$
- MLE di una NORMALE __$N(\mu, \sigma^2)$__
 $l(\mu, \sigma^2; x_1, x_2, ..., x_n) = (\frac{1}{2\pi})^{n/2} \frac{1}{\sigma^n} e^{-\frac{1}{2\sigma^2}\sum_{i=1}^{n} (x_i-\mu)^2}$
  __stima MLE__ : $\hat{\mu} = \frac{\sum_{i=1}^{n} x_i}{n} = \bar{x}$e$\hat{\sigma}^2 = \frac{\sum_{i=1}^{n} (x_i-\hat{\mu})^2}{n}$(vedere eccezione sotto)
  > in caso siano dati un numero finito di dati per la MLE di$\sigma^2$si usa$\sigma^2 = s^2 = \frac{\sum_{i=1}^{n} (x_i-\bar{x})^2}{n-1}$

  __stimatore distorto della varianza__ : $\frac{\sum_{i=1}^{n} (x_i-\bar{x})^2}{n}$

__perdita/loss__ : $L(T(x), \theta) = \begin{cases} = 0 & \text{se } T(x) = \theta \\ > 0 & \text{se } T(x) \neq \theta \end{cases}$ | T(x) è lo stimatore(/stima ?)
__funzione quadratica di perdita__ : $L(T(x), \theta) = \begin{cases} 0 & \text{se } T(x) = \theta \\ (T(x)-\theta)^2 & \text{se } T(x) \neq \theta \end{cases}$
__rischio__ : $MSE(\theta) = E[(T(x)-\theta)^2] = \int_{-\infty}^{\infty} (T(x)-\theta)^2 f_X(T(x)|\theta)$
__bias__ : $b_\theta(T) = E[T(x)] - \theta$

__stimatore corretto__ : $b_\theta(T) = 0 \implies E[T(x)] = \theta$
> se$T(x) = \sum_{i=1}^{n} \alpha_i x_i$ed è corretto, ovvero$E[T(x)] = \theta$allora$\sum_{i=1}^{n} \alpha_i = 1$
> mentre __l'errore quadratico medio__ o __rischio__ è$r(\theta, T) = E[(T-\theta)^2] = Var[T] + b_\theta(T)^2 = Var[T]$

___
__intervalli di confidenza per$\mu$dato$X \sim N(\mu, \sigma)$__ :
$\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$
$P(-z_{\frac{\alpha}{2}} \leq \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \leq z_{\frac{\alpha}{2}}) = 1-\alpha$con$\alpha$livello di confidenza 
> eg.$\alpha = 0.05 \implies z_{\frac{\alpha}{2}} = 1.96$e$P(-1.96 \leq \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \leq 1.96) = 0.95$

__intervallo di confidenza__ : $\mu \in [\bar{X}-z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}, \bar{X}+z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}]$
__ampiezza intervallo__ : $ci = 2z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}$
__numerosità campionaria__ : $n = (\frac{2z_{\frac{\alpha}{2}}\sigma}{ci})^2$
> __intervallo di predizione__ : $X_{n+1} \in [\bar{X}-z_\alpha \sigma\sqrt{1+1/n}, \bar{X}+z_\alpha \sigma\sqrt{1+1/n}]$(sempre con probabilità$1-\alpha$)
___
__intervalli di confidenza per$\mu$di una Normale con varianza$\sigma$incognita__ :
$\frac{\bar{X}-\mu}{S/\sqrt{n}} \sim t_{n-1}$con$S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar{X})^2$
$P(-t_{\frac{\alpha}{2},n-1} \leq \frac{\bar{X}-\mu}{S/\sqrt{n}} \leq t_{\frac{\alpha}{2},n-1}) = 1-\alpha$con$\alpha$livello di confidenza
__intervallo di confidenza__ : $\mu \in [\bar{X}-t_{\frac{\alpha}{2},n-1}\frac{S}{\sqrt{n}}, \bar{X}+t_{\frac{\alpha}{2},n-1}\frac{S}{\sqrt{n}}]$
> __intervallo di predizione__ : $X_{n+1} \in [\bar{X}-t_{\frac{\alpha}{2},n-1}S\sqrt{1+1/n}, \bar{X}+t_{\frac{\alpha}{2},n-1}S\sqrt{1+1/n}]$(sempre con probabilità$1-\alpha$)
___
__intervalli di confidenza per$\sigma^2$di una Normale__ :
$\frac{(n-1)S^2}{\sigma^2} \sim \Chi_{n-1}$(Chi)
$P(\frac{(n-1)S^2}{\Chi_{\frac{\alpha}{2},n-1}} \leq \sigma^2 \leq \frac{(n-1)S^2}{\Chi_{1-\frac{\alpha}{2},n-1}}) = 1 - \alpha$con$\alpha$livello di confidenza
__intervallo di confidenza__ : $\sigma^2 \in [\frac{(n-1)S^2}{\Chi_{\frac{\alpha}{2},n-1}}, \frac{(n-1)S^2}{\Chi_{1-\frac{\alpha}{2},n-1}}]$
___
__intervalli di confidenza per la differenza di medie di due Normali -$\sigma_1^2$e$\sigma_2^2$NOTE -__ :
$\frac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{\sqrt{\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m}}} \sim N(0,1)$
$P(\bar{X}-\bar{Y}-z_{\frac{\alpha}{2}}\sqrt{\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m}} \leq \mu_1-\mu_2 \leq \bar{X}-\bar{Y}+z_{\frac{\alpha}{2}}\sqrt{\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m}}) = 1-\alpha$con$\alpha$livello di confidenza
__intervallo di confidenza__ : $\mu_1-\mu_2 \in [\bar{X}-\bar{Y}-z_{\frac{\alpha}{2}}\sqrt{\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m}}, \bar{X}-\bar{Y}+z_{\frac{\alpha}{2}}\sqrt{\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m}}]$
___
__intervalli di confidenza per la differenza di medie di due Normali -$\sigma_1^2$e$\sigma_2^2$INCOGNITE -__ :
$\frac{(\bar{X}-\bar{Y})-(\mu_1-\mu_2)}{S_p \sqrt{1/n + 1/m}} \sim t_{n+m-2}$con$S_p^2 = \frac{(n-1)S_1^2 + (m-1)S_2^2}{n+m-2}$
$P(\bar{X}-\bar{Y}-t_{\frac{\alpha}{2},n+m-2}S_p \sqrt{1/n + 1/m} \leq \mu_1-\mu_2 \leq \bar{X}-\bar{Y}+t_{\frac{\alpha}{2},n+m-2}S_p \sqrt{1/n + 1/m}) = 1-\alpha$con$\alpha$livello di confidenza
__intervallo di confidenza__ : $\mu_1-\mu_2 \in [\bar{X}-\bar{Y}-t_{\frac{\alpha}{2},n+m-2}S_p \sqrt{1/n + 1/m}, \bar{X}-\bar{Y}+t_{\frac{\alpha}{2},n+m-2}S_p \sqrt{1/n + 1/m}]$
___
__intervalli di confidenza per p di una Bernoulliana__ :
$\hat{p} = \frac{\sum_{i=1}^{n} x_i}{n}$
$\hat{p} \sim N(p, \frac{p(1-p)}{n}) \implies \frac{\hat{p}- p}{\sqrt{p(1-p)/n}} \sim N(0,1)$
$P(\hat{p} - z_{\frac{\alpha}{2}}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \leq p \leq \hat{p} + z_{\frac{\alpha}{2}}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}) = 1-\alpha$con$\alpha$livello di confidenza
__intervallo di confidenza__ : $p \in [\hat{p} - z_{\frac{\alpha}{2}}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}, \hat{p} + z_{\frac{\alpha}{2}}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}]$
___

### Test di ipotesi
Vogliamo stabilire se l'ipotesi fatta su un certo parametro che regola una distribuzione di una certa v.a. è accettabile o meno alla luce delle osservazioni fatte su un campione di osservazioni della v.a. in questione (ovvero verificare se il campione supporta l'ipotesi avanzata).

Sia $H_0$ __l'ipotesi nulla__ (da verificare su $\theta$ ). __Accetto__ $H_0$ se $(x_1, ..., x_n) \notin C$ con$C$__regione critica__. \
Indico con $H_1 \neq H_0$ __l'ipotesi alternativa__ (che è un ipotesi non compatibile con l'ipotesi nulla, non necessariamente l'opposto ma l'una esclusiva dell'altra) e $\alpha$ la probabilità di __errore di prima specie__ ovvero la probabilità che il campione cada nella regione critica pur essendo vera l'ipotesi nulla. 

Le ipotesi alternative possono essere di tre tipi : __bilaterali__ ($\neq$), __unilaterali__ (< o >), __puntuali__ (=).

Esiste anche la probabilità di __errore di seconda specie__, indicata con $\beta$ ovvero la probabilità di scelta dell'ipotesi nulla pur essendo vera l'ipotesi alternativa.\
<!-- TODO --> check. \
$\beta(\mu) = P_\mu(-z_\frac{\alpha}{2} \leq \frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}} \leq z_\frac{\alpha}{2}) = \Phi(-z_\frac{\alpha}{2} - \frac{\mu-\mu_0}{\sigma/\sqrt{n}}) - \Phi(z_\frac{\alpha}{2} - \frac{\mu-\mu_0}{\sigma/\sqrt{n}})$ \
__funzione potenza__ : $1 - \beta(\mu)$

con $H_1 : \mu \neq \mu_0$ si ha $C = [-\infty , -z_{\frac{\alpha}{2}}] \cup [ z_{\frac{\alpha}{2}}, \infty ]$ \
con $H_1 : \mu < \mu_0$ si ha $C = [-\infty , -z_{\alpha}]$ \
con $H_1 : \mu > \mu_0$ si ha $C = [z_{\alpha} , \infty ]$

cosa devo valutare se appartiene a $C$ ? \
$\frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}}$ 

oppure con la p-value confrontata con $\alpha$ : \
$1 - \Phi(\frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}})$ 

__test d'ipotesi sulla proporzione__ : \
$\frac{\hat{p}-p_0}{\sqrt{\hat{p}(1-\hat{p})/n}}$


- __verifica di ipotesi su$\mu$con$X \sim N(\mu, \sigma^2)$(test bilaterale)__ : 
   $H_0 : \mu = \mu_0$e$H_1 : \mu \neq \mu_0$
   $C = ((x_1, ..., x_n) : |\bar{x}-\mu_0| > z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}})$
    si rifiuta$H_0$se$\bar{x} \notin [\mu_0 - z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}, \mu_0 + z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}]$

    Indico con$\beta$la probabilità di __errore di seconda specie__ ovvero la probabilità di scelta$H_0$con$H_1$vera (con$H_0 : \mu = \mu_0$e$H_1 : \mu \neq \mu_0$).


    >$n \approx (\frac{z_\frac{\alpha}{2} + z_\beta}{\mu-\mu_0})^2 \sigma^2$

    > approccio p-value p-value$= \Phi(z)$, accetto$H_0$se p-value$>> \alpha$

- __test unilaterali__ :
   $H_0 : \mu = \mu_0$e$H_1 : \mu > \mu_0$
   $C = ((x_1, ..., x_n) : \bar{x} - \mu_0 > + z_\alpha\frac{\sigma}{\sqrt{n}})$
    si rifiuta$H_0$se$\bar{x} > \mu_0 + z_\alpha\frac{\sigma}{\sqrt{n}}$
    oppure p-value$= 1 - \Phi(\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}) < \alpha$
    si accetta$H_0$se$\bar{x} \leq \mu_0 + z_\alpha\frac{\sigma}{\sqrt{n}}$
    (con$H_0 : \mu = \mu_0$e$H_1 : \mu < \mu_0$si inverte il segno di$z_\alpha$e della disequazione)

    #TODO scelta test unilaterali
___
__t-test con$\sigma^2$incognita__ :
- __test bilaterale__ :
   $H_0 : \mu = \mu_0$e$H_1 : \mu \neq \mu_0$
    rifiuto$H_0$se$|\frac{\bar{X}-\mu_0}{S/\sqrt{n}}| > t_{\alpha/2, n-1}$
- __test unilaterale__ :
   $H_0 : \mu = \mu_0$e$H_1 : \mu \geq \mu_0$
    rifiuto$H_0$se$\frac{\bar{X}-\mu_0}{S/\sqrt{n}} > t_{\alpha, n-1}$
___
__identità delle medie di due popolazioni normali con$\sigma_1^2$e$\sigma_2^2$note__ :
$H_0 : \mu_1 = \mu_2$e$H_1 : \mu_1 \neq \mu_2$
rifiuto$H_0$se$\frac{\bar{X}-\bar{Y}}{\sqrt{\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m}}} > z_{\frac{\alpha}{2}}$

__identità delle medie di due popolazioni normali con$\sigma_1^2$e$\sigma_2^2$incognite ma uguali__ :
$S_p^2 = \frac{(n-1)S_x^2+(m-1)S_y^2}{n+m-2}$
rifiuto$H_0$se$|\frac{\bar{X}-\bar{Y}}{S_p\sqrt{\frac{1}{n}+\frac{1}{m}}}| > t_{\frac{\alpha}{2}, n+m-2}$
accetto$H_0$se$|\frac{\bar{X}-\bar{Y}}{S_p\sqrt{\frac{1}{n}+\frac{1}{m}}}| \sim t_{n+m-2}$

__identità delle medie di due popolazioni normali con$\sigma_1^2$e$\sigma_2^2$incognite e diverse ma$n$e$m$uguali__ :
accetto$H_0$se$z_{\alpha/2} \leq \frac{\bar{X}-\bar{Y}}{\sqrt{S_x^2/\sqrt{n} + S_y^2/\sqrt{m}}} \leq z_{\alpha/2}$
___
__test t su dati appaiati__ :

$w_i = x_i - y_i$,$W \sim N(\mu_w, \sigma_w^2)$
$H_0 : \mu_w = 0$e$H_1 : \mu_w \neq 0$
accetto$H_0$se$|\frac{\bar{W}}{S_w/\sqrt{n}}| \leq t_{\frac{\alpha}{2}, n-1} \implies -t_{\frac{\alpha}{2}, n-1} \leq \sqrt{n}\frac{\bar{W}}{S_w} \leq t_{\frac{\alpha}{2}, n-1}$

__test sulla varianza di una normale__ :
$H_0 : \sigma^2 = \sigma_0^2$e$H_1 : \sigma^2 \neq \sigma_0^2$
$\frac{S^2}{\sigma_0^2}(n-1) \sim \Chi_{n-1}^2$(Chi)
accetto$H_0$se$\Chi_{1-\alpha/2, n-1}^2 \leq \frac{S^2}{\sigma_0^2}(n-1) \leq \Chi_{\alpha/2, n-1}^2$

__test sull'uguaglianza della varianza di due normali__ :
$H_0 : \sigma_1^2 = \sigma_2^2$e$H_1 : \sigma_1^2 \neq \sigma_2^2$
$\frac{S_1^2}{S_2^2} \sim F_{n-1, m-1}$(Fisher)
accetto$H_0$se$F_{1-\alpha/2, n-1, m-1} \leq \frac{S_1^2}{S_2^2} \leq F_{\alpha/2, n-1, m-1}$

__test su p di una popolazione Bernoulliana__ :
$H_0 : p \leq p_0$e$H_1 : p > p_0$dato$X \sim Ber(p)$e$Y = \sum_{i=1}^{n} X_i \sim Bin(p,n)$
rifiuto$H_0$se$Y > k^* := \text{min} ( k | \sum_{i=k}^{n} \binom{n}{i} p_0^i (1- p_0)^{n-i} \leq \alpha )$
> oppure rifiuto $H_0$se$\frac{Y-np_0}{\sqrt{np_0(1-p_0)}} > z_\alpha$(approssimazione buona se$np_0(1-p_0) \geq 20$)

__test su p di due popolazioni Bernoulliane__ :
$H_0 : p_1 = p_2$e$H_1 : p_1 \neq p_2$dato$Y_1 \sim Bin(p_1, n_1)$e$Y_2 \sim Bin(p_2, n_2)$
rifiuto$H_0$se$Y_1 \geq k^* := \text{min} ( k | \sum_{i=1}^{n_1} \frac{\binom{n_1}{i} \binom{n_2}{k-i}}{\binom{n_1+n_2}{k}} \leq \alpha )$
> oppure rifiuto$H_0$se$Y_1 \leq k^* := \text{max} ( k | \sum_{i=1}^{n_1} \frac{\binom{n_1}{i} \binom{n_2}{k-i}}{\binom{n_1+n_2}{k}} \leq \alpha )$

__test sul$\lambda$di una Poisson__ :
$H_0 : \lambda = \lambda_0$e$H_1 : \lambda \neq \lambda_0$dato$Y = \sum x_i \sim Pois(n \lambda)$
rifiuto$H_0$se$Y \in [k^* := \text{min}(k | \sum_{i=1}^{n_1} \frac{(n\lambda_0)^ie^{-n\lambda_0}}{i!} < \alpha/2), k^* := \text{max}(k | \sum_{i=1}^{n_1} \frac{(n\lambda_0)^ie^{-n\lambda_0}}{i!} < \alpha/2)]$

__test tra i paramentri di due popolazioni di Poisson__ : #TODO fix
$H_0 : \lambda_2 = c\lambda_2$e$H_1 : \lambda_1 \neq \lambda_2$dato$Y_1 = \sum x_i \sim Pois(n_1 \lambda_1)$e$Y_2 = \sum x_i \sim Pois(n_2 \lambda_2)$
___

### Modello lineare
Chiamiamo$Y$la variabile __di risposta__ da perdire,$x_1, ..., x_n$variabili __di regressione__ e$y_1, ..., y_n$le __determinazioni__ di$Y$.
__modello lineare stocastico base__ : $Y = \alpha + \beta_1 x_1 + ... + \beta_n x_n + \epsilon$
$E[\epsilon] = 0 \implies E[Y] - E[\alpha + \beta_1 x_1 + ... + \beta_n x_n] = 0$ovvero la retta di regressione stimata deve passare in mezzo ai dati

- __stima ai minimi quadrati__ :
    __danno quadratico__ : $SS = \sum_{i=1}^{n} (y_i - \alpha - \beta x_i)^2 \implies \alpha = \bar{y} - \hat{\beta}\bar{x}$con$\hat{\beta} = \frac{(\sum_{i=1}^{n} x_iy_i) - \bar{x}(\sum_{i=1}^{n}y_i)}{(\sum_{i=1}^{n}x_i^2) - n\bar{x}^2}$
- __distribuzione degli stimatori__ :
    __distribuzione di$B$__:
   $B = \frac{\sum_i (x_i -\bar{x})y_i - \bar{y}\sum_i (x_i - \bar{x}) }{\sum_i x_i^2 - n\bar{x}^2}$
   $E[B] = \frac{\sum_i(x_i-\bar{x})E[y_i]}{\sum_i x_i^2 - n\bar{x}^2} = \frac{\sum_i(x_i-\bar{x})(\alpha + \beta x_i)}{\sum_i x_i^2 - n\bar{x}^2} = \beta$stimatore corretto
   $Var[B] = \frac{\sigma^2}{\sum_i x_i^2 - n\bar{x}^2}$
   $Cov(B, \bar{Y}) = 0$
    __distribuzione di$A$__:
   $A = \bar{y} - B\bar{x} \sim N(E[A], Var[A])$
   $E[A] = E[\bar{y} - B\bar{x}] = E[\bar{y}] - E[B]\bar{x} = \alpha$stimatore corretto
   $Var[A] = \frac{\sigma^2 \sum_i x_i^2 }{n(\sum_i x_i^2-n\bar{x})}$
    __stimatori di$\sigma^2$__:
   $\frac{\sum_i(y_i - \mu)^2}{\sigma^2} \sim \Chi_{n}^2$(Chi)
   $\frac{\sum_i(y_i - \bar{y})^2}{\sigma^2} \sim \Chi_{n-1}^2$(Chi)
   $\frac{\sum_i(y_i - A - Bx_i)^2}{\sigma^2} \sim \Chi_{n-2}^2$(Chi)
   $SS_R = \sum_i (y_i -A -Bx_i)^2 \implies \frac{SS_R}{\sigma^2} \sim \Chi_{n-2}^2$(Chi)
   $E[\frac{SS_R}{\sigma^2}] = n-2 \implies E[\frac{SS_R}{n-2}] = \sigma^2$stimatore non distorto
    __somma dei quadrati__:
   $S_{xy} = \sum_i (x_i - \bar{x})(y_i - \bar{y}) = \sum_i x_iy_i - n\bar{x}\bar{y} = r \sqrt{S_{xx}S_{yy}}$
   $S_{xx} = \sum_i (x_i - \bar{x})^2 = \sum_i x_i^2 - n\bar{x}^2$
   $S_{yy} = \sum_i (y_i - \bar{y})^2 = \sum_i y_i^2 - n\bar{y}^2$
   $\hat{\beta} = \frac{S_{xy}}{S_{xx}}$,$\hat{\alpha} = \bar{y} - \hat{\beta}\bar{x}$
   $SS_R = \frac{S_{xx}S_{yy}-S_{xy}^2}{S_{xx}}$
___
- __Inferenza sui parametri di regressione__:
   $\frac{B-\beta}{\sigma/\sqrt{S_{xx}}} \sim N(0,1)$,$\frac{SS_R}{\sigma^2} \sim \Chi_{n-2}^2$
   $\implies$
   $\frac{B-\beta}{\sqrt{\frac{SS_R}{(n-2)S_{xx}}}} \sim t_{n-2}$
    ___
    __test d'ipotesi su$\beta$__:
       $H_0 : \beta = 0$e$H_1 : \beta \neq 0$
        rifiuto$H_0$se$\sqrt{\frac{(n-2)S_{xx}}{SS_R}}|\hat{\beta}| > t_{\frac{\alpha}{2}, n-2}$
        p-value$= 2P(t_{n-2} > \sqrt{\frac{(n-2)S_{xx}}{SS_R}}|\hat{\beta}|)$
       $P(-t_{\frac{\alpha}{2}, n-2} < \sqrt{\frac{(n-2)S_{xx}}{SS_R}}(B-\beta) < t_{\frac{\alpha}{2}, n-2}) = 1-\alpha$
        __intervallo di confidenza__: $\beta \in [\hat{\beta} - t_{\frac{\alpha}{2}, n-2}\sqrt{\frac{(n-2)S_{xx}}{SS_R}}, \hat{\beta} + t_{\frac{\alpha}{2}, n-2}\sqrt{\frac{(n-2)S_{xx}}{SS_R}}]$
    ___
    __inferenza su$\alpha$,$\sigma^2$incognito__:
       $A \sim N(\alpha, \frac{\sigma^2 \sum_i x_i^2 }{nS_{xx}})$
       $SS_R/\sigma^2 \sim \Chi_{n-2}^2$
       $\frac{N(0,1)}{\sqrt{\Chi_n^2/n}} \sim t_{n-2}$
        statistica test: $\frac{(A-\alpha)\sqrt{n(n-2)S_{xx}}}{\sqrt{SS_R\sum_i x_i^2}} \sim t_{n-2}$
        __intervallo di confidenza__: $\alpha \in [\hat{\alpha} - t_{\frac{\alpha}{2}, n-2}\sqrt{\frac{SS_R\sum_i x_i^2}{n(n-2)S_{xx}}}, \hat{\alpha} + t_{\frac{\alpha}{2}, n-2}\sqrt{\frac{SS_R\sum_i x_i^2}{n(n-2)S_{xx}}}]$
    ___
    __inferenza sulla risposta in media__:
        stima puntuale: $E[A+Bx_0] = \alpha + \beta x_0$
       $B = \sum_i \frac{(x_i-\bar{x})y_i}{S_{xx}}$,$A = \bar{y} - B\bar{x}$
       $Var[A+Bx_0] = \sigma^2(\frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}})$
       $A + Bx_0 = \bar{y} - B(\bar{x}-x_0) = \sum_i (\frac{1}{n} - \frac{(x_i-\bar{x})(\bar{x}-x_0)}{S_{xx}})y_i$
    ___
    __inferenza sulla risposta in media,$\sigma^2$incognito__:
       $A+Bx_0 \sim N(\alpha + \beta x_0, \sigma^2(\frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}))$
       $\frac{A+Bx_0 - (\alpha + \beta x_0)}{\sqrt{\frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}}\sqrt{\frac{SS_R}{n-2}}} \sim t_{n-2}$
        __intervallo di confidenza__: $[\hat{\alpha}+\hat{\beta}x_0 - t_{\frac{\alpha}{2}, n-2}\sqrt{\frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}}\sqrt{\frac{SS_R}{n-2}}, \hat{\alpha}+\hat{\beta}x_0 + t_{\frac{\alpha}{2}, n-2}\sqrt{\frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}}\sqrt{\frac{SS_R}{n-2}}]$
    ___
    __inferenza sualla predizione della risposta__:
        per ogni possibile x_0 cosa posso dire su Y | x_0 ?
       $Y \sim N(\alpha +\beta x_0, \sigma^2)$
       $A + Bx_0 \sim N(\alpha + \beta x_0, \sigma^2(\frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}))$
       $Y - A - Bx_0 \sim N(0, \sigma^2(\frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}))$
       $\implies$
       $\frac{Y - A - Bx_0}{\sqrt{\frac{n+1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}}\sqrt{\frac{SS_R}{n-2}}} \sim t_{n-2}$
        __intervallo di confidenza__: $[\hat{\alpha}+\hat{\beta}x_0 - t_{\frac{\alpha}{2}, n-2}\sqrt{\frac{n+1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}}\sqrt{\frac{SS_R}{n-2}}, \hat{\alpha}+\hat{\beta}x_0 + t_{\frac{\alpha}{2}, n-2}\sqrt{\frac{n+1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}}\sqrt{\frac{SS_R}{n-2}}]$
    ___
    __coefficiente di determinazione e di correlazione__:
        __coef. di determinazione__: $R^2 = \frac{S_{yy}-SS_R}{S_{yy}}$
        __coef. di correlazione__: $r = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}$
       $R^2 = r^2$
___
- __Linearizzazione__:
    se la risposta media non è una funzione linaere posso trasformare le variabili e usare il modello lineare.
    eg.
   $f(t) = c*e^{-\delta t} \implies \ln(f(t)) = \ln(c) - \delta t$
   $Y = \ln(f(t))$,$\alpha = \ln(c)$,$\beta = -\delta$
   $Y = \alpha + \beta t + e \implies f(t) = e^{A+Bt}$
___
- __Regressione lineare multipla__:
   $Y = \beta_0 + \beta_1 x_1 + ... + \beta_n x_n + \epsilon$,$\epsilon \sim N(0, \sigma^2)$
   $E[Y_i] = \beta_0 + \beta_1 x_{i1} + ... + \beta_n x_{in}$
    vogliamo minimizzare$S = \sum_i (y_i - \beta_0 - \sum_j \beta_j x_{ij})^2$ 
    __notazione matriciale__: $Y = X\Beta + e$,$p = k+1$(numero di parametri)
   $\begin{aligned}
    Y = \left[\begin{array}{ccc}
    y_1 \\
    y_2 \\
    \vdots \\
    y_n    
    \end{array}\right] \text{ , } 
    X = \left[\begin{array}{ccc}
    1 & x_{11} & \cdots & x_{1k} \\
    1 & x_{21} & \cdots & x_{2k} \\
    \vdots & \vdots & \ddots & \vdots \\
    1 & x_{n1} & \cdots & x_{nk} 
    \end{array}\right] \text{ , }
    \Beta = \left[\begin{array}{ccc}
    \beta_0 \\
    \beta_1 \\
    \vdots \\
    \beta_k
    \end{array}\right] \text{ , }
    e = \left[\begin{array}{ccc}
    e_1 \\
    e_2 \\
    \vdots \\
    e_n
    \end{array}\right]
    \end{aligned}$
    __stimatore di$\Beta$__: $\hat{\Beta} = (X^TX)^{-1}X^TY$
   $E[\hat{\Beta}] = \Beta$
   $Cov(\hat{\Beta}) = \sigma^2(X^TX)^{-1}$
    __stimatore di$\sigma^2$__: $S = \sum_i (y_i - \beta_0 - \sum_j \beta_j x_{ij})^2 \implies E[\frac{S}{\sigma^2}] = n-p \implies E[\frac{S}{n-p}] = \sigma^2 \implies \frac{S}{n-p}$stimatore corretto di$\sigma^2$
    __coefficiente di determinazione multipla__: $R^2 = 1 - \frac{S}{\sum_i(y_i-\bar{y})^2}$
- __Predizione di risposte future__:
   $E[Y|X] = \beta_0 + \beta_1 X_1 + ... + \beta_n X_n$
   $\sum_i^k \beta_i X_i$[natura stimatoriale]$\implies E[\sum_i^k \beta_i X_i] = E[Y|X]$
   $Var[\sum_i^k \beta_i X_i] = \sigma^2 X^T(X^TX)^{-1}X$
    __intervallo di confidenza__: $[\sum_i^k X_i\hat{\Beta} - t_{\frac{\alpha}{2}, n-p}\sqrt{\frac{S}{n-p}}\sqrt{X^T(X^TX)^{-1}X},\sum_i^k X_i\hat{\Beta} + t_{\frac{\alpha}{2}, n-p}\sqrt{\frac{S}{n-p}}\sqrt{X^T(X^TX)^{-1}X}]$
    __nuova osservazione__: $Y_{n+1} = \beta_0 + \beta_1 x_{n+1,1} + ... + \beta_n x_{n+1,n} + \epsilon_{n+1}$
