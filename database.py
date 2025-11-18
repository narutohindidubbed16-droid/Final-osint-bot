# ===============================
# 📌 database.py
# User Database + Referral System
# ===============================

import sqlite3

DB_NAME = "users.db"


# ----------------------------------
# CREATE TABLES
# ----------------------------------
def init_db():
    with sqlite3.connect(DB_NAME) as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            credits INTEGER DEFAULT 10,
            referred_by INTEGER
        )
        """)

        db.execute("""
        CREATE TABLE IF NOT EXISTS referrals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            referrer_id INTEGER,
            referred_id INTEGER,
            UNIQUE(referrer_id, referred_id)
        )
        """)
        db.commit()


# ----------------------------------
# CREATE USER
# ----------------------------------
def create_user(uid, username, first_name):
    with sqlite3.connect(DB_NAME) as db:
        cur = db.execute("SELECT user_id FROM users WHERE user_id=?", (uid,))
        if cur.fetchone():
            return False  # already exists

        db.execute("""
            INSERT INTO users (user_id, username, first_name, credits)
            VALUES (?, ?, ?, ?)
        """, (uid, username, first_name, 10))
        db.commit()
        return True


# ----------------------------------
# GET CREDITS
# ----------------------------------
def get_user_credits(uid):
    with sqlite3.connect(DB_NAME) as db:
        cur = db.execute("SELECT credits FROM users WHERE user_id=?", (uid,))
        row = cur.fetchone()
        return row[0] if row else 0


# ----------------------------------
# DECREASE CREDIT
# ----------------------------------
def decrease_credit(uid):
    with sqlite3.connect(DB_NAME) as db:
        db.execute("""
            UPDATE users SET credits = credits - 1
            WHERE user_id=? AND credits > 0
        """, (uid,))
        db.commit()


# ----------------------------------
# ADD REFERRAL
# ----------------------------------
def add_referral(referrer, referred):
    if referrer == referred:
        return False

    with sqlite3.connect(DB_NAME) as db:

        cur = db.execute("""
            SELECT 1 FROM referrals WHERE referrer_id=? AND referred_id=?
        """, (referrer, referred))
        if cur.fetchone():
            return False  # already counted

        # add referral
        db.execute("""
            INSERT INTO referrals (referrer_id, referred_id)
            VALUES (?, ?)
        """, (referrer, referred))

        # give credit to referrer
        db.execute("""
            UPDATE users SET credits = credits + 1 WHERE user_id=?
        """, (referrer,))

        # register referred_by
        db.execute("""
            UPDATE users SET referred_by=? WHERE user_id=?
        """, (referrer, referred))

        db.commit()
        return True
