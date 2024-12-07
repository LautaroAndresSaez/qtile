#!/bin/bash

export DISPLAY=:0

# Detecta las pantallas conectadas
PRIMARY=$(xrandr --query | grep " connected primary" | cut -d" " -f1)
SECONDARY=$(xrandr --query | grep " connected" | grep -v "primary" | cut -d" " -f1)

# Configura pantallas según las detectadas
if [ -n "$PRIMARY" ] && [ -n "$SECONDARY" ]; then
  # Configuración: pantalla secundaria a la derecha de la primaria
  xrandr --output "$PRIMARY" --auto --primary --output "$SECONDARY" --auto --right-of "$PRIMARY"
elif [ -n "$PRIMARY" ]; then
  # Solo la pantalla primaria
  xrandr --output "$PRIMARY" --auto
elif [ -n "$SECONDARY" ]; then
  # Solo la pantalla secundaria
  xrandr --output "$SECONDARY" --auto
fi
