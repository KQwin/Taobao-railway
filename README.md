# Taobao Railway Bot

Bu loyiha Taobao sahifasini avtomatik ochadigan va skrinshot oladigan Python botdir.  
Bot **Playwright** asosida yozilgan va **Railway** platformasida doimiy ishlaydi.

---

## Funktsiyasi

- Taobao sahifasini ochadi
- Screenshot oladi (`screenshot.png`)
- Keyinchalik mahsulot tahlili va Telegram bot funksiyasi qo‘shiladi

---

## Texnologiyalar

- Python 3.10+
- Playwright
- Railway (deployment)

---

## Fayllar

| Fayl nomi       | Tavsif                             |
|------------------|--------------------------------------|
| `bot.py`         | Asosiy bot kodi                     |
| `build.sh`       | Kutubxonalarni va Chromium’ni o‘rnatadi |
| `requirements.txt` | Python kutubxonalar ro‘yxati         |

---

## Railway’da ishga tushirish

1. GitHub’da repozitoriy yarating (masalan: `taobao-railway-bot`)
2. Ushbu 3 faylni yuklang: `bot.py`, `build.sh`, `requirements.txt`
3. Railway’da `New Project > Deploy from GitHub` tanlang
4. `Start Command` maydoniga yozing:

```
bash build.sh && python bot.py
```

5. `Deploy` tugmasini bosing
6. Loglarda “✅ Sahifa ochildi va screenshot olindi.” yozuvi chiqsa, bot ishlayapti

---

## Kelajakdagi rejalar

- Taobao’da mahsulotlarni qidirish
- Mahsulotlarni tahlil qilish (narx, sotuvlar)
- Foydali mahsulotlarni Telegram botga yuborish
