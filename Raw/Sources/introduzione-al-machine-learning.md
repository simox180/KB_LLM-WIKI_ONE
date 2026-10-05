---
Title: Introduzione al Machine Learning
Reference: Raw/Files/scuolaMarche2025.pdf
Created: 2026-10-05
Processed: true
tags:
  - source
---

# Introduzione al Machine Learning

Trascrizione automatica dal PDF originale; la struttura delle pagine e conservata nei marcatori.

===== PAGE 1

Introduzione al Machine Learning
Guido Tiana, Dipartimento di Fisica, Università degli Studi di Milano
Basi per chi non ne sa niente o ne sa poco
Buone pratiche
Sviluppi recenti
Laboratorio pratico (altre 2h) 
Di cosa parliamo:
Struttura:
Metodi non-deep
Metodi deep usando la rete feed-forward come modello
Panoramiche delle architetture

## Pagina 2

Obbiettivi del ML
supervised learning
{xi,yi}given
and a        predictxk yk
unsupervised learning
reinforcement learning
da Wikipedia
optimization problem when the 
function to be optimized is not 
completely known.
Session 1:
Forecasting e ottimizzaizone
Session 2:
Language models, artiﬁcial 
vision
Session 2/3:
Teoria del reiforcement L.
generative models
dimensional reduction

## Pagina 3

Metodi di learning non-deep


## Pagina 4

Importanza del non-deep ML
Ci sono situazioni in cui il numero P di dati è piccolo rispetto al 
dimensione N dell'input.
Se P è molto piccolo, impossibile perche non abbiamo abbastanza 
informazione.  
Se P è piccolo, il risultato dipende dall'algoritmo. Esempio: medicina.
Se P è grande, vai coi metodi deep.....!
P=3
clustering:
Spesso hanno soluzioni esatte (non ottimizzazioni numeriche),
dipendono da un numero piccolo di parametri, sono robusti.
Pimpossibile non-deep deep

## Pagina 5

Importanza del non-deep ML
Supervised learning:
supported vector machines (SVM), random forest, XGboost, etc.
classiﬁcation vs regression
Unsupervised learning: 
clustering, hierarchical clustering
source: datacamp.com
Decision tree

## Pagina 6

Esempio di non-deep ML: predizioni mediche
tipico P ~ 100
RNA-seq
age          56
sex          M
smoker    no
drinker     no
..... 
personal info
response to chemoterapy 
(complete/partial/progress)
dimensional reduction (PCA) + cascade prediction ( svm + random forest )
training test

## Pagina 7

Esempio di non-deep ML: predizioni mediche
Spesa medica italiana = 126 BEuro
Spesa medica  oncologica italiana = 20 BEuro
Costo chemioterapa = 1.8 kEuro (molto variabile)
Costo radioterapia = 12-24 kEuro
Mercato importante, ma molto regolato.
fonte: Fondazione Umberto Veronesi


## Pagina 8

Support vector machine (SVM)
Considera il caso di dover trainare un modello lineare sulla base di (xp, yp) con  yp=±1.
Il caso più semplice è quando esiste un iperpiano 
che separa i punti con yp diversi. Potrebbero esisterne inﬁniti. Scegliamo quello che 
massimizza il margine d,
wTx−b=0
wTx−b≥d for yp=1 
wTx−b≤−d for yp=-1 
Se moltiplico W per una costante aumento il margine in modo banale. Allora cerco W per cui
wTx−b≥1 for yp=1 
wTx−b≤−1 for yp=-1 
per il piu piccolo valore possibile di |W|.
Operativamente, minimizzo |W|2 sotto le condizioni 
yp(wTxp−b)≥1
Estendibile a kernel nonlineari....

## Pagina 9

