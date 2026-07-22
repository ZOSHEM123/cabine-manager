"""
Global application settings.

This module contains all global constants used by the application.
Every other module should import its configuration from here.
"""

from pathlib import Path

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "Cabine Management"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Zoé Mpiana Mbaya"

# ==========================================================
# Language
# ==========================================================

DEFAULT_LANGUAGE = "fr"

# ==========================================================
# Currency
# ==========================================================

DEFAULT_CURRENCY = "CDF"
SECONDARY_CURRENCY = "USD"

# ==========================================================
# Window
# ==========================================================

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_MIN_WIDTH = 1024
WINDOW_MIN_HEIGHT = 600

# ==========================================================
# Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"

DATABASE_FILE = DATABASE_DIR / "cabin_management.db"

ASSETS_DIR = BASE_DIR / "assets"

REPORTS_DIR = BASE_DIR / "reports"

BACKUP_DIR = BASE_DIR / "backups"

LOGS_DIR = BASE_DIR / "logs"

# ==========================================================
# Database
# ==========================================================

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"