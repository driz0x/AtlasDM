"""
Main window module for AtlasDM.
"""

from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QStatusBar, QWidget

from atlasdm.ui.widgets.sidebar import Sidebar
from atlasdm.ui.widgets.toolbar import Toolbar


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
        
        self._setup_layout()

    def _setup_layout(self) -> None:
        """
        Set up the main layout and reserve placeholders.
        """
        # Toolbar
        self._toolbar = Toolbar(self)
        self.addToolBar(self._toolbar)

        # Central widget layout
        self._central_widget = QWidget(self)
        self._central_widget.setObjectName("CentralWidget")
        self.setCentralWidget(self._central_widget)

        self._main_layout = QHBoxLayout(self._central_widget)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        # Sidebar
        self._sidebar = Sidebar(self._central_widget)
        self._main_layout.addWidget(self._sidebar)

        # Main Content placeholder
        self._main_content_placeholder = QWidget(self._central_widget)
        self._main_content_placeholder.setObjectName("MainContentPlaceholder")
        self._main_layout.addWidget(self._main_content_placeholder)

        # Status Bar placeholder
        self._status_bar = QStatusBar(self)
        self._status_bar.setObjectName("StatusBar")
        self.setStatusBar(self._status_bar)
