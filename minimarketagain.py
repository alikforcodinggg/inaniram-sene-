users={
    1:{"name":"Alik","history":[],"favorites":[],"basket":[],"balance":24.0},
    2:{"name":"Nihad","history":[],"favorites":[],"basket":[],"balance":10.0},
    3:{"name":"Lenin","history":[],"favorites":[],"basket":[],"balance":123445654.0},
    4:{"name":"Memis","history":[],"favorites":[],"basket":[],"balance":3.0}
}
products={
    101:{"name":"alma","price":1.2,"category":"meyvə"},
    102:{"name":"banan","price":1.5,"category":"meyvə"},        
    201:{"name":"çörək","price":0.8,"category":"ərzaq"},
    202:{"name":"yumurta","price":2.4,"category":"ərzaq"},
    301:{"name":"cola","price":1.7,"category":"içki"},
    302:{"name":"fanta","price":1.6,"category":"içki"},
    401:{"name":"ayaqqabi","price":59,"category":"geyim"},
    402:{"name":"koynek","price":12,"category":"geyim"},
    403:{"name":"jaket","price":45,"category":"geyim"},
}


categories=["meyvə","ərzaq","içki","geyim"]
def select_user():
    print("İstifadəçilər:")
    for uid, data in users.items():
        print(uid, "-", data["name"])
    uid=int(input("ID daxil edin: "))
    if uid in users:
        print("Giriş edildi:",users[uid]["name"])
        print("Balans:",users[uid]["balance"],"AZN")
        return uid
    else:
        print("Belə istifadəçi yoxdur!")
        return select_user()        
select_user()