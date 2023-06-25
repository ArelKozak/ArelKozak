while True:
    print("Yapmak istediğiniz işlemin numarasını girin: ")
    print("(Kesirler ve ya Virgülü işlem yapılmaz)")
    print("1 Toplama")
    print("2 Çıkarma")
    print("3 Çarpma")
    print("4 Bölme")
    x=int(input("girin: "))
    if x==1 : #Toplama
        a=int(input("Toplanıcak ilk tam sayıyı girin: "))
        b=int(input("Toplanıcak ikinci tam sayıyı girin: "))
        print(a+b)
        o=int(input("Çıkmak için 1'e basın Devam etmek için 2'ye basın: "))
        if o==1 :
            break
        elif o==2 :
            import os
            continue
        else:
            print("Lütfen Doğru Yazın")
    if x==2 : #Çıkarma
        c=int(input("Çıkarılıcak tam sayıyı girin: "))
        d=int(input("Çıkıcak tam sayıyı girin: "))
        print(c-d)
        o=int(input("Çıkmak için 1'e basın Devam etmek için 2'ye basın: "))
        if o==1 :
            break
        elif o==2 :
            continue
        else:
            print("Lütfen Doğru Yazın")
    if x==3 : #Çarpma
        e=int(input("Çarpılıcak ilk tam sayıyı girin: "))
        f=int(input("Çarpılıcak ikinci tam sayıyı girin: "))
        print(e*f)
        o=int(input("Çıkmak için 1'e basın Devam etmek için 2'ye basın: "))
        if o==1 :
            break
        elif o==2 :
            continue
        else:
            print("Lütfen Doğru Yazın")
    if x==4 : #Bölme
        z=int(input("Bölümün tam sayısını giriniz: "))
        y=int(input("Bölenin tam sayısını girin: "))
        print(z/y)
        o=int(input("Çıkmak için 1'e basın Devam etmek için 2'ye basın: "))
        if o==1 :
            break
        elif o==2 :
            continue
        else:
            print("Lütfen Doğru Yazın")
    else :
        print("Lütfen Doğru Yazın")