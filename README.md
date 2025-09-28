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
- If a model has a foreign_key related to another model



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
