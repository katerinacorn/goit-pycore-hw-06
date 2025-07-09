from collections import UserDict
from .record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
