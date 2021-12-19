# Sending mail using django

## Setup Steps:

- git clone https://github.com/shankarlmc/emailsender.git

```
git clone https://github.com/shankarlmc/emailsender.git
```

- setup environment

```
python -m venv env
# activate the environment
env\Scripts\activate
```

- change the directory to emailsender

```
cd emailsender
```

- Install the packages by using requirements.txt

```
pip install -r requirements.txt
```

- rename the .env-sample file to .env and setup the variables like this

```
SECRET_KEY=from settings.py
DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email_address
EMAIL_HOST_PASSWORD=your_email_password
```

- Make migrations

```
python manage.py makemigrations
python manage.py migrate
```

- Runserver

```
python manage.py runserver
```

---

<h2 align="center">Thank You!!!</h2>
