import json

class AppService:
    '''
    le service CRUD sur les tâches.
    Une tache task est composé 
       d'un identifiant (la clé),
       d'un nom (une deuxième clé secondaire)
       et une description

       L'ensemble des données est archivé en mémoire dans une liste de dictionnaire

       tasks est un attribut de classe (liste des taches)

       taskJSON un attribut d'instance (liste des t6ache au format JSON)
    '''
    # Les données
    tasks = [
        {
            'id': 1,
            'name': "task1",
            "description": "This is task 1"
        },
        {
            "id": 2,
            "name": "task2",
            "description": "This is task 2"
        },
        {
            "id": 3,
            "name": "task3",
            "description": "This is task 3"
        }
    ]

    
    def __init__(self):
        self.tasksJSON = json.dumps(self.tasks)

    def get_tasks(self):
        return self.tasksJSON

    def create_task(self,task):
        tasksData = json.loads(self.tasksJSON)
        tasksData.append(task)
        self.tasksJSON = json.dumps(tasksData)
        return self.tasksJSON

    def update_task(self, request_task):
        tasksData = json.loads(self.tasksJSON)
        for task in tasksData:
            if task["id"] == request_task['id']:
                task.update(request_task)
                return json.dumps(tasksData);
        return json.dumps({'message': 'task id not found'});

    def delete_task(self, request_task_id):
        tasksData = json.loads(self.tasksJSON)
        for task in tasksData:
            if task["id"] == request_task_id:
                tasksData.remove(task)
                return json.dumps(tasksData);
        return json.dumps({'message': 'task id not found'});

    
