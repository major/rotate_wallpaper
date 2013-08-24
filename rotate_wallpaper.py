#!/usr/bin/python
#
# Copyright 2013 Major Hayden
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from random import shuffle
import os
import shlex
import subprocess
import sys


WALLPAPER_PATH = "/home/major/Pictures/Wallpapers/"

try:
    with open('/usr/bin/feh'):
        pass
except IOError:
    print 'Missing feh executable. On Fedora, try running "yum install feh"'
    sys.exit(1)


image_files = os.listdir(WALLPAPER_PATH)
shuffle(image_files)

cmd = "feh --bg-fill %s/%s" % (WALLPAPER_PATH, image_files[0])
retval = subprocess.call(shlex.split(cmd))
sys.exit(retval)
