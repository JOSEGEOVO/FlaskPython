setup: requirements.txt
	pip install -r requirements.txt

run:
	flask run

debug:
	python app.py

all: setup run