#!/bin/bash

while true; do
  # Espera a que ocurra un cambio en los dispositivos (conectado/desconectado)
  udevadm monitor | grep -q "change.*drm"
  ~/.config/qtile/monitor_change.sh
done
