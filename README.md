# NotebookApp

Простое консольное приложение для работы с заметками.

## Как запустить

1. Убедитесь, что у вас установлен Python 3.8 или выше.
2. Перейдите в директорию проекта `NotebookApp`.
3. Запустите программу:
. ```bash
   pip install -r requirements.txt
   python notebook_app.py

Возможности

1. Добавление заметок ID проставляет машина и предлагает пользователю после внесения в файл.
2. Просмотр списка заметок по ID и дате.
3. Редактирование заметок.
4. Удаление заметок, ID удаляется, а вносятся ID по нарастающей.
5. Фильтрация заметок по дате.

Структура проекта

NotebookApp/
│
├── README.md            # Описание проекта
│
├── data/                # Директория для хранения данных
│   └── notes.json       # Файл данных для хранения заметок
│
├── app/                 # Директория с основными модулями приложения
│   ├── controller.py    # Логика обработки команд пользователя
│   ├── model.py         # Работа с данными (CRUD операции)
│   └── view.py          # Взаимодействие с пользователем
│
└── main.py              # Главный файл для запуска приложения


Описание файлов

README.md: Файл с описанием проекта, инструкциями по запуску и использованию.

data/notes.json: Файл данных в формате JSON для хранения заметок.

app/controller.py: Модуль, содержащий логику обработки команд пользователя.

app/model.py: Модуль, отвечающий за работу с данными (CRUD операции над заметками).

app/view.py: Модуль, реализующий взаимодействие с пользователем, вывод информации и запросы на ввод данных.

main.py: Главный файл для запуска приложения, который может содержать основной цикл программы и инициализацию нужных компонентов.


Рекомендации по разработке

1. Разделение обязанностей:Каждый модуль выполняет только свои задачи, а взаимодействие между ними происходит через четкие интерфейсы.

2. Тестирование и отладка: После реализации каждого модуля провести тестирование функционала и отладку для предотвращения ошибок.

3. Документация: Поддерживать актуальную документацию (README.md) с описанием проекта, инструкциями по установке и запуску, а также описание функционала.

4. Создание новой ветки new-branch, перехожу к работе по созданию Pull requests.