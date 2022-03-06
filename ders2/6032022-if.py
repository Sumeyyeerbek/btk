#KARŞILAŞTIRMA OPERATÖRLERİ
"""
<: küçüktür
>: büyüktür
<= :küçük eşit
>= :büyük eşit
== : eşittir
!= : eşit değildir
"""
cinsiyet=input("Bir harf giriniz:")

if cinsiyet=="e" or cinsiyet:"E"# or 2 şarttan biri doğru ise çalışır
    Print ("Cinsiyet olarak Erkek girdiniz")
    print("if içerisinden selamlar")
elif cinsiyet =="k" or cinsiyet:#2. veya daha sonraki şartları eklemek için elif kullanılır
    print("cinsiyet olarak kadın girdiniz")
    print("Şuanda elif içinden mesaj veriyorum")
else:#şartların dışında herhangi birşey girilirse çalışır
    print("ben sana e ya da k gir demedim mi?")
print("şuanda if dışındasın")