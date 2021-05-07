# python-flask-restapi

Exemple de projet sur la façon de développer une API RESTful avec Flask et Python avec Docker

L'application est simple, elle gères des tâches.

Une tâche est définie par un `id`, un `nom` et une `description`

En format dictionnaire Python on aurait par exemple quelque chose comme ceci `{'id': 1, nom: 'tache1', description: 'La première tache'}`

Dans cette version initiale la liste des tâches est mémorisé dans une liste interne

Nous allons utilisé une architecture tel que celle ci.
![Archi](imgs\archi.png)
On utilise une interface service pour accedes aux resources, une interface service CRUD


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