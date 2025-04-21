import numpy as np
import pickle

# Fonction d'activation ReLU
def ReLU(Z):
    return np.maximum(Z, 0)

# Fonction d'activation softmax
# Utilisation de softmax sur la couche de sortie pour obtenir les probabilités
def softmax(Ypred):
    exp_Ypred = np.exp(Ypred - np.max(Ypred))
    return exp_Ypred / np.sum(exp_Ypred, axis=0)

# Propagation avant qui prend en entrée les données, les poids et les biais
def propagation_avant(X, W, b, Ws, bs):
    Z = np.dot(W, X) + b
    H = ReLU(Z)
    Zs = np.dot(Ws, H) + bs
    Ypred = softmax(Zs)
    
    return Z, H, Ypred


# Fonction de prédiction dans laquelle on utilise les poids et les biais appris 
def predict(X, Wc, bc, Ws, bs):
    _, _, Ypred = propagation_avant(X.T, Wc, bc, Ws, bs)
    return Ypred


# Afin d'obtenir le nom de l'espece a partir de la prediction du modele.
def obtenir_espece_iris(Ypred):
    classes = ["Setosa", "Versicolor", "Virginica"]
    return classes[np.argmax(Ypred)]


# Fonction pour répondre avec les détails de l'iris, type prédit inclus.
def repondre_iris(features):
    longeur_sepale, largeur_sepale, longeur_petale, largeur_petale = features
    x = np.asmatrix([features])
    
    with open("./model/iris_model.pkl", "rb") as f:
        W, b, Ws, bs = pickle.load(f)
    
    # Prédire
    Ypred = predict(x, W, b, Ws, bs)
    espece = obtenir_espece_iris(Ypred)
    
    return {
        "spH": longeur_sepale,
        "spW": largeur_sepale,
        "ptH": longeur_petale,
        "ptW": largeur_petale,
        "specie": espece
    }