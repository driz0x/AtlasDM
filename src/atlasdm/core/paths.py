"""
Path management for AtlasDM.
"""

import os
from pathlib import Path

from atlasdm.core.constants import APP_NAME


class PathManager:
    """
    Centralized path manager for application directories.
    """

    @property
    def project_root(self) -> Path:
        """
        Get the root directory of the project.

        Returns:
            The root Path of the project.
        """
        return Path(__file__).parent.parent.parent.parent.resolve()

    @property
    def _app_data_dir(self) -> Path:
        """Internal helper to get the OS-specific app data directory."""
        if os.name == "nt":
            base = Path(os.environ.get("APPDATA", "~")).expanduser()
        else:
            base = Path("~/.config").expanduser()
        app_dir = base / APP_NAME
        app_dir.mkdir(parents=True, exist_ok=True)
        return app_dir

    @property
    def assets_dir(self) -> Path:
        """
        Get the assets directory.

        Returns:
            The assets Path.
        """
        return self.project_root / "assets"

    @property
    def config_dir(self) -> Path:
        """
        Get the configuration directory.

        Returns:
            The configuration Path.
        """
        config = self._app_data_dir / "config"
        config.mkdir(parents=True, exist_ok=True)
        return config

    @property
    def logs_dir(self) -> Path:
        """
        Get the logs directory.

        Returns:
            The logs Path.
        """
        logs = self._app_data_dir / "logs"
        logs.mkdir(parents=True, exist_ok=True)
        return logs

    @property
    def cache_dir(self) -> Path:
        """
        Get the cache directory.

        Returns:
            The cache Path.
        """
        cache = self._app_data_dir / "cache"
        cache.mkdir(parents=True, exist_ok=True)
        return cache

    @property
    def plugins_dir(self) -> Path:
        """
        Get the plugins directory.

        Returns:
            The plugins Path.
        """
        plugins = self._app_data_dir / "plugins"
        plugins.mkdir(parents=True, exist_ok=True)
        return plugins

    @property
    def downloads_dir(self) -> Path:
        """
        Get the default downloads directory.

        Returns:
            The downloads Path.
        """
        downloads = Path.home() / "Downloads" / APP_NAME
        downloads.mkdir(parents=True, exist_ok=True)
        return downloads
