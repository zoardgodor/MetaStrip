import os
from PIL import Image
import piexif
import mutagen
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime

SUPPORTED_IMAGE_FORMATS = {'.jpg', '.jpeg', '.tiff', '.tif', '.png', '.bmp', '.gif', '.webp', '.ico', '.svg'}
SUPPORTED_AUDIO_FORMATS = {'.mp3', '.flac', '.ogg', '.wav'}
SUPPORTED_PDF_FORMATS = {'.pdf'}


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()


def get_file_info(file_path):
    """Extract basic file properties (size, date, permissions, etc.)"""
    file_info = {}
    try:
        stat = os.stat(file_path)
        file_info["FILE:Fájlnév"] = os.path.basename(file_path)
        file_info["FILE:Teljes útvonal"] = file_path
        file_info["FILE:Fájlméret"] = format_file_size(stat.st_size)
        file_info["FILE:Méret (bájt)"] = str(stat.st_size)
        
        mod_time = datetime.fromtimestamp(stat.st_mtime)
        file_info["FILE:Módosítás dátuma"] = mod_time.strftime("%Y:%m:%d %H:%M:%S")
        
        access_time = datetime.fromtimestamp(stat.st_atime)
        file_info["FILE:Hozzáférés dátuma"] = access_time.strftime("%Y:%m:%d %H:%M:%S")
        
        change_time = datetime.fromtimestamp(stat.st_ctime)
        file_info["FILE:Módosítás időpontja"] = change_time.strftime("%Y:%m:%d %H:%M:%S")
        
        file_info["FILE:Fájltípus"] = detect_file_type(file_path)
        
    except Exception as e:
        file_info["FILE:Hiba"] = str(e)
    
    return file_info


def format_file_size(size_bytes):
    """Convert bytes to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def detect_file_type(file_path):
    """Detect MIME type and file type"""
    try:
        from PIL import Image
        img = Image.open(file_path)
        format_str = img.format or "Unknown"
        mime_map = {
            'JPEG': 'image/jpeg',
            'PNG': 'image/png',
            'TIFF': 'image/tiff',
            'GIF': 'image/gif'
        }
        mime = mime_map.get(format_str, 'image/' + format_str.lower())
        return f"{format_str} ({mime})"
    except:
        return "Unknown"


def extract_image_file_info(file_path):
    """Extract image-specific file properties (dimensions, encoding, etc.)"""
    file_info = {}
    try:
        img = Image.open(file_path)
        file_info["FILE:Képméretek"] = f"{img.width}x{img.height}"
        file_info["FILE:Megapixel"] = f"{(img.width * img.height) / 1000000:.1f}"
        file_info["FILE:Képformátum"] = img.format or "Unknown"
        file_info["FILE:Képmód"] = img.mode
        
        if hasattr(img, 'info'):
            if 'dpi' in img.info:
                dpi = img.info['dpi']
                file_info["FILE:DPI"] = f"{dpi[0]}x{dpi[1]}"
    except Exception as e:
        file_info["FILE:Hiba"] = str(e)
    
    return file_info


def extract_metadata(file_path):
    ext = get_file_extension(file_path)
    
    meta = get_file_info(file_path)
    
    if ext in SUPPORTED_IMAGE_FORMATS:
        meta.update(extract_image_file_info(file_path))
        meta.update(extract_image_metadata(file_path))
    elif ext in SUPPORTED_AUDIO_FORMATS:
        meta.update(extract_audio_metadata(file_path))
    elif ext in SUPPORTED_PDF_FORMATS:
        meta.update(extract_pdf_metadata(file_path))
    else:
        meta["Nem támogatott fájltípus"] = ext
    
    return meta


def extract_image_metadata(file_path):
    try:
        img = Image.open(file_path)
        exif_data = img.info.get('exif')
        if exif_data:
            exif_dict = piexif.load(exif_data)
            meta = {}
            for ifd in exif_dict:
                if exif_dict[ifd] is None:
                    continue
                for tag in exif_dict[ifd]:
                    try:
                        tag_name = piexif.TAGS[ifd][tag]["name"]
                        value = exif_dict[ifd][tag]
                        meta[f"EXIF:{tag_name}"] = value
                    except Exception:
                        continue
            return meta if meta else {"EXIF": "Nincs EXIF metaadat"}
        else:
            return {"EXIF": "Nincs EXIF metaadat"}
    except Exception as e:
        return {"Hiba": str(e)}


def extract_audio_metadata(file_path):
    try:
        audio = mutagen.File(file_path, easy=True)
        if not audio:
            return {"ID3": "Nem olvasható vagy nincs metaadat"}
        meta = {}
        items = getattr(audio, 'items', None)
        if callable(items):
            for k, v in audio.items():
                meta[f"ID3:{k}"] = v
        return meta if meta else {"ID3": "Nincs metaadat"}
    except Exception as e:
        return {"Hiba": str(e)}


def extract_pdf_metadata(file_path):
    try:
        reader = PdfReader(file_path)
        info = reader.metadata
        if info and hasattr(info, 'items'):
            meta = {f"PDF:{k}": v for k, v in info.items()}
            return meta if meta else {"PDF": "Nincs metaadat"}
        else:
            return {"PDF": "Nincs metaadat"}
    except Exception as e:
        return {"Hiba": str(e)}


def remove_metadata(file_path):
    ext = get_file_extension(file_path)
    if ext in SUPPORTED_IMAGE_FORMATS:
        return remove_image_metadata(file_path)
    elif ext in SUPPORTED_AUDIO_FORMATS:
        return remove_audio_metadata(file_path)
    elif ext in SUPPORTED_PDF_FORMATS:
        return remove_pdf_metadata(file_path)
    else:
        return False, "Nem támogatott fájltípus"


def remove_image_metadata(file_path):
    try:
        img = Image.open(file_path)
        data = list(img.getdata())
        img_no_exif = Image.new(img.mode, img.size)
        img_no_exif.putdata(data)
        out_path = file_path  
        img_no_exif.save(out_path)
        return True, "EXIF metaadatok eltávolítva"
    except Exception as e:
        return False, str(e)


def remove_audio_metadata(file_path):
    try:
        audio = mutagen.File(file_path)
        if audio is None:
            return False, "Nem olvasható vagy nincs metaadat"
        audio.delete()
        audio.save()
        return True, "ID3/metaadatok eltávolítva"
    except Exception as e:
        return False, str(e)


def remove_pdf_metadata(file_path):
    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        out_path = file_path
        with open(out_path, 'wb') as f:
            writer.write(f)
        return True, "PDF metaadatok eltávolítva"
    except Exception as e:
        return False, str(e)
