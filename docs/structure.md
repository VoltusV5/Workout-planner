WorkoutPlanner/
├── frontend/                          # Папка с проектом Vue
│   ├── workout-planner-frontend/       # Основная папка проекта Vue
│   │   ├── public/                    # Статические файлы (index.html, изображения)
│   │   ├── src/                       # Исходные файлы
│   │   │   ├── assets/                # Ресурсы (например, изображения)
│   │   │   ├── components/            # Компоненты (Главная, Тренировка, Каталог)
│   │   │   ├── views/                 # Страницы (Тренировка, Выбор упражнений)
│   │   │   ├── store/                 # Vuex (состояние приложения)
│   │   │   ├── router/                # Маршруты (навигация между экранами)
│   │   │   └── App.vue                # Главный компонент
│   │   ├── package.json               # Зависимости проекта
│   │   └── README.md                  # Документация
├── backend/                           # Папка с проектом Django
│   ├── workout_planner_backend/        # Основная папка проекта Django
│   │   ├── workout_planner_backend/    # Папка с настройками проекта
│   │   │   ├── __init__.py
│   │   │   ├── settings.py            # Настройки проекта
│   │   │   ├── urls.py                # Основные маршруты
│   │   │   ├── wsgi.py
│   │   ├── workouts/                  # Приложение для тренировок
│   │   │   ├── __init__.py
│   │   │   ├── models.py              # Модели для упражнений
│   │   │   ├── serializers.py         # Сериализаторы для API
│   │   │   ├── views.py               # Представления API
│   │   │   ├── urls.py                # URL-ы API
│   │   ├── db.sqlite3                 # База данных SQLite
│   │   ├── manage.py                  # Управление проектом Django
│   │   └── requirements.txt           # Зависимости проекта
├── mobile/                            # Папка с проектом Android
│   ├── WorkoutPlannerAndroid/          # Основная папка проекта Android
│   │   ├── app/                       # Папка приложения
│   │   │   ├── src/                   # Исходные файлы
│   │   │   │   ├── main/
│   │   │   │   │   ├── java/com/example/workoutplanner/ # Kotlin код
│   │   │   │   │   │   ├── MainActivity.kt       # Главная активность
│   │   │   │   │   │   ├── WorkoutActivity.kt   # Активность тренировки
│   │   │   │   │   │   └── RetrofitClient.kt    # Для работы с API
│   │   │   │   ├── res/                   # Ресурсы (layout, изображения)
│   │   │   │   │   ├── layout/
│   │   │   │   │   │   ├── activity_main.xml
│   │   │   │   │   │   └── activity_workout.xml
│   │   ├── build.gradle                  # Настройки сборки
│   ├── gradle/                           # Настройки Gradle
│   └── build.gradle                      # Зависимости проекта
├── README.md                            # Документация проекта
└── .gitignore                           # Игнорируемые файлы для Git
