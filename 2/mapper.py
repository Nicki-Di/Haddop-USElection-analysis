#!/usr/bin/env python

import sys
import csv
from datetime import time

start_time = time(9, 0, 0)
end_time = time(17, 0, 0)
states = ["new york", "texas", "california", "florida"]

cols = csv.reader(sys.stdin)
next(cols)
for col in cols:
    # (State, Both, Biden, Trump, 1 as total)
    if col[18].lower() in states and start_time <= time(int(col[0].split(" ")[1].split(":")[0]),
                                                        int(col[0].split(" ")[1].split(":")[1]),
                                                        int(col[0].split(" ")[1].split(":")[2])) <= end_time:
        # Both
        if (col[2].__contains__("#Trump") or col[2].__contains__("#DonaldTrump")) and ((
                col[2].__contains__("#Biden") or col[2].__contains__("#JoeBiden"))):
            print(
                '%s\t%s\t%s\t%s\t%s' % (col[18].lower(), 1, 0, 0, 1))

        # Donald Trump
        elif col[2].__contains__("#Trump") or col[2].__contains__("#DonaldTrump"):
            print(
                '%s\t%s\t%s\t%s\t%s' % (col[18].lower(), 0, 1, 0, 1))

        # Joe Biden
        elif col[2].__contains__("#Biden") or col[2].__contains__("#JoeBiden"):
            print(
                '%s\t%s\t%s\t%s\t%s' % (col[18].lower(), 0, 0, 1, 1))
