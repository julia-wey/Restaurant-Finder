#!/usr/bin/env python3
# lib/debug.py

import ipdb
from models.__init__ import CONN, CURSOR

from models.city import City
from models.restaurant import Restaurant 

#City.create(name="Kismet", state="NY")
#City.find_by_id(2)
ipdb.set_trace()
