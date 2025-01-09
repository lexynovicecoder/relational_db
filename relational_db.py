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
        self.categories = []

        user.events.append(self.name)

    def __str__(self):
        return f"id:{self.userID}\nname:{self.name}\nimage:{self.image}" \
               f"\ndescription:{self.description}\n categories:{self.categories}\nstatus:{self.status}\ndate:{self.date}"


class Category(BaseModel):
    def __init__(self, name: str, description: str, event: Event):
        super().__init__()
        self.name = name
        self.description = description
        self.event = event
        self.eventID = event.id
        self.contestants = []

        event.categories.append(self.name)

    def __str__(self):
        return f"id:{self.eventID}\nname:{self.name}\ndescription:{self.description}"


class Contestant(BaseModel):
    def __init__(self, name: str, image: str):
        super().__init__()
        self.name = name
        self.image = image
        self.categories = []

    def __str__(self):
        return f"name:{self.name}\nimage:{self.image}\n"


class CategoryContestant(BaseModel):
    def __init__(self, category: Category, contestant: Contestant, vote_count: int, description: str):
        super().__init__()
        self.category = category
        self.contestant = contestant
        self.vote_count = vote_count
        self.description = description
        category.contestants.append(contestant.name)
        contestant.categories.append(category.name)

    def __str__(self):
        return f"category:{self.contestant.categories}\ncontestant:{self.contestant}\nvote count:{self.vote_count}\ndescription:{self.description}"


user1 = User('cacheonly@gmail.com', '980u8493hijfiuh89nwiojw', '+1278990133')
# print(user1, '\n')
event1 = Event(name="Music Fest", description="A grand music festival.", image="musicfest.jpg", date=datetime(2025, 2, 15), user=user1, status="Upcoming")
# print(event1, '\n')
category1 = Category(name='Best Dancer', description="Person with best dance moves", event=event1)
# print(category1, '\n')
category2 = Category(name='Best Singer', description="Person with best vocals", event=event1)
contestant1 = Contestant(name="Akua", image="Akua.jpg")
contestant2 = Contestant(name="Edwin", image="Edwin.jpg")
contestant1_category1 = CategoryContestant(category= category1, contestant= contestant1, vote_count= 5, description="")
contestant1_category1 = CategoryContestant(category= category2, contestant= contestant1, vote_count= 5, description="")
contestant2_category2 = CategoryContestant(category= category2, contestant= contestant2, vote_count= 5, description="")

print(contestant1_category1)
# event1 created by user1 and categories under event1

# user2 = User('cache@gmail.com', '980u8493hi', '+1570890183')
# print(user2, '\n')
# event2 = Event(name="Tech Fest", description="A grand tech festival.", image="techfest.jpg", date=datetime(2025, 2, 15), user=user2, status="Upcoming")
# print(event2, '\n')
# user2 who created event2



