#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 on Synthesizing"""

DAY = raw_input('What day is it?: \n').lower()[:3:]
TIME = raw_input('What time is it?: \n')[:4:]
TIME = int(TIME)

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or \
    TIME < 0600 else False

if not SNOOZE:
    print 'BEEP!' * 5
