from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.deleted_at = None
        self.is_deleted = False


class User(BaseModel):
    def __init__(self, email: str, password: str, phone_number: str):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.events = []

    def __str__(self):
        return f"id:{self.id}\nemail:{self.email}\npassword:{self.password}\nphone number:{self.phone_number}\n events:{self.events}"

class Event(BaseModel):
    def __init__(self, name: str, description: str, image: str, date: datetime, user: User, status: str):
        super().__init__()

        self.user = user
        self.name = name
        self.description = description
        self.image = image
        self.date = date
        self.status = status
        self.userID = user.id


user = User('cacheonly@gmail.com', '980u8493hijfiuh89nwiojw', '+1278990133')
print(user)
