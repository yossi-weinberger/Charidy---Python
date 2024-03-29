from datetime import datetime

# import mongo_config
from mongo_config import client
# from pymongo import MongoClient

# client = mongo_config.client
db = client.charidy
donation_collection = db.donation_collection
total_tithe_collection = db.total_tithe_collection


class Donation:
    # total_tithe = total_tithe_collection.find_one({"total": {"$exists": True}})['total']
    # print(total_tithe)

    document = total_tithe_collection.find_one()
    if document is None:
        total_tithe = 0
        total_tithe_collection.insert_one({"total": total_tithe})
    else:
        total_tithe = document.get('total', 0)

    def __init__(self):
        self.description = input("Type the donation description: ")
        self.amunt = float(input("Type the amunt: "))
        self.day = datetime.now()
        self.day_date = self.day.strftime("%d/%m/%Y %H:%M:%S")
        # self.tithe = self.amunt/10

    def save_total_tithe(self):
        Donation.total_tithe -= self.amunt
        total_tithe_collection.update_one({}, {"$set": {"total": Donation.total_tithe}})

    def save_donation(self):
        donation_collection.insert_one({"description": self.description,
                                        "amunt": self.amunt,
                                        "date": self.day_date,
                                        "Total tithe": Donation.total_tithe})

    def __repr__(self):
        return (f"\n\ndescription:{self.description}\n"
                f"amunt:{self.amunt}\n"
                f"date: {self.day_date}\n"
                # f"tithe: {self.tithe}\n"
                f"total tithe: {Donation.total_tithe}")
