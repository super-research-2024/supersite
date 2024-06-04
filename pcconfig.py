import pynecone as pc

class SupersiteConfig(pc.Config):
    pass

config = SupersiteConfig(
    app_name="supersite",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)