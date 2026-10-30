# Online Mod Notları

Demoda tek kişilik olarak denenen mekaniklerin gerçek oyuncularla nasıl çalışacağına dair notlar.

## Sesli konuşma
Oyuncuları birbirine en çok bağlayacak özellik. Ama riskleri de en yüksek olan özellik bu.

**Nerede açık olur?**
- **Bordo Oda:** Baş başa, süreli (3 dk) sesli görüşme. En doğal yer burası.
- **Misafirlik:** Karşı eve geçen oyuncu orada bulunanlarla oda içi sesli sohbet yapabilir.
- **Gala:** Herkes izler; sadece sandık başındaki kişinin "son sözü" (10-15 sn) açık mikrofonla.
- Genel alanlarda (Havuz Başı, evler) varsayılan olarak yazılı sohbet. Sesli konuşma "yakınlık tabanlı" olarak ileride.

**Zorunlu güvenlik katmanı:**
- 18+ doğrulama. Sesli özellik yalnızca yaşı doğrulanmış hesaplara açık.
- Bas-konuş ya da açık mikrofon tercihi. Her an kapatma; herkesi tek dokunuşla susturma.
- Şikâyet ve engelleme butonu görüşme ekranında her zaman görünür.
- Kayıt politikası: Şikâyet durumunda incelenebilmesi için son X dakikanın kısa süreli saklanması. Bunun KVKK aydınlatma metnine ve açık rızaya eklenmesi gerekir.
- Otomatik ses moderasyonu: Sesten metne çeviri, küfür/taciz tespiti ve iletişim bilgisi (telefon, Instagram) paylaşımının tespiti.
- Gerçek buluşmaya yönlendirmeyen kurgu dili ve kurallar.

**Teknik seçenekler:** LiveKit, Agora ya da Daily gibi WebRTC hizmetleri. Supabase Realtime sinyalleşme ve oda durumu için kullanılabilir; ses akışı ayrı hizmetten geçer.

## Odalar ve zamanlama (gerçek süreler)
| Mekanik | Demo | Online |
|---|---|---|
| Bordo Oda | 45 sn | 3 dk |
| Misafirlik | 90 sn | 5 dk |
| Gün | Konuşmalar bitince | Gerçek zamanlı takvim (örn. 1 gün = 1 akşam oturumu) |
| Gala | Oyuncu başlatır | Sabit saatte, herkes için aynı anda |

## Hukuki not
Kızlar evi / erkekler evi ayrımı, yeni gelenin dans ritüeli ve "Gala" adı esin kaynağı formata çok yakın.
Tür kalıbı olarak savunulabilir olabilir, ama segment adları ve sıralı ritüellerin birebir kopyası
"haksız rekabet / format taklidi" tartışması doğurabilir. Lansman öncesi avukata sorulacak listesi:
"Gala", "Bordo Oda", ayrı evler + misafirlik, yeni gelen töreni (tanışma → dans → özel oda).
