# MetaStrip

Az adatvédelemre összpontosított, offline működő Windows asztali alkalmazás metaadatok megtekintésére, szerkesztésére és eltávolítására képekből, dokumentumokból és médiafájlokból.

## Főbb jellemzők

- **Metaadatok megtekintése**: EXIF, XMP, ID3 és PDF metaadatok megjelenítése
- **Metaadatok szerkesztése**: Meglévő metaadatok módosítása, új bejegyzések hozzáadása és törlése
- **Metaadatok eltávolítása**: Teljes metaadat eltávolítás támogatott fájltípusokból
- **Másolás funkcionalitás**: Kijelölt metaadatok másolása a vágólapra (Ctrl+C)
- **Fájl tulajdonságok megjelenítése**: 
  - Fájlméret, módosítási/hozzáférési/módosítás dátumai
  - Kép dimenzió és megapixel érték
  - DPI információ képek esetén
  - Fájltípus és MIME típus detektálása
- **Többnyelvű támogatás**: Angol és magyar felhasználói felület, nyelvbeállítás tárolása AppData-ban
- **Széles fájltámogatás**:
  - **Képek**: JPEG, PNG, TIFF, BMP, GIF, WebP, ICO, SVG ...stb.
  - **Audio**: MP3, FLAC, OGG, WAV ...stb.
  - **Dokumentumok**: PDF, PPTX, DOCX, XLSX ...stb.
- **Felhasználóbarát felület**: Tiszta és intuitív felület a PySide6-tal készítve, fülekre szervezett megjelenítés
- **Offline működés**: Teljes adatvédelem - nem küldi az adatokat külső szervereire
- **Moduláris szerkezet**: Jól szervezett kódstruktúra az egyszerű karbantartás és bővítés érdekében

## Telepítés

https://github.com/zoardgodor/MetaStrip/releases/
Töltse le innen a legutóbbi installert. (MetaStrip_vx.x_WIN64_installer.exe) futtassa a programot.
Vagy töltse le a tömörített archívumot amely azt tartalmazza amit az installer
telepítene. (MetaStrip_vx.x_WIN64.zip)

## Forráskód nyers futtatása

### Követelmények
- Python 3.8+
- Windows operációs rendszer (Windows 10/11-en tesztelve)

### Beállítás

1. Klónozza vagy töltse le az adattárat:
```bash
git clone https://github.com/zoardgodor/MetaStrip.git
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

2. **Metaadatok megtekintése**: A megnyitott fájl metaadatai különböző füleken jelennek meg:
   - **EXIF / Fájl adatok**: EXIF metaadatok és az alkalmazás által feldolgozott fájl információ
   - **Fájl tulajdonságok**: Fájlméret, dátumok, kép dimenziók, DPI, megapixel érték
   - **Audio metaadatok**: ID3 tagek audio fájlokhoz
   - **PDF metaadatok**: PDF dokumentumok metainformációi

3. **Másolás**: Kattintson jobb gombbal a metaadatokra és válassza a "Másolás" lehetőséget, vagy használja a Ctrl+C billentyűkombinációt több tétel kiválasztásakor

4. **Metaadatok szerkesztése**: Kattintson a "Szerkesztés" gombra a metaadat szerkesztő megnyitásához
   - Módosítson meglévő értékeket
   - Adjon hozzá új metaadat bejegyzéseket az "Új metaadat hozzáadása" gombbal
   - Töröljön nem kívánt bejegyzéseket a "Kijelölt törlése" gombbal
   - Kattintson a "Mentés" gombra a módosítások alkalmazásához

5. **Metaadatok eltávolítása**: Kattintson a "Metaadatok eltávolítása" gombra a fájl összes metaadatának eltávolításához
   - JPEG és TIFF képek: EXIF metaadatok eltávolítása
   - Audio fájlok: ID3 tagek törlése
   - PDF dokumentumok: PDF metaadat szekciók eltávolítása

6. **Nyelvváltás**: Használja a "Language" menüt az angol és magyar közötti váltáshoz. A kiválasztott nyelv automatikusan mentésre kerül

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

## Funkciók részletesen

### Fájl Tulajdonságok
Az alkalmazás automatikusan kiolvassa és megjelenít:
- **Fájlnév és útvonal**: Teljes elérési út és fájlnév
- **Fájlméret**: Formázott (KB, MB, GB) és bájt-ban kifejezve
- **Dátumok**: Módosítás, hozzáférés és metadata módosítás időpontja
- **Fájltípus**: Automatikus fájltípus és MIME típus detektálása
- **Kép metriká** (képek esetén):
  - Dimenzió (szélességx magasság)
  - Megapixel érték
  - Képformátum (JPEG, PNG, stb.)
  - Képmód (RGB, RGBA, stb.)
  - DPI információ

### Metaadat Szerkesztés
- **Táblázatos szerkesztő**: Intuitív táblázat formában szerkeszthetők az EXIF és ID3 tagek
- **Új bejegyzések**: Gyakorlatilag korlátlan számú új metaadat hozzáadása
- **Flexibilis módosítás**: Meglévő értékek szerkesztése tetszőlegesen
- **Szelektív törlés**: Csak a szükséges bejegyzések törlése
- **Támogatott formátumok**:
  - JPEG/TIFF: EXIF metaadatok (piexif könyvtár használatával)
  - Audio: ID3 tagek és Vorbis Comments (Mutagen könyvtár)
  - PDF: PDF metaadat szekciók (PyPDF2 könyvtár)

### Adatvédelem
- Az alkalmazás **teljes mértékben offline** működik
- Nem küld semmilyen adatot internetre vagy külső szervereire
- Minden feldolgozás a helyi gépen történik
- Az alkalmazás csak AppData mappában tárolt nyelvbeállítást ment


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
