gitlm:
	@python cli/gitlm.py --model $(model)

freeze:
	pip freeze > requirements.txt