Principal component analysis (PCA)
Assumiamo di avere P dati d-dimensionali, xji  con i=1...d, j=1...P
La matrice di covarianza è
i cui elementi diagonali sono le varianze di ogni feature i. Vogliamo una trasformazione lineare (una roto-dilatazione) 
che massimizzi la varianza in una direzione. Questa si può ottenere attraverso una singular-value decomposition
Σ= 1
P−1XTX
X=USVT
dove S è una matrice dxP diagonale, per cui
Σ=(USVT)2
P−1=VΛVT
Le proiezioni di X nel nuovo spazio sono Y=XV e le loro varianze sono le componenti ("autovalori") di 𝛬. 
Selezionando gli autovalori piu grandi si selezionano le proiezioni di maggiore variabilità delle features dei dati.
E' lineare !!!!
x1
x2

## Pagina 10

Metodi di Deep Learning


## Pagina 11

Reti neurali artiﬁciali
Caso standard supervised: rete feed-forward ⃗y=fW(⃗x)
input
output
hidden layers
x1
x2
x3
...
y1
y2
...
h1(I)
h2(I)
...
h1(II)
...
...
w(I)
ij
percettrone
h(n+1)
j =σ(∑i
wn
jih(n)
i)
h(n)
1
h(n)
2
...
h(n+1)
j
Teorema di rappresentazione universale: un network feedforward con almeno un hidden layer, attivazioni nonlineari ed un numero arbitrario di nodi può 
approssimare qualunque funxione f(x) con accuratezza arbitraria [Hornik, 1989]. 
Minimizzazione della loss: dati               minimizzare ℒ=
P
∑k=1
|⃗yk−fW(⃗xk)|{xi,yi}

## Pagina 12

Scelta delle funzioni di attivazione
Deve essere (almeno una) nonlineare, altrimenti:
- non vale il teorema di rappresentazione universale
- non ha senso fare reti deep
- stai facendo PCA
Spesso ReLU per strati intermedi perchè aiuta il training.
Lei è convessa (e nonlineare), ma la composizione di funzioni convesse (es. un layer 
e MSE) non è convessa. 
 
Esempio: f(x)=-sqrt(x), g(x)=x^2 ==> f(g(x))=-|x| è concava.
Combinazione di funzione convessa e funzione non-decrescente è convessa. MSE è 
convesso.
Discorso a parte per softmax:
(versione morbida di argmax)
yi=eβxi
∑jeβxj

## Pagina 13

Scelta della loss
Generalmente le richieste minime sono che sia continua, derivabile e uguale a zero se                        . È importante per determinare (insieme alle funzioni di attivazione) 
quant'è facile il training
ℒ=
P
∑k=1
[yk−fW(xk)]2
ℒ=
P
∑k=1
|yk−fW(xk)|
Problemi di classiﬁcazione
Scelte tipiche, per problemi di regressione
loss L2 
loss L1  
W
ℒ
convesso
campo da golf
frastagliato
esempio:ℒ=1−1
P
P
∑k=1
δyk,f(xk)
cross-entropy
cross-entropy (binary case ±1)
hinge loss (binary case ±1)
no L2
yk=fW(xk)∀k
ℒ=−
P
∑k=1
C
∑c=1
δyk,cloge(fw(xk))c
∑de(fw(xk)d
ℒ=
P
∑k=1
log(1+e−2ykfw(xk)))
estimatore maximum-likelihood quando gli errori sono gaussiani, quindi enfatizza gli 
outliers (non gaussiani);  convessa.
maximum-likelihood quando errore segue distribuzione di Laplace, non derivabile in 0
convessa, deﬁnita come informazione mancante
(non continua)
ℒ=∑k
max[0,1−ykf(xk)]

## Pagina 14

Regolarizzatori
ℒ′ =ℒ+λ∑i
wα
i con tipicamente 𝜶=1,2
Vantaggi:
- contrasta overﬁtting
- aumenta sparsità
- di conseguenza, migliora la generalizzazione (il sistema non impara a memoria)
- elimina alcune simmetrie banali (es. hinge loss)
- elimina divergenze
considera                                                   con (x,y)=(1,1); i pesi tenderebbero a divergere...
Svantaggi:
- bisogna aggiustare 𝝀
ℒ=(y−tanh(wx))2

## Pagina 15

