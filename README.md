

## запуск приложения
```
flask --app ./acme/server.py run
```


### получение всего списка заметок
```
curl http://127.0.0.1:5000/api/v1/calendar/
```


### добавление новой заметки
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-01|title1|text1"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-02|title2|text2"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-03|title3|text3"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-04|title4|text4"
```


### получение заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```


### обновление текста заметки по идентификатору / ID == 1 /
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "new title|new text"
```


### удаление заметки по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```


### удаление всех заметок
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X DELETE
```


### проверка переполнения
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-04|title|text"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-04|title|text"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-05|titleLONG1234567890987654321234567|text"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-06|title|textLONG000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
```


### отладка
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X DELETE
curl http://127.0.0.1:5000/api/v1/calendar/
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-01|title|text"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-02|title|text"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-03|title|text"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-01|title|text"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-03|titleLONG1234567890987654321234567|text"
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2023-11-03|title|textLONG000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
curl http://127.0.0.1:5000/api/v1/calendar/
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "new title|new text"
curl http://127.0.0.1:5000/api/v1/calendar/
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
curl http://127.0.0.1:5000/api/v1/calendar/ -X DELETE
curl http://127.0.0.1:5000/api/v1/calendar/
```


