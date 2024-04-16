import testBot, os, load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__))
ENV_PATH = str(APP_ROOT.split("src", 1)[0]) + ".env"

load_dotenv.load_dotenv(ENV_PATH)

BOT_TOKEN = os.getenv("BOT_TOKEN")

testBot.start_bot(BOT_TOKEN)