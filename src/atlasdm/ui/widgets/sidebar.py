"""
Sidebar widget for AtlasDM.
"""

from PySide6.QtWidgets import QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget


class Sidebar(QWidget):
    """
    Main navigation sidebar for the application.
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        """
        Initialize the Sidebar widget.

        Args:
            parent: The parent widget.
        """
        super().__init__(parent)
        self.setObjectName("Sidebar")
        self.setFixedWidth(250)

        self._setup_ui()

    def _setup_ui(self) -> None:
        """
        Set up the sidebar layout and navigation items.
        """
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(10, 20, 10, 20)
        self._layout.setSpacing(10)

        # Navigation items
        self._btn_downloads = QPushButton("Downloads")
        self._btn_downloads.setObjectName("NavBtnDownloads")

        self._btn_queue = QPushButton("Queue")
        self._btn_queue.setObjectName("NavBtnQueue")

        self._btn_history = QPushButton("History")
        self._btn_history.setObjectName("NavBtnHistory")

        self._btn_settings = QPushButton("Settings")
        self._btn_settings.setObjectName("NavBtnSettings")

        # Add buttons to layout
        self._layout.addWidget(self._btn_downloads)
        self._layout.addWidget(self._btn_queue)
        self._layout.addWidget(self._btn_history)

        # Spacer to push settings to the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self._layout.addItem(spacer)

        self._layout.addWidget(self._btn_settings)
