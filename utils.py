import pickle
import json
import numpy as np
import Config

class CarDekho():
    def __init__(self,Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner):
        print("__INIT__")
        self.Year = Year
        self.Present_Price = Present_Price
        self.Kms_Driven = Kms_Driven
        self.Fuel_Type = Fuel_Type
        self.Seller_Type = Seller_Type
        self.Transmission = Transmission
        self.Owner = Owner


    def __load_save_data(self):
        
        with open (Config.MODEL_FILE_PATH , 'rb') as f:
            self.model = pickle.load(f)


        with open (Config.JSON_FILE_PATH , 'r') as f:
            self.json_data = json.load(f)


    def get_predicted_price(self):
        self.__load_save_data()
        
        Seller_Type = self.json_data['Seller_Type'][self.Seller_Type]
        Transmission = self.json_data["Transmission"][self.Transmission]
        Fuel_Type = "Fuel_Type_" + self.Fuel_Type
        
        Fuel_Type_index =self.json_data["Columns_Names"].index(Fuel_Type)
        
        test_array = np.zeros([1,self.model.n_features_in_])

        test_array[0,0] = self.Year
        test_array[0,1] = self.Present_Price
        test_array[0,2] = self.Kms_Driven

        test_array[0,Fuel_Type_index] = 1

        test_array[0,4] = Seller_Type
        test_array[0,5] = Transmission
        test_array[0,6] = self.Owner


        predicted_charges = np.around(self.model.predict(test_array)[0], 2)
        return predicted_charges
