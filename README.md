# Rick and Morty API Tests

Create and activate virtual env 

```mkdir .venv
python3 -m venv ./.venv/rick-and-morty
chmod +x ./.venv/rick-and-morty/bin/activate
./.venv/rick-and-morty/bin/activate
```

Install the requirements 

```
pip install -r ./src/requirements.txt
```

Add config file and fill section for baser url

```
touch src/config/config.ini
echo "[APP]" >> src/config/config.ini
echo "BASEURL=https://rickandmortyapi.com/api" >> src/config/config.ini
```