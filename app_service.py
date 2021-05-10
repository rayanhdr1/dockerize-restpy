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
        pass

    def get_tasks(self):
        return self.tasks

    def create_task(self,task):
        task['id'] = int(task['id'])
        self.tasks.append(task)
        return self.tasks

    def update_task(self, request_task):
        for task in self.tasks:
            if task["id"] == int(request_task['id']):
                task.update(request_task)
                return self.tasks;
        return {'message': 'id de tâche non trouvé'}

    def delete_task(self, request_task_id):
        for task in self.tasks:
            if task["id"] == request_task_id:
                self.tasks.remove(task)
                return self.tasks
        return {'message': 'id de tâche non trouvé'}

    
