   Superare i limiti di Vader tramite identiﬁcazione argomenti di
   discussione e analisi tramite dizionari specializzati

Vittorio Haardt, Luca Porcelli & Riccardo Fossato

May 30, 2022

**Abstract**

   L’obiettivo di questo progetto (Progetto per l’esame di *Statistica
   Spaziale ed Ambientale* dell’anno 2022, Appello del 27 giugno) \`e
   proporre una nuova strada di sviluppo per la sentiment analisi, in
   particolare centrata su una resa pi`u accurata di Vader e
   sull’individuazione di argomenti di discussione. Il progetto descrive
   le principali strategie sperimentate e descrive brevemente
   l’implementazione del pacchetto proposto.

**1** **Introduzione**

Il progetto parte dall’idea di base del superamento dei limiti di Vader,
il quale risulta troppo generale e non applicabile a contesti speciﬁci.
Un esempio del problema appena esposto si ritrova in termini quali”bull”
che in lingua quotidiana signiﬁca ”toro” ma in un contesto ﬁnanziario
signiﬁca che un determinato titolo azionario \`e destinato a crescere.
Il progetto verr`a articolato in due parti, che hanno il ﬁne di creare
la base per un sistema articolato e coeso di riconoscimento e analisi
speciﬁca di argomenti di discussione. I passi verranno aﬀrontati in
ordine temporale di esecuzione ed inﬁne verr`a proposta una visione
generale del funzionamento immaginato.

Il primo passaggio consiste nell’allenamento di dizionari speciﬁci per
ogni argomento, partendo dalla base di Vader. Il problema viene
aﬀrontato sia con l’utilizzo di modelli supervisionati che non
supervisionati. Si usa un modello logistico per capire le parole pi`u
importanti (supervisionato). Successivamente si \`e optato per un word
embedding per trovare le parole pi`u simili a quelle ottenute
precedentemente (non supervisionato). Le parole ottenute verranno poi
messe in un dizionario assegnando un punteggio scelto arbitrariamente.
Come ultimo passo si \`e attuata una valutazione tra i dizionari di
partenza e quelli modiﬁcati per capire se il cambiamento porti ad un
risultato sensato.

Il secondo passo aﬀrontato consiste nella creazione e valutazione di un
modello che sia in grado di cogliere il contesto di cui si parla. Il
modello ottimale che viene scelto, non necessariamente corrisponde al
modello ottimale in generale, si \`e scelto piuttosto un modello
semplice e facilmente replicabile. Questa seconda fase, ha lo scopo non
tanto di trovare il modello ottimale per la classiﬁcazione di argomenti,
dato che modelli pi`u complessi potrebbero gestire meglio un numero di
target anche superiore a quello usato, quanto pi`u uno scopo
dimostrativo per le potenzialit`a dell’idea di partenza.

In generale il lavoro svolto vuole avere la funzione di ispirare un
punto di partenza per un lavoro di specializzazione di Vader il quale
nonostante la sua utilit`a risulta molto generale e poco adeguato per
argomenti di discussione con lessici speciﬁci. Si immagina quindi in
prospettiva un sistema coeso ed articolato per la sentiment analysis, o
pi`u in generale per l’analisi dei testi, che sia in grado di cogliere
l’argomento o gli argomenti trattati in testi speciﬁci ed eﬀettuare
analisi riferendosi ad un dizionario Vader modellato per cogliere tutte
le sfumature dell’argomento in questione.

La valutazione dei risultati avverr`a per comparazione con Vader, ci si
attende che i dizionari specializzati abbiano un accuratezza maggiore
nel capire il sentiment, tuttavia se si dovesse giungere al risultato
disatteso, si arriverebbe all’interessante conclusione secondo la quale
si necessiti di modelli pi`u complessi o addirittura di interventi
manuali per ottenere dizionari specializzati.


