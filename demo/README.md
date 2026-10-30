# Villa demosu (oyun sistemi prototipi)

Tarayıcıda çalışan, tek dosyalık bir prototip. Amaç çizimleri değil **hareketi ve oyun sistemini** test etmek;
tüm görseller kodla çizilmiş geçici şekiller.

## Çalıştırma
`index.html` dosyasını herhangi bir tarayıcıda aç. Kurulum, sunucu veya bağımlılık yok
(fontlar Google Fonts'tan gelir, internet yoksa sistem fontuna düşer).

## Oyun döngüsü
1. **Giriş:** Kız ya da erkek karakter seçilir, isim girilir.
2. **Gün:** Birine dokununca yanına gidip konuşma başlar. Karşı cinsle yapılan konuşmada 3 soru gelir;
   cevaplar karakterin kişiliğine göre **uyumu** (0-10) artırır ya da düşürür.
   - Uyum 7 ve üstüyse karakter **match** teklif eder. Match'in tek kişi; yeni match eskisini bitirir.
   - Karakter başka biriyle match'liyse teklif etmez ("kalbim başka yerde").
   - Sonraki günlerde uyum 4'ün altına düşerse match biter.
   - Aynı cinsle konuşma kısa bir arkadaş sohbetidir, sayılmaz.
3. **Diğer yarışmacılar** kendi aralarında (kız-erkek) yürüyüp konuşur, gerekirse diğer alana geçer;
   uyumları yüksekse gizlice match olurlar.
4. **Gala kapısı:** Evdeki her kız her erkekle konuşmadan (oyuncu dahil) Gala butonu açılmaz. Sayaç üstte.
5. **Gala:**
   - Önce gün içinde oluşan match'ler açıklanır.
   - Herkes karşı takımdan birini eleme için seçer. Yarışmacılar en düşük uyumlu olduklarını seçer, kendi match'lerini seçmez.
   - Match olanların aleyhine verilen oylardan biri silinir (+1 avantaj).
   - En çok net oyu alan villadan ayrılır. Eşitlikte uyumu en düşük olan gider. Oyuncu da elenebilir.
6. **Yeni gün:** Elenenin cinsinden yeni bir yarışmacı girer, konuşmalar sıfırlanır, uyumlar ve match'ler korunur.

## Diğer
- Havuz Başı ve Teras alanları; kapı paspası ya da Harita ile geçiş.
- Sohbet kutusu: yazılanlar baloncuk olur, yakındaki karakter cevap verir. Telefon numarası, @kullanıcı adı ve
  Instagram gibi ifadeler `***` ile maskelenir (moderasyon örneği).
- "Evdekiler" ekranı: kiminle konuştuğun, uyumlar, match durumu, diğerlerinin kalan konuşma sayısı.

## Bilinçli olarak yapılmayanlar
- Gerçek çok oyunculu bağlantı (Supabase Realtime) yok; diğer karakterler yapay zekâsız basit kurallarla hareket ediyor.
- Avatar giydirme, kalıcı kayıt ve izleyici oyu yok.
- Gerçek oyunda motor olarak Phaser + Tiled düşünülüyor; bu demo bağımlılıksız olsun diye düz Canvas ile yazıldı.
  Izgara, yol bulma ve oyun kuralları birebir taşınabilir.
