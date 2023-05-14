# Airbus-Aerothon-5.0

## Problem Statement
The manufacturing company's supply chain process generates a significant amount of redundant intermediate data, leading to storage and sustainability issues. The data produced by various departments, including logistics, planning, and forecasting, needs to be consolidated efficiently and made accessible to relevant users. A solution is required to reduce redundancy, establish data authenticity, automate data stamping, and provide domainspecific dashboards for data access and monitoring.

## Setup

```bash
$ # Clone the Repository
$ git clone https://github.com/VirajPatidar/Airbus-Aerothon-5.0.git 
$ cd Airbus-Aerothon-5.0
```

### Backend

> #### `Unix`, `Linux`, `MacOS` 
```bash
$ cd backend
$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

> #### `Windows` 
```
$ cd backend
$ pip install virtualenv
$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```

> #### Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> Populate Database with sample data via scripts
```bash
$ python manage.py scripts/populate_fabrication.py 
$ python manage.py scripts/machine.py 
$ python manage.py scripts/subassembly.py
```

> Run the Backend Server

```bash
$ python manage.py runserver
```

At this point, the backend server runs at `http://127.0.0.1:8000/`. 

<br />

# Frontend

> Install Node Modules 
```bash
$ cd frontend
$ npm install
$ npm start

```
At this point, the frontend server runs at `http://127.0.0.1:3000/`.

<br />

[video presentation](https://drive.google.com/file/d/1lg_8satarY9BJLqzXiN3Jzw8iF67p2fL/view?usp=share_link)
