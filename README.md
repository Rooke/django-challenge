# Bungalow Django Challenge

_djangochallenge_ is an attempt at the Bungalow Django Challenge. It mainly uses two python libraries, `django-csvimport` and
`djangorestframework`. Thus, to run the development server first install them with:

```sh
$ pip3 install djangorestframework django-csvimport
```

The `House` model is located [here](./fungalow/models.py)


After initializing the django environment (e.g. with `python manage.py migrate`), to import the data, run the command:

```sh
python3 manage.py importcsv --model='fungalow.Home' --delimiter=',' /path/to/challenge_data.csv
```

You can then view the data by navigating your browser to (http://127.0.0.1:8000/homes/)

## Notes

Many columns have blank data, so an attempt at made at making the schema forgiving enough to allow this data. Unfortunately the CSV import tool will not deal with blank columns well, so the data that ends up in the database after the `importcsv` is incorrect.


## Time breakdown

Day 1:
T+20 (minutes): Look at data, put into postgres to query

T+40: Setup fresh Django project

T+57: Read docs on Django models (field types, etc.)

T+65: Model 'Home' using some guesses at field types

T+82: Finished modelling Home type

t+100: Successfully imported (incorrect) data

T+120: Commit progress (end of day)

Day 2:
T+130: Reading about rest_framework

T+150: Working demo with rest_framework

T+155: Attempt to write a test, bail

t+170: Attempt to POST some data using rest_framework's default UI

t+190: Write this log/README