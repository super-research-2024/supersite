import pynecone as pc

class SupersiteConfig(pc.Config):
    pass

config = SupersiteConfig(
    app_name="supersite",
    api_url="http://161.253.74.202:8000",
    bun_path="$HOME/.bun/bin/bun"
    db_url="sqlite:///pynecone.db",
)