**1.1** **Vader**

   Per poter partire da una base autorevole e consolidata, si \`e scelto
   di utilizzare il tool , ovvero il tool rule-based per la sentiment
   analisi pi`u eﬃcace (in particolare per i social media). Il quale
   come gi`a detto in precedenza verr`a aggiornato e manipolato a
   seconda dell’argomento trattato, in modo da specializzarsi il pi`u
   possibile.

**1.2** **Lime**

   Crediamo fortemente che l’expleinability del progetto vada messa in
   primo piano, con un doppio scopo. Il primo \`e quello di comprensione da
   parte degli sviluppatori dei problemi altrimenti non visibili. Il
   secondo \`e quello di poter fornire una trasparenza tale da poter far
   comprendere all’ipotetico utilizzatore del sistema come i testi vengono
   classiﬁcati e valutati. Per la parte di XAI verr`a utilizzato per la sua
   semplicit`a ed intuibilitá.

**1.3** **PyPi**

   Poich´e il progetto ha una prospettiva di funzionamento reale si \`e
   scelto di pubblicare il progetto su per rendere il pacchetto Python
   realmente utilizzabile (almeno nella sua forma primordiale). Inoltre
   si \`e usato servizio di hosting per progetti software, , per
   mostrare il funzionamento del pacchetto ed il relativo progetto da
   cui proviene. I dettagli del funzionamento verranno esplicitati in
   una sezione apposita pi`u avanti.

**2** **Dati**

I dati utilizzati provengono da diversi dataset provenienti dalla
nota piattaforma . Per ogni argomento sono stati selezionati dei
dataset separati e speciﬁci. In linea generale i dataset sono delle
review fatte sui vari argomenti di discussione, questa tipologia di
testo risulta cruciale ai ﬁni dell’analisi per la creazione di
implementazioni per Vader. L’importanza \`e data dal fatto che \`e
possibile identiﬁcare la positivit`a e la negativit`a della sentiment
dei commenti basandosi sul voto ad essi associato, cosi da poter
attuare delle survey sensate. Procediamo ora alla rassegna delle
propriet`a dei dati usati.

La parte di interesse dei dati scaricati sono i testi i quali,
verranno raggruppati sotto 4 argomenti (che vedremo a breve). Per
quanto riguarda il primo modello si utilizzeranno solamente i testi
relativi di volta in volta ad un argomento diverso e le relative
label ottenute dalle votazioni (verranno successivamente spiegate nel
dettaglio per ogni dataset). Invece il dataset per il secondo modello
si compone di una colonna ”testo”e una colonna target ”argomento”, e
comprende al suo interno un unione di tutti i quattro dataset.

L’obbiettivo di partenza nella ricerca dei dati era di avere a
disposizione circa 40.000 righe per argomento. Di cui successivamente
il 50% viene utilizzato per la creazione dei dizionari specializzati
ed il restante viene usato per il modello di classiﬁcazione. Vediamo
ora gli argomenti nel dettaglio.

**Argomenti**

   1. *Food*
   Il dataset contiene review di prodotti alimentari, lasciate dai consumatori
   sul sito di Amazon, con un relativo ranking che spazia da 1 a 5. 
   Per la creazione della label sono state considerate le review con punteggio
   1 o 2 come "Negative", quelle con 4 o5 come "Positive". 
   Quelle con punteggio 3 sono state scartate poiché non di interesse per 
   l'analisi, è stato considerato 3 un voto troppo volatile 
   che rischia di raggruppare in una teorica categoria "Neutral" recensioni 
   positive e negative, andando di fatto ad indebolire l'analisi.

   2. *Electronics*
   Il dataset contiene review di prodotti elettronici, lasciate dai consumatori 
   sul sito di Amazon, con un relativo ranking che spazia da 1 a 5. 
   Per la creazione di label sono state considerate le review con punteggio 1 o 
   2 come "Negative", quelle con 4 o 5 come "Positive".
   Le review con punteggio 3 sono state scartate per motivi analoghi a quelli 
   mostrati per il dataset precedente.

   3. *Disneyland*
   Il dataset contiene review dei tre famosi parchi di divertimento di 
   Disneyland, ovvero quelli di Parigi, della California e di Hong Kong. 
   Le review sono state lasciate dai clienti sul sito di recensioni Trip Advisor,
   con un relativo ranking che spazia da punteggi di 1 a 5. Per la creazione 
   di label sono state considerate le review con punteggio 1 o 2 come "Negative",
   quelle con 4 o 5 come "Positive". Le review con punteggio 3 sono state 
   scartate per motivi analoghi ai dataset precedenti.

   4. *Finance*
   Il dataset contiene review e tweet riguardanti argomenti finanziari, 
   il dataset completo è stato ottenuto unendo i tre dataset riportati sopra.
   Tutti e tre i dataset sono già dotati di una label che ne indica 
   la positività o la negatività. 


Si é cercato di selezionare argomenti il più possibile eterogenei. I
dataset selezionati ovviamente non forniscono una visuale completa
dell’argomento. Il lavoro svolto non vuole essere deﬁnitivo ma vuole
essere un punto di partenza per poter sviluppare idee in senso di
miglioramento e specializzazione di Vader.

**3** **Preprocessing**

La pulizia dei testi gioca un ruolo fondamentale per i risultati
dell’analisi, specialmente trattando testi provenienti da recensioni e
tweet, i quali spesso risultano sporcati da link, tag e hastag. Nel caso
dei dataset selezionati, questo tipo di *preprocessing* era gia stato
svolto, lasciando semplicemente il testo ripulito. Il *preprocessing*
\`e leggermente diverso per le due fasi del progetto, per questo motivo
verranno spiegati i passaggi in modo separato.

La pulizia attuata ugualmente per entrambe i modelli, ricopre la parte
precedente all’avvio delle analisi in ”Python”. Inizialmente si \`e
attuata una *tokenization* separando le parole con spazi ed eliminando
tutto ci`o che non \`e una parola uno spazio o un numero, in seguito si
sono rese le parole minuscole con un *lowercase*. Per ogni singola
parola \`e stato poi applicata la *lemmatization* per ridurre le forme
ﬂesse di una parola alla loro forma canonica. Solamente per quanto
riguarda il secondo modello, ovvero quello per la classiﬁcazione per
argomento, sono state eliminate le *stopwords*, le quali non sono
informative ai ﬁni dell’analisi.

Avendo ﬁnito questa fondamentale fase \`e possibile ora procedere con
l’esplicazione dei modelli usati e al loro funzionamento.

**4** **Parte 1: Specializzazione di Vader**

Questa prima parte del progetto ha lo scopo di identiﬁcare le parole
ritenute pi`u importanti per i vari argomenti al ﬁne di modiﬁcarne il
peso all’interno del dizionario di partenza, per creare dizionari
plasmati appositamente per gli argomenti trattati. Si vuole identiﬁcare
lo stato d’animo del creatore dei testi, in particolare il target \`e
”Positive” e ”Negative” rispettivamente se il testo \`e giudicato
positivamente o negativamente dallo score, come si \`e visto in fase di
descrizione dei dati, al ﬁne di valutare l’eﬃcacia dei cambiamenti
applicati ai dizionari. Come riportato precedentemente si \`e presa una
met`a dei dati per identiﬁcare le parole pi`u frequenti e l’altra met`a
(la quale viene anche usata per la parte relativa alla classiﬁcazione
degli argomenti) per valutare il comportamento dei nuovi dizionari
specializzati.

**4.1** **Identiﬁcazione parole**

Al ﬁne di identiﬁcare le parole pi`u frequenti si \`e usata una *bag of
words*. La procedura si \`e svolta usando *count vectorizer* per
selezionare solamente le 2000 parole pi`u importanti dei testi separati
per argomento. Quindi \`e stato costruito un dataset ad hoc contenente
testi con relativi pesi (di frequenza normalizzata) delle parole scelte.
Essendo state scelte solamente 2000 parole, saranno presenti, in questa
fase, testi con peso 0 dato che non contengono nessuna delle parole
selezionate.

**4.2** **Descrizione modello e modello surrogato**

Al ﬁne di avere delle performance migliori e ridurre l’overﬁtting sui
dati si \`e scelto di adoperare una metodologia usante un modello
principale per spiegare il target e un suo surrogato che fosse pi`u
leggibile e che si adattasse al meglio per assegnare dei pesi alle
parole.

