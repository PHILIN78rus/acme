from typing import List

import model
import storage

class DBException(Exception):
    pass

class CalendarDB:
    def __init__(self):
        self._storage = storage.LocalStorage()

    def create(self, calendar: model.Calendar) -> str:
        try:
            return self._storage.create(calendar)
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Calendar]:
        try:
            return self._storage.list()
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, _data: str) -> model.Calendar:
        try:
            return self._storage.read(_data)
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, _data: str, calendar: model.Calendar):
        try:
            return self._storage.update(_data, calendar)
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, _data: str):
        try:
            return self._storage.delete(_data)
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
