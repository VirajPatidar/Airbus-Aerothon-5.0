# Airbus-Aerothon-5.0

## ✨ How to use it

> Download the code 

```bash
$ # Get the code
$ git clone https://github.com/VirajPatidar/Airbus-Aerothon-5.0.git 
$ cd Airbus-Aerothon-5.0
```

<br />

# Backend

### 👉 Set Up for `Unix`, `MacOS` 


> Install modules via `VENV`  

```bash
$ cd backend
$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```
### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ cd backend
$ pip install virtualenv
$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Generate sample data using scripts
```bash
$ python manage.py scripts/populate_fabrication.py 
$ python manage.py scripts/machine.py 
$ python manage.py scripts/subassembly.py
```
<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the backend server runs at `http://127.0.0.1:8000/`. 

<br />

# Frontend

> Install modules 
```bash
$ cd frontend
$ npm install
$ npm start

```
At this point, the frontend server runs at `http://127.0.0.1:3000/`.

<br />