Per la scelta del modello, cos`ı detto, principale sono stati valutati
due modelli, una *Random Forest* e un *Naive Bayes*. Il modello
giudicato migliore \`e stato scelto per i suoi parametri maggiori nel
dataset con le performance peggiori, tuttavia i modelli sono
paragonabili.

La *Random Forest* \`e quindi il modello scelto, i cui parametri di
tuning sono stati trovati attraverso una *Grid Search* di volta in volta
rilanciata per ogni dataset. Per i dati di training si sono presi il 70%
e il restante 30% \`e stato usato come validation. Nel caso si fosse
interessati ai parametri in particolare, si rimanda alla sezione LINK in
fondo che a sua volta rimanda allo script originale. In generale il
modello ha delle performance accettabili su tutti i dataset come
osservabile da tabella (Table 1).

=========== ====================== =======================
Argomenti   Accuracy Random Forest    Accuracy Naive Bayes
=========== ====================== =======================
Food        0.82                   **0.85**
Electronics **0.87**               0.85
Disneyland  0.82                   **0.86**
Finance     **0.79**               0.75
=========== ====================== =======================

..

   Table 1: Tabella che mostra i livelli di accuracy ottenuti dai
   modelli a confronto sui vari dataset

Prima di usare il modello surrogato si \`e rilanciato il modello
principale su tutti i dati e sono state salvate le prediction.
Successivamente si \`e scelto di applicare un modello surrogato per
spiegare il modello principale, da cui poi sono stati derivati i pesi.
Il modello in questione \`e un *Logistic Model* con i parametri di
default. Per adattare questo modello si \`e usato come target le
prediction salvate precedentemente.

Per assegnare in ﬁne i pesi alle parole, sono stati usati i coeﬃcienti
ottenuti dal modello surrogato, che sono stati riadattati al metodo di
pesi congruente con Vader.

**4.3** **Assegnazione pesi**

Come appena esplicitato i coeﬃcienti del modello surrogato sono stati
usati come base per poter applicare dei pesi per il dizionario rule
based. Sono state attuate diverse prove di metodologia per applicare i
pesi al meglio, le strategie in questione comportano l’assegnazione di
pesi da -4 a 4 a seconda dei valori dei coeﬃcienti relativi alle parole.

Il primo metodo (metodo 1) consiste nel assegnare punteggi a fasce,
come segue.

+------------+----------+----------+------------------+---------------+-------+----------+
| coeﬃciente | *≤ −*\ 2 | *≤ −*\ 1 | *≤ −*\ 0\ *.*\ 5 | *≥* 0\ *.*\ 5 | *≥* 1 |    *≥* 2 |
+============+==========+==========+==================+===============+=======+==========+
| punteggio  |    -4    |    -3.5  |    -2.5          |    2.5        | 3.5   |    4     |
+------------+----------+----------+------------------+---------------+-------+----------+

Il secondo metodo (metodo 2) consiste solamente nell’assegnare i pesi
estremi, secondo come mostrato di seguito.

========== ================ ================
coeﬃciente *≤ −*\ 0\ *.*\ 6    *≥* 0\ *.*\ 6
========== ================ ================
punteggio     -4               4
========== ================ ================

..

   Inﬁne il terzo metodo (metodo 3) \`e un incrocio dei primi due, come
   visibile di seguito.

========== ================ ======== ============= ========
coeﬃciente *≤ −*\ 0\ *.*\ 5 *≤ −*\ 1 *≥* 0\ *.*\ 5    *≥* 1
========== ================ ======== ============= ========
punteggio      -4               -3       3             4
========== ================ ======== ============= ========

Dopo queste prove per l’assegnazione di pesi si \`e optato per
selezionare solamente le parole con valori”estremi” ovvero maggiori di
0.6 e minori di -0.6, alle quali si \`e applicato un peso
rispettivamente di 4 e -4.

Si é osservato che tra le tre alternative proposte il metodo 1 e il
metodo 2 fossero preferibili al metodo 3. Non essendoci diﬀerenze
signiﬁcative tra i metodi fatta eccezione che per il dataset riguardante
l’argomento Food, si \`e scelto di usare il metodo 2. Si possono
osservare dalla tabella (Table 2) i valori di adattamento.

======== =========== =========== =========== ==============
          Food        Electoinic  Disneyland     Finance
======== =========== =========== =========== ==============
Metodo 1  80.4%       82.3%       **83.8**\ %    **63.9**\ %
Metodo 2 **86.9**\ % **83.0**\ % 83.3%          63.1%
Metodo 3 81.3%       82.9%       83.7%          63.5%
======== =========== =========== =========== ==============

..

   Table 2: Tabella che confronta il livello adattamento dei vari metodi
   sui vari dataset

Con i pesi risultanti dall’operazione appena vista, sono stati creati i
dizionari specializzati per ogni argomento, che verranno ora valutati
per le loro performance rispetto ai dizionari di partenza.

**4.4** **Confronto con Vader**

Da questo punto in avanti ci si riferisce ai dizionari specializzati
come a *Vader New* (V.N.). \`E ora necessario valutare se eﬀettivamente
il passaggio da Vader a i V.N. abbia portato a qualche sorta di
miglioria per la valutazione del sentimento. Quello che ci si aspetta
\`e che, essendo i V.N. plasmanti ad hoc sugli argomenti trattati, siano
in grado di portare ad analisi pi`u speciﬁche e quindi ad avere un
accuratezza maggiore per identiﬁcare il sentimento dei testi. Nel caso
contrario invece ci si interrogherebbe sulle cause di un mancato
miglioramento, valutando altri metodi per l’assegnazione di pesi oppure
valutando l’insuperabilit`a di Vader.

Per valutare l’accuratezza di Vader e dei V.N., \`e stato preso il
valore di compound risultante e si \`e etichettato il testo come
”Positive”, nel caso quest’ultimo fosse maggiore di 0, e ”Negative”
altrimenti. Successivamente si sono confrontate queste etichette basate
sul compund con la loro controparte reale, ottenuta come spiegato in
precedenza. Come ci si sarebbe aspettati, vedendo la tabella (Table 3)
si osserva che per ogni argomento V.N. risulti pi`u preciso di Vader di
svariati punti in percentuale.

