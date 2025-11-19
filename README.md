# Monitoramento Industrial - Backend (Python + FastAPI)

Este é um backend mínimo para o sistema de monitoramento descrito no documento do projeto.
Ele faz:
- Consome dados via MQTT (arquivo `mqtt_worker.py`)
- Persiste telemetria em MySQL (`models.py`, `database.py`)
- Expõe endpoints simples com FastAPI (`main.py`)

## Como usar (passo a passo para iniciantes)

1. Crie e ative um ambiente virtual:
   - Windows:
     ```
     python -m venv venv
     venv\\Scripts\\activate
     ```
   - Linux / macOS:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Instale dependências:
```
pip install -r requirements.txt
```

3. Crie o banco de dados MySQL:
- Edite `init_db.sql` se necessário e execute no seu cliente MySQL:
```
mysql -u root -p < init_db.sql
```

4. Configure variáveis de ambiente (ou crie um `.env` a partir de `.env.example`):
```
export DB_USER=root
export DB_PASS=sua_senha
export DB_HOST=localhost
export DB_NAME=monitoramento
export MQTT_HOST=localhost
export MQTT_PORT=1883
```

5. Rodar o worker MQTT (em um terminal):
```
python mqtt_worker.py
```

6. Rodar o backend FastAPI (em outro terminal):
```
uvicorn main:app --reload
```

Acesse a API em: http://127.0.0.1:8000  
Documentação automática: http://127.0.0.1:8000/docs

## Arquivos
- `main.py` - endpoints FastAPI
- `mqtt_worker.py` - worker que consome MQTT e salva no banco
- `database.py` - conexão SQLAlchemy com MySQL
- `models.py` - definição da tabela `telemetria`
- `init_db.sql` - script para criar o banco
- `.env.example` - exemplo de variáveis de ambiente
