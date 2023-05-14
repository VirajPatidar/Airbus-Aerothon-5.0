# Airbus Aerothon 5.0

## Optimising Washing Machine Manufacturing Supply Chain Using Data Lake 
The manufacturing company's supply chain process generates a significant amount of redundant intermediate data, leading to storage and sustainability issues. The data produced by various departments, including logistics, planning, and forecasting, needs to be consolidated efficiently and made accessible to relevant users. A solution is required to reduce redundancy, establish data authenticity, automate data stamping, and provide domain specific dashboards for data access and monitoring.

<br />

![Implementation](https://github.com/VirajPatidar/Airbus-Aerothon-5.0/blob/main/frontend/src/images/SupplyChain.JPG)

<br />

### Features
- Multirole Authentication and Authorization
- Data Redundancy Checks
  - Normalized Database
  - User defined constraints aligned to business requirements
  - Cron job scheduler to handle redundant data across departments after logical completion of cross functional business processes
- Multiple Stakeholders
- Interactive Dashboard
- Responsive UI
- Inventory Forecasting Model

<br />

## Tech Stack
### Backend
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)
- [PostgreSQL](https://www.postgresql.org/)

### Frontend
- [React](https://react.dev/)
- [React Router](https://reactrouter.com/en/main)
- [Recoil](https://recoiljs.org/)
- [MUI](https://mui.com/)
- [Axios](https://axios-http.com/)


<br/>

## Contributors
| Sr. No. | Name     | GitHub |
| ------ | -------- | ----------- |
| 1.     | Viraj Patidar | [@VirajPatidar](https://github.com/VirajPatidar) |
| 2.     | Somya Malgudi | [@Sage-2001](https://github.com/Sage-2001)|
| 3.     | Om Khade | [@khadeom](https://github.com/khadeom)|
| 4.     | Rishav Kumar | [@HappY-FaceS](https://github.com/HappY-FaceS)|

<br/>


## Setup

```bash
# Clone the Repository
$ git clone https://github.com/VirajPatidar/Airbus-Aerothon-5.0.git 
$ cd Airbus-Aerothon-5.0
```

### Backend

> #### Setup: Linux, Unix 
```bash
$ cd backend
$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

> #### Setup: Windows
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
# Populate database with sample data via scripts
$ python manage.py scripts/populate_fabrication.py 
$ python manage.py scripts/machine.py 
$ python manage.py scripts/subassembly.py
```

> #### Run the Backend Server

```bash
$ python manage.py runserver
```

<br />

### Frontend

> Install Node Modules 
```bash
$ cd frontend
$ npm install
$ npm start

```

<br />
