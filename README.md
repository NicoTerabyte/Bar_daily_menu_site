# Bar_daily_menu_site
A little project about putting on a site a daily menu. The customer would be able to look at it and book a spot in the restaurant. Django project


## The django challenge is like racing mini cars

[![the real challenge]](https://youtu.be/Z9bpxphRj-g)


## The django architecture
The project created with the "django-admin startproject <project name> <directory name>" command

the apps that are created within the project with the command "python manage.py startapp <directory>

Every model is like a table in django and can be created the same way we create classes in python



### Models good to know
- Models are like classes in python
- Most of the models are created in apps
- Every time you want to include a model to the project you have to add it in the settings.py of the project
- after adding the model or after some changes you have to do a ```bash python manage.py makemigrations```
- If a model has a foreign_key related to another model you can establish a relation between the classes (study)



## Database handling with django shell cheatsheet



# Diary log
For now i created the main user
just now that the username is lorenzo_nicotera, the password you need to remember.

Where's the main in a django project? I hope i don't need to use the django shell command everytime

Dridolfo mi ha consigliato di fare attenzione a come lavora **l'ORM di django**
Studiare anche la teoria sql, one-to-one, one-to-many, many-to-many, ah e questo.

Finita praticamente la lezione 3 ho un po' magheggiato con **python manage.py shell** per testare un po' i comportamenti delle tabelle.
Penso di aver capito il rapporto comunque tra i modelli, grazie alla foreign key possono comunicare tra di loro, solo che a causa dell'orm di python il rapporto pare inverso. Per essere sintetici la foreign key in questo caso sta nel modello choice ma quando crei la tabella possono essere modificati da Question, è una preimpostazione per semplificare le cose tutto qui.
Ho fatto anche il lato admin creando un super user con **python manage.py createsuperuser**

30 settembre 2025

16 ottobre 2025choice
Ripresa seria del progetto, ho ripassato al volo la lezione 3 ma mi sono ripromesso di avere più ricadenza settimanale. Alla fine ho imparato/ricordato il classico workflow fatto da django in merito al rapporto che hanno i vari file.
Semplicemente vediamoli così:
**models.py** -> dove vengono salvate le classi che manipolano i dati in django (sono in realtà tabelle di un database)
**views.py** -> è come django deve prendere e mostrare i dati presi da un modello, la vista grafica del modello rappresentata sottoforma di codice in python. definisce anche le risposte date dal rendering (successo o 404) è praticamente fa anche da url più o meno
**urls.py** -> al suo interno si definisce i path disponibili che possono esplorati tramite il server locale. teoricamente lavora con le views per definire il tipo di rendering da fare ad un determinato url

**admin.py** -> definizione dei modelli disponibili nella sezione admin (più o meno)

*templates* -> cartella che deve avere al suo interno un'altra cartella con il nome dell'app. La sottocartella dei templates possiederà del codice html per gestire la parte grafica del rendering dei dati sul sito.

questo è quanto per ora


19 Ottobre 2025
Niente di troppo speciale, ho raffinato le mie competenze in merito alla creazione e linkaggio delle app con il principale.
**Un piccolo fallimento** è stato di provare a mettere delle views nella root del progetto ma per motivi a me sconosciuti pare che django non riesca renderizzare le view dal progetto, o c'è qualche procedura, comportamento diverso oppure sono cieco perché appena ho fatto l'app "homePage" il rendering è andato pulito.

compresioni:
- creato template che dipende dal rendering delle view
- il processo è sempre il seguente (a meno che non mi cambiano idea) crei app -> definisci app in settings.py del progetto principale -> crei urls.py nell'app -> unisci con include (unico metodo al momento) app e progetto principale indirizzando il progetto principale al file urls dell'app -> A livello grafico rappresenti con views che prendono dati e poi vengono *aggiustati* dai template -> a livello di dati gestisci il comportamento dei modelli in **models.py**

Mancante:
- Non ricordo come django inserisce dati nei db oltre a utilizzare da riga di comando sqlite, che mi sembra un po' esagerato, la procedura richiederebbe più tempo, sicuro un modo per toccare i modelli c'è.


**21 22 27 ottobre elaborazioni particolari**

i set è l'accesso ai dati tabella in django sono una cosa **automatica**
appunto.



Allora, se parliamo in modo più concettuale, django gestisce i rapporti tra modelli in maniera contraria rispetto alle tabelle sql. Questo cosa comporta, beh che se io dichiaro una foreign all'interno di un modello che ne punta ad un altro la relazione tra i due sarà inversa. Colui che possiede la foreign key determina essenzialmente la dipendenza tra quel modello e quello che sta puntando. l'ORM farà la ricerca inversa per definire la dipendenza di più modelli con quello a cui è stata data la foreign key.
La riga di codice calda che spiega questa meccanica è la seguente:
```python
question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
class Choice(models.Model):
	#! the foreign key signifies that links each Choice to the Question class
	#? related_name makes it able to avoid ambiguity. so you can refer to the name here
	#? instead of the modelName_set prefix
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self) -> str:
		return self.choice_text
```

la classe utilizza il metodo ForeignKey, questo collegherà inversamente tutti i modelli Choice a delle domande specifiche. Questo permette poi al modello che ne gestisce di più nel rapporto, di ottenere questi dati quando vuole

per esempio nel seguente snippet di codice:
```python
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	try:
		selected_choice = question.choices.get(pk=request.POST["choice"])

	except (KeyError, Choice.DoesNotExist):
		return render(
			request, "polls/detail.html",
			{
				"question": question,
				"error_message": "You didn't select a choice.",
			},
		)

	else:
		selected_choice.votes = F("votes") + 1
		selected_choice.save()
		return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

Otteniamo il modello question e ci riferiamo a quanti modelli Choice sono in esso con question.choices.get notare che abbiamo usato la nomenclatura definita nel **related_name** quando abbiamo dichiarato la foreign key.
La cosa che deve entrare in testa è il rapporto inverso ORM che per farla semplice sarebbe, il modello che dichiara la foreign_key dipende dal modello definito e **NON** fa dipendere quel modello.

**1 Novembre 2025**
Prima di procedere devo menzionare le generic views di django. Praticamente in soldoni invece che utilizzare dei metodi per fare il rendering a mano, si possono utilizzare delle **generic_views** che sono delle classi che al loro interno, tramite delle variabili builtin velocizzano e automatizzano il processo di rendering.
una generic_view viene inizializzata così
```python
# capisci che è una generic view perché eredita da generic quello che sussegue di nome definito (DrtailView è un'altra classe generic fatta da me)

class ResultsView(generic.DetailView):
	pass

#per essere invece invocata nel file urls.py devi scrivere
	path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

```


Generic views vs class view
Lo scopo delle generic views è di essere più semplici delle funzioni view.
Invece lo scopo delle class view è quello di essere più malleabili delle funzioni view
Anche perché ciò che potrebbe fare una funzione view lo farebbe la classe view con un suo metodo.

Le classi view  possiedono dei mixins cioè possono ereditare più attributi da padri diversi volendo.
Ci sono anche altre cose che possono fare ma al momento non riesco a fare un nesso logico per spiegare le possibili implementazioni (So di non sapere).

per creare una classe view, serve dichiararla come classe e farla ereditare da View.
```python
from django.views import View
class BasicView(View):
	pass
```

**11 novembre 2025 ziopera ho dimenticato tutto**
Allora mi sono fatto un piccolo risassunto delle varie cose studiate l'ultima volta, come l'utilizzo delle generic_views, la possibilità di implementare delle classi come view e infine i vari rapporti tra le varie view i loro rendering e il loro menzionare gli altri template.

Oggi punto a creare una view personalizzata per un modello mio che c'è in poll possiamo dire, questo sarebbe Comment, voglio correlarlo alle scelte quindi dare la possibilità da parte di più utenti di commentare una scelta fatta nel form diciamo.
Mo', non ho idee, ma sogni quindi vediamo un po'

**17 dicembre 2025, we are back stronger**
Non mi ricorderò una ciola, MA non mi arrendo così facile, oggi andiamo un po' avanti o comunque mi faccio una piccola code review, sicuro non mi sono dimenticato tutto.


## to-do
- testare le competenze acquisite facendo un proprio modello [x]
- Fare homepage [x]
- Andare alla lezione 4 [x]
- Andare alla lezione 5 []
