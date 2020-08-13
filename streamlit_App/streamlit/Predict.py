import os
import pandas as pd
import numpy as np
import preprocess as prepro
from joblib import load


class Predict:
    MODEL_PATH = "Model/"

    def __init__(self):
        self.X, self.y = prepro.load_training_data()
        self.clf = self.load_model().fit(self.X, self.y)
        self.gender_type = {
            0: "Femme",
            1: "Homme"
        }

    def load_model(self, path=MODEL_PATH):
        return load(os.path.join(path, "lr.joblib"))

    def predict_gender(self, X_to_pred: dict):
        X_df = pd.DataFrame([X_to_pred])
        X_df = prepro.preprocess(X_df)
        # Get the columns dummies not inquire
        X_df = X_df.reindex(labels=self.X.columns, axis=1).fillna(0)
        prediction = self.clf.predict_proba(X_df)
        text_res = f"L'algorithme prédit que vous êtes un(e) {self.gender_type[np.argmax(prediction)]} avec une " \
                   f"probabilité de {round(max(prediction[0])*100, 2)}% "
        return text_res
