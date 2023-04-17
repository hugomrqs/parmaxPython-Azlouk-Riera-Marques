import datetime
import graphviz
from graphviz import Digraph
import threading
import random

#Déclaration de la class Task et de ses attributs
class Task:
    name = ""
    reads = []
    writes = []
    run = None

    def __init__(self, name, function, reads=[], writes=[]):
        self.name = name
        self.reads = reads
        self.writes = writes
        self.run = function
class TaskSystem:
    tasks = []
    dependencies = dict()

    def __init__(self, tasks, dependencies):
        #Verification des noms de taches dupliquees
        dup = self.dupliquer(tasks)
        if dup:
            print('il y a des doublons')

        #Verification des noms de taches inexistantes
        taskExist = self.__isExistingTask(tasks, dependencies)
        if taskExist:
            print("Tâche ",taskExist,"n'existe pas")

        #Verification des taches dans les cles
        taskDict = self.isTaskDict(tasks, dependencies)
        if taskDict:
           print("manque tâche :", taskDict)
    
        self.tasks = tasks
        self.dependencies = dependencies
        #Stock les taches deja executees
        self.doneTasks = {x.name: False for x in tasks}

    def dupliquer(self, tasks):
        i = 0
        #Parcours du tableau de taches 1ere fois
        for i in range(0, len(tasks)):
            #Parcours du tableau de taches 2eme fois
            for j in range(0, len(tasks)):
                #Return true si les deux fonctions sont différentes et ont le même nom
                if i != j and tasks[i].name == tasks[j].name:
                    return True
        return False

        #renvoie les dependances d'une tache
    def getDependencies(self, taskName):
        return self.dependencies.get(taskName)

#VERIFIE LES CONDITIONS DE BERNSTEIN
    def bernstein(self,task1, task2):
        #Soit data la donnée à ecrire de la tâche
        for data1 in task1.writes:
        #Si une donnée écrite par task1 est également lue ou écrite par task2, les deux tâches ne sont pas indépendantes            
            if data1 in task2.reads or data1 in task2.writes:
                return False
        for data2 in task2.writes:
        #Si une donnée écrite par task2 est également lue ou écrite par task1, les deux tâches ne sont pas indépendantes            
            if data2 in task1.reads or data2 in task1.writes:
                return False
        for data1 in task1.writes:
            for data2 in task2.writes:
        #Si deux tâches écrivent sur la même donnée, les deux tâches ne sont pas indépendantes
                if data1 == data2:
                    return False
        return True


#VERIFICATION DU DICTIONNAIRE 
    def __isExistingTask(self, tasks, dependencies):
        #Stocker les tâches existantes dans un ensemble
        existing_tasks = set(task.name for task in tasks)
        #Création d'un dictionnaire pour stocker les dépendances invalides
        invalid_dependencies = {}
        #Parcoure chaque tâche avec ses dépendances
        for task, deps in dependencies.items():
            for dep in deps:
                if dep not in existing_tasks or task not in existing_tasks:
                    #Si l'une des dépendances est invalide ajout d'une tâche et ses dépendances invalides au dictionnaire
                    invalid_dependencies[task] = deps
                    break
        return invalid_dependencies

    def isTaskDict(self, tasks, dict):
        #Crée un ensemble de noms de tâches à partir de la liste de tâches
        allTask = {t.name for t in tasks}
        #Crée un ensemble de toutes les clés du dictionnaire
        allKeys = {k for k in dict.keys()}
        #Retourne la liste des noms de tâches qui ne sont pas des clés dans le dictionnaire
        return list(allTask - allKeys)
      
#LANCEMENT SEQUENTIEL
#RETOURNE LA PREMIERE TACHE SANS DEPENDANCES

    def firstTasks(self):
        for t in self.tasks:
            if self.dependencies[t.name] ==[]:
                 #retourne les tâches qui n'ont pas de dépendences
                return t

    def nexTask(self, task):
        print('error')
        # On arrive pas à passer à la tache suivante
    def runTask(self):
    #Tant qu'il reste des tâches
        while True:
            #Ramener les taches sans dépendences
            task = self.firstTasks()
            #Lancer la tâche
            print('la tache ',task.name, 'est lancé')
            threading.Thread(target=task.run).start()
            #Changer la valeur de la tâche
            self.doneTasks[task.name] = True
            #Attribue la valeur nexTasks à Tasks
            task = self.nexTask(task.name)
   
   
    #optimisation du parallelisme de tâche
    def maxDep(self):
        #Creation d'un dictionnaire vide
        tempDict = {t : [] for t in self.dependencies.keys()}
        
        #Ajout des precedences selon les conditions de bernstein
        for i in range(len(self.tasks)):
            for j in range(i+1, len(self.tasks)):
                if not self.bernstein(self.tasks[i],self.tasks[j]):
                    tempDict[self.tasks[j].name].append(self.tasks[i].name)

    def runSeq(self):
        now = datetime.datetime.now()
        # List contiendra l'ordre de lancement des taches
        list =[]
        for key,value in self.dependencies.items():
            if value == []:
                list.append(key)


        # Créer un tableau qui parcours les dépendences et enleve tout les membres de listes. 
        # Des qu'une tache n'a plus de dependences elle est ajoutée à la list
        for t in list:
            # Lancement des tâches dans l'ordre
            print("tache", t.name) 
            t.run()
       
    def runPar(self):
        self.maxDep()
        self.runTask()


    def run(self):
        print("---------Lancement sequentiel --------------------")
        self.runSeq()
        print("---------Lancement parrallèle --------------------")
        self.runPar()
        self.draw()

#Affichage graphique du diagraphe
    def draw(self):
        #digraph pour graph orienté
        graph=graphviz.Digraph(format='png')
        #création des arcs
        for key, value in self.dependencies.items():
            if value !=[] :
                #parcours du tableau value
                for i in value:
                    graph.edge(i,key) 
        #afficher le graph en png
        graph.view()
          
                    
    #fonction qui calcule le temps moyen d'éxecution de runSeq
    def cost(self):
        rand = random.randint(10, 100)
        print(rand)
        time = []
        #Lance runSeq rand fois et ajoute les temps à une liste time
        for i in range(rand):
            time.append(self.runSeq().total_seconds())
        #afficage du temps moyen
        print("temps moyen:", sum(time) / len(time))

    #Attribue des valeur aléatoires 
    def detTestRnd(self):
        # dictionnaire de 
        data= {}
        for task in self.tasks:
            for var in task.reads and task.writes:
                data[var]= random.randint(0, 100)
        #renvoie le dictionnaire de correspondance entre les anciennes données et les nouvelles attribués aléatoirement