========== ===== ============
Argomenti  Vader    Vader New
========== ===== ============
Food       72.1%    **86.9%**
Electronic 75.5%    **83.0%**
Disneyland 82.2%    **83.3%**
Finance    49.7%    **63.1%**
========== ===== ============

..

   Table 3: Tabella che confronta il livello di adattamento in
   percentuale tra Vader e Vader New

Il risultato ottenuto mostra come lo scopo del progetto possa
eﬀettivamente portare ad un miglioramento sostanziale di Vader
attraverso la sua specializzazione, portando ad analisi sempre pi`u
precise su argomenti sempre pi`u capillari.

**4.5** **Word embedding e confronto con modello precedente**

Si é scelto di valutare se l’utilizzo di un *word embedding* potesse
ulteriormente far crescere le performance dei V.N. rispetto alla loro
forma classica. Sono state valutate due alternative chiamate
rispettivamente *Vader New four* e *Vader New one change*.

In generale quello che svolgono queste due modiﬁche \`e, grazie al word
embedding, la modiﬁca dei pesi per le parole maggiormente simili a
quelle modiﬁcate in precedenza. Si \`e optato per l’utilizzo del modello
non supervisionato con *fastText* piuttosto che *word2vec* poich´e
considerato pi`u eﬃciente. *V.N. four* in particolare seleziona le
parole con punteggio di similarit`a maggiore di 0.99, rispetto alle
parole contenute in V.N., e assegna a queste parole un valore di 4 o -4
in base al valore positivo o negativo delle parole a cui sono state
associate. Invece, *V.N. one change* seleziona le parole per cui
cambiare il peso in maniera analoga a *V.N. four*, ma cambia i pesi
sommando o sottraendo 1 rispetto al valore che queste parole hanno in
Vader, in base al valore positivo o negativo delle parole a cui sono
state associate.

Come riportato dalla tabella (Table 4) si osservano le performance dei
vari metodi di V.N., per scegliere la metodologia pi`u appropriata per
ogni metodo.

========== ========= ========== ==================
Argomenti  Vader New V.N. four     V.N. one change
========== ========= ========== ==================
Food       **86.9%** 81.86%        81.86%
Electronic 83.0%     83.08%        **83.23%**
Disneyland **83.3%** 83.12%        83.12%
Finance    63.1%     **70.15%**    43.36%
========== ========= ========== ==================

