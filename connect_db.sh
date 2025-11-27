#!/bin/bash
# Quick script to connect to the SQLite database

cd "$(dirname "$0")"
sqlite3 data/todo_manager.db

