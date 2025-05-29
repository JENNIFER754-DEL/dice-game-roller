from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    games = relationship("Game", back_populates="player")

    def __repr__(self):
        return f"<Player(id={self.id}, name={self.name})>"

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    start_time = Column(DateTime, default=datetime.utcnow)

    player = relationship("Player", back_populates="games")
    rolls = relationship("Roll", back_populates="game")

    def __repr__(self):
        return f"<Game(id={self.id}, player_id={self.player_id}, start_time={self.start_time})>"

class Roll(Base):
    __tablename__ = 'rolls'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    die1 = Column(Integer, nullable=False)
    die2 = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)

    game = relationship("Game", back_populates="rolls")

    def __repr__(self):
        return f"<Roll(id={self.id}, game_id={self.game_id}, die1={self.die1}, die2={self.die2}, total={self.total})>"