Table 4: Tabella che confronta il livello di adattamento tra Vader New e
le sue versioni che usano word embedding

Avendo valutato le performance di adattamento si \`e scelto di non
applicare word embedding agli argomenti Food e Disneyland, invece per
quanto riguarda Electronic la scelta migliore ricade su *V.N. one
change* ed inﬁne per Finance si osserva un netto miglioramento in
confronto agli altri due metodi per quanto riguarda *S.V. four*.

I dizionari specializzati sono ora completi e pienamente utilizzabili
per analisi sui testi per i relativi argomenti, come visto durante i
passaggi che hanno portato al risultato, i dizionari specializzati
produrranno analisi pi`u accurate di quanto faceva Vader. Si vuole ora
riportare l’attenzione su come, indipendentemente dalle scelte fatte sui
metodi di assegnazione pesi e sull’utilizzo del word embedding, i
risultati dei dizionari specializzati comunque sorpassano quelli di
Vader per praticamente tutte le combinazioni di scelte su tutti gli
argomenti.

Un esempio pratico di come i dizionari specializzati abbiano migliorato
Vader si riporta una delle frasi dell’argomento Electronic.

”\ *Faulty on arrival. The wire for one channel wasn’t ...*\ ”

La parola *faulty* (ovvero non funzionate) assume un connotato
generalmente pi`u negativo nel linguaggio naturale quando si parla di
oggetti elettronici. Dato che l’argomento in questione comprende
recensioni di oggetti elettronici vediamo come il peso di questa parola
sia passato da -1.8 per Vader ad un-4 per Specialized Vader. Facendo
passare l’intera frase da un valore di compound di -0.32 a uno di -0.90.

**5** **Parte 2: Classiﬁcazione argomenti**

Come detto in precedenza il secondo modello si preﬁgge lo scopo di
riuscire a classiﬁcare dei testi secondo gli argomenti di cui parlano.
Il modello scelto ha quindi ovviamente la variabile target multi-classe,
riferita agli argomenti sopra riportati. In questo paragrafo ne verranno
descritte le principali caratteristiche. Del 50% del totale dei dati
preso in precedenza, si \`e optato per una proporzione di 70% e 30%
rispettivamente per i dati di training e di test.

**5.1** **Descrizione modelli**

Al ﬁne di avere delle performance classiﬁcative ottimali si sono
valutati due diversi modelli. I modelli in questione sono *Naive Bayes*
e *Decision Tree*. Per il *Naive Bayes* si \`e optato per un valore di
alpha di 0.1. Per il *Decision Tree* si \`e optato per il criterion di
Gini, un albero con maxleafnodes senza limite e una maxdeap anche essa
illimitata, cos`ı da lasciare il modello il pi`u lasso possibile. Tutti
i parametri sono stati tunati per selezionare quelli ottimali.

**5.2** **Modello vincente**

La metrica di interesse principalmente osservata \`e l’accuracy, ma
comunque i modelli tendono ad avere alti valori anche per le altre
metriche. Osservando le performance, il modello vincente \`e risultato
il *Naive Bayes*, con un livello di accuracy di 0.95 (rispetto ad un
0.88 per l’albero). Dunque la classiﬁcazione multitarget

con il ﬁne di individuare l’argomento di discussione sar`a appunto
aﬃdata al *Naive Bayes* con i parametri precedentemente selezionati.

É tuttavia necessario precisare che questo modello risulti ottimale per
questo tipo di classiﬁcazione di solamente quattro argomenti. Nel caso
di sistemi di classiﬁcazione di argomenti di discussione pi`u ampi con
numeri di alternative di target estremamente maggiori, il modello
ottimale verosimilmente sar`a un modello con una complessit`a maggiore,
come ad esempio una rete neurale. Viene quindi ricordato che il modello
viene creato, non tanto per la sua eﬀettiva utilit`a, ma piuttosto per
mostrare la possibilit`a di sviluppo di un sistema coeso che identiﬁchi
l’argomento di discussione e rimandi ad uno speciﬁco dizionario. Lo
scopo \`e quindi il poter ispirare alla creazione di dizionari speciﬁci,
per tutti gli argomenti di discussione, e creare un sistema che
automaticamente riconosca l’argomento e reindirizzi al dizionario
specializzato associato.

**5.3** **Explainability**

L’explainability, come precedentemente precisato, \`e stata aﬃdata
interamente a Lime. L’importanza di questa ultima fase non \`e da
sottovalutare, poich´e per poter fare realmente aﬃdamento su un modello
di classiﬁcazione \`e necessario conoscerne profondamente il
funzionamento ed il metodo di scelta, cos`ı da poter applicare migliorie
e poter guadagnare la ﬁducia dell’utente non esperto.

