install:
	poetry install

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

patch:
	poetry version patch
	poetry build
	poetry publish --dry-run --username ' ' --password ' '
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games
