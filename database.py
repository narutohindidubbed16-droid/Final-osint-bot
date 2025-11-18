# ===============================================
# 📌 database.py — SQLite Database System (FINAL)
# ===============================================

import sqlite3
import os

DB_FILE = "users.db"


# -----------------------------
# 🔥 CREATE DATABASE + TABLES
# -----------------------------
def init_db():
    db = sqlite3.connect(DB_FILE)
    cur = db.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            credits INTEGER DEFAULT 5,
            referred_by INTEGER
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS referrals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            referrer_id INTEGER,
            referred_id INTEGER,
            UNIQUE(referrer_id, referred_id)
        )
    """)

    db.commit()
    db.close()


# -----------------------------
# 👤 CREATE NEW USER
# -----------------------------
def create_user(user_id, username, first_name):
    db = sqlite3.connect(DB_FILE)
    cur = db.cursor()

    cur.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
    exists = cur.fetchone()

    if exists:
        db.close()
        return False  # user already exists

    cur.execute(
        "INSERT INTO users(user_id, username, first_name) VALUES(?,?,?)",
        (user_id, username, first_name)
    )

    db.commit()
    db.close()
    return True


# -----------------------------
# 💰 GET USER CREDITS
# -----------------------------
def get_user_credits(user_id):
    db = sqlite3.connect(DB_FILE)
    cur = db.cursor()

    cur.execute("SELECT credits FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()

    db.close()
    return row[0] if row else 0


# -----------------------------
# ➖ DECREASE CREDITS
# -----------------------------
def decrease_credit(user_id):
    db = sqlite3.connect(DB_FILE)
    cur = db.cursor()

    cur.execute("UPDATE users SET credits = credits - 1 WHERE user_id=?", (user_id,))
    db.commit()
    db.close()


# -----------------------------
# 🎁 REFERRAL SYSTEM
# -----------------------------
def add_referral(referrer_id, referred_id):
    if referrer_id == referred_id:
        return False

    db = sqlite3.connect(DB_FILE)
    cur = db.cursor()

    # Check duplicate referral
    cur.execute(
        "SELECT 1 FROM referrals WHERE referrer_id=? AND referred_id=?",
        (referrer_id, referred_id)
    )
    if cur.fetchone():
        db.close()
        return False

    # Insert new referral
    cur.execute(
        "INSERT INTO referrals(referrer_id, referred_id) VALUES(?,?)",
        (referrer_id, referred_id)
    )

    # Give credit to referrer only
    cur.execute(
        "UPDATE users SET credits = credits + 1 WHERE user_id=?",
        (referrer_id,)
    )

    # Store who referred this user
    cur.execute(
        "UPDATE users SET referred_by=? WHERE user_id=?",
        (referrer_id, referred_id)
    )

    db.commit()
    db.close()
    return True
