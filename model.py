from flask import Flask, render_template, url_for, session, request, g, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
from hashlib import sha256
import os, uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rschool.db'
app.secret_key = "secret"
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(400), nullable=False)
    firstname = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(400), nullable=False)
    profile = db.Column(db.Text, nullable=False)
    grade = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
