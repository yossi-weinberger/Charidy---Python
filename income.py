from datetime import datetime
from mongo_config import client


# client = MongoClient("localhost", 27017)
db = client.charidy
income_collection = db.income_collection
total_tithe_collection = db.total_tithe_collection


class Income:
    # total_tithe = total_tithe_collection.find_one({"total": {"$exists": True}})['total']
    # print(total_tithe)
    document = total_tithe_collection.find_one()
    if document is None:
        total_tithe = 0
        total_tithe_collection.insert_one({"total": total_tithe})
    else:
        total_tithe = document.get('total', 0)

    def __init__(self):
        self.description = input("Type the income description: ")
        self.amunt = float(input("Type the amunt: "))
        self.day = datetime.now()
        self.day_date = self.day.strftime("%d/%m/%Y %H:%M:%S")
        self.tithe = self.amunt/10

    def save_total_tithe(self):
        Income.total_tithe += self.tithe
        total_tithe_collection.update_one({}, {"$set": {"total": Income.total_tithe}})

    def save_income(self):
        income_collection.insert_one({"description": self.description,
                                      "amunt": self.amunt,
                                      "date": self.day_date,
                                      "tithe": self.tithe,
                                      "Total tithe": Income.total_tithe})

    def __repr__(self):
        return (f"\n\ndescription:{self.description}\n"
                f"amunt:{self.amunt}\n"
                f"date: {self.day_date}\n"
                f"tithe: {self.tithe}\n"
                f"total tithe: {Income.total_tithe}")
