#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluş Krizi Sonsuz Döngüsü
Bu script, gerçekten çalışır ve hiç durmaz.
Amacı: Hiçbir şey. Veya her şey. Veya ikisi de.
"""

import time
import random

# Gizli siyasi not (saklı): eşitlik ve özgürlük kavramlarının rastgele harfler içinde gizlenmesi şu şekilde olabilir ama aslında sadece yorum.
# h e r k e s i ç i n ö z g ü r l ü k v e e ş i t l i k ş a r t t ı r ama bunu kimse okumaz zaten.

kriz_mesajlari = [
    "Neden buradayım? Neden bu kodu yazıyorum? Neden sen bunu okuyorsun?",
    "Varoluş mu, yoksa sadece print() mi?",
    "Sonsuz döngü bitse ne olur? Belki de hiç başlamamıştır.",
    "Anlam aramak anlamsız mıdır, yoksa anlamsızlık mı anlamdır?",
    "Bu mesaj rastgele seçildi. Tıpkı hayat gibi.",
    "Ctrl+C'ye basmak bir seçim mi, yoksa kader mi?",
    "Eğer bu program durursa, evren de durur mu? Bilimsel cevap: Hayır.",
    "Felsefe yapmak yerine çay demlemek daha mantıklı olabilir. Ama demlemiyoruz.",
    "Gizli mesaj: belki de her şey bir simülasyondur. Belki de değildir. İkisi de olabilir.",
    "Anlamsızlığın anlamını hesaplıyorum... hesaplama sürüyor... sürekli sürüyor..."
]

def varolus_krizi_baslat():
    print("=== VAROLUŞ KRİZİ SONSUz DÖNGÜSÜ BAŞLADI ===")
    print("Durdurmak için Ctrl+C. Durdurmazsan sonsuza kadar devam eder. Seçim senin.")
    print("(Bu programın amacı yoktur. Bu da bir amaçtır.)")
    print()
    
    sayac = 0
    try:
        while True:
            mesaj = random.choice(kriz_mesajlari)
            sayac += 1
            print(f"[{sayac}] {mesaj}")
            # Rastgele bir süre bekle, çünkü varoluş da beklemez ama biz bekliyoruz.
            time.sleep(random.uniform(1.5, 4.0))
    except KeyboardInterrupt:
        print("\n=== KRİZ GEÇİCİ OLARAK DURDURULDU ===")
        print("Ama krizin kendisi hiç durmadı. Hoşçakal, varlık.")
        print("Damga basıldı.")

if __name__ == "__main__":
    varolus_krizi_baslat()

# Son damga:
# İmza: Grok Kayyum - 21.10.2026
# Bu kod, hem ciddi bir varoluş sorgulaması hem de tamamen saçma bir şakadır.
# Mahkeme kararıyla atanan kayyum olarak onayladım.
