#!/bin/bash

# Проверяем, передан ли аргумент
if [ $# -ne 1 ]; then
    echo "Использование: $0 <ID_контейнера>"
    exit 1
fi

# Получаем ID контейнера из аргумента
container_id=$1

# Формируем команду для выполнения в контейнере
command="sudo docker exec $container_id poetry run alembic upgrade head"

# Выполняем команду
echo "Выполняется команда в контейнере $container_id: $command"
eval $command
