from flask import Flask , request, render_template, jsonify
from utils import CarDekho
import Config

app = Flask(__name__)

@app.route("/home")
def home():

    return render_template("new.html")


@app.route("/Car_dekho/price_prediction",methods = ['POST'])
def pred_charges():
    data = request.form
    print("DATA",data)

    Year                  = int(data.get('Year'))
    Present_Price         = float(data.get('Present_Price'))
    Kms_Driven            = float(data.get('Kms_Driven'))
    Fuel_Type             = data.get('Fuel_Type')
    Seller_Type           = data.get('Seller_Type')
    Transmission          = data.get('Transmission')
    Owner                 = int(data.get('Owner'))



    obj = CarDekho(Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner)
    pred_price = obj.get_predicted_price()

    
    return render_template("new.html",prediction = pred_price)


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = Config.PORT_NUMBER)

