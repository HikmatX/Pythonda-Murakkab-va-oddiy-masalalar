print('           ')
# 1-savol: Umid marketda konfet narxi
x = 10;  # Masalan 10kg konfet
f = 30000;  #Masalan 30.000 so`m dursa
narx = f / x;
print("Javob 1kg konfet",narx, 'so`m turadi') #Javob 1kg konfet 3000 so`m turadi
print('           ')
# 2-savol: Uy devorini o'rash
uzunlik = 15
eni = 25
perimetr = 2 * (uzunlik + eni)
print("Javob devor maydoni", perimetr, "Metr kvadrat")  #Javob devor maydoni 80 Metr kvadrat
print('           ')
# 3-savol: UZB vs ENG Futbol o'yini
taym = 45;
qoshimcha_vaqt = 5;
jami_vaqt = (taym + qoshimcha_vaqt) * 2;
gol_har_15_min = jami_vaqt / 15;
print("o`zbekiston jami", gol_har_15_min, "ta go`l uradi");
print('           ')

# 4-savol: Dilnura har kuni 4 ta Snickers yeydi, har bir Snickersda 250 kkal bor ekan
har_kuni = 4;
snickers_kkal = 250; #internet malumotiga ko`ra
jami_kkal = har_kuni * snickers_kkal;
print('Dilnura har kuni', jami_kkal , 'Kkal snikers istemol qiladi');
print('           ')

# 5-savol: 4 Ahmad piyoda 1000 qadam bosdi, 1 qadam taxminan 0.27 kkal bo’lsa u jami qancha energiya sarf qildi?
qadam_soni = 1000;
kkal_har_qadam = 0.27;
jami_energiya = qadam_soni * kkal_har_qadam;
print("Ahmad 100 qadam uchun", jami_energiya, "kkal energiya sarf qildi");
print('           ')

# 6-savol: Google kompaniyasi yiliga X mln$ daromad qiladi. Yil boshidagi statistikaga qaraganda. Uning daromadi oyiga 35.8% oshsa, shu oy u qancha daromad qiladi?
Nomalum_daromad = 224.47; #google malumotiga ko`ra In 2024, it is anticipated to reach $273.37 billion
a = Nomalum_daromad / 12;
# Oylik o'sish foizi
foiz = a + 0.358;
print("Ushbu oy daromad:", foiz, "mlrd$");
print('           ')

# 7-savol: 7. Angliya va O’zbekiston futbo’l o’yinida terma jamoamiz har 15 minutdan go’l ursa hisob qancha bo’ladi. Qo’shimcha vaqtlar hisobga olinmasin.
time = 45;
obshiy = time * 2;
gol_har_15_min = obshiy / 15;
print("o`zbekiston jami", gol_har_15_min, "ta go`l uradi");
print('           ')

# 8-savol: Ahmad aka uyini xavfsizlik uchun uyini devor bilan o’ramoqchi
uyning_uzunligi = 15;
uyning_eni = 25;
balanddlik = 1.5;
gisht_uzunligi = 24;
gisht_qalinligi = 5;
uzunlik_devori = 2 * (uyning_uzunligi * balanddlik);
eni_devori = 2 * (uyning_eni * balanddlik);
umumiy_yuza = uzunlik_devori + eni_devori;
gisht_yuza = (gisht_uzunligi * gisht_qalinligi) / 10000;
kerakli_gisht_soni = umumiy_yuza / gisht_yuza;
print("Kerakli g'ishtlar soni:", kerakli_gisht_soni);
print('           ')

# 9-savol:Bu energiyani chiqarib yuborish uchun Firdavsbekjon qancha qadam bosishi kerak?
kaloriya = 502.4;
snickers_soni = 2;
jami_kaloriya = kaloriya * snickers_soni;
bir_qadam_kkal = 0.04; #O‘rtacha odam 1 qadamda 0.04 kkal
qadamlar_soni = jami_kaloriya / bir_qadam_kkal;
print("Firdavsbekjon energiyani chiqarib yuborish uchun", qadam_soni, "ta qadam yurishi kerak");
print('           ')



# interger-1
L1 = 465
L2 = 200
L3 = 37
L4 = 123
toliq_metrlar_soni1 = L1 // 100
toliq_metrlar_soni2 = L2 // 100
toliq_metrlar_soni3 = L3 // 100
toliq_metrlar_soni4 = L4 // 100
print("Integer1 natijalar:",toliq_metrlar_soni1,",", toliq_metrlar_soni2,",", toliq_metrlar_soni3,",", toliq_metrlar_soni4)
print(        )

# interger-2
M1 = 3000
M2 = 4561
M3 = 712
M4 = 12563
toliq_tonnalar_soni1 = M1 // 1000
toliq_tonnalar_soni2 = M2 // 1000
toliq_tonnalar_soni3 = M3 // 1000
toliq_tonnalar_soni4 = M4 // 1000
print("Integer2 natijalar:")
print(toliq_tonnalar_soni1)
print(toliq_tonnalar_soni2)
print(toliq_tonnalar_soni3)
print(toliq_tonnalar_soni4)
print(        )

# interger-2
bit = int(input("Faylning bitdagi hajmini kiritning; Bit to KB"));
bit_to_kb =  bit // 1024;
print(bit_to_kb)
print(        )

# interger-6:
son = int(input("Ikki xonali sonni kiriting: "));
onliklar = son // 10;
birlar = son % 10;
print("O'nliklar xonasidagi raqam:", onliklar);
print(f"Birlar xonasidagi raqam:", birlar);
print('           ')

