gitlm:
	@python -m gitlm $(filter-out $@,$(MAKECMDGOALS))

freeze:
	pip freeze > requirements.txt