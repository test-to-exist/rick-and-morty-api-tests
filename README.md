# Rick and Morty API Tests

# Create and activate virtual env 

```commandline
mkdir .venv
python3 -m venv ./.venv/rick-and-morty
chmod +x ./.venv/rick-and-morty/bin/activate
./.venv/rick-and-morty/bin/activate
```
Have in mind that in windows, you would rather use
```commandline
mkdir .venv
python -m venv ./.venv/rick-and-morty
./.venv/rick-and-morty/bin/Activate.ps1
```

# Install the requirements with this line:
```commandline
pip install -r ./src/requirements.txt
```

Add config file and fill section for baser url

On linux
```commandline
touch src/config/config.ini
echo "[APP]" >> src/config/config.ini
echo "BASEURL=https://rickandmortyapi.com/api" >> src/config/config.ini
```

On windows just create file in config.ini in projects subfolder src/
And fill it with:
```text
[APP]
BASEURL=https://rickandmortyapi.com/api
```

# Run all tests

```commandline
 python3 -m unittest discover 
```
or
```commandline
python -m unittest discover 
```

Run all tests and generate JUnit xml report

```commandline
python main.py
```
or
```commandline
python3 main.py
```

Here is the page with the report from the last run

https://test-to-exist.github.io/rick-and-morty-api-tests/22/#

