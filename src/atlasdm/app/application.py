"""
Application module for AtlasDM.
"""

from PySide6.QtWidgets import QApplication

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
        self._app.setApplicationName("AtlasDM")
        self._app.setOrganizationName("driz0x")
        self._app.setOrganizationDomain("github.com/driz0x")
        self._app.setApplicationVersion("0.1.0")
        
        self._main_window = MainWindow()

    def run(self) -> int:
        """
        Launch the application main window and start the event loop.

        Returns:
            Exit code of the application.
        """
        self._main_window.show()
        return self._app.exec()
