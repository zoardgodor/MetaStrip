"""Dialog for editing metadata"""
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
                              QTableWidget, QTableWidgetItem, QMessageBox)
from PySide6.QtCore import Qt
from .translations import get_text


class MetadataEditorDialog(QDialog):
    def __init__(self, parent, metadata_dict, language='en'):
        super().__init__(parent)
        self.metadata_dict = metadata_dict.copy()
        self.language = language
        self.result_metadata = None
        
        self.setWindowTitle(get_text('edit_metadata', language))
        self.setGeometry(100, 100, 700, 500)
        
        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels([
            get_text('metadata_key', language),
            get_text('metadata_value', language)
        ])
        self.table.horizontalHeader().setStretchLastSection(True)
        
        self.populate_table()
        
        layout.addWidget(self.table)
        
        button_layout = QHBoxLayout()
        
        add_button = QPushButton(get_text('add_metadata', language))
        add_button.clicked.connect(self.add_row)
        button_layout.addWidget(add_button)
        
        delete_button = QPushButton(get_text('delete_metadata', language))
        delete_button.clicked.connect(self.delete_row)
        button_layout.addWidget(delete_button)
        
        button_layout.addStretch()
        
        save_button = QPushButton(get_text('save_button', language))
        save_button.clicked.connect(self.save_changes)
        button_layout.addWidget(save_button)
        
        cancel_button = QPushButton(get_text('cancel_button', language))
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def populate_table(self):
        """Populate table with metadata"""
        self.table.setRowCount(len(self.metadata_dict))
        
        for row, (key, value) in enumerate(self.metadata_dict.items()):
            if key.startswith("FILE:"):
                continue
            
            key_item = QTableWidgetItem(key)
            value_item = QTableWidgetItem(str(value))
            
            self.table.setItem(row, 0, key_item)
            self.table.setItem(row, 1, value_item)
    
    def add_row(self):
        """Add new metadata row"""
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
    
    def delete_row(self):
        """Delete selected metadata row"""
        current_row = self.table.currentRow()
        if current_row >= 0:
            self.table.removeRow(current_row)
    
    def save_changes(self):
        """Save metadata changes"""
        self.result_metadata = {}
        
        for row in range(self.table.rowCount()):
            key_item = self.table.item(row, 0)
            value_item = self.table.item(row, 1)
            
            if key_item and value_item:
                key = key_item.text().strip()
                value = value_item.text().strip()
                
                if key and value:  
                    self.result_metadata[key] = value
        
        for key, value in self.metadata_dict.items():
            if key.startswith("FILE:"):
                self.result_metadata[key] = value
        
        self.accept()
    
    def get_result(self):
        """Get edited metadata"""
        return self.result_metadata
