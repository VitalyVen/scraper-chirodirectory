BOT_NAME = "chir"

LOG_LEVEL = "INFO"

SPIDER_MODULES = ["src.spiders"]
NEWSPIDER_MODULE = "src.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
)

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    "src.pipelines.SQLAlchemyPipeline": 300,
}

# DB Configs
# -------------------------------------------------------------------
DB = {
    "dialect": "postgresql",
    "host": "localhost",
    "port": "15432",
    "username": "docker",
    "password": "docker",
    "db_name": "chir",
}
