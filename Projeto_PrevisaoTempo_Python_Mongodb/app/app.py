from flask import Flask, request
import requests
import pymongo
app = Flask(__name__)

@app.route("/api/v1/previsaotempo", methods=["GET"])
def obterprevisao():
    api_url = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}".format(
    city=request.args.get("city"), api_key="c20f9a317c829284e2fe71c94b5d1224"
    )
    response = requests.get(api_url)
    if response.status_code != 200:
        return {"error": "Não foi possível obter os dados da previsão do tempo."}
    response_json = response.json()
    response_json_serializable = response_json.copy()  
    response_json_serializable.pop("_id", None)
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["raizen"]
    collection = db["previsao"]
    collection.insert_one(response_json_serializable)
    return response_json
if __name__ == "__main__":
    app.run(debug=True)
