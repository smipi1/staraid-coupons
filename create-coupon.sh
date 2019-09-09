#!/bin/bash

rm -rf output/
mkdir -p output/

composite \
    -font Maven-Pro-Bold \
    -pointsize 30 \
    label:`./get-code.py` \
    -gravity center \
    -geometry +0-25 \
    src/back.png \
    output/coupon.pdf

