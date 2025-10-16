# Bar_daily_menu_site
A little project about putting on a site a daily menu. The customer would be able to look at it and book a spot in the restaurant. Django project



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



## Database handling with django


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

16 ottobre 2025
Ripresa seria del progetto, ho ripassato al volo la lezione 3 ma mi sono ripromesso di avere più ricadenza settimanale. Alla fine ho imparato/ricordato il classico workflow fatto da django in merito al rapporto che hanno i vari file.
Semplicemente vediamoli così:
**models.py** -> dove vengono salvate le classi che manipolano i dati in django (sono in realtà tabelle di un database)
**views.py** -> è come django deve prendere e mostrare i dati presi da un modello, la vista grafica del modello rappresentata sottoforma di codice in python. definisce anche le risposte date dal rendering (successo o 404) è praticamente fa anche da url più o meno
**urls.py** -> al suo interno si definisce i path disponibili che possono esplorati tramite il server locale. teoricamente lavora con le views per definire il tipo di rendering da fare ad un determinato url

**admin.py** -> definizione dei modelli disponibili nella sezione admin (più o meno)

*templates* -> cartella che deve avere al suo interno un'altra cartella con il nome dell'app. La sottocartella dei templates possiederà del codice html per gestire la parte grafica del rendering dei dati sul sito.

questo è quanto per ora

## to-do
- testare le competenze acquisite facendo un proprio modello []
