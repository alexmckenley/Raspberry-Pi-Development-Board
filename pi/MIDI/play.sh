#!/bin/bash
# ------------------------------------------------------------------
# Alex Taylor 
# MIDI Light Show
# ------------------------------------------------------------------
SONG = $1
#python alsa_client.py
aplaymidi -p 128:0 SONG & sleep .35 && aplaymidi -p 14:0 SONG