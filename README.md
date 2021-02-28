# Task Management for Konvergen Assignment

## How to Install

Program used to develop this application:
- [Python 3.6.2](https://www.python.org/downloads/release/python-362/)

1. Start your command terminal on the root project of this project
2. Create a **python virtual environment** by running the command:
    ```bash
    python -m venv env
    ```
3. Activate your virtual environment and instally requirements by running these commands:

    Windows:
    
    ```bash
    env\Scripts\activate.bat
    pip install -r requirements.txt
    ```

    Linux & Mac OS:

    ```bash
    source env/bin/activate
    pip install -r requirements.txt
    ```

4. Do database migrations and populate user table by running these commands:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loadfixture tasks/fixture.json
    ```

5. Collect static files by running this command:
    ```bash
    python manage.py collectstatic
    ```

6. You can now run the program by running this command:
    ```bash
    python manage.py runserver
    ```

## Details
1. After properly migrating the database, you can log in with this user information:
   ```
   user: defaultuser
   password: defaultpass
    ```

2. You can also sign a user up on the application itself!

3. Uploading tasks is done in the **All Tasks** tab. You can also see all the tasks that have been uploaded, book a task, and delete a task here. The task deletion is a soft delete, so even when the task isn't shown in the app anymore, the files will still be stored in the server.

4. You can see the tasks you have assigned for yourself in the **My Tasks** tab. You can also revoke a booked task and download tasks here.

5. Please make sure to be connected to the internet when running the program, as the bootstrap is connected via CDN.