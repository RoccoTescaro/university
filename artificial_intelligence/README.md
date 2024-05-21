# Forma Normale Congiuntiva

Il programma è complemente implementato nel file 'main.py'. Per erguirlo è necessario avere installato Python 3.7 o superiore.

Per eseguire il programma è necessario lanciare il comando:

```bash
python main.py
```

Una volta eseguito il programma sarà richiesto all'utente la tipologia di test che vuole eseguire.

In caso si voglia eseguire il test per specifiche formule è necessario inserire 2 e alla richiesta della formula inserire la formula desiderata (inserendo spazi fra operatori, parentesi e operandi).

Se si vuole eseguire il test per formule casuali è necessario inserire 1. In questo caso sarà richiesto all'utente il numero di formule random da generare e il numero di variabili e ripetizioni di variabili da utilizzare. Sarà poi richiesto se generare formule valide o non valide.
Nel primo caso saranno stampate a video le formule generate e la formula convertita in cnf, nel secondo caso sarà segnalato all'utente solo il caso in cui si è verificato un errore, ovvero una formula non valida non è stata riconosciuta come tale.

Eg. di esecuzione:

```bash
python main.py
```

```
Enter 1 for random test or 2 for custom test: 1
Enter number of tests: 10
Enter number of variables: 3
Enter number of repetitions: 0
Enter 1 for valid tests or 2 for invalid tests: 1
! ( ! x_2 | ( x_1 & ! x_3 ) )
x_2 & ( ! x_1 | x_3 )

( x_1 <=> ( x_2 | ! x_3 ) )
( ! x_1 | x_2 | ! x_3 ) & ( ! x_2 | x_1 ) & ( x_3 | x_1 )

( ! x_3 & ( ! x_2 <=> ! x_1 ) )
! x_3 & ( x_2 | ! x_1 ) & ( x_1 | ! x_2 )
...
```

```
Enter 1 for random test or 2 for custom test: 2
Enter test case: ( A & B ) | C
( A | C ) & ( B | C )
```