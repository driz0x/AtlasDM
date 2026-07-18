"""
Resource management for AtlasDM.
"""

from pathlib import Path

from atlasdm.core.paths import PathManager


class ResourceManager:
    """
    Locates application resources.
    """

    def __init__(self) -> None:
        """Initialize the resource manager."""
        self._path_manager = PathManager()

    def icon(self, name: str) -> Path:
        """
        Resolve an icon path.

        Args:
            name: The name of the icon file.

        Returns:
            The resolved path to the icon.
        """
        return self._path_manager.assets_dir / "icons" / name

    def image(self, name: str) -> Path:
        """
        Resolve an image path.

        Args:
            name: The name of the image file.

        Returns:
            The resolved path to the image.
        """
        return self._path_manager.assets_dir / "images" / name

    def stylesheet(self, name: str) -> Path:
        """
        Resolve a stylesheet path.

        Args:
            name: The name of the stylesheet file.

        Returns:
            The resolved path to the stylesheet.
        """
        return self._path_manager.assets_dir / "styles" / name
