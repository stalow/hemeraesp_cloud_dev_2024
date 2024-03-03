#  une image Python de base
FROM python:3.8

#  le répertoire de travail dans le conteneur
WORKDIR /app

#  le fichier requirements.txt dans le conteneur
COPY requirements.txt .

#  les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste du code dans le conteneur
COPY . .

# Exposez le port sur lequel le service Python s'exécute
EXPOSE 5000

# Commande pour exécuter le service Python
#CMD ["python", "app.py"]
