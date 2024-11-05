#!/bin/bash

rm -rf ../francescovitucci/*

bundle exec jekyll build

python3.12 lilypondprocess.py

cp -R _site/* ../francescovitucci
