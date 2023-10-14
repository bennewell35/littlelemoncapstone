# littlelemoncapstone
Create a Python virtual environment, activate it and install Django in it.

python -m venv workspace
cd workspace
scripts\activate
scripts\pip3 install django
scripts\pip3 install mysqlclient
scripts\pip3 install djangorestframework
scripts\pip3 install djoser

Use this git repo files in virtual environment

edit settings.py to match your database environment [servername, port, db name, etc]

cd workspace\littlelemoncapstone
python .\manage.py makemigrations  //should detect no changes
python .\manage.py migrate
