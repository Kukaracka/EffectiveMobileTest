# Effective Mobile Test

## Описание

Данное приложение представляет собой простую веб-службу, развернутую с использованием Docker и Docker Compose.

Архитектура включает:

* backend-сервис на FastAPI
* reverse proxy на Nginx

Nginx принимает входящие HTTP-запросы и проксирует их на backend внутри Docker-сети.

---

## Архитектура

```
Client → Nginx (port 80) → Backend (FastAPI, port 8080)
```

* Backend доступен только внутри Docker-сети
* Внешний доступ осуществляется только через Nginx

---

## Используемые технологии

* Docker
* Docker Compose
* FastAPI
* Nginx

---

## Запуск проекта

### 1. Клонировать репозиторий

```
git clone https://github.com/Kukaracka/EffectiveMobileTest
cd EffectiveMobileTest
```

### 2. Запустить контейнеры

```
docker compose up --build
```

---

## Проверка работоспособности

После запуска выполните:

```
curl http://localhost
```

Ожидаемый результат:

```
Hello from Effective Mobile!
```

