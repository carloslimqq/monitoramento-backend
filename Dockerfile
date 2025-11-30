FROM python:3.11-slim

# Instalar dependências do sistema para mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Criar pasta da aplicação
WORKDIR /app

# Copiar dependências
COPY requirements.txt .

# Instalar pacotes Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Comando para iniciar API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
