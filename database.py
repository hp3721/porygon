import sqlalchemy as sa


metadata = sa.MetaData()

restrictions_tbl = sa.Table("restrictions", metadata,
                            sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                            sa.Column("user", sa.BigInteger, nullable=False),
                            sa.Column("type", sa.String(30), nullable=False, index=True),
                            sa.Column("expiry", sa.DateTime, nullable=True, index=True),
                            sa.UniqueConstraint("user", "type", name="user-type"))

config_tbl = sa.Table("config", metadata,
                      sa.Column("name", sa.String(50), primary_key=True),
                      sa.Column("value", sa.String(100)))

github_watch_tbl = sa.Table("github-watch", metadata,
                      sa.Column("name", sa.String(100), nullable=False, primary_key=True),
                      sa.Column("owner", sa.String(50), nullable=False, primary_key=True),
                      sa.Column("commit", sa.String(50), nullable=False))

starboard_tbl = sa.Table("starboard", metadata,
                      sa.Column("message_id", sa.BigInteger, primary_key=True),
                      sa.Column("author_id", sa.BigInteger, nullable=False),
                      sa.Column("star_count", sa.Integer),
                      sa.Column("starboard_id", sa.Integer, nullable=False),
                      sa.Column("channel_id", sa.BigInteger, nullable=False))
