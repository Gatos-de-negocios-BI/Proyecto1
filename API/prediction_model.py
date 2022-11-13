from joblib import load
import pickle as pkl
from TextPreprocessor import TextPreprocessor

class PredictionModel:

    def __init__(self):
        self.model = pkl.load(open('../Pipeline/pipeline.pkl', 'rb'))

    def make_prediction(self, data):
        result = self.model.predict(data)
        return result
