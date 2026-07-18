"""
Configuration management for AtlasDM.
"""

from typing import Any

DEFAULT_CONFIG = {
    "theme": "dark",
    "language": "en",
    "download_directory": None,
}


class ConfigManager:
    """
    Application configuration management.
    """

    def __init__(self) -> None:
        """Initialize the configuration manager."""
        self._config: dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> None:
        """Load the configuration."""
        # Persistent storage out of scope for Milestone 1.2
        pass

    def save(self) -> None:
        """Save the configuration."""
        # Persistent storage out of scope for Milestone 1.2
        pass

    def get(self, key: str) -> Any:
        """
        Get a configuration value.

        Args:
            key: The configuration key.

        Returns:
            The configuration value.
        """
        return self._config.get(key)

    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.

        Args:
            key: The configuration key.
            value: The configuration value.
        """
        self._config[key] = value

    def reset(self) -> None:
        """Reset the configuration to default values."""
        self._config = DEFAULT_CONFIG.copy()
