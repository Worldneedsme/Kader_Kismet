# Arayüz Şablonları (Instagram + Oyun ortak)

Amaç: Instagram'daki Reels görselleri **gerçek oyun ekranı** gibi görünsün; oyun geliştirilirken
aynı ekranlar React Native'e taşınsın. Bu yüzden her şablon bir oyun bileşenine karşılık gelir.

## Genel ölçüler
- Tuval: **1080 × 1920** (9:16), Canva'da "Instagram Reels" boyutu.
- **Güvenli alan:** Üstten 250 px ve alttan 450 px'e önemli içerik koyma (Reels arayüzü, açıklama
  ve butonlar buraya biner). Sağ kenardan 150 px'i de boş tut (beğeni/yorum ikonları).
- Telefon çerçevesi kullanma; ekran tam tuvali kaplasın, "uygulamanın içindeymiş" hissi versin.

## Görsel kimlik (öneri, isim kararından sonra kesinleşir)
Esin kaynağı programın renk ve fontlarından bilinçli olarak uzak durulur.

| Token | Renk | Kullanım |
|-------|------|----------|
| `gece` | `#1B2A41` | Arka plan (koyu tema varsayılan; Reels'te daha sinematik) |
| `turunc` | `#F28C28` | Ana vurgu, butonlar, oy rengi |
| `kum` | `#F3E9DC` | Kart yüzeyleri, metin (koyu zeminde) |
| `deniz` | `#2BB3A3` | Olumlu durum, çift olma, "güvende" |
| `mercan` | `#E4572E` | Tehlike, ifşa, "eleme riski" |
| `gri` | `#8A94A6` | İkincil metin, zaman damgası |

- **Font:** Türkçe karakter (ğ, ş, ı, İ) desteği olan Google Fonts: başlıklar için *Fraunces*,
  arayüz metni için *Manrope*. Canva'da ikisi de mevcut.
- **Karakter görselleri:** Gerçek kişi fotoğrafı **yok**. Tutarlı tek stil illüstrasyon portreler
  (bkz. [Açık sorular ve öneriler](07-acik-sorular-oneriler.md)). Her karakterin sabit bir
  imza rengi olur; sohbet balonu kenarı ve isim etiketi bu renkte.

## Şablon listesi

| # | Şablon | Oyun bileşeni | İçerik alanları | Hangi bölümlerde |
|---|--------|---------------|-----------------|------------------|
| 1 | **Grup sohbeti** ("Villa" kanalı) | `GroupChat` | Kanal adı, çevrimiçi sayısı, 3-6 mesaj balonu, "yazıyor..." göstergesi | Her gün; çatışma sahnesi |
| 2 | **İkili mesaj** | `DirectChat` | Karşı tarafın avatarı/adı, 2-5 mesaj, "görüldü" durumu, silinen mesaj izi | Gizli konuşmalar, sahte çift teklifi |
| 3 | **Bildirim** | `PushBanner` | Uygulama ikonu, başlık, tek satır mesaj, saat | Kanca (ilk 2-3 sn) ve askıda bitiş |
| 4 | **Karakter kartı** | `ProfileCard` | Portre, ad, yaş, şehir, meslek, tek cümle "villaya neden geldim", 3 etiket | Tanıtım bölümleri, yeni gelen |
| 5 | **Günlük** (kameraya konuşma) | `DiaryEntry` | Portre, saat, iç ses metni (izleyici duyar, karakterler duymaz) | İtiraf anı, sırlar |
| 6 | **Sır kartı** | `SecretCard` | Kapalı kart (ön yüz), açılan sır (arka yüz), "sadece sen biliyorsun" etiketi | Ana mekanik; haftalık sır |
| 7 | **Görev kartı** | `TaskCard` | Görev adı, açıklama, süre, gizli görevse kilit ikonu | Görev günleri |
| 8 | **Oylama ekranı** | `VoteScreen` | Soru, 2-4 aday kartı, geri sayım | Cumartesi büyük oylama |
| 9 | **Oylama sonucu** | `VoteResult` | Yüzde çubukları, kazanan vurgulu, "oyunu kim değiştirdi" notu | Pazar sonuç |
| 10 | **Çift kartı** | `CoupleCard` | İki portre, çift adı, uyum/güven göstergesi, "resmîleşti" ya da "kırılgan" etiketi | Çift olma / ayrılma |
| 11 | **Bölüm kapağı** | `EpisodeTitle` | Bölüm no, başlık, gün (Gün 3 · Çarşamba) | Her bölümün ilk karesi |
| 12 | **Askıda bitiş + anket yönlendirme** | `Cliffhanger` | "Devamı yarın", anket sorusu tekrarı, "Hikâyede oy ver" oku | Her bölümün son karesi |

## Bir Reels'in tipik sırası (15-30 sn)
1. **Bildirim** (0-3 sn) – kanca: "Selin seni bir konuşmaya ekledi."
2. **Bölüm kapağı** (çok kısa, 1 sn)
3. **Grup sohbeti / İkili mesaj** – çatışma
4. **Günlük** – iç ses, kırılma anı
5. **Sır kartı** veya **bildirim** – askıda bitiş
6. **Askıda bitiş + anket yönlendirme**

## Canva üretim notları
- Her şablonu bir **Canva marka şablonu** olarak kaydet; metin alanlarını adlandır
  (`mesaj_1_metin`, `mesaj_1_karakter` gibi) ki toplu doldurma (Bulk Create / autofill) kullanılabilsin.
- Mesaj balonu bileşenini tek bir grup olarak hazırla; karakter rengi tek bir şekil rengiyle değişsin.
- Hareket: mesajların sırayla belirmesi (Canva "Rise" / "Pop") yeterli; Lottie animasyonları oyun aşamasında.
- Ses: Telifsiz müzik / Instagram'ın lisanslı kütüphanesi. Esin kaynağı programın jeneriğini veya ona benzeyen müzik **kullanma**.
