ejecutar:
	pipenv run python app.py

deploy:
	git remote add dokku dokku@trifulca.space:stimulus-dashboard || true
	git push dokku master:master
