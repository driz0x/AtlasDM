"""
Main window module for AtlasDM.
"""

from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """
    The main window of the AtlasDM application.
    """

    def __init__(self) -> None:
        """
        Initialize the main window.
        """
        super().__init__()
        self.setWindowTitle("AtlasDM")
        self.resize(1280, 720)
