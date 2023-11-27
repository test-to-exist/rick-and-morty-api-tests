# Rick and Morty API Tests

Create and activate virtual env 

```commandline
mkdir .venv
python3 -m venv ./.venv/rick-and-morty
chmod +x ./.venv/rick-and-morty/bin/activate
./.venv/rick-and-morty/bin/activate
```

Install the requirements 

```commandline
pip install -r ./src/requirements.txt
```

Add config file and fill section for baser url

```commandline
touch src/config/config.ini
echo "[APP]" >> src/config/config.ini
echo "BASEURL=https://rickandmortyapi.com/api" >> src/config/config.ini
```

Run all tests

```commandline
 python -m unittest discover 
```

Run all tests and generate JUnit xml report

```commandline
python main.py
```

Here is the page with the report from the last run

https://test-to-exist.github.io/rick-and-morty-api-tests/22/#

