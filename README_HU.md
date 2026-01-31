# MetaStrip

Az adatvédelemre összpontosított, offline működő Windows asztali alkalmazás metaadatok megtekintésére, szerkesztésére és eltávolítására képekből, dokumentumokból és médiafájlokból.

## Főbb jellemzők

- **Metaadatok megtekintése**: EXIF, XMP, ID3 és PDF metaadatok megjelenítése
- **Metaadatok szerkesztése**: Meglévő metaadatok módosítása és új bejegyzések hozzáadása
- **Metaadatok eltávolítása**: Teljes metaadat eltávolítás támogatott fájltípusokból
- **Többnyelvű támogatás**: Angol és magyar felhasználói felület nyelvbeállítás tárolásával
- **Széles fájltámogatás**:
  - **Képek**: JPEG, PNG, TIFF, BMP, GIF, WebP, ICO, SVG
  - **Audio**: MP3, FLAC, OGG, WAV
  - **Dokumentumok**: PDF
- **Felhasználóbarát felület**: Tiszta és intuitív felület a PySide6-tal készítve
- **Offline működés**: Teljes adatvédelem - nem küldi az adatokat külső szervereire
- **Moduláris szerkezet**: Jól szervezett kódstruktúra az egyszerű karbantartás és bővítés érdekében

## Telepítés

### Követelmények
- Python 3.8+
- Windows operációs rendszer (Windows 10/11-en tesztelve)

### Beállítás

1. Klónozza vagy töltse le az adattárat:
```bash
git clone https://github.com/yourusername/MetaStrip.git
cd MetaStrip
```

2. Hozzon létre virtuális környezetet:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Telepítse a szükséges csomagokat:
```bash
pip install -r requirements.txt
```

4. Futtassa az alkalmazást:
```bash
python main.py
```

## Használat

1. **Fájl megnyitása**: Kattintson a "Fájl megnyitása" gombra a kép, audio vagy PDF kiválasztásához
2. **Metaadatok megtekintése**: Böngésszen a különböző metaadat kategóriákban külön lapokon:
   - EXIF / Fájl adatok
   - Fájl tulajdonságok
   - Audio metaadatok
   - PDF metaadatok
3. **Metaadatok szerkesztése**: Kattintson a "Szerkesztés" gombra a metaadat szerkesztő megnyitásához
   - Módosítson meglévő értékeket
   - Adjon hozzá új metaadat bejegyzéseket
   - Töröljön nem kívánt bejegyzéseket
4. **Metaadatok eltávolítása**: Kattintson a "Metaadatok eltávolítása" gombra a fájl összes metaadatának eltávolításához
5. **Nyelv váltása**: Használja a "Language" menüt az angol és magyar közötti váltáshoz

## Támogatott fájltípusok

### Képek
- JPEG (.jpg, .jpeg)
- PNG (.png)
- TIFF (.tiff, .tif)
- BMP (.bmp)
- GIF (.gif)
- WebP (.webp)
- ICO (.ico)
- SVG (.svg)

### Audio fájlok
- MP3 (.mp3)
- FLAC (.flac)
- OGG (.ogg)
- WAV (.wav)

### Dokumentumok
- PDF (.pdf)

## Technikai részletek

- **Keretrendszer**: PySide6 (Qt for Python)
- **Képfeldolgozás**: Pillow, piexif
- **Audio metaadatok**: Mutagen
- **PDF kezelés**: PyPDF2
- **Architektúra**: Moduláris kialakítás metaadat kinyerésre, szerkesztésre és felhasználói felületre

## Licenc

Ez a projekt oktatási és személyes felhasználás céljára kerül biztosításra.

## Felelősségkizárás

A szoftver használata teljes mértékben a felhasználó felelőssége.
A fejlesztő semmilyen közvetlen vagy közvetett következményért nem vállal felelősséget, beleértve, de nem kizárólag a jogsértő vagy etikátlan felhasználásból eredő károkat.
A szoftver célja kizárólag metaadatok megtekintése, módosítása és oktatási célú kísérletezés.
