# Projet Cassandra : Inspection des Restaurants

## Introduction

Ce projet consiste à déployer un cluster Cassandra à l'aide de conteneurs Docker pour centraliser les résultats des inspections de restaurants. Une API a été développée pour tester l'accessibilité et les temps de réponse de la base de données.

## Prérequis

- Docker

## Structure du projet

Le projet est structuré comme suit :

```
/projet-cassandra
    /cassandra1_data
    /cassandra2_data
    /serveur_rest
    docker-compose.yml
    Dockerfile-serveur
    README.md
```

## API

L'API a été développée en utilisant Flask et offre les fonctionnalités suivantes :

- Obtenir les informations d'un restaurant à partir de son identifiant.
- Récupérer la liste des noms de restaurants en fonction du type de cuisine.
- Obtenir le nombre d'inspections d'un restaurant à partir de son identifiant.
- Récupérer les noms des 10 premiers restaurants d'un grade donné.

## Déploiement du cluster Cassandra et de l'API

Pour déployer le cluster Cassandra et l'API, exécutez la commande suivante à la racine du projet :

```bash
docker-compose up -d
```

Cela va démarrer deux nœuds Cassandra et l'API en utilisant Docker.

## Utilisation de l'API

Voici comment utiliser l'API :

- Pour obtenir les informations d'un restaurant à partir de son identifiant :

```http://localhost:5001/api/restaurant/<id>```

- Pour récupérer la liste des noms de restaurants en fonction du type de cuisine :

```http://localhost:5001/api/type_cuisine/<type_de_cuisine>```

- Pour obtenir le nombre d'inspections d'un restaurant à partir de son identifiant :

```http://localhost:5001/api/inspection/<id>```

- Pour récupérer les noms des 10 premiers restaurants d'un grade donné :

```http://localhost:5001/api/grade/<grade>```

Les URL retournent la réponse en JSON de l'API.

## Conclusion

Ce projet démontre comment déployer un cluster Cassandra à l'aide de conteneurs Docker et comment développer une API pour interagir avec la base de données. Il illustre également comment Cassandra peut être utilisée pour gérer une grande quantité de données tout en offrant des temps de réponse rapides.