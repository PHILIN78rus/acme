from typing import List

import model

class StorageException(Exception):
    pass

class LocalStorage:
    def __init__(self):
        self._id_counter = 0
        self._storage = {}

    def create(self, calendar: model.Calendar) -> str:
        for existing_calendar in self._storage.values():
            if existing_calendar.data == calendar.data:
                raise StorageException(f"Data '{existing_calendar.data}' already exists.")
        self._id_counter += 1
        calendar.id = str(self._id_counter)
        self._storage[calendar.id] = calendar
        return calendar.data

    def list(self) -> List[model.Calendar]:
        return list(self._storage.values())

    def read(self, _data: str) -> model.Calendar:
        for existing_calendar in self._storage.values():
            if existing_calendar.data == _data:
                return existing_calendar
        raise StorageException(f"{_data} not found in storage")
        

    def update(self, _data: str, calendar: model.Calendar):
        for existing_calendar in self._storage.values():
            if existing_calendar.data == _data:
                calendar.id = existing_calendar.id
                self._storage[calendar.id] = calendar
                return
        raise StorageException(f"{_data} not found in storage")

    def delete(self, _data: str):
        for existing_calendar in self._storage.values():
            if existing_calendar.data == _data:
                _id = existing_calendar.id
                del self._storage[_id]
                return
        raise StorageException(f"{_data} not found in storage")