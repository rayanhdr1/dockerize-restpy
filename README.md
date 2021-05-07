# python-flask-restapi

Exemple de projet sur la façon de développer une API RESTful avec Flask et Python avec Docker

```bash
# contruire l'image
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

Quand vous avez publier votre image, tout le monde peut l'utiliser ainsi

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