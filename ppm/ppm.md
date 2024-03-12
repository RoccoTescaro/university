# Programmazione e produzione multimediale 

UNIVERSITA’ DEGLI STUDI DI FIRENZE \
Facolta di Ingegneria \
Corso di Laurea in Ingegneria Informatica \
[[B028451] Programmazione e produzione multimediale](https://e-l.unifi.it/enrol/index.php?id=40198)
___

Professore : [Marco Bertini](marco.bertini@edu.unifi.it) #TODO check email
___

## Indice: 

- [Immagine digitale](#immagini-digitali)
- #TODO second lesson
- [PNG (Portable Network Graphics)](#png-portable-network-graphics)
- [JPEG (Joint Photographic Experts Group)](#jpeg-joint-photographic-experts-group)
- [Video](#video)
___

## Immagini digitali

snapshot, fotografie temporalui elettroniche, prese da una scena reale o documenti. Un immagine digitale è composta e mappata ad una griglia di punti detti pixels che assumono valori numerichi binari e sono 'mappati' a loro volta a frequenze luminose. Questi valori numerici sono spesso compressi (vale a dire, ridotti ad un numero inferiore a quello necessario a rappresentare l'immagine originale completa).\
La profondità di bit (__bit depth__) è il numero di bit usati per rappresentare ogni pixel.\
Da una sorgente di ill'uminazione l'oggetto assorbe alcune frequenze luminose altre le riflette e i recettori che possono essere biologici o elettronici le trasformano in segnali elettrici. I sensori elettrici utilizzano dispositivi CMOS o CCD che recepiscono tre segnali di luce rossa, verde e blu aka __RGB__ (analogo al sistema di visione umano, sebbene la risposta ai segnali luminosi non sia identica).\
Cattura di immagini digitali:\
![](/images/sensor_grid.png) \
I pixel come detto sono organizzati su una matrice, l'ordine che viene scelto tipicamente (__CCD__) prevede che ci siano più sensori verdi che rossi e blu, questo perchè l'occhio umano è più sensibile al verde. In particolare i sensori verdi assumono una scacchiera alternata metre i sensori rossi e blu sono disposti in modo che ogni sensore sia adiacente ad almeno un sensore verde. Il rapporto tra il numero di sensori verdi e il numero di sensori rossi e blu è di 2:1.\
Dal momento che i sensori registrano solo una frequenza luminosa, per ottenere un'immagine a colori è necessario combinare i segnali, questo processo è chiamato __demosaicing__ ed fondamentalmente un algoritmo che interpola i valori dei pixel mancanti.\
Le altre caratterische importanti per l'acquisizione e display sono: la __risoluzione__ (la densità di pizel per unità di area, PPI pixel per inch), la __profondità di bit__ (il numero di bit usati per rappresentare ogni pixel), la __gamma__ (la relazione tra la luminosità e l'intensità del segnale elettrico), la __dimenzione dei pixel__ (l'effettiva dimensione fisica di un pixel e la forma). Altre caratterische importanti sono l'___aspect-ratio___ (il rapporto tra la larghezza e l'altezza dell'immagine), ___color spaces__ (temperatura, luminosità, staturazione ecc., un sistema a tre dimensioni, queste tre dimensioni possono assumere significati diversi e mappature diverse in base al sistema di colori utilizzato, CIE commissione che ha definito un sistema di colori standard).\
Oltre alla dimensione dei sensori è importate quanta luce raggiunge il sensore, ed è quello che rende ancora le macchine motografiche professionali migliori degli smartphone. Oltre a questo la quantità di __rumore__ (noise), generalmente le macchine fotografiche hanno un rumore minore. Ultimo elemento distinquente è la lente che cambia l'apertura, ...
Oltre a sensori che lavorano su frequenze di luce visibile, esistono sensori che lavorano su altre frequenze come l'infrarosso o l'ultravioletto (applicate per sistemi di sicurezza), in questo caso servono lenti speciali poichè quelle in vetro non trasparenti a queste frequenze (si usano lenti in germanio).
___Neuromorphic cameras___ (in commercio dal 2016): ciascun sensore ha un proprio sistema di campionamento, non c'è delay fra il campionamento del pixel più in alto a sinistra e quello più in basso a destra. Sono macchine interessate a catturare il cambiamento di ciascun pixel (generalemente sono interessate solo al cambiamento luminoso, quindi su scale di bianco e nero, non a colori), il flusso sincrono di _frames_. Queste camere sono applicate principalmente per rilevare il movimento, quindi la guida di un drone o per rilevare la presenza di persone o animali in un'area.

___

#TODO missing lesson

___

## PNG (Portable Network Graphics)

il formato Png è un formato di immagini creato in competizione al formato GIF, supera i 256 colori del GIF e supporta la trasparenza. E' stato creato per trasferire immagini su internet, ed è buono per la rappresentazione di immagini fotorealistiche. Essendo meno compresso del JPEG, è meno adatto per essere distribuito.  L'algoritmo di compressione è composto da sottoalgoritmi: __LZ77__ (algoritmo di compressione lossless, in realtà una variante) e __Huffman__ (algoritmo di compressione lossless).\
Questa combinazione di algoritmi è detta __DEFLATE__ ed è alla base di tutti le compressioni zip.

LZ77 ricerca ripetizioni di stringhe o buffer di memoria e le sostituisce con un puntatore alla stringa ripetuta. Più la stringa è lunga maggiore è il grado di compressione, ma maggiore è anche il tempo di compressione.\
L'ampiezza delle stringhe ricercate è alpiù di 32k caratteri.\
Quando la stringa è ripetuta viene sostituita da:
- distanza (15 bit) dalla posizione corrente
- lunghezza (8 bit) della stringa
- primo carattere diverso dalla stringa ripetuta 

Prima viene quindi creato un dizionario, finchè non abbiamo una ripetizione conveniente la stringa da ripetere aumenta. Quando diventa conveniente viene sostituita con la tripletta e si resetta la stringa da ripetere dal punto in cui si è arrivati.\
E' possibile anche ripetere una stringa più grande di quella salvata come dizionario ma in questo caso il buffer verrà attraversato modularmente (cioè se la stringa è più lunga del buffer, si riparte dall'inizio del buffer).\
Per la decodifica si parte dalla fine del file e si risale, quando si trova un puntatore si sostituisce la stringa ripetuta e si risale ancora.

![](/images/lz77.png)

___

## JPEG (Joint Photographic Experts Group)

Formato __lossy__, cioè la compressione è irreversibile. E' il formato più diffuso per le immagini fotografiche, pessimo invece per immagini senza linee nette o con pochi colori.\
Definisce sia un formato di file che un algoritmo di compressione/decodifica (___codec___).\
Il primo tipo di conversione che fa è dello spazio dei colori, passa dallo spazio RGB a quello YCbCr (Y luminanza, Cb e Cr sono le componenti del colore) o Y'CbCr. Questo permette di eliminare in prima istanza le informazioni di colore, che sono meno importanti per l'occhio umano (le lunghezze d'onda che l'occhio umano non riesce a distinguere).\
L'algoritmo lavora separate su luminanza e colore (primo elemento di compressione lossy).\
Ci sono diversi schemi per rimuovere i dati del colore usati anche per la codifica di video.
> __Nota__: il primo valore identifica la finestra di pixel, il secondo di quanti pixel su righe pari (nella dinestra di pixel) ho l'effettivo colore e non un'interpolazione, il terzo come il secondo ma per le righe dispari.

eg. 4:2:0 significa che per ogni 4 pixel ho due pixel di colore per le righe pari e nessuno per le righe dispari.
![](/images/chroma_compression_jpeg.png)

> __Fun fact__: per questo motivo è pratica comune per i titolatori video scrivere testo con bordo e interno ad alto contrasto di luminosità, anche solo di un pixel di spessore, in modo che se non dovesse venire campionato il bordo essendo comunque la luminosità campionata per ogni pixel si eviterebbe il così detto effetto __bleeding__.

#TODO fix notation

La differenza fra Y e Y' per la luminosità che nel secondo caso è codificata non linearmente ma usando la gamma. La gamma è la relazione fra la luminosità e l'intensità del segnale elettrico: $D = I^\gamma$.

Il Jpeg elimina le alte frequenze quindi il dettaglio ad altro contrasto si perde (eg. i bordi e il bianco-nero).

L'immagine viene divisa in blochi (generalmente 8x8 pixel, se l'immagine originale non è divisibile per 8 vengono creati dei pixel fasulli che possono essere riempiti con diverse strategie) e per ogni blocco si applica la __DCT__ (Discrete Cosine Transform) che semplifica il segnale. Vengono quantizzati i coefficienti della DCT, cioè si arrotonda il valore dei coefficienti. Viene fatta una __scanzione zigzag__ (lossless) che trasforma il buffer due dimesionale in uno monodimensionale. si procede con l'__entropy coding__ (lossless) che comprime i dati in base alla frequenza di apparizione dei valori ovvero __coefficients encoding__ (DPCM o RLE) + __Huffman coding__.
La DCT serve a separare i coefficienti di bassa frequenza da quelli di alta frequenza, i primi sono più importanti per l'occhio umano e separandoli possono essere applicati diversi algoritmi di compressione.\
Per la quantizzazzione si usa una matrice di quantizzazione, i valori della matrice sono scelti in base alla qualità dell'immagine che si vuole ottenere (in genere si usano quelle standardizzate da jpeg).

__RLE__ (Run Length Encoding) è un algoritmo di compressione lossless che sostituisce le ripetizioni di valori in particolare, in questo caso, di 0 (che sono i valori più frequenti nella DCT) e pone un simbolo speciale per indicare che il valore è ripetuto fino alla fine del buffer.

__DPCM__ (Differential Pulse Code Modulation) è un algoritmo di compressione lossless che sostituisce i valori con la differenza fra il valore corrente e quello precedente.
___

## Video

#TODO add interlacciato ecc.

Un video è una sequenza di immagini, la frequenza di riproduzione è detta __frame rate__ (fps).\
La frequenza limite di riproduzione usata nell'industria cinematografica è di 24 fps, ma per la televisione e i monitor si usano 30 fps. Questo vuol dire che l'algoritmo di decompressione deve essere in grado di decodificare ciascun frame in meno di 1/24 di secondo. Per questo motivo gli algoritmi di compressione sono spesso asimmetrici, ci vuole tanto tempo per comprimere, molto meno per decomprimere.\
Nel caso di videochiamate invece la compressione deve essere simmetrica.\
Ormai il video viene riprodotto completamente in digitale, ma in passato veniva registrato in analogico su pellicola.\
I primi algoritmi di compressione video erano privati ora invece sono standardizzati mpeg.

I video possono essere trasmessi o a __bitrate__ variabile o costante:
- nel primo caso la compressione cercherà di mantenere tale bitrate costante, questo vuol dire che se sono presenti scene complesse il bitrate sarà alto nonostante magari la maggior parte delle scene è semplice. D'altra parte questo ci permette di determinare la banda necessaria alla trasmissione con maggiore accuratezza ed essere certi che il video non abbia cali di frame.
- nel secondo caso al contrario avremo una compressione maggiore e più efficiente ma dovremo assicurare una banda abbastanza grande per la trasmissione di frame complessi.

C'è una relazione fra bitrate e risoluzione (la densità del video), un basso bitrate può far risultare un video ad alta risoluzione a bassa risoluzione.

Nel caso di broadcasting la catena di streaming comporta una catena di compressioni.

Anche nel video abbiamo a che fare con campionamenti e quantizzazione della crominanza (come per le immagini).\
Anche per i video ci sono degli standard, le aziende private non possono proporre degli algoritmi di compressione codec e ridurre il numero di brevetti. Per questi standard puoi cambiare l'encoder ma non il decoder (a differenza dei jpeg, e di fatto nel mpeg gli algoritmi di decodifica non sanno il tipo di codifica fatta, non viene comunicata).

>__Fun fact__: nello standard mpeg-4 (quello attuale) in una vecchia versione (un vecchio standard H) erano codificati gli oggetti del video con flussi separati, ad esempio una palla da calcio aveva una sua parte di bit nel flusso dati separtata da quella di un giocatore, e le reti di trasmissioni potevano decidere come regolare la trasmissione quindi se pagavi vedevi il pallone altrimenti vedevi solo i giocatori...

Ci sono diversi contenitori di mpeg, la maggior parte morta. I più favosi per le vecchie versioni mpeg-1 e mpeg-2 era __mp3__ mentre i più famosi per mpeg-4 sono __mp4__ e __flash__. I contenitori contengono una serie di metadati che permettono l'accesso a diverse informazioni (ad esempio lo stream dell'audio e del video, la risoluzione ecc., alcuni contenitori potrebbero non fornire specifici metadati ad esempio potrebbero non separare lo stream dell'audio e del video, il decoder sarebbe comunque in grado di decomprimere il file ma non si avrebbe il flusso dei dati separati).

Per avere una compressione buona (che scenda al bit per pixel o meno) si deve _"codificare la differenza fra i fotogrammi"_. Ci sono due copressioni __intra-frame__ ovvero spaziale, interna al fotogramma, nell'__inter-frame__ codifico le differenze temporali ovvero tra un frame e un altro frame chiave (non necessariamente quello immediatamente prima), se si ha il video intergrale e non un flusso _in real time_, _live_ questa compressione può essere molto più efficiente. 

Una sequenza di fotogrammi è detta __GOP__ (group of pictures) che compone un layer. Il tipo di frame possono essere __I__ ovvero compressi intra-frame, __P__ compressi inter-frame ma solo conosciendo i frame precedenti, __B__ compressi inter-frame conoscendo tutto il video (e quindi si può trovare un miglior match e comprimerli maggiormente). Esistono anche i fotogrammi di tipo __D__ ma non li vediamo in questo corso. Un GOP è chiuso se non sono necessarie informazioni da GOP precedenti, ovvero se fondamentalemente inizia con un frame I. Un GOP più lungo potenzialmente mantiene più dettagli di un GOP più corto, perchè ci sono meno B e P frame.

#TODO finish this part and calrify GOP più grandi

Le differenze vengono memorizzate con il vettore di moto.\
Poichè quello che si ottiene è una sorta di rumore quando verà compressa l'immagine utilizzando l'algoritmo del jpeg non possiamo escludere nessuna frequenza, in particolare non possiamo escludere quelle alte.\
In un flusso mpeg i fotogrammi non sono ordinati temporalmente ma per dipendenza, se un frame B dipende da un frame P futuro sarà in ordinato conseguentemente e poi mostrati con il giusto ordine temporale.

Dentro lo standard non ci sono protocolli di recupero, se ci sono perdite nella trasmissione tecniche moderne prevedono di ricostruire l'immagine con reti neurali, ma sono software separati che non fanno parte del decoder standard.

I frame sono divisi in macroblocchi se è di tipo I viene fatta una compressione jpeg, per B e P frame si deve prima recuperare i pixel mancanti. Dalla compressione jpeg cambiano solo le tabelle di quantizzazione e di Huffman, comunque fornite dallo standard. Per la codifica di frame P e B il tempo di codifica è determinante, determina ad esempio l'area di ricerca. Il macroblocco con cui calcolo la differenza è allineato con una griglia il blocco stesso non necessariamente, ovvero si riconosce la somiglianza non tra i pixel effettivi ma tra un pixel ed un'interpolazione di di un altro pixel (un pixel non reale). 