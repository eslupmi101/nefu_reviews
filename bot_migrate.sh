#!/bin/bash

# Проверяем, передан ли аргумент
if [ $# -ne 1 ]; then
    echo "Использование: $0 <ID_контейнера>"
    exit 1
fi

# Получаем ID контейнера из аргумента
container_id_1=$1
container_id_2=$2

# Формируем команду для выполнения в контейнере
command="sudo docker exec $container_id_1 poetry run alembic upgrade head"
command="sudo docker exec $container_id_2 poetry run python manage.py migrate"

# Выполняем команду
echo "Выполняется команда в контейнере $container_id: $command"
eval $command
