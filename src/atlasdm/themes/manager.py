"""
Theme management for AtlasDM.
"""

from PySide6.QtWidgets import QApplication

from atlasdm.core.config import ConfigManager
from atlasdm.core.logger import get_logger
from atlasdm.core.resources import ResourceManager

logger = get_logger(__name__)


class ThemeManager:
    """
    Manages loading, applying, and switching themes for the application.
    """

    def __init__(self) -> None:
        """Initialize the theme manager."""
        self._config_manager = ConfigManager()
        self._resource_manager = ResourceManager()
        self._current_theme = "dark"

    def available_themes(self) -> list[str]:
        """
        Get a list of available themes.

        Returns:
            A list of theme names.
        """
        return ["dark", "light"]

    def load(self) -> None:
        """
        Load the configured theme from settings and apply it.
        """
        theme = self._config_manager.get("theme")
        if theme not in self.available_themes():
            theme = "dark"
        self.apply(theme)

    def apply(self, name: str) -> None:
        """
        Apply a theme to the application.

        Args:
            name: The name of the theme to apply.
        """
        if name not in self.available_themes():
            logger.warning(f"Theme '{name}' not found, falling back to dark")
            name = "dark"

        # Resolve path using the existing ResourceManager (which points to assets/styles)
        theme_path = self._resource_manager.theme(name)

        if theme_path.exists():
            try:
                with open(theme_path, encoding="utf-8") as f:
                    qss = f.read()

                app = QApplication.instance()
                if app:
                    app.setStyleSheet(qss)
                    self._current_theme = name
                    self._config_manager.set("theme", name)
                    logger.info(f"Successfully applied theme: {name}")
                else:
                    logger.error("Failed to apply theme: QApplication instance not found.")
            except OSError as e:
                logger.error(f"Error loading theme '{name}': {e}")
        else:
            logger.error(f"Theme file not found: {theme_path}")

    def current_theme(self) -> str:
        """
        Get the currently applied theme.

        Returns:
            The name of the current theme.
        """
        return self._current_theme
