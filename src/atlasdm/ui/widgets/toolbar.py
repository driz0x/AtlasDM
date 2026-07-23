"""
Toolbar widget module for AtlasDM.
"""

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar, QWidget


class Toolbar(QToolBar):
    """
    The main toolbar of the AtlasDM application.
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        """
        Initialize the toolbar.
        """
        super().__init__("Main Toolbar", parent)
        self.setObjectName("MainToolbar")
        
        self._setup_actions()

    def _setup_actions(self) -> None:
        """
        Set up the toolbar actions.
        """
        self.action_new_download = QAction("New Download", self)
        self.addAction(self.action_new_download)

        self.action_paste_url = QAction("Paste URL", self)
        self.addAction(self.action_paste_url)
        
        self.action_start = QAction("Start", self)
        self.addAction(self.action_start)

        self.action_pause = QAction("Pause", self)
        self.addAction(self.action_pause)

        self.action_stop = QAction("Stop", self)
        self.addAction(self.action_stop)
