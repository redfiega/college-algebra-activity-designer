import sqlite3
import os
from datetime import datetime


def initialize_database():
    """Create the database and activities table if they don't exist."""
    conn = sqlite3.connect("activities.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            topic TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_activity(title: str, topic: str, content: str):
    """Save a generated activity to the database."""
    conn = sqlite3.connect("activities.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO activities (title, topic, content, created_at)
        VALUES (?, ?, ?, ?)
    """, (title, topic, content, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def get_all_activities():
    """Retrieve all saved activities from the database."""
    conn = sqlite3.connect("activities.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, topic, created_at FROM activities
        ORDER BY created_at DESC
    """)
    activities = cursor.fetchall()
    conn.close()
    return activities


def get_activity_by_id(activity_id: int):
    """Retrieve one specific activity by its ID."""
    conn = sqlite3.connect("activities.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, topic, content, created_at
        FROM activities WHERE id = ?
    """, (activity_id,))
    activity = cursor.fetchone()
    conn.close()
    return activity