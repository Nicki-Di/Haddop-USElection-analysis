#!/usr/bin/env python

import sys
import csv
from datetime import datetime, time

start_time = time(9, 0, 0)
end_time = time(17, 0, 0)

cols = csv.reader(sys.stdin)
next(cols)
for col in cols:
    # (State, Both, Biden, Trump, 1 as total)

    if col[13] != '' and col[14] != '':
        if 40.4772 < float(col[13]) < 45.0153 and -79.7624 < float(col[14]) < -71.7517 and start_time < time(
                int(col[0].split(" ")[1].split(":")[0]),
                int(col[0].split(" ")[1].split(":")[1]),
                int(col[0].split(" ")[1].split(":")[2])) < end_time:
            # Both
            if (col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump")) and ((
                    col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"))):
                print(
                    '%s\t%s\t%s\t%s\t%s' % ("new york", 1, 0, 0, 1))

            # Donald Trump
            elif col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump"):
                print(
                    '%s\t%s\t%s\t%s\t%s' % ("new york", 0, 1, 0, 1))

            # Joe Biden
            elif col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"):
                print(
                    '%s\t%s\t%s\t%s\t%s' % ("new york", 0, 0, 1, 1))

        elif 32.5121 < float(col[13]) < 42.0126 and -124.6509 < float(col[14]) < -114.1315 and start_time < time(
                int(col[0].split(" ")[1].split(":")[0]),
                int(col[0].split(" ")[1].split(":")[1]),
                int(col[0].split(" ")[1].split(":")[2])) < end_time:
            # Both
            if (col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump")) and ((
                    col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"))):
                print(
                    '%s\t%s\t%s\t%s\t%s' % ("california", 1, 0, 0, 1))

            # Donald Trump
            elif col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump"):
                print(
                    '%s\t%s\t%s\t%s\t%s' % ("california", 0, 1, 0, 1))

            # Joe Biden
            elif col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"):
                print(
                    '%s\t%s\t%s\t%s\t%s' % ("california", 0, 0, 1, 1))
