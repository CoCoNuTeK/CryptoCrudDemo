from app.core.database import db  # Import the existing Gino instance

class Crypto(db.Model):
    __tablename__ = 'cryptos'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=True)
    symbol = db.Column(db.String(), nullable=True)
    current_price = db.Column(db.Numeric(), nullable=True)
    market_cap = db.Column(db.Numeric(), nullable=True)
    market_cap_rank = db.Column(db.Integer(), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    last_updated = db.Column(db.DateTime(), nullable=True)

    def __repr__(self):
        return f"<Crypto {self.name} ({self.symbol})>"
