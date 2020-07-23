import os

import preprocess as prepro
import numpy as np
import pandas as pd
from joblib import load


class GenderClassifier:
    # schema_extra = {
    #     "example": {
    #         "Favorite Color": "['Cool','Neutral','Warm']",
    #         "Favorite Music Genre": "['Rock','Hip hop','Folk/Traditional','Jazz/Blues','Pop','Electronic','R&B and "
    #                                 "soul']",
    #         "Favorite Beverage": "['Vodka','Wine','Whiskey','Doesn't drink','Beer','Other']",
    #         "Favorite Soft Drink": "['7UP/Sprite','Coca Cola/Pepsi','Fanta','Other']",
    #     }
    # }

    MODEL_PATH = "../Model"

    def __init__(self):
        self.X, self.y = prepro.load_training_data()
        self.clf = self.train_model().fit(self.X, self.y)
        self.gender_type = {
            0: "Femme",
            1: "Homme"
        }

    def train_model(self, path=MODEL_PATH):
        return load(os.path.join(path, "lr.joblib"))

    def gender_predict(self, features: dict):
        # Convert the jsonrequest to dict
        X_dict = {"Favorite Color": features["Favorite Color"],
                  "Favorite Music Genre": features["Favorite Music Genre"],
                  "Favorite Beverage": features["Favorite Beverage"],
                  "Favorite Soft Drink": features["Favorite Soft Drink"]}

        # Convert the dict request to dataframe
        X_df = pd.DataFrame([X_dict])
        X_df = prepro.preprocess(X_df)
        # Get the columns dummies not inquire
        X_df = X_df.reindex(labels=self.X.columns, axis=1).fillna(0)
        prediction = self.clf.predict_proba(X_df)
        dict_res = {"class": self.gender_type[np.argmax(prediction)],
                    'probabilité': round(max(prediction[0]), 2)}
        text_res = f"L'algorithme prédit que vous êtes un(e) {self.gender_type[np.argmax(prediction)]}\n" \
                   f"avec une probabilité de {round(max(prediction[0]), 2) * 100}%"
        return text_res
