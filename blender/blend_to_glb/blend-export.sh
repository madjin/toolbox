#!/usr/bin/env bash

DIR=$(dirname "$0")
blender "$1" --background -noaudio -P "$DIR/blender/to-glb.py"
