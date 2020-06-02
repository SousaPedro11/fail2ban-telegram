from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


infos = db.Table('infos',
                 db.Column('target_ip',
                           db.Integer,
                           db.ForeignKey('ip_address.id'),
                           primary_key=True),
                 db.Column('log',
                           db.Integer,
                           db.ForeignKey('logs.id'),
                           primary_key=True))


class IPAddress(db.Model):
    __tablename__ = 'ip_address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip_addr = db.Column(db.String(45), unique=True, nulable=False)
    region = db.Column(db.String(20))
    
    logs = db.relationship('Log', backref='ip_address', lazy=True)
    infos = db.relationship('Log', secondary=infos, lazy='subquery',
                            backref=db.backref('ip_addresses', lazy=True))
    
    def __init__(self, ip_addr, region):
        self.ip_addr = ip_addr
        self.region = region
    
    def __repr__(self):
        return self.ip_addr


class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_moment = db.Column(db.DATETIME, default=datetime.now, nulable=False)
    protocol = db.Column(db.String(20), nullable=False)
    origin_ip = db.Column(db.Integer, db.ForeignKey('ip_address.id'), nulable=False)

    def __init__(self, event_moment, protocol, origin_ip):
        self.event_moment = event_moment
        self.protocol = protocol
        self.origin_ip = origin_ip

    def __repr__(self):
        return f'{self.origin_ip} {self.protocol}'
