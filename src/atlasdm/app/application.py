"""
Application module for AtlasDM.
"""

from PySide6.QtWidgets import QApplication

from atlasdm.core.constants import (
    APP_NAME,
    APP_VERSION,
    ORGANIZATION_DOMAIN,
    ORGANIZATION_NAME,
)
from atlasdm.themes.manager import ThemeManager
from atlasdm.ui.main_window import MainWindow


class AtlasDMApplication:
    """
    Main application class responsible for managing the application lifecycle.
    """

    def __init__(self, argv: list[str]) -> None:
        """
        Initialize the application.

        Args:
            argv: Command line arguments.
        """
        self._app = QApplication(argv)
        self._app.setApplicationName(APP_NAME)
        self._app.setOrganizationName(ORGANIZATION_NAME)
        self._app.setOrganizationDomain(ORGANIZATION_DOMAIN)
        self._app.setApplicationVersion(APP_VERSION)

        self._theme_manager = ThemeManager()
        self._theme_manager.load()

        self._main_window = MainWindow()

    def run(self) -> int:
        """
        Launch the application main window and start the event loop.

        Returns:
            Exit code of the application.
        """
        self._main_window.show()
        return self._app.exec()
