class User:
    def __init__(self, userpkID, password, phone_number, createdAt, is_deleted, deletedAt, updateAt):
        self.userpkID = userpkID
        self.password = password
        self.phone_number = phone_number
        self.createdAt = createdAt
        self.is_deleted = False
        self.deletedAt = None
        self.updateAt = None


class Event:
    def __init__(self, user, fkID, pkID, name, description, image, updateAt, date, deletedAt, status, is_deleted,
                 createdAt):

        self.user = user
        self.pkID = pkID
        self.name = name
        self.description = description
        self.image = image
        self.updateAt = None
        self.date = date
        self.deleteAt = None
        self.status = status
        self.is_deleted = False
        self.createdAt = createdAt
        self.fkID = fkID

first_user = User(userpkID='198',password="bduw9", phone_number="+233 9872019101", createdAt="1/08/26",
                  is_deleted=False, deletedAt=None, updateAt=None)
first_event = Event(user=first_user, fkID=first_user.userpkID, pkID="0273", name='talent_show',
                    description="showing off talents", image="image.png", updateAt=None, date="3/09/27",
                    deletedAt=None, status="in_progress", is_deleted=False,createdAt=first_user.createdAt)


