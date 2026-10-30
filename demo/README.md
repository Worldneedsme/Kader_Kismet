# Villa demosu (oyun sistemi prototipi)

Tarayıcıda çalışan, tek dosyalık bir prototip. Amaç **hareketi ve oyun sistemini** test etmek;
tüm görseller kodla çizilmiş geçici şekiller.

## Çalıştırma
- **Paylaşmak için:** `kader-kismet.html` tek dosyalık tam sürümdür. Arkadaşına gönder, çift tıklayıp tarayıcıda açsın.
  Kurulum yok; fontlar Google Fonts'tan gelir, internet yoksa sistem fontuna düşer.
- `index.html` geliştirme kaynağıdır. Değiştirdikten sonra paylaşılabilir dosyayı yeniden üret:
  `python3 demo/build_standalone.py`

## Mekân
- **Kızlar Evi** ve **Erkekler Evi** ayrı. **Havuz Başı** ortak alan; karşı cinsle orada buluşulur.
- Karşı eve sadece misafirlikte girilir; kapı ve harita kilitli görünür.
- **Bordo Oda:** Baş başa konuşma odası (mumlu sehpa, bordo koltuklar). Sadece çağrıyla girilir.

## Günlük döngü
1. **Kostüm ekranı:** Kız/erkek, isim, ten rengi, saç modeli ve rengi, üst rengi, alt tipi (şort, pantolon, elbise) ve rengi, ayakkabı, sakal; canlı önizleme ve "Rastgele" butonu. Oyuncu kendi evinde başlar.
1. **Misafirlik:** Gün içinde rastgele biri (bazen sen) 90 saniyeliğine karşı eve misafir olur ve oradakilerle konuşabilir. Sayaç ekranda görünür.
1. **Bordo Oda:**
   - Günde bir kez karşı cinsten birini 45 saniyelik baş başa konuşmaya çağırabilirsin. Etkisi normal sohbetten güçlü: beğenilen cevap +3/+2, beğenilmeyen -2.
   - Seni de çağırabilirler; reddedersen uyum -2.
   - Diğer yarışmacılar da kendi aralarında gider.
   - Herkes kimin kiminle gittiğini duyar. Match'i olanın match'iyle uyumu -2 düşer.
2. **Konuşmalar:** Birine dokununca yanına gidip 3 soruluk konuşma başlar. Cevaplar karakterin kişiliğine göre puanlanır.
   - Karşı cinsle: **uyum** (0-10). 7 ve üstünde match teklif edilir. Match tek kişiyle olur, uyum 4'ün altına düşerse biter.
   - Kendi cinsinle: **güven** (0-10). 7 ve üstünde gruba davet edilirsin ya da birlikte grup kurarsınız.
3. **Gruplar:** Başlangıçta "Havuz Kızları" (Nehir, Defne, Ece) ve "Teras Ekibi" (Kaan, Tolga) var.
   Grup renkleri isim etiketlerinde görünür. Grubun güveni 3'ün altına düşerse gruptan çıkarılırsın.
4. **Diğer yarışmacılar** kız-erkek ikililer halinde birbirinin yanına yürüyüp konuşur; uyum yüksekse gizlice match olurlar.
5. **Villa haberi:** Konuşmaların dörtte biri bitince günün olayı çıkar (dedikodu, tartışma, not...) ve ilişkileri etkiler.
6. **Villa oyunu:** Konuşmaların yarısı bitince zorunlu toplu oyun başlar. Günler sırayla değişir:
   - **Çift Yarışı (tek günler):** Match'ler birlikte, diğerleri en iyi anlaştığı kişiyle takım olur.
     Oyuncu zamanlama oyunu oynar (3 tur, alan daralır). Kazanan çift galada dokunulmaz.
   - **Grup Mücadelesi (çift günler):** Gruplar ve bağımsızlar yarışır. Oyuncu 5 saniye hızlı dokunur (halat çekme).
     Kazanan grup karşı takımdan birini koruma altına alır (genelde kendi match'ini).
7. **Gala kapısı:** Her kız her erkekle konuşmadan ve günün oyunu oynanmadan Gala açılmaz.
8. **Gala gecesi (sinematik):**
   - Altın "Gala Gecesi" açılış kartı, gece salonu; kızlar ve erkekler karşılıklı koltuklara oturur.
   - Dokunulmazlar ve match'ler spot ışığında açıklanır.
   - Gruplar ortak hedef belirler. Herkes tek tek sandığa yürür, oy pusulasını atar, yerine döner. Oyuncunun sırası gelince seçim paneli açılır.
   - Oylar sandıktan tek tek okunur, canlı sayım tablosu dolar; son oylarda gerilim için bekleme uzar.
   - En çok oyu alan veda eder ve kapıdan çıkar. Eşitlikte karşı takımla uyumu en düşük olan gider.
   - Match'ler birbirine oy vermez. Grubundan farklı oy verirsen ihanet sayılır (güven -3, gerekirse gruptan atılma).
   - "Hızlandır ×3" ile sinematik hızlanır.
9. **Yeni gün ve yeni yarışmacı töreni:** Elenenin cinsinden yeni yarışmacı gelir.
   - "Yeni Yarışmacı" açılış kartı gösterilir. Yeni gelen karşı cinsin evine girer, herkes kendini tanıtır.
   - Yeni gelen birini dansa kaldırır (müzikli dans animasyonu, uyum +2).
   - Bordo Oda'ya geçip iki kişiyi sırayla baş başa konuşmaya çağırır; sen çağrılırsan konuşma sana açılır.
   - Sonra herkes evine döner. Konuşmalar, oyun, Bordo hakkı ve dokunulmazlık sıfırlanır.

## Görsel
- Arayüz realite şovu yayın grafiği dilinde: Anton başlıklar, Barlow Condensed etiketler, siyah-beyaz zemin ve tek vurgu rengi fuşya; keskin köşeli alt bantlar, "CANLI" rozeti, sahnenin altında kayan villa haberleri bandı.
- Gökyüzü gün içinde konuşmalar ilerledikçe sabahtan gün batımına döner; evlerdeki ışık zincirleri akşama doğru parlar.
- Karakterlerde çizgi, göz kırpma, nefes alma, kaş, ayakkabı ve saç parlaması var. Havuzda simitler yüzüyor.
- Gala salonu: yıldızlı gece, altın süslemeli duvarlar, kırmızı halı, bordo koltuklar, ışıklı cam sandık.

## Diğer
- Konuşma balonları sınırlı: tam metin yalnızca senin, konuştuğun kişinin ve sana en yakın iki konuşmacının balonunda görünür; diğerlerinde küçük "•••" göstergesi çıkar.
- Havuz Başı, Kızlar Evi, Erkekler Evi; kapı paspası ya da Harita ile geçiş.
- Sohbet kutusu: telefon numarası, @kullanıcı adı ve Instagram gibi ifadeler `***` ile maskelenir.
- "Evdekiler": gruplar, uyum/güven değerleri, match ve dokunulmazlık durumu.

## Bilinçli olarak yapılmayanlar
- Gerçek çok oyunculu bağlantı (Supabase Realtime) yok; diğer karakterler basit kurallarla hareket ediyor.
- Kalıcı kayıt ve izleyici oyu yok. Kostümler oyun içinde sonradan değiştirilemiyor.
- Gerçek oyunda motor olarak Phaser + Tiled düşünülüyor; bu demo bağımlılıksız olsun diye düz Canvas ile yazıldı.