Campionando casualmente tra i diversi testi, si \`e osservato come il
modello classiﬁchi sulla base di parole realmente signiﬁcative e come al
contrario non si basi su parole generali, le quali sarebbero applicabili
a qualunque contesto. 

**6** **Funzionamento congiunto modelli**

Il funzionamento congiunto dei modelli \`e stato largamente introdotto
nelle sezioni precedenti. Per riassumere, si riporta come le due parti
di studio, ovvero la creazione dei Vader New e la creazione di un
modello che sia in grado di identiﬁcare l’argomento di discussione,
siano pensate come parti distinte di un unico processo. Ovviamente, come
gi`a precisato, lo studio fatto non ha lo scopo di essere in nessun modo
deﬁnitivo, bens`ı vuole fungere come punto di partenza e ispirazione.

É stata creata quindi una funzione che ricevendo un testo qualsiasi
(ovviamente limitandoci ai nostri quattro argomenti) sia in grado di
riconoscerne con precisione l’argomento e quindi aﬃdare una sentiment
analysis, che produca un punteggio di compund, al dizionario adeguato
per l’argomento. Grazie a funzioni che lavorino come quella appena
esplicitata \`e possibile fornire un vero salto in avanti per
l’accuratezza e la reliability di un sistema come Vader, che, per quanto
aﬃdabile e utile, necessita di un’evoluzione poich´e rimane troppo
generale, portando ad analisi poco aﬃdabili per testi riguardanti
argomenti speciﬁci e che quindi hanno un linguaggio speciﬁco.


**7** **Un nuovo package Python: ”vadernew”**

In questa sezione viene presentato velocemente il pacchetto introdotto
frutto delle analisi fatte. ”vadernew”`e utilizzabile per analisi sui
testi per gli argomenti sopra riportati. Le analisi utilizzanti questo
pacchetto al posto di Vader, come spiegato in precedenza, saranno pi`u
precise ed aﬃdabili.

Si inizia installando il pacchetto ”vadernew” tramite pip install

   In [1]: ! pip install vadernew

   | Looking in indexes: https://pypi.org/simple,
     https://us-python.pkg.dev/colab-wheels/public/simple/ Collecting
     vadernew
   | Downloading vadernew-2.0.tar.gz (208 kB)
   | \|--------------------------------\| 208 kB 4.9 MB/s
   | Requirement already satisfied: requests in
     /usr/local/lib/python3.7/dist-packages (from vadernew)
     (2.23Requirement already satisfied: certifi>=2017.4.17 in
     /usr/local/lib/python3.7/dist-packages (from requeRequirement
     already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in
     /usr/local/lib/python3.7/distRequirement already satisfied:
     idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from
     requests->vRequirement already satisfied: chardet<4,>=3.0.2 in
     /usr/local/lib/python3.7/dist-packages (from requesBuilding wheels
     for collected packages: vadernew
   | Building wheel for vadernew (setup.py) ... done
   | Created wheel for vadernew:
     filename=vadernew-2.0-py2.py3-none-any.whl size=201181
     sha256=73123c38b4d Stored in directory:
     /root/.cache/pip/wheels/6e/61/92/b3cf7e69a81abfdb3186292b908158e2a0590c7871fa6adSuccessfully
     built vadernew
   | Installing collected packages: vadernew
   | Successfully installed vadernew-2.0

Nel pacchetto sono contenuti separatamente i dizionari e le funzioni
relative ai 4 argomenti, importabili singolarmente.

   In [2]: from vadernew import vader_food

   In [3]: from vadernew import vader_electronic

   In [4]: from vadernew import vader_disneyland

   In [5]: from vadernew import vader_finance

Di fatto le funzioni contenute non variano da quelle di Vader fatto
da cjhutto, per le quali si invita a guardare la pagina GitHub
relativa. Il cambiamento apportato riguarda i dizionari utilizzati,
ovvero quelli prodotti dallo studio fatto e speciﬁci per gli
argomenti. Menzioniamo in partilcolare due funzioni ripetibili per
ogni argomento.

Ovvero due funzioni sostitutive, rispettivamente di SentiText() la
quale identiﬁca le propriet`a a livello di stringa rilevanti per il
sentiment del testo di input, e SentimentIntensityAnalyzer() che
invece assegna un punteggio di intensit`a del sentimento alle frasi.
Le due funzioni sono rinominate per ogni argomento.

   In [6]: from vadernew.vader_food import Food_ST, Food_SIA

   In [7]: from vadernew.vader_electronic import Electronic_ST, Electronic_SIA

   In [8]: from vadernew.vader_disneyland import Disney_ST, Disney_SIA

   In [9]: from vadernew.vader_finance import Finance_ST, Finance_SIA

Per il funzionamento delle funzioni ST si invita a guardare la guida
di Vader classico per SentiText(), dato che non sono il punto dei
cambiamenti apportati.

Ora vediamo il funzionamento delle funzioni SIA e come con una sua
sotto funzione troviamo i valori dicompund. I valori che si ottengono
sono pi`u accurati, dato che fanno riferimento ai dizionari speciﬁci.
Per tutte le sotto funzioni chiamabili si fa sempre riferimento alla
guida di VaderSentiment, ricordiamo che il funzionamento del
pacchetto vadernew \`e in tutto e per tutto lo stesso di quello di
VaderSentiment, l’unico cambiamento \`e la speciﬁcit`a dei dizionari
utilizzati.

   In [11]: sentence = "Just an example" 
   
   analyzer = vader_finance.Finance_SIA() 
   
   vs =analyzer.polarity_scores(sentence) 
   
   print("*{*:<13\ *} {}*".format(sentence, str(vs))

   Out [11]:Just an example *{*\ ’neg’: 0.0, ’neu’: 0.286, ’pos’: 0.714, ’compound’: 0.7184\ *}*

Inconclusione si invita a provare e sperimentare le potenzialit`a del
pacchetto, il quale, si ricorda ancora una volta, funge solamente da
showcase di come una specializzazione di VaderSentiment conduca ad
analisi pi`u accurate.

**8** **Conclusioni**

Prendendo in rassegna tutti i passaggi del progetto, abbiamo visto come,
da risultati attesi, apportare modiﬁche al ﬁne di specializzare Vader su
argomenti di discussione porti solamente a miglioramenti. In generale
è doveroso sottolineare il risultato osservato nelle sezioni 4.4 e
4.5, secondo il quale, indipendentemente dai metodi di assegnazione dei
pesi e dai modelli utilizzati per assegnarli, Vader risulti sempre
peggiore rispetto alle sue versioni specializzate. Questo risultato
porta alla conclusione per cui Vader nonostante sia stato un sistema
innovativo ed estremamente e�cace, ormai \`e facilmente superabile, o
per meglio dire migliorabile.

Come conclusione si invita a cogliere l’input proposto da questo
progetto, ovvero lo sviluppo, partendoda Vader di un sistema che
riesca ad identiﬁcare l’argomento di discussione testo per testo,
frase per frase e che utilizzi dei dizionari specializzati al ﬁne di
avere analisi performanti ed accurate.

Come ultima nota consigliamo, a chiunque abbia intenzione di
applicare delle analisi testuali, come unasentiment analisi, su dei
testi di cui si conosce gi`a in partenza l’argomento di discussione,
di prendere dei dataset con le caratteristiche simili a quelle viste
in precedenza e di addestrare un dizionario specializzato per
l’argomento. Il dizionario risultante, utilizzato come illustrato nel
progetto, indipendentemente dall’attenzione riposta per la scelta dei
modelli e dell’assegnazione dei pesi, dovrebbe comunque risultare
pi`u performante di quello generale utilizzato da Vader.
