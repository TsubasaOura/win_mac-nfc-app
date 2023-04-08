```bash
docker compose build
docker compose run --rm api poetry install
docker compose run --rm api python create_table.py
```
