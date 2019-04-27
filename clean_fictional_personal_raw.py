#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:05:38 2019

@author: mkayvanrad
"""

with open('fictional_person_raw.txt','r') as f:
    lines = f.readlines()

clean_lines = [x[0:x.find('(')].strip() for x in lines]

with open('fictional_person.txt','w') as f:
    for s in clean_lines:
        if len(s)>1:
            f.write(f"{s}\n")

