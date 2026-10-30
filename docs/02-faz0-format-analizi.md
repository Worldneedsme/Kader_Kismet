# Faz 0: Format Analizi

Amaç: Türün **kalıplarını** (kişileri değil) çıkarıp kendi senaryolarımız için bir
"drama kalıp kütüphanesi" oluşturmak.

## Kurallar
- Kişi adı, lakap, birebir replik **not alınmaz**. Yarışmacılar `K1`, `E2` gibi rol kodlarıyla anılır
  (K = kadın, E = erkek, numara giriş sırası). Notlar kalıp düzeyinde tutulur.
- Ekran görüntüsü, video kesiti, müzik arşivlenmez. Yalnızca yazılı not.
- Bir sahne birden fazla kalıba uyuyorsa satırı tekrarlamak yerine `olay_tipi` alanına `+` ile ekle
  (örn. `ask_ucgeni+kiskanclik`).

## Örneklem planı (~35 bölüm + kesitler)

Bölüm numaraları kanal/platforma göre farklı olabildiği için liste **tarih aralığıyla**
tanımlandı. İzlemeye başlarken her satırın gerçek bölüm numarasını tabloya yaz.

| Blok | Sezon | Ne izlenecek | Yaklaşık adet | Neden |
|------|-------|--------------|---------------|-------|
| A. Açılış | S1 | İlk 2 hafta (Aralık 2022 sonu – Ocak 2023 başı) | 8-10 | İlk izlenim, ilk çift denemeleri, rol dağılımı nasıl kuruluyor |
| B. Açılış | S2 | İlk hafta (Eylül 2023) | 4-5 | 2. sezonda açılış formülü değişmiş mi |
| C. Hafta sonu | S1 + S2 | Rastgele 6 hafta sonu oylama/eleme bölümü (her 4-6 haftadan 1) | 6 | Haftalık yayın patlama noktası |
| D. Yeni gelen | S1 + S2 | Yeni yarışmacı giriş haftasından 3 örnek (giriş günü + ertesi gün) | 6 | "Yeni gelen" kalıbının tetikleyici ve tırmanışı |
| E. Popüler kesitler | S1 + S2 | YouTube'da en çok izlenen 10-15 kesit | 10-15 kesit | İzleyicinin gerçekten neye tepki verdiği |
| F. Finaller | S1 + S2 | Sezon finali + finalden önceki hafta | 4-6 | Yayların nasıl kapandığı, final duygu yükü |

### Popüler kesitleri seçme yöntemi (Blok E)
1. YouTube'da resmî kanalı "En popüler" sıralamasıyla aç.
2. İlk 30 videodan **farklı olay tiplerini** temsil eden 10-15 tanesini seç (hepsi kavga olmasın).
3. Her kesit için izlenme ve yorum sayısını `izleyici_tepkisi` alanına yaz; en çok beğenilen
   3 yorumun **temasını** (alıntı değil) not al: "taraf tutma", "mizah", "ihanete öfke" gibi.

## Analiz tablosu

Dosya: [`faz0/analiz-tablosu.csv`](faz0/analiz-tablosu.csv) (Google Sheets / Excel'e aktarılabilir).

| Alan | Açıklama | Örnek |
|------|----------|-------|
| `id` | Satır numarası | 12 |
| `sezon` | S1 / S2 | S1 |
| `bolum_tarih` | Bölüm no + yayın tarihi | 34 / 2023-02-03 |
| `blok` | Örneklem bloğu (A-F) | C |
| `olay_tipi` | Kalıp kodu (aşağıdaki listeden) | gizli_konusma_ifsasi |
| `roller` | Rol kodları | K2, E1, E4 |
| `tetikleyici` | Olayı başlatan şey | Bir yarışmacı başkasının konuşmasına kulak misafiri oluyor |
| `tirmanis_bolum` | Kaç bölüm sürdü | 3 |
| `tirmanis_adimlari` | Kısa adım listesi | duyma → arkadaşına aktarma → grup içinde yüzleşme |
| `cozum` | Nasıl kapandı / açık mı kaldı | Özür + kırgınlık sürdü |
| `izleyici_tepkisi` | Kesit izlenme/yorum teması | Yüksek; yorumlarda taraf tutma |
| `uyarlanabilirlik` | 1-5 (5 = oyuna çok uygun) | 5 |
| `anket_fikri` | Instagram anket sorusu fikri | "Duyduğunu söylemeli mi?" |
| `mekanik_fikri` | Oyun mekaniği fikri | Kulak misafiri kartı: oyuncu bir sohbeti gizlice okuyabilir, ama yakalanırsa güven puanı düşer |
| `not` | Serbest | |

### Olay tipi kodları
| Kod | Kalıp |
|-----|-------|
| `ask_ucgeni` | Aşk üçgeni |
| `sahte_cift` | Stratejik/sahte çift |
| `yanlis_dedikodu` | Yanlış anlaşılan dedikodu |
| `gizli_konusma_ifsasi` | Gizli konuşma ifşası |
| `yeni_gelen` | Yeni gelen |
| `gecmis_sir` | Geçmişten tanışıklık/sır |
| `oylama_ihaneti` | Oylamada ihanet |
| `ittifak_bolunme` | İttifak ve bölünme |
| `ikinci_sans` | İkinci şans |
| `kiskanclik` | Kıskançlık krizi |
| `itiraf_ani` | İtiraf anı (izleyici bilir, karakterler bilmez) |
| `diger` | Listede olmayan; `not` alanında tanımla, 3+ kez görülürse yeni kod aç |

## Analiz bitince çıktılar
1. **Kalıp kütüphanesi:** Her olay tipi için ortalama tırmanış süresi, en sık tetikleyici,
   en çok tepki alan çözüm biçimi.
2. **Anket bankası:** `uyarlanabilirlik >= 4` satırlardaki anket fikirleri.
3. **Mekanik listesi:** Tekrar eden `mekanik_fikri` önerileri; ana mekanik kararına girdi
   (bkz. [Açık sorular ve öneriler](07-acik-sorular-oneriler.md)).
