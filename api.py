from flask import Flask
from flask import request

app = Flask(__name__)


import model
import logic

_calendar_logic = logic.CalendarLogic()


class ApiException(Exception):
    pass


def _from_raw(raw_calendar: str) -> model.Calendar:
    parts = raw_calendar.split('|')
    if len(parts) == 2:
        calendar = model.Calendar()
        calendar.id = None
        calendar.data = None
        calendar.title = parts[0]
        calendar.text = parts[1]
        return calendar
    elif len(parts) == 3:
        calendar = model.Calendar()
        calendar.id = None
        calendar.data = parts[0]
        calendar.title = parts[1]
        calendar.text = parts[2]
        return calendar
    else:
        raise ApiException(f"invalid RAW calendar data {raw_calendar}")


def _to_raw(calendar: model.Calendar) -> str:
    if calendar.id is None and calendar.data is None:
        return f"{calendar.title}|{calendar.text}"
    else:
        return f"{calendar.data}|{calendar.title}|{calendar.text}"


API_ROOT = "/api/v1"
NOTE_API_ROOT = API_ROOT + "/calendar"


@app.route(NOTE_API_ROOT + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode('utf-8')
        calendar = _from_raw(data)
        _id = _calendar_logic.create(calendar)
        return f"new ivent data: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(NOTE_API_ROOT + "/", methods=["GET"])
def list():
    try:
        calendars = _calendar_logic.list()
        raw_calendars = ""
        for calendar in calendars:
            raw_calendars += _to_raw(calendar) + '\n'
        return raw_calendars, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(NOTE_API_ROOT + "/<_data>/", methods=["GET"])
def read(_data: str):
    try:
        calendar = _calendar_logic.read(_data)
        raw_calendar = _to_raw(calendar)
        return raw_calendar, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(NOTE_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        calendar = _from_raw(data)
        _calendar_logic.update(_id, calendar)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(NOTE_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _calendar_logic.delete(_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404

if __name__ == "__main__":
    app.run(debug=True)