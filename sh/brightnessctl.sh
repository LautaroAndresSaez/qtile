#!/usr/bin/env bash

MIN=10

current=$(brightnessctl -m | cut -d, -f4 | tr -d '%')
if [[ "$1" == "down" ]]; then
    if (( current > MIN )); then
        brightnessctl set 5%-
    fi
else
    brightnessctl set +5%
fi
