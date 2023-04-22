import os


class Config:

    API_ID = "2929027"
    API_HASH = "2beecc3ee357e6e3f2b2e783d4159f9f"
    BOT_TOKEN = "1878355269:AAGz9ApuIzIPs1EOjKHdCPQ_7bz2oiWRlUk"
    SESSION_NAME = "ScreenShotBot"
    LOG_CHANNEL = "-1001866679531"
    DATABASE_URL = "mongodb+srv://ksai:ksai@cluster0.kayzwoi.mongodb.net/cluster0?retryWrites=true&w=majority"
    AUTH_USERS = "959184369"
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
