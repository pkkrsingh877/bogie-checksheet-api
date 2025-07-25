# bogie-checksheet-api

## How to setup this code to run on your device

1. Download the code as zip from github or use git clone command to get a copy of project on your device

2. Run following command to create virtual environment

```
py -m venv .venv
```

3. Run the virtual enviornment using command

```
.venv\Scripts\activate #For Windows
source .venv\Scripts\activate #For Linux
```

4. Run the following command to get all packages listed in requirements(dependecies)

```
uv sync
```

5. Finally you have virtual environment setup and all dependencies to run the project. Run the following command

```
uvicorn main:app --reload
```

6. If no error is showing then project is running successfully. Now you are ready to make requests to the api. You can do so by postman, thunderclient or similar tool

## Database Setup

1. Open psql terminal or login to psql on any terminal. Eg.

```
psql -U postgres
password: <your local psql password>
```

2. Once successfully logged in, run the following command.
```
CREATE DATABASE bogie_db;
```

3. After this the database will be created.

4. Then in the vscode, run following command
```
py dbinit.py
```

5. Once this is done, the database is prepared to save data coming in the POST request


## API Documentation

1. Once you have ran the app, let us say on "http://localhost:8000" then you can got to "http://localhost:8000/docs" to access the API docs.