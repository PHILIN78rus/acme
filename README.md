## запуск приложения

```
./venv/bin/flask --app ./acme/server.py run
```


## cURL тестирование

### добавление нового события
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2000-12-31|title|text"
```

### получение всего списка событий
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### получение заметки по дате / data == 2000-12-31
```
curl http://127.0.0.1:5000/api/v1/calendar/2000-12-31/
```

### обновление текста заметки по дате / data == 2000-12-31 /  новый текст == "new text"
```
curl http://127.0.0.1:5000/api/v1/calendar/2000-12-31/ -X PUT -d "2000-12-31|title|new text"
```

### удаление заметки о дате / data == 2000-12-31
```
curl http://127.0.0.1:5000/api/v1/calendar/2000-12-31/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2000-12-31|title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/
1|2000-12-31|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2000-12-31|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2000-12-31|title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2000-12-31|title|new text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2000-12-31|title|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: text lenght > MAX: 120

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2000-12-31|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 60

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/calendar/
-- пусто --
```
