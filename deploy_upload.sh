#! /usr/bin/env sh
git pull
python export_db.py
python upload.py
