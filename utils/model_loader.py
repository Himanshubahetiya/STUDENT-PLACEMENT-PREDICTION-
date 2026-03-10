import pickle

def load_model():
    try:
        with open("models/stp.pkl","rb") as f:
            return pickle.load(f)
    except:
        return None