# interger-7:
berilgan_son = int(input("Ikki xonali son kiriting va yig`indisini ko`ring: "));
digit1 = berilgan_son // 10;
digit2 = berilgan_son % 10;
yigindi = digit1 + digit2;
print("Kiritilgan 2 xonali son:", berilgan_son);
print("Birinchi raqam:", digit1);
print("Ikkinchi raqam:", digit2);
print("Raqamlar yig'indisi:", yigindi);
print('           ')

# 8-intergerga ummuman tushunmadim!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# interger-9:
uch_xonali_son = int(input("Uch xonali sonni kiriting: "));
yuzliklar = uch_xonali_son // 100;
onliklar = uch_xonali_son // 10;
birlar = uch_xonali_son % 10;
print("Yuzliklar xonasidagi raqam:", yuzliklar);
print("O'nliklar xonasidagi raqam:", onliklar);
print(f"Birlar xonasidagi raqam:", birlar);
print('           ')

# interger-10:#birinchi 1liklar xonasidagi raqam keyin esa 10liklar xonasidagi raqam
uch_xonali_soon = int(input("uch xonali sonni kiriting interger-10:"));
yuzliklar = uch_xonali_soon // 100;
onliklar = uch_xonali_soon // 10;
birlar = uch_xonali_soon % 10;
print(f"Birlar xonasidagi raqam:", birlar); 
print("O'nliklar xonasidagi raqam:", onliklar);
print('           ')

# interger-11:
berillgan_son = int(input("Uch xonali son kiriting va yig`indisini ko`ring: "));
digit1 = berillgan_son // 100;
digit2 = berillgan_son // 10;
digit3 = berillgan_son % 10;
yigindi = digit1 + digit2;
print("Kiritilgan 3 xonali son:", berillgan_son);
print("Birinchi raqam:", digit1);
print("Ikkinchi raqam:", digit2);
print("Uchinchi raqam:", digit3);
print("Raqamlar yig'indisi:", yigindi);
print('           ')

# interger-12:
nuumber = int(input("Uch xonali son kiriting va teskari yozilishi ko`ring: "));
raqam1 = nuumber // 100;
raqam2 = (nuumber // 10) % 10;
raqam3 = nuumber % 10;
reversed_nuumber = raqam3 * 100 + raqam2 * 10 + raqam1;
print("Uch xonali son:", nuumber);
print("Birinchi raqam:", raqam1);
print("Ikkinchi raqam:", raqam2);
print("Uchinchi raqam:", raqam3);
print("Teskari tartibdagi son:", reversed_nuumber);
print('           ')


# interger-15
kiritilgan_son = int(input("Uch xonali son kiriting va ko`ring: "));
kirish1 = kiritilgan_son // 100;
kirish2 = (kiritilgan_son // 10) % 10;
kirish3 = kiritilgan_son % 10;
print(kirish2);
print(kirish1);
print(kirish3);
print('           ')

# interger-16
kiritilgan_son = int(input("Uch xonali son kiriting va ko`ring-2:"));
kirish1 = kiritilgan_son // 100;
kirish2 = (kiritilgan_son // 10) % 10;
kirish3 = kiritilgan_son % 10;
print(kirish1);
print(kirish3);
print(kirish2);
print('           ')

# interger-17
kiritilgan_son_2 = int(input("999+ son kiriting va sizga uni ichidagi yuzliklar xonasiga kiruvchi sonni aniqlab berman:"));
yuzlikni_aniqlash = kiritilgan_son_2 / 100;
print(yuzlikni_aniqlash);
print('           ')

# interger-18
kiritilgan_son_3 = int(input("999+ son kiriting va sizga uni ichidagi yuzliklar xonasiga kiruvchi sonni aniqlab berman:"));
mingliklarni_aniqlash = kiritilgan_son_3 / 1000;
print(mingliklarni_aniqlash);
print('           ')

# interger-19
N = int(input("Kun boshidan o'tgan sekundlarni kiriting "));
minutes = N // 60;
print("To'la o'tgan minutlar:", minutes);
print('           ')

# interger-20
H = int(input("Kun boshidan o'tgan sekundlarni kiriting "));
Hour = N // 3600;
print("To'la o'tgan Soatlar:", Hour);
print('           ')

# interger-21
second_and_minut = int(input("Kun boshidan o'tgan sekundlarni kiriting "));
minutes2 = second_and_minut // 60;
print("Kun boshidan o'tgan sekundlar:", second_and_minut);
print("To'la o'tgan minutlar:", minutes2);
print('           ')

# interger-22
hour_and_minut = int(input("Kun boshidan o'tgan sekundlarni kiriting "));
hour2 = hour_and_minut // 3600;
print("Kun boshidan o'tgan sekundlar:", hour_and_minut);
print("To'la o'tgan soatlar:", hour2);
print('           ')

# interger-23
hour_second_and_minut = int(input("Kun boshidan o'tgan sekundlarni kiriting "));
hour3 = hour_second_and_minut // 3600;
minutes3 = hour_second_and_minut // 60;
print("Kun boshidan o'tgan sekundlar:", hour_second_and_minut);
print("To'la o'tgan soatlar:", hour3);
print("To'la o'tgan minutlar:", minutes3);
print('           ')


# interger-13 va 14 ga tushunmadim:

