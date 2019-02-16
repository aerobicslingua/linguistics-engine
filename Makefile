prepare:
	pip3 install -U spacy
	pip3 install webvtt-py
	python3 -m spacy download en
run:
	./PoS.py ./sample-beautifulmind.vtt


