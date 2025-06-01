# Progetto Django: Little Lemon Capstone

Questo è il progetto finale sviluppato per il corso Meta Back-End Developer – Coursera.

## 📦 Tecnologie utilizzate

- Python 3
- Django
- Django REST Framework
- MySQL
- HTML + Bootstrap (opzionale)

## ⚙️ Istruzioni per l’installazione

1. Clona il repository:

```bash
git clone https://github.com/tuo-username/little-lemon-capstone.git
cd little-lemon-capstone
```
2. Crea un ambiente virtuale e attivalo:

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate.bat    # Windows
```
3. Installa le dipendenze:
```bash
pip install -r requirements.txt
```
4. Esegui le migrazioni del database:
```bash
python manage.py migrate
```
5. Avvia il server locale:
```bash
python manage.py runserver
```
6. Vai su ```http://127.0.0.1:8000``` per vedere il progetto in esecuzione.

## 📁 Struttura del progetto

- /booking: App per la gestione delle prenotazioni

- /menu: App per la gestione dei piatti

- /users: App per la gestione dell'autenticazione

- /api: Endpoint REST

## 📌 Note finali

- Il progetto è pensato per essere eseguito in locale.
  
- È consigliato testare l'app con MySQL correttamente configurato.
