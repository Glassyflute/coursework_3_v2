# Курсовая работа 4 
#  

## Описание проекта
- Задание для курсовой работы по ссылке: https://skyengpublic.notion.site/4-ee227276cbde4b5b950c29772427b950
- Исходный код для курсовой работы №3 по ссылке: https://github.com/skypro-008/coursework_3_source
- Курсовая проверяет знания Flask, SQLAlchemy, Marshmallow (или любого другого валидатора на выбор), REST, CRUD, JWT
- 
- Поле email класса User является обязательным и уникальным, поэтому используется в коде вместо id пользователя там,
где это более логично (как при действиях пользователя в его профиле). 
- 
- Авторизованный пользователь (декоратор @auth_required) может видеть данные по режиссерам, фильмам или жанрам 
(всем либо одному выбранному по id) через GET запросы.
- Авторизованный админ (декоратор @admin_required) может видеть данные по режиссерам, фильмам или жанрам 
(всем либо одному выбранному по id) через GET запросы; может добавлять (POST), обновлять (PUT) или удалять (DELETE)
данные по фильмам, режиссерам, жанрам через соответствующие вьюшки directors, movies, genres. Админ может получать всю
информацию по пользователям, по выбранному пользователю, а также добавлять, обновлять и удалять пользователей. 
- Авторизованный пользователь (декоратор @auth_required) может работать с данными своего профиля: видеть всю информацию
профиля, вносить дополнительную информацию в необязательные поля name, surname, favorite_genre. Пользователь может 
менять свой пароль, указывая старый и новый пароль, при этом, получая обновленные токены. 
- Новый пользователь может пройти регистрацию, указав обязательные данные для своего профиля, через эндпоинт 
POST /auth/register. При аутентификации пользователь получает access_token, refresh_token; с помощью refresh_token
пользователь может пересоздать новую пару токенов.
- Всем новым пользователям по умолчанию разрешено иметь роль 'user' при регистрации. Роль пользователя может быть
изменена только админом. 
- 
- Информация по всем фильмам сортируется по дате выпуска (новинки), если применяется необязательный параметр status=new.
- Применяется пагинация на выводе всех данных по режиссерам, фильмам, жанрам и пользователям, если указывается 
необязательный параметр page в запросе.
- В проекте используется сложная архитектура со слоями DAO, services, views.
- Для слоя сервисов используется подход CRUD.
- Для пользователя на уровне сервисов используются доп методы на хэширование
пароля пользователя для базы данных. Пароль, указанный пользователем при регистрации или авторизации, хранится в базе 
в хэшированном виде. При проверке пользователя сравниваются хэшированные пароли. 
- 
