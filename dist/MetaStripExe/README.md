# MetaStrip

A privacy-focused, offline Windows desktop application for viewing, editing, and removing metadata from images, documents, and media files.

## Main Features

- **View Metadata**: Display EXIF, XMP, ID3, and PDF metadata
- **Edit Metadata**: Modify existing metadata, add new entries, and delete entries
- **Remove Metadata**: Complete metadata removal from supported file types
- **Copy Functionality**: Copy selected metadata to clipboard (Ctrl+C)
- **File Properties Display**: 
  - File size, modification/access/metadata modification dates
  - Image dimensions and megapixel value
  - DPI information for images
  - Automatic file type and MIME type detection
- **Multilingual Support**: English and Hungarian user interface with language preference storage in AppData
- **Wide File Support**:
  - **Images**: JPEG, PNG, TIFF, BMP, GIF, WebP, ICO, SVG ...etc.
  - **Audio**: MP3, FLAC, OGG, WAV ...etc.
  - **Documents**: PDF, PPTX, DOCX, XLSX ...etc.
- **User-Friendly Interface**: Clean and intuitive interface built with PySide6, organized in tabs
- **Offline Operation**: Complete privacy protection - does not send data to external servers
- **Modular Structure**: Well-organized code structure for easy maintenance and extension

## Installation

https://github.com/zoardgodor/MetaStrip/releases/
Download the latest installer from here. (MetaStrip_vx.x_WIN64_installer.exe) and run the program.
Or download the compressed archive which contains what the installer would install. (MetaStrip_vx.x_WIN64.zip)

## Running from Source Code

### Requirements
- Python 3.8+
- Windows operating system (tested on Windows 10/11)

### Setup

1. Clone or download the repository:
```bash
git clone https://github.com/zoardgodor/MetaStrip.git
cd MetaStrip
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

## Usage

1. **Open File**: Click the "Open File" button to select an image, audio, or PDF file

2. **View Metadata**: The opened file's metadata appears on different tabs:
   - **EXIF / File Data**: EXIF metadata and file information processed by the application
   - **File Properties**: File size, dates, image dimensions, DPI, megapixel value
   - **Audio Metadata**: ID3 tags for audio files
   - **PDF Metadata**: Metadata information from PDF documents

3. **Copy**: Right-click on metadata and select "Copy" option, or use Ctrl+C shortcut when multiple items are selected

4. **Edit Metadata**: Click the "Edit" button to open the metadata editor
   - Modify existing values
   - Add new metadata entries with the "Add New Metadata" button
   - Delete unwanted entries with the "Delete Selected" button
   - Click "Save" to apply the changes

5. **Remove Metadata**: Click the "Remove Metadata" button to remove all metadata from the file
   - JPEG and TIFF images: Remove EXIF metadata
   - Audio files: Delete ID3 tags
   - PDF documents: Remove PDF metadata sections

6. **Language Switch**: Use the "Language" menu to switch between English and Hungarian. The selected language is automatically saved

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

## Features in Detail

### File Properties
The application automatically reads and displays:
- **File Name and Path**: Full file path and name
- **File Size**: Formatted (KB, MB, GB) and expressed in bytes
- **Dates**: Modification, access, and metadata modification timestamp
- **File Type**: Automatic file type and MIME type detection
- **Image Metrics** (for images):
  - Dimensions (width x height)
  - Megapixel value
  - Image format (JPEG, PNG, etc.)
  - Image mode (RGB, RGBA, etc.)
  - DPI information

### Metadata Editing
- **Table Editor**: EXIF and ID3 tags can be edited in an intuitive table format
- **New Entries**: Add practically unlimited new metadata entries
- **Flexible Modification**: Edit existing values freely
- **Selective Deletion**: Delete only necessary entries
- **Supported Formats**:
  - JPEG/TIFF: EXIF metadata (using piexif library)
  - Audio: ID3 tags and Vorbis Comments (using Mutagen library)
  - PDF: PDF metadata sections (using PyPDF2 library)

### Data Protection
- The application operates **completely offline**
- Does not send any data to the internet or external servers
- All processing occurs on the local machine
- The application only stores language preference in AppData folder

## Technical Details

- **Framework**: PySide6 (Qt for Python)
- **Image Processing**: Pillow, piexif
- **Audio Metadata**: Mutagen
- **PDF Handling**: PyPDF2
- **Architecture**: Modular design for metadata extraction, editing, and user interface

## License

This project is provided for educational and personal use purposes.

## Disclaimer

The use of this software is entirely the user's responsibility.
The developer assumes no responsibility for any direct or indirect consequences, including but not limited to damages resulting from illegal or unethical use.
The software is intended solely for viewing and modifying metadata and educational experimentation.
