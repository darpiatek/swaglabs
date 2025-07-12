# Common configuration for all environments
import platform
from pathlib import Path


os_name = platform.system()

PROJECT_DIR = Path(__file__).parent.parent.resolve()
JUNIT_REPORTS_DIR = PROJECT_DIR / "reports"
SCREENSHOTS_DIR = JUNIT_REPORTS_DIR / "screenshots"
LOG_DIR = PROJECT_DIR / "log"
URLS_FILE = PROJECT_DIR / "data" / "urls.ini"
USERS_FILE = PROJECT_DIR / "data" / "users.ini"

# create folders needed for the project
_folders_to_create = [JUNIT_REPORTS_DIR,
                      SCREENSHOTS_DIR,
                      LOG_DIR]

for folder in _folders_to_create:
    folder.mkdir(parents=True, exist_ok=True)
