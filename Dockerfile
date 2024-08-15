# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le script Python et le fichier HTML dans le conteneur
COPY convert_html_to_md.py file_to_convert.html ./

# Installer la bibliothèque html2text
RUN pip install html2text

# Définir la commande par défaut pour exécuter le script
CMD ["python", "convert_html_to_md.py"]