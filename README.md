# 🤖 DataMind

Мультиагентная система анализа данных на базе **LangGraph + FastAPI + SQL + Selectel S3**.

Пользователь загружает CSV-файлы или задаёт вопросы на естественном языке, а система
разбирает запрос через цепочку LangGraph-агентов, обращается к базе данных и возвращает
структурированный ответ.

Полное описание задания — в [phase3_README.md](phase3_README.md).

## Структура проекта

```
project/
├── app/
│   ├── api/          # FastAPI роутеры
│   ├── agents/       # LangGraph граф и узлы
│   ├── db/           # SQLAlchemy модели и миграции
│   ├── storage/      # Клиент Selectel S3
│   └── main.py
├── data/             # Тестовый датасет orders.csv
├── .env.example
├── docker-compose.yml
└── README.md
```

## Стек

| Технология | Роль |
|---|---|
| LangGraph | Граф агентов: роутинг, инструменты, синтез ответа |
| FastAPI | REST API: загрузка файлов, запросы, история сессий |
| PostgreSQL | Хранение данных, истории запросов, логов агентов |
| Selectel Object Storage | Хранение исходных CSV (S3-совместимый API) |

## Быстрый старт

Окружение управляется через [uv](https://docs.astral.sh/uv/).

```bash
# 1. Установить зависимости (создаст .venv автоматически)
uv sync

# 2. Настроить переменные окружения
cp .env.example .env
# заполните DATABASE_URL, DEEPSEEK_API_KEY и ключи Selectel S3

# 3. Поднять базу данных
docker-compose up -d db

# 4. Запустить API
uv run uvicorn app.main:app --reload
```

После запуска документация доступна на http://localhost:8000/docs

## Переменные окружения

См. [.env.example](.env.example).
