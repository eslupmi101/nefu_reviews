# **Nefu Reviews прототип**

**Запуск через docker**

Копировать .env. Указать в .env токен бота и localhost:8000 или домен для 
веб интерфейса
```
cp .env.dist .env
```

Запустить проект через Docker compose
```
docker compose -f docker-compose.yml up -d
или
docker-compose -f docker-compose.yml up -d
```

Провести миграции через скрипт. Указать id контейнера с ботом и с интерфейсом
```
./bot_migrate.sh
```
