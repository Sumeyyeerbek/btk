#kullanıcı adı ve şifre alınız.. kullanıcı adı olarak "admin" şifre olarak 123456 girilince
#"sisteme başarıyla giriş yaptınız"yazsın ..
#yanlış girildikçe "kullanıcıadı veya şifre hatalı"yazıp
#tekrar kullanıcı adı ve şifre sorsun!!!!

while True:
    kullaniciadı=input("kullaniciadı giriniz")
    sifre=input("parolanız:")
    if kullaniciadı=="admin"and sifre=="123456":
        break
    else:
         print("kullanıcı adı veya parola hatalı")
print("sisteme başarıyla giriş yaptınız")