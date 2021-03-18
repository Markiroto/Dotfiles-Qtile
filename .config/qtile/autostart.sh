#! /bin/bash
cbatticon &
lxsession &
picom --config /home/mark/.config/picom/picom.conf --experimental-backends &
nitrogen --restore &
urxvtd -q -o -f &
nm-applet &
dunst &
flameshot &
