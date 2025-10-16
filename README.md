

# 🧪 API REST - Laboratorio Desarrollo Seguro (1er entrega)

Proyecto backend desarrollado con **FastAPI** y **MySQL**, diseñado para gestionar la **recepción y manejo de muestras en laboratorio**.  
Incluye autenticación básica (HTTP Basic), modelos ORM con SQLAlchemy y endpoints iniciales para usuarios, roles, recepciones y muestras.

---

## 🚀 Características

- Framework: **FastAPI**
- Base de datos: **MySQL 8+**
- ORM: **SQLAlchemy**
- Autenticación básica HTTP (username/password)
- Compatible con Adminer y TablePlus

---

Requerimientos:
* python3.x
* Docker Compose
* Postman o Cliente http

## Getting Started

Clonar este repositorio:
```sh
git clone https://github.com/aalesann/tp-final-desarrollo-seguro.git
```

Ingresar al directorio de trabajo:
```sh
cd tp-final-desarrollo-seguro
```


---

### Base de datos MySQL

Dentro del directorio tp-final-desarrollo-seguro:
```sh
docker compose up -d
```
---
### Servidor back-end

Instalación de Dependencias:
```sh
pip install -r requirements.txt
```

Iniciar el servidor en desarrollo:
```sh
uvicorn main:app --reload
```

Probar api:
```sh
curl -u admin:example http://localhost:8000/health
```
y 

```sh
curl -u admin:example http://localhost:8000/auth/health
```

>Alternativamente, probar con Postman o similar

