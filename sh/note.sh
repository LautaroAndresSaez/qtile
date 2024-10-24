#! /bin/bash
NOTE=$(rofi -dmenu -p "Note")

if [ ! -z "$NOTE"]; then
    joplin note "$NOTE"
    notify-send "Note added" "$NOTE"
fi
