def sayi():
    u = input("Kullanıcı izinleri: ")
    g = input("Grup izinleri: ")
    o = input("Diğerlerinin izinleri: ")
    ks = 0
    gs = 0
    ds = 0
    for i in u:
        if i == "r":
            ks += 4
        if i == "w":
            ks += 2
        if i == "x":
            ks += 1
    for i in g:
        if i == "r":
            gs += 4
        if i == "w":
            gs += 2
        if i == "x":
            gs += 1
    for i in o:
        if i == "r":
            ds += 4
        if i == "w":
            ds += 2
        if i == "x":
            ds += 1
    snc = [ks, gs, ds]
    for i in snc:
        print(i, end="")
sayi()