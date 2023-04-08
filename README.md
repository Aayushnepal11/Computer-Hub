# Favorite Brands
___
# Computer HUb 
___
* This whole project is oop based.
* Class based views
* when you are using thsi project setup a .env file.
* Then create a constant called SECRET_KEY="KEPP your key here"
___

* Create a virtual environment
`
    Windows: python -m venv env
    Linux: python3 -m venv env
`
___

* And Install the file requirements.txt
`
    pip install -r requirements.txt
`
___

* Then use the shell 
`
    python manage.py shell
`
___

* And generate the random key
` 
    By using: 
    ___
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())

`