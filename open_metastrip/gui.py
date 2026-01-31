from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QListWidget, QMessageBox, QTabWidget, QHBoxLayout, QMenu, QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QKeySequence
import sys
import os
from pathlib import Path
from .translations import get_language, set_language, get_text, get_all_texts

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_language = get_language()
        self._setup_menu_bar()
        self._init_ui()
        self.setAcceptDrops(True)

    def _setup_menu_bar(self):
        menubar = self.menuBar()
        language_menu = menubar.addMenu("Language")
        
        hu_action = QAction("Magyarország (HU)", self)
        hu_action.triggered.connect(lambda: self.change_language('hu'))
        language_menu.addAction(hu_action)
        
        en_action = QAction("English (EN)", self)
        en_action.triggered.connect(lambda: self.change_language('en'))
        language_menu.addAction(en_action)

    def change_language(self, lang):
        if lang != self.current_language:
            self.current_language = lang
            set_language(lang)
            self._refresh_ui()

    def _get_default_path(self):
        pictures_path = Path.home() / "Pictures"
        if pictures_path.exists():
            return str(pictures_path)
        return str(Path.home())

    def _init_ui(self):
        self.setWindowTitle(get_text('title', self.current_language))
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.info_label = QLabel(get_text('select_file', self.current_language))
        self.layout.addWidget(self.info_label)

        top_layout = QHBoxLayout()
        self.open_button = QPushButton(get_text('open_file', self.current_language))
        self.open_button.clicked.connect(self.open_file)
        top_layout.addWidget(self.open_button)
        
        self.edit_button = QPushButton(get_text('edit_button', self.current_language))
        self.edit_button.clicked.connect(self.edit_metadata)
        self.edit_button.setEnabled(False)
        top_layout.addWidget(self.edit_button)
        
        self.remove_button = QPushButton(get_text('remove_metadata', self.current_language))
        self.remove_button.clicked.connect(self.remove_metadata)
        self.remove_button.setEnabled(False)
        top_layout.addWidget(self.remove_button)
        self.layout.addLayout(top_layout)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.exif_list = QListWidget()
        self.exif_list.setSelectionMode(QListWidget.ExtendedSelection)
        self.exif_list.setAcceptDrops(True)
        self._setup_list_actions(self.exif_list)
        self.tab_widget.addTab(self.exif_list, get_text('exif_tab', self.current_language))

        self.file_info_list = QListWidget()
        self.file_info_list.setSelectionMode(QListWidget.ExtendedSelection)
        self._setup_list_actions(self.file_info_list)
        self.tab_widget.addTab(self.file_info_list, get_text('file_tab', self.current_language))

        self.audio_list = QListWidget()
        self.audio_list.setSelectionMode(QListWidget.ExtendedSelection)
        self._setup_list_actions(self.audio_list)
        self.tab_widget.addTab(self.audio_list, get_text('audio_tab', self.current_language))

        self.pdf_list = QListWidget()
        self.pdf_list.setSelectionMode(QListWidget.ExtendedSelection)
        self._setup_list_actions(self.pdf_list)
        self.tab_widget.addTab(self.pdf_list, get_text('pdf_tab', self.current_language))

        self.document_list = QListWidget()
        self.document_list.setSelectionMode(QListWidget.ExtendedSelection)
        self._setup_list_actions(self.document_list)
        self.tab_widget.addTab(self.document_list, get_text('docx_tab', self.current_language))

        self.presentation_list = QListWidget()
        self.presentation_list.setSelectionMode(QListWidget.ExtendedSelection)
        self._setup_list_actions(self.presentation_list)
        self.tab_widget.addTab(self.presentation_list, get_text('pptx_tab', self.current_language))

        self.spreadsheet_list = QListWidget()
        self.spreadsheet_list.setSelectionMode(QListWidget.ExtendedSelection)
        self._setup_list_actions(self.spreadsheet_list)
        self.tab_widget.addTab(self.spreadsheet_list, get_text('xlsx_tab', self.current_language))

        self.video_list = QListWidget()
        self.video_list.setSelectionMode(QListWidget.ExtendedSelection)
        self._setup_list_actions(self.video_list)
        self.tab_widget.addTab(self.video_list, get_text('video_tab', self.current_language))

        self.file_path = None
        self.metadata = None

    def _refresh_ui(self):
        self.setWindowTitle(get_text('title', self.current_language))
        self.info_label.setText(get_text('select_file', self.current_language))
        self.open_button.setText(get_text('open_file', self.current_language))
        self.edit_button.setText(get_text('edit_button', self.current_language))
        self.remove_button.setText(get_text('remove_metadata', self.current_language))
        
        self.tab_widget.setTabText(0, get_text('exif_tab', self.current_language))
        self.tab_widget.setTabText(1, get_text('file_tab', self.current_language))
        self.tab_widget.setTabText(2, get_text('audio_tab', self.current_language))
        self.tab_widget.setTabText(3, get_text('pdf_tab', self.current_language))
        self.tab_widget.setTabText(4, get_text('docx_tab', self.current_language))
        self.tab_widget.setTabText(5, get_text('pptx_tab', self.current_language))
        self.tab_widget.setTabText(6, get_text('xlsx_tab', self.current_language))
        self.tab_widget.setTabText(7, get_text('video_tab', self.current_language))
        
        if self.file_path:
            self.display_metadata()

    def _setup_list_actions(self, list_widget):
        list_widget.setContextMenuPolicy(Qt.ActionsContextMenu)
        copy_action = QAction(get_text('copy', self.current_language), self)
        copy_action.setShortcut(QKeySequence.Copy)
        copy_action.triggered.connect(lambda: self.copy_selected_items(list_widget))
        list_widget.addAction(copy_action)

    def copy_selected_items(self, list_widget):
        selected = list_widget.selectedItems()
        if not selected:
            return
        text = '\n'.join([item.text() for item in selected])
        QApplication.clipboard().setText(text)

    def open_file(self):
        default_path = self._get_default_path()
        file_path, _ = QFileDialog.getOpenFileName(self, get_text('file_select', self.current_language), default_path)
        if file_path:
            self.file_path = file_path
            self.display_metadata()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files:
            self.file_path = files[0]
            self.display_metadata()

    def display_metadata(self):
        from .metadata import extract_metadata
        self.exif_list.clear()
        self.file_info_list.clear()
        self.audio_list.clear()
        self.pdf_list.clear()
        self.document_list.clear()
        self.presentation_list.clear()
        self.spreadsheet_list.clear()
        self.video_list.clear()
        
        self.metadata = extract_metadata(self.file_path)
        if not isinstance(self.metadata, dict):
            self.exif_list.addItem(get_text('error_read', self.current_language))
            self.remove_button.setEnabled(False)
            self.info_label.setText(f"{get_text('error_metadata', self.current_language)} {self.file_path}")
            return
        
        if not self.metadata:
            self.exif_list.addItem(get_text('no_metadata', self.current_language))
            self.remove_button.setEnabled(False)
            self.edit_button.setEnabled(False)
        else:
            exif_data = {}
            file_data = {}
            audio_data = {}
            pdf_data = {}
            docx_data = {}
            pptx_data = {}
            xlsx_data = {}
            video_data = {}
            
            for k, v in self.metadata.items():
                if k.startswith("EXIF:"):
                    exif_data[k] = v
                elif k.startswith("FILE:"):
                    file_data[k] = v
                elif k.startswith("ID3:"):
                    audio_data[k] = v
                elif k.startswith("PDF:"):
                    pdf_data[k] = v
                elif k.startswith("DOCX:"):
                    docx_data[k] = v
                elif k.startswith("PPTX:"):
                    pptx_data[k] = v
                elif k.startswith("XLSX:"):
                    xlsx_data[k] = v
                elif k.startswith("VIDEO:"):
                    video_data[k] = v
                else:
                    exif_data[k] = v
            
            if exif_data:
                for k, v in exif_data.items():
                    self.exif_list.addItem(f"{k}: {v}")
            else:
                self.exif_list.addItem(get_text('no_exif', self.current_language))
            
            if file_data:
                for k, v in file_data.items():
                    self.file_info_list.addItem(f"{k}: {v}")
            else:
                self.file_info_list.addItem(get_text('no_file_info', self.current_language))
            
            if audio_data:
                for k, v in audio_data.items():
                    self.audio_list.addItem(f"{k}: {v}")
            
            if pdf_data:
                for k, v in pdf_data.items():
                    self.pdf_list.addItem(f"{k}: {v}")
            
            if docx_data:
                for k, v in docx_data.items():
                    self.document_list.addItem(f"{k}: {v}")
            
            if pptx_data:
                for k, v in pptx_data.items():
                    self.presentation_list.addItem(f"{k}: {v}")
            
            if xlsx_data:
                for k, v in xlsx_data.items():
                    self.spreadsheet_list.addItem(f"{k}: {v}")
            
            if video_data:
                for k, v in video_data.items():
                    self.video_list.addItem(f"{k}: {v}")
            
            self.remove_button.setEnabled(True)
            self.edit_button.setEnabled(True)
        self.info_label.setText(f"{get_text('metadata_in_file', self.current_language)} {self.file_path}")

    def remove_metadata(self):
        from .metadata import remove_metadata
        ok, msg = remove_metadata(self.file_path)
        if ok:
            QMessageBox.information(self, get_text('remove_success', self.current_language), msg)
        else:
            QMessageBox.warning(self, get_text('error_title', self.current_language), msg)
        self.display_metadata()

    def edit_metadata(self):
        if not self.metadata:
            return
        
        from .metadata_editor_dialog import MetadataEditorDialog
        from .metadata_editor import save_metadata
        
        dialog = MetadataEditorDialog(self, self.metadata, self.current_language)
        if dialog.exec() == QDialog.Accepted:
            edited_metadata = dialog.get_result()
            if edited_metadata:
                ok, msg = save_metadata(self.file_path, edited_metadata)
                if ok:
                    QMessageBox.information(self, get_text('save_success', self.current_language), msg)
                    self.display_metadata()
                else:
                    QMessageBox.warning(self, get_text('error_title', self.current_language), msg)

def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
