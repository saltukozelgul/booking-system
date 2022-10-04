def getUsersFromMongo(client, id):
    db = client["booking"]
    col = db["reservations"]
    users = col.find({"activity_id": id})
    return users

def addReservationToMongo(client, data):
    db = client["booking"]
    reservations = db["reservations"]
    data = convertLowerCase(data)

    if reservations.find_one({"email": data["email"], "activity_id": data["activity_id"], "phone": data["phone"] , "name": data["name"]}):
        return "Zaten bu etkinliğe daha öncesinde kayıt olmuşsunuz. {E}"
    
    reservations.insert_one(data)
    return "Rezervasyon işleminiz başarıyla gerçekleştirildi. {S}"

def getReservationByIdAndNumber(client, id, number):
    db = client["booking"]
    reservations = db["reservations"]

    founded = reservations.find_one({"activity_id": id, "phone": number})
    if founded:
        return founded
    return None


def deleteReservationByIdAndNumber(client, id, number):
    db = client["booking"]
    reservations = db["reservations"]

    founded = reservations.find_one({"activity_id": id, "phone": number})
    if founded:
        reservations.delete_one(founded)
        return True
    return False

def convertLowerCase(data):
    for key in data.keys():
        data[key] = data[key].lower()
    return data
