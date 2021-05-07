from flask import Flask, request, jsonify, make_response
from app_service import AppService
import json

app = Flask(__name__)
appService = AppService();


def tasks_to_json_rep(tasks):
    '''
    Retourne une répouse HTTP au format JSON à partir d'une liste de tâches

    tasks : Liste de tâches au format dictionnaire
    return : réponse HTML JSON
    '''
    response = make_response(jsonify(tasks),401)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/')
def home():
    return "App Works!!!"


@app.route('/api/tasks')
def tasks():
    return tasks_to_json_rep(appService.get_tasks())
    

@app.route('/api/task', methods=['POST'])
def create_task():
    # On récupère les resources au fromat JSON dans un dictionnaire
    task = request.get_json()
    print(type(task), task, task['id'])
    return tasks_to_json_rep(appService.create_task(task))


@app.route('/api/task', methods=['PUT'])
def update_task():
    task = request.get_json()
    return tasks_to_json_rep(appService.update_task(task))


@app.route('/api/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    return tasks_to_json_rep(appService.delete_task(id))


