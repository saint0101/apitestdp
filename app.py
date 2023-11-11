# !/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
from flask import Flask, request


# creation de l'application
app = Flask(__name__)

# liste contenant les données
stores = [
    {
        "name": "My Store",
        "items":
            [
                {
                    "name": "my item",
                    "price": 15.99
                }
            ]
    }
]

# creation d'une fontion qui retournera toutes les données
@app.get("/store")
def get_stores():
    """ get all stores in databaase """
    return {"stores": stores}


@app.post("/store")
def create_store():
    """ creaet a store and save in database """
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    """ creation d'un aticle dans un magasin existant """
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "le magasin n'existe pas!"}, 404


@app.get('/store/<string:name>/')
def get_store(name):
    """ afficher le contenu d'un magasin spécifique / """
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "le magasin n'existe pas !"}, 404


@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    """ retourner seulment les articles du magasin demander"""
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404

