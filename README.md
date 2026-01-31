# MetaStrip

A privacy-focused, offline Windows desktop application for viewing, editing, and removing metadata from images, documents, and media files.

## Features

- **Metadata Viewing**: Display EXIF, XMP, ID3, and PDF metadata
- **Metadata Editing**: Edit existing metadata and add new metadata entries
- **Metadata Removal**: Completely remove metadata from supported file types
- **Multi-language Support**: English and Hungarian interface with language preference storage
- **Wide Format Support**:
  - **Images**: JPEG, PNG, TIFF, BMP, GIF, WebP, ICO, SVG
  - **Audio**: MP3, FLAC, OGG, WAV
  - **Documents**: PDF
- **User-Friendly Interface**: Clean and intuitive GUI built with PySide6
- **Offline Operation**: Complete privacy - no data sent to external servers
- **Modular Architecture**: Well-organized code structure for easy maintenance and extension

## Installation

### Requirements
- Python 3.8+
- Windows OS (tested on Windows 10/11)

### Setup

1. Clone or download the repository:
```bash
git clone https://github.com/yourusername/MetaStrip.git
cd MetaStrip
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

## Usage

1. **Open a File**: Click "Open File" to select an image, audio file, or PDF
2. **View Metadata**: Browse different metadata categories in separate tabs:
   - EXIF / File Data
   - File Properties
   - Audio Metadata
   - PDF Metadata
3. **Edit Metadata**: Click "Edit" to open the metadata editor
   - Modify existing values
   - Add new metadata entries
   - Delete unwanted entries
4. **Remove Metadata**: Click "Remove Metadata" to strip all metadata from the file
5. **Change Language**: Use the "Language" menu to switch between English and Hungarian

## Supported File Types

### Images
- JPEG (.jpg, .jpeg)
- PNG (.png)
- TIFF (.tiff, .tif)
- BMP (.bmp)
- GIF (.gif)
- WebP (.webp)
- ICO (.ico)
- SVG (.svg)

### Audio Files
- MP3 (.mp3)
- FLAC (.flac)
- OGG (.ogg)
- WAV (.wav)

### Documents
- PDF (.pdf)

## Technical Details

- **Framework**: PySide6 (Qt for Python)
- **Image Processing**: Pillow, piexif
- **Audio Metadata**: Mutagen
- **PDF Handling**: PyPDF2
- **Architecture**: Modular design with separate components for metadata extraction, editing, and UI

## License

This project is provided as-is for educational and personal use.

## Disclaimer

The use of this software is entirely the user's responsibility.
The developer assumes no liability for any direct or indirect consequences, including but not limited to damages resulting from infringing or unethical use.
This software is intended solely for viewing, modifying, and experimenting with metadata for educational purposes.
