# Villa demosu (hareket ve mekanik prototipi)

Tarayıcıda çalışan, tek dosyalık bir prototip. Amaç çizimleri değil **hareketi ve mekaniği** test etmek;
tüm görseller kodla çizilmiş geçici şekiller.

## Çalıştırma
`index.html` dosyasını herhangi bir tarayıcıda aç. Kurulum, sunucu veya bağımlılık yok
(fontlar Google Fonts'tan gelir, internet yoksa sistem fontuna düşer).

## Neler var
- **Karo tabanlı izometrik dünya:** Dokun-yürü, 8 yönlü yol bulma (köşe kesmeden), derinlik sıralaması,
  sürükleyerek kamera kaydırma.
- **İki alan:** Havuz Başı ve Teras. Kapı paspası ya da Harita ile geçiş.
- **Karakterler:** Nehir, Bora, Selin, Kaan, Defne (dolaşıyor), Tolga, Ece, Arda. Senaryo dokümanındaki repliklerle konuşuyorlar.
- **Konuşma:** Birine dokununca yanına gidip konuşursun; ilk tanışma güveni +4 artırır. Sohbet kutusuna yazılanlar
  baloncuk olarak çıkar, yakındaki karakter cevap verir.
- **Kulak misafiri:** Havuz başındaki sarı köşeden Selin ile Kaan'ın gizli konuşması duyulur.
  Saklanmadan 2-3 kareden fazla yaklaşırsan yakalanırsın (Güven -15).
- **Sır kartları:** "Eski tanıdıklar" (dinleyerek) ve "İmzasız not" (terastaki masada).
- **Oturma:** Şezlong ve sandalyeler.
- **Moderasyon örneği:** Sohbete yazılan telefon numarası, @kullanıcı adı ve Instagram gibi ifadeler `***` ile maskelenir.
- **Yüzleşme Saati** geri sayımı (şimdilik süs).

## Bilinçli olarak yapılmayanlar
- Gerçek çok oyunculu bağlantı (Supabase Realtime) yok; diğer karakterler senaryolu.
- Avatar giydirme, kalıcı kayıt ve oylama ekranı yok.
- Gerçek oyunda motor olarak Phaser + Tiled düşünülüyor; bu demo bağımlılıksız olsun diye düz Canvas ile yazıldı.
  Mekanikler (ızgara, yol bulma, bölgeler) birebir taşınabilir.