Algoritmi di minimizzazione
Gradient descent
⃗w(t+1)=⃗w(t)−γ(t)∇ℒ(⃗w(t))
ℒ
[∇ℒ(⃗w(t))]i=∂ℒ(⃗w(t))
∂wi
Il learning rate 𝛾 può essere diminuito col tempo. Se la funzione è convessa, 
esistono schemi che garantiscono la convergenza al minimo (𝛾 proporzionale 
alla correlazione tra spostamento e gradiente).
Se 𝛾 molto piccolo, non servirebbe renderlo dipendente dal tempo, perché il 
gradiente va già a zero.
Se cadi in un minimo, non ne esci (ma in alta dimensionalità la maggior parte dei punti critici di una funzione sono punti sella)
Se il gradiente è zero o piccolo, non ti muovi.

## Pagina 16

Backpropagation
∂ℒ
∂wljk
=∂ℒ
∂zlj
∂zl
j
∂wljk
=Δl
jal−1
k
ℒ
wl
jk
l layer
jk al
k
al
k=σ∑j=0
wl
kjal−1
j =σ(zl
k)
Δl
j=∂ℒ
∂zlj
=∑k
∂ℒ
∂zl+1
k
∂zl+1
k
∂zlj
=∑k
Δl+1
k
∂zl+1
k
∂zlj
=σ′ (zl
j)∑k
Δl+1
kwl+1
kj
idea: se                        alloray=f(g(x)) dy
dx=f′ (g(x))⋅g′ (x)
ΔL
j=∂ℒ
∂zLj
Gli "errori" di un layer possono essere calcolati iterativamente
a partire dall'ultimo layer
Problema: nei deep network il prodotto  Δl
j=σ′ (zl
j)∑k
σ′ (zl+1
k)∑m(σ′ (zl+2
m)∑n
(...)wl+3
nm)wl+2
mk wl+1
kj va a zero se ho tanteσ′ (z)<1
zkl

## Pagina 17

ResNet
al=σ(al−1)+al−1
l layer
Δl
j=[σ′ (zl
j)+1]∑k
Δl+1
kwl+1
kj
y=f(g(x)+x)
dy
dx=f′ (g(x)+x)[g′ (x)+1]
L'idea è che
che nel caso di una rete deep signiﬁca
gli svantaggi sono:
- facile che ci sia overﬁtting
- instabilità nel training

## Pagina 18

Stochastic gradient descent
Tutte le funzioni loss hanno la formaℒ=
P
∑k=1
ℓ(yk,F(xk)), quindi il calcolo del gradiente scala come P , che può diventare pesante per P>>1.
Divido l'input in minibatch {B} di taglia P'<<P: ̂ℒ=
P′ 
∑k∈B
ℓ(yk,F(xk))=ℒ+ϵ
W
ℒ
𝜀>>0
𝜀=0
Questa "temperatura" può aiutare a superare le barriere...
L'eﬀetto diminuisce più i dati sono correlati tra loro.
v(t+1)=γv(t)−η(t)∇ℒ
w(t+1)=w(t)+v(t)
dx
dt=v(t)
mdv
dt=−γv(t)−∇U(x)
Si può inserire un'inerzia per evitare troppo random walk...
che ricorda la soluzione di 
v(t+Δt)=v(t)−γm−1v(t)−m−1∇U(x)
x(t+Δt)=x(t)+v(t)

## Pagina 19

ADAM algorithm
Cambia adattivamente il learning rate
mi(t)=β1mi(t−1)+(1−β1)∇ℒi
si(t)=β2si(t−1)+(1−β2)(∇ℒi)2}running averages
̂mi(t)=mi(t)
1−βt1
̂si(t)=mi(t)
1−βt2
}normalizzazione
wi(t+1)=wi(t)−α ̂mi(t)
̂si(t)1/2+ϵ
Valori tipici sono 𝛽1=0.90, 𝛽2=0.99 e 𝜀=10-8 (𝜀 serve per evitare divergenze). Considera cheσi(t)2=̂si(t)2−̂mi(t)2
wi(t+1)=wi(t)−α ̂mi(t)
̂mi(t)2+σ(t)2+ϵ
Se 𝜎→0, allora Δwi(t)→−αmi
|mi|
Se             , allora σi≫̂mi Δwi(t)→−α̂mi(t)
̂σi(t) (proporzionale al rapport segnale-rumore)
(applica un cutoﬀ di 𝜶 alla derivata)

## Pagina 20

I dati
simply wrong source....
unbalanced databiased data


## Pagina 21

I dati
I dati vanno standardizzati 
Separare training set da test set
xi=0
σi=1∀i
Bilanciati
Corretti
In numero suﬃciente (vedi dopo)
Se categoriali, codiﬁcarli con one-hot-encoding
(controllarli con PCA)


## Pagina 22

Data augmentation
Sigiﬁca aumentare artiﬁcialmente i dati attraverso delle trasformazioni (in genere stocastiche):
- rotazioni e traslazioni (per immagini)
- applicazione di rumore
- ecc
Diverso da dati sintentici.
In generale può essere pericoloso: si sta sempre inserendo nuova informazione a priori
(esempio: rotazioni -> invarianza rotazionale)
Utile per imbalanced datasets.
Si può fare in modo controllato


## Pagina 23

Dati correlati 
Ci sono architetture appositamente pensate per i dati correlati ( LSTM ) e architetture che vogliono dati estratti indipendentemente dalla stessa distribuzione (VAE).
Le architetture feed-forward in generale sono tolleranti, basta che non inducano problemi di numerosità (𝛼 dipende dai dati eﬀettivi) e di unbalancing.
Per eliminarli, si può fare whitening (opposto alla data augmentation)
  
se x sono i dati correlati con matrice di correlazione 𝛴, applico y=Wx, dove W𝛴WT=1  
yyT=Wx(Wx)T=WxxTWT=WΣWT=1
Ci sono anche le correlazioni tra gli elementi... -> PCA

## Pagina 24

#dati vs #parametri
Quanti parametri N devo avere per imparare P dati d-dimensionali?
Caso semplice: P dati distinti tali che yp=f(xp), rete feedforwad con 1 hidden layer (ReLU+linear)
x y
y=
m
∑k
w(2)
kσ
d
∑j
w(1)
kjxj
Si dimostra che è sempre possibile trovare una matrice w(1) tale che  {𝝈(z1), ..., 𝝈(zp)} è una base nello spazio 
dei vettori {f(x1),..., f(xp)}. Quindi basta che m=P [F . Bach, 2017] e servono N=dm+m=P(d+1) parametri.
In pratica: scelgo un vettore w casuale da distribuzione gaussiana, siano                  , scegliamo dei  
 b1... bp tali che b1<z1<b2<z2<... e Apq = 𝝈( zp-bq ) = max[ zp-bq, 0 ]. La matrice A è triangolare e quindi 
invertibile, quindi w(2) = A-1 y
zp=wTxp
In realtà si dimostra che bastano m=4P/d neuroni hidden [Bubeck, 2020], quindi N=4(d+1) P/d~4P parametri. 
In questo caso la dimensionalità è beneﬁca....
Questo suggerisce che             ("constrained density") sia un buon parametro per capire se la rete può imparare il training set.α=P
N

## Pagina 25

La visione classica 
 Interpolation 
threshold
=1/α
=1/αc

## Pagina 26

La visione classica 


## Pagina 27

La visione moderna 
ChatGPT-3:    3 1011 words, 1014 parameters

## Pagina 28

La visione moderna 
Grokking:

## Pagina 29

Perché il caso sovraparametrizzato funziona?
LEMMA: Il ﬂusso di gradiente                                che usiamo nel gradient descent converge ad una soluzione di minima normadW
dt==∇ℒ(W(t)) |W|
Nel caso di modello lineare e norma L2 la dimostrazione è semplice:
∇ℒ=−xT(y−xW(t))=
P
∑i=1
αixi , cioè il gradiente rimane nel sottospazio lineare generato dai dati. Quindi esistono dei parametri a per cui 
il problema è convesso, quindi converge ad una soluzione stazionaria xW=y
W=xTa
Quindi,                   da cui si ottiene                        e quindi                            , che è la matrice pseudoinversa applicata a y.xxTa=y a=(xxT)−1y W=xT(xxT)−1y
La matrice pseudoinversa produce la soluzione di minima norma di un sistema lineare.
Il lemma si estende a diversi tipi di norma e a sistemi non-lineari.
Abbiamo visto nel caso delle SVM che minimizzare il gradiente signiﬁca massimizzare il margine, e quindi ottenere soluzioni "migliori".
Morale:
Quando 𝜶=𝜶c, esiste una sola soluzione per W e quindi non posso sceglierne il margine.
Più 𝜶<𝜶c, più ho possibilità di scegliere soluzioni con margine grande.
Non incorro nell'overﬁtting perché c'è un regolarizzatore implicito nel SD.

## Pagina 30

