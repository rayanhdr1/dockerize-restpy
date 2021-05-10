# python-flask-restapi


Exemple de projet sur la façon de développer une API RESTful avec Flask et Python avec Docker

L'application est simple, elle gères des tâches.

Une tâche est définie par un `id`, un `nom` et une `description`

En format dictionnaire Python on aurait par exemple quelque chose comme ceci `{'id': 1, nom: 'tache1', description: 'La première tache'}`

Dans cette version initiale la liste des tâches est mémorisé dans une liste interne

Nous allons utilisé une architecture tel que celle ci.
![Archi](https://github.com/ISSAE/dockerize-restpy/raw/main/imgs/archi.png)
On utilise une interface service pour accedes aux resources, une interface service CRUD

## Les bases de flask (routage)

Les applications Web utilisent des URL significatives pour aider les utilisateurs. Les utilisateurs sont plus susceptibles de mémoriser une page et de revenir si la page utilise une URL significative dont ils peuvent se souvenir et utiliser pour visiter directement une page.

### Utilisez le décorateur `route()` pour lier une fonction à une URL.

#### Route statique
`@app.route('PATH STATIQUE')`

> exemples:

```python
@app.route('/')
def index():
    return 'Page indexe'

@app.route('/hello')
def hello():
    return 'Bonjour à vous'
```

#### Route dynamique

Vous pouvez rendre certaines parties de l'URL dynamiques et associer plusieurs règles à une fonction.

Vous pouvez ajouter des sections variables à une URL en marquant les sections avec <nom_variable>. Votre fonction reçoit alors le <nom_variable> comme argument de mot-clé. En option, vous pouvez utiliser un convertisseur pour spécifier le type de l'argument comme <convertisseur: nom_variable>.

> exemples

```python

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'Utilisateur {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath{escape(subpath)}'
```


Remarque: MarkupSafe implémente un objet texte qui échappe les caractères afin qu'il puisse être utilisé en toute sécurité en HTML et XML. Les caractères qui ont des significations spéciales sont remplacés afin qu'ils s'affichent en tant que caractères réels. Cela atténue les attaques par injection, ce qui signifie que les entrées d'utilisateurs non fiables peuvent être affichées en toute sécurité sur une page.

## Conteneuriser

Utilisez le décorateur route () pour lier une fonction à une URL.
```bash
# construire l'image
docker build -t flask-restapi .
# lister les images
docker images
# login à Docker Hub
docker login
# tag l'image
docker tag flask-restapi <repository name>/flask-restapi
# push l'image
docker push <repository name>/flask-restapi
```

Quand vous avez publié votre image, tout le monde peut l'utiliser ainsi

```bash
# run the container
docker run -d -p 5000:5000 --name python-restapi flask-restapi
# list the container
docker ps
# logs
docker logs python-restapi
# exec into running container
docker exec -it python-restapi /bin/sh
```
