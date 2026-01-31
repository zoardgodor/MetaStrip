import os
import json
from pathlib import Path

APPDATA_PATH = Path(os.getenv('APPDATA')) / 'MetaStrip'
LANGUAGE_FILE = APPDATA_PATH / 'language.json'

TRANSLATIONS = {
    'hu': {
        'title': 'MetaStrip',
        'select_file': 'Válassz egy fájlt a metaadatok megtekintéséhez.',
        'open_file': 'Fájl megnyitása',
        'remove_metadata': 'Metaadatok eltávolítása',
        'edit_metadata': 'Metaadatok szerkesztése',
        'edit_button': 'Szerkesztés',
        'exif_tab': 'EXIF / Fájl adatok',
        'file_tab': 'Fájl tulajdonságok',
        'audio_tab': 'Audio',
        'pdf_tab': 'PDF',
        'docx_tab': 'Word',
        'pptx_tab': 'PowerPoint',
        'xlsx_tab': 'Excel',
        'video_tab': 'Videó',
        'copy': 'Másolás',
        'no_exif': 'Nincs EXIF metaadat',
        'no_file_info': 'Nincs fájl információ',
        'no_metadata': 'Nincs metaadat a fájlban.',
        'error_title': 'Hiba',
        'error_read': 'Hiba: metaadatok nem olvashatók vagy ismeretlen formátum.',
        'error_metadata': 'Metaadat hiba:',
        'metadata_in_file': 'Metaadatok a fájlban:',
        'remove_success': 'Eltávolítás',
        'file_select': 'Fájl kiválasztása',
        'metadata_key': 'Kulcs',
        'metadata_value': 'Érték',
        'add_metadata': 'Új metaadat hozzáadása',
        'delete_metadata': 'Kijelölt törlése',
        'save_button': 'Mentés',
        'cancel_button': 'Mégse',
        'save_success': 'Sikeres mentés',
        'metadata_saved': 'Metaadatok sikeresen mentve!',
        'supported_formats': 'Támogatott formátumok: képek, audio, PDF, Word, PowerPoint, Excel, videók',
    },
    'en': {
        'title': 'MetaStrip',
        'select_file': 'Select a file to view metadata.',
        'open_file': 'Open File',
        'remove_metadata': 'Remove Metadata',
        'edit_metadata': 'Edit Metadata',
        'edit_button': 'Edit',
        'exif_tab': 'EXIF / File Data',
        'file_tab': 'File Properties',
        'audio_tab': 'Audio',
        'pdf_tab': 'PDF',
        'docx_tab': 'Word',
        'pptx_tab': 'PowerPoint',
        'xlsx_tab': 'Excel',
        'video_tab': 'Video',
        'copy': 'Copy',
        'no_exif': 'No EXIF metadata',
        'no_file_info': 'No file information',
        'no_metadata': 'No metadata in file.',
        'error_title': 'Error',
        'error_read': 'Error: metadata cannot be read or unknown format.',
        'error_metadata': 'Metadata error:',
        'metadata_in_file': 'Metadata in file:',
        'remove_success': 'Remove',
        'file_select': 'Select File',
        'metadata_key': 'Key',
        'metadata_value': 'Value',
        'add_metadata': 'Add New Metadata',
        'delete_metadata': 'Delete Selected',
        'save_button': 'Save',
        'cancel_button': 'Cancel',
        'save_success': 'Success',
        'metadata_saved': 'Metadata saved successfully!',
        'supported_formats': 'Supported formats: images, audio, PDF, Word, PowerPoint, Excel, videos',
    }
}


def get_language():
    try:
        if LANGUAGE_FILE.exists():
            with open(LANGUAGE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                lang = data.get('language', 'en')
                if lang in TRANSLATIONS:
                    return lang
    except:
        pass
    return 'en'


def set_language(lang):
    try:
        APPDATA_PATH.mkdir(parents=True, exist_ok=True)
        with open(LANGUAGE_FILE, 'w', encoding='utf-8') as f:
            json.dump({'language': lang}, f)
    except Exception as e:
        print(f"Error saving language: {e}")


def get_text(key, language=None):
    if language is None:
        language = get_language()
    
    if language not in TRANSLATIONS:
        language = 'hu'
    
    return TRANSLATIONS[language].get(key, key)


def get_all_texts(language=None):
    if language is None:
        language = get_language()
    
    if language not in TRANSLATIONS:
        language = 'hu'
    
    return TRANSLATIONS[language]
