#! /usr/bin/env sh

echo "######START######"
echo $("date")

git pull
python export_db.py
python upload.py

echo "######END######"
