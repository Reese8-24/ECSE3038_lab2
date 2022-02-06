from flask import Flask, request, jsonify
from datetime import datetime

app=Flask(__name__)

FAKE_DATABASE = []
FAKE_DATABASE2 =[]
count=0

#Profile CRUD
#CREATE
@app.route("/profile", methods=["POST"])
def postpro():
    uname=request.json["username"]
    r=request.json["role"]
    fcol=request.json["color"]
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    user_object = {
        "last_updated": dt_string,
        "username": uname,
        "role": r,
        "color": fcol
    }
    FAKE_DATABASE.append(user_object)
    return jsonify(user_object)


#READ
@app.route("/profile", methods=["GET"])
def getpro():
    return jsonify(FAKE_DATABASE)


#UPDATE
@app.route("/profile", methods=["PATCH"])
def patchpro():
    for uname in FAKE_DATABASE:
        uname["username"]=request.json["username"]
        for r in FAKE_DATABASE:
            r["role"]=request.json["role"]
            for fcol in FAKE_DATABASE:
                fcol["color"]=request.json["color"]
    return jsonify(FAKE_DATABASE)

#Data CRUD

#CREATE
@app.route("/data", methods=["POST"])
def postd():
    loc=request.json["location"]
    lat=request.json["lat"]
    lon=request.json["long"]
    cent=request.json["percentage_full"]

    global count
    count +=1

    data_object = {
        "id": count,
        "location": loc,
        "lat": lat,
        "long": lon,
        "percentage_full": cent
    }
    FAKE_DATABASE2.append(data_object)
    return jsonify(data_object)

#READ
@app.route("/data", methods=["GET"])
def getd():
    return jsonify(FAKE_DATABASE2)

#UPDATE
@app.route("/data/<int:id>", methods=["PATCH"])
def update(id):
    for loc in FAKE_DATABASE2:
        if loc["id"] == id:
           loc["location"] = request.json["location"]
        for lat in FAKE_DATABASE2:
                if lat["id"] == id:
                   lat["lat"] = request.json["lat"]
                   for lon in FAKE_DATABASE2:
                       if lon["id"] == id:
                          lon["long"] = request.json["long"]
                          for cent in FAKE_DATABASE2:
                              if cent["id"] == id:
                                 cent["percentage_full"] = request.json['percentage_full']
                              return jsonify(FAKE_DATABASE2)

#DELETE
@app.route("/data/<int:id>", methods=["DELETE"])
def deldata(id):
    for loc in FAKE_DATABASE2:
        if loc["id"] == id:
            FAKE_DATABASE2.remove(loc)
    return f"Success"























if __name__ == '__main__':
    app.run(
       debug=True,
       port=3000,
       host="0.0.0.0"
    )  