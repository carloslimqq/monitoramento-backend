-- script SQL para criar o banco de dados (execute no MySQL como root)
CREATE DATABASE IF NOT EXISTS monitoramento CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE monitoramento;

CREATE TABLE IF NOT EXISTS telemetria (
  id INT AUTO_INCREMENT PRIMARY KEY,
  maquina VARCHAR(50),
  parametro VARCHAR(50),
  valor DOUBLE,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
