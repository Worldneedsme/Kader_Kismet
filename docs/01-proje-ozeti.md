# Proje Özeti: Kader & Kısmet

> **İsim riski:** "Kısmet" kelimesi esin kaynağı programı ("Kısmetse Olur") çağrıştırıyor ve
> brief'teki "benzer isim kullanılmayacak" kuralıyla çelişiyor. Karıştırılma / haksız rekabet riski
> nedeniyle Instagram kanalı ve mağaza kaydından **önce** TÜRKPATENT araştırması (sınıf 9, 38, 41)
> ve marka avukatı görüşü şart. Bkz. [İsim adayları](03-isim-adaylari.md).

## Konsept
Flört / reality show türündeki programlardan **esinlenen**, kendi markasıyla çıkacak bir mobil oyun.
- **Hikâye modu (tek kişilik):** Oyuncu evdeki karakterlerden biri. Seçimler (kiminle konuşacak, kimi koruyacak, oylamada kime oy verecek) hikâyeyi değiştirir.
- **Online "Ev" modu (sonraki aşama):** 8-12 gerçek oyuncu sanal bir evde. Günlük döngü: sohbet, ikili konuşmalar, görevler ve ittifaklar, akşam oylama/eleme. Çift olma mekaniği, yeni gelen oyuncular, izleyici modu. Önce yavaş mod (5-7 günlük sezon), oyuncu yetmezse yapay zekâ botlarıyla doldurma.
- Hibrit plan: Önce hikâye modu, sonra online mod.

## Hukuki çizgi (taklit riskine karşı)
- Esin kaynağı programın **adı, logosu, fontu, renkleri, segment isimleri, sunucu tarzı, müziği KULLANILMAYACAK.**
- **Benzer isim de kullanılmayacak** (karıştırılma ihtimali ve haksız rekabet riski). Kendi başına duran, özgün bir isim seçilecek.
- Gerçek yarışmacılar ya da onları çağrıştıran karakterler yok. Gerçek kişi fotoğrafı yok.
- Genel tür kalıpları (aşk üçgeni, yalan, ifşa, oylama) serbest.
- Kendi terimleri ve kendine özgü mekanikler (gizli görev, izleyici sırrı) kullanılacak. Mekân fikri: Alanya'da bir otel/yaz villası.
- Lansman öncesi isim için TÜRKPATENT ön araştırması ve marka/fikri mülkiyet avukatı danışması.

> Terim notu: "gala" yerine önerilen **"Kader Gecesi"**, dinî bir gece olan "Kadir Gecesi"ne
> çok yakın okunuyor; yanlış anlaşılma ve tepki riski var. **"Yüzleşme Saati"** önerilir
> (bkz. [Açık sorular ve öneriler](07-acik-sorular-oneriler.md)).

## Faz 1: Instagram testi (geliştirmeden önce)
- Kurgusal 6-8 karakterle "dizi" havasında Reels (numaralı bölümler, sonu askıda biten).
- Görseller **gerçek oyun arayüzü** gibi olacak: sohbet ekranı, bildirim, oylama ekranı, çift kartı. Canva şablonları kullanılacak.
- Ritim: Pzt-Cuma günde 1 Reels ve hikâye anketi, Cumartesi büyük oylama, Pazar sonuç. **Anket sonucu hikâyeyi gerçekten değiştirir.**
- Ölçülecekler: anket katılımı, geri dönen yorumcular, kaydetme/paylaşım, "oyun nerede?" yorumları. Örnek hedef: 4 haftada ~1.000 bekleme listesi kaydı ya da güçlü etkileşim.
- Yayından önce 5-6 bölüm hazır tutulacak.

## Faz 0: Format analizi (senaryo kaynağı)
- Kaynak: Aşkın Gücü 1. sezon (Ara 2022 – Eyl 2023, ~245 bölüm) ve 2. sezon (Eyl 2023 – Mar 2024, ~139 bölüm).
- Hepsi izlenmeyecek. Örneklem: ilk haftalar, hafta sonu gala/final bölümleri, yeni yarışmacı haftaları, YouTube'da en çok izlenen kesitler, sezon finalleri (~30-40 bölüm ve kesitler).
- **Kişiler değil kalıplar not alınacak.**
- Analiz tablosu alanları: bölüm/tarih, olay tipi, tetikleyici, tırmanış (kaç bölüm sürdü), çözüm, izleyici tepkisi, oyuna uyarlanabilirlik (anket/mekanik fikri).

Ayrıntı: [Faz 0: Format analizi](02-faz0-format-analizi.md)

## Drama kalıpları (başlangıç listesi)
Aşk üçgeni · Stratejik/sahte çift · Yanlış anlaşılan dedikodu · Gizli konuşma ifşası · Yeni gelen · Geçmişten tanışıklık/sır · Oylamada ihanet · İttifak ve bölünme · İkinci şans · Kıskançlık krizi · İtiraf anı (izleyici bilir, karakterler bilmez)

**Bölüm iskeleti:** Kanca (ilk 2-3 sn) → Çatışma → Kırılma anı → Askıda bitiş → Anket
**Haftalık yay:** Pazartesi gerilim tohumu → hafta içi büyüme → oylamada patlama → Pazar sonuç ve yeni gerilim. Her hafta açık kalan bir "kim yalan söylüyor?" sırrı.
**Sınır:** Entrika var ama hakaret, aşağılama, şiddet yok. "Kötü" karakterlerin anlaşılır bir nedeni olmalı.

## Teknik
- React Native (arayüz), Supabase (auth, veritabanı, Realtime sohbet ve oylama, Edge Functions ve cron ile oylama gecesi zamanlaması), Lottie (animasyon), Canva (içerik).
- Hızlı mod büyürse ileride Colyseus gibi ayrı bir oyun sunucusu.
- Gelir: reklam ağırlıklı (Türkiye'de oyun içi harcama düşük), elmas veya özel sahneler.

## Riskler ve zorunluluklar
- **Moderasyon:** Küfür filtresi, şikâyet/engelleme, yapay zekâ ile mesaj kontrolü, iletişim bilgisi paylaşımını (telefon, Instagram) filtreleme.
- **Yaş:** Flört teması nedeniyle 18+ ya da gerçek buluşmaya yönlendirmeyen kurgusal yapı.
- **KVKK:** Gizlilik politikası ve aydınlatma metni.
- **Soğuk başlangıç:** Online modda botlar.
- **İçerik üretimi:** Haftada en az 1 yeni bölüm gerekli.

## Sıradaki adımlar
1. Analiz tablosunu kur (Faz 0) ve izlenecek bölüm listesini çıkar
2. İsim adayları ve TÜRKPATENT ön kontrolü
3. Karakter listesi, kişilikler, ilişki haritası
4. Arayüz ekranı şablonları (Instagram ve oyun için ortak)
5. İlk 2 haftanın bölüm senaryoları ve anket soruları
6. Instagram kanalını aç, 5-6 bölüm hazır olunca yayına başla

## Açık sorular
- Oyun/kanal adı?
- Mekân: ev mi, villa mı, Alanya'da otel mi?
- Görsel stil: illüstrasyon mu, avatar mı?
- Kendine özgü ana mekanik hangisi olacak (gizli görev, izleyici sırrı...)?