Le soluzioni non sono tutte uguali
ℒ
ϕ(W)=log∫dNW′ e−βℒ(W′ )−γd(W,W′ )
"local entropy"
soluzioni con maggiore local entropy generalizzano meglio.
non ci sono vicino a 𝜶c (ci sono due transizioni, la seconda è 
improvvisa e fa comparire i minimi larghi.
Anche se sono piu larghi, non si trovano piu facilmente.


## Pagina 31

Le soluzioni non sono tutte uguali
Un algoritmo per trovare le soluzioni "larghe"
Algoritmo con y repliche accoppiate del sistema, minimizzando
y
∑i=1
ℒ(Wi)−γ
y
∑i,j=1
d(Wi,Wj)
e riducendo lentamente il parametro 𝜸.

## Pagina 32

Lo spazio delle soluzioni
Non è vero che diventa convesso se 𝜶→0
ℒ(W)
La loss è una funzione frastagliata dei parametri W.
La ragione è nella frustrazione del sistema:
Ci sono tanti (eN) minimi locali.
Steepest descent rimane intrappolato, SGD e algoritmi con inerzia meno.
ℒ=
P
∑k=1
|y(k)−σ(Wx(k))|2

## Pagina 33

Lo spazio delle soluzioni
α≈αc α≪αc
SGD
Conclusione: ha senso provare diverse ottimizzazioni, con diversi algoritmi, e non applicare ciecamente l'early stopping.


## Pagina 34

Deloitte, Unpacking the Complexity in AI Training, 2025
Training Utilizzo
ChatGPT 4 ha usato 6.2 GWh (Milano usa 10 GWh al giorno)
Consumo elettrico

## Pagina 35

AI neuromorﬁca


## Pagina 36

AI neuromorﬁca
Il cervello non usa la backpropagation (che coinvolge sempre tutti i neuroni)
Utilizza 0.3 kWh / giorno ( = 10 W = 400 kcal / giorno )
Caratteristiche principali:
-asincrona
-cpu e memoria accoppiate
-codiﬁca con spike temporali
-online training
Problema del training: idea di reinforcement learning

## Pagina 37

Alternative alla backpropagation
* Hebbian learning (neuroni che vengono attivati insieme rinforzano la connessione)
* reinforcement learning ( lezioni di Restelli )
* random feedback alignment
* synthetic gradients
* metodi Monte Carlo (compresi algoritmi genetici)
Δl
j=σ′ (zl
j)∑k
Δl+1
kwl+1
kjinvece che Δl
j=σ′ (zl
j)∑k
Δl+1
kRkjone calculates , where Rkj is a quenched random variable.

## Pagina 38

Tipi di architettura


## Pagina 39

Convolutional neural networks
Usato tipicamente per immagini (risolve il problema della simmetria traslazionale)
aconv
ij =∑kl
xi+k,j+lKi,jconvoluzione con kernel K:
e poi pooling (esempio media) 
Architetture più famose: (Lenet), Alexnet


## Pagina 40

Convolutional neural networks
mnist database
cifar10 database
how it is encoded


## Pagina 41

Graph neural networks
Utile quando le proprietà dei dati hanno relazioni topologiche 
h0
ν=f(xν)un qualche embedding dei dati 
itero N volte una mappa che aggrega le proprietà dei nodi vicini
k=0
k=1
k=N
(message passing)
La rete è equivariante per permutazione dei nodi.
Un ragionamento simile si può fare per studiare le proprietà delle connessioni.
Task:
- classiﬁcazione del network
- classiﬁcazione di nodi incogniti
- predizione dei link
- clusterizzazione dei nodi

## Pagina 42

Graph neural networks
Esempi real-life:
sistemi di raccomandazione ( nodi sono i prodotti, link sono suggerimenti di acquisto)
molecular design
knowledge graphs


## Pagina 43

Long short-term memory networks
I network ricorrenti sono utili per liste o serie temporali
ma soﬀrono di problemi al gradiente
y=f1(f2(...(fn(x)))⇒y′ =f′ 1⋅f′ 2⋅...⋅f′ n(x)→0
La memoria è mantenuta da una variabile 'stato della cella'  Ct 
Ct+1
ht+1
Ct−1
ht−1


## Pagina 44

Long short-term memory networks
Esempio: predizione dei passeggeri di una tratta aerea
Previsioni atmosferiche (multivariata)

## Pagina 45

Transformers
x
embedding Q
K
We WQ
WK
Attention Matrix
WV
V
*
u z
W1
ReLU
(modulo prof. Mousavi)
applicazioni: LLM, traduzione, chatGPT, protein prediction,...

## Pagina 46

Kolmogorov-Arnold networks
Molto sperimentale
Basato sul Kolmogorov-Arnold Representation Theorem
Funzioni di attivazione descritte da B-spline, modiﬁcate
durante il training
Risultati interpretabili


## Pagina 47

Autoencoder
Unsupervised task: riduzione dimensionale
Se lineare, è equivalente a PCA


## Pagina 48

Variational Autoencoder
𝝁
𝝈
z
stochastic variable
Versione stocastica dell'autoencoder
Lo spazio delle variabili latenti è connesso
Impara delle distribuzioni p(x)
E' generativo
Training minimizzando la distanza tra le distribuzioni


## Pagina 49

Diﬀusion models
Sono modelli generativi (come VAE e GAN)
Viene ottimizzato il deconding                    , che è un modello
Gaussiano ~N(𝜇,𝜎) dove la media e la stdev sono determinati 
da una rete feedforward,                      e
Per generare nuovi dati, basta fare il decoding di array 
Gaussiani.
Gaussian noise
pθ(xt−1|xt)
pθ(xt−1|xt)
∼N(0,1)
μt−1=Fθ(xt) σt−1=Fθ(xt)


## Pagina 50

Restricted Boltzmann machines
Sono reti generative basati sull'energia. Imparano distribuzioni tipo
che marginalizza
Impara con la contrastive divergence
p(v)=∫dh1
Zexp∑ij
viWijhj
p(v,h)=1
Zexp∑ij
viWijhj
L(W)=⟨logp(v)⟩data
∂L
∂Wij
=⟨vihj⟩data−⟨vihj⟩model
spesso si usano minibatch di n=1 elementi.
(maximum entropy distribution)

## Pagina 51

Restricted Boltzmann machines
Usato nei sistemi di raccomandazione, tipo Netﬂix.....
Quindi è fondamentale nel marketing....
La maggior parte dei prodotti non li vedremo mai.....

## Pagina 52

One-pixel attack


## Pagina 53

Combinare più modelli....
Se ho un modello solo per descrivere dei dati
cioè abbiamo un metodo statistico per minimizzare una funzione costo                                             
 cioè
di cui conosciamo
Il generalization error  è
Quindi,
=Bias2 =Var
=Noise


## Pagina 54

Combinare più modelli....
Se invece abbiamo M modelli e assumiamo che la stima dell predizione sia la media dei modelli
Il conto è simile a prima
=Noise
Ma questa volta,
dove deﬁniamo il coeﬃciente di correlazione normalizzato
che può andare a zero se 𝛒=0 e M→∞
