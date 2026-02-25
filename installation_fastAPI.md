# A savoir pour garder par coeur

Pour créer environnement virtuel, tu fais : python -m venv .venv
Tu peux mettre le nom que tu veux, mais .venv c’est une convention.
Ensuite, tu actives l’environnement :
**Windows**
.venv\Scripts\Activate.ps1
**Linux / Mac**

```source .venv/bin/activate

Pour mettre à jour pip :
python -m pip install --upgrade pip

Pour installer les dépendances :
pip install "fastapi[standard]"

Pour lancer le serveur de développement :
fastapi dev main.py
