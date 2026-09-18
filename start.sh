#!/bin/sh

set -e

export DISPLAY=:99

echo "A iniciar display virtual..."

Xvfb :99 -screen 0 1280x800x24 &
sleep 2

xsetroot -solid "#0f172a"

echo "A iniciar window manager..."

fluxbox &
sleep 2

echo "A iniciar VNC..."

x11vnc \
    -display :99 \
    -forever \
    -shared \
    -nopw \
    -rfbport 5900 &

echo "A iniciar noVNC..."

websockify \
    --web=/usr/share/novnc \
    6080 \
    localhost:5900 &

echo "A iniciar MediSync..."

exec python src/main.py