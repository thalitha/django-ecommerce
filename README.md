#command to create the virtual env \r
python -m venv  ./venv

#command to install the dependencies of the project
pip install -r requirements.txt

#setup the web server
python manage.py runserver     
