"""
Application entry point for AtlasDM.
"""

import sys

from atlasdm.app.application import AtlasDMApplication


def main() -> None:
    """
    Launch the AtlasDM application.
    """
    app = AtlasDMApplication(sys.argv)
    sys.exit(app.run())


if __name__ == "__main__":
    main()
