#!/usr/bin/env python

import sys
import csv

cols = csv.reader(sys.stdin)
next(cols)
for col in cols:
    # Both
    if (col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump")) and ((
            col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"))):
        print(
            '%s\t%s\t%s\t%s\t%s\t%s' % ("Both Candidates", col[3], col[4], 1 if col[5] == "Twitter Web App" else 0,
                                        1 if col[5] == "Twitter for iPhone" else 0,
                                        1 if col[5] == "Twitter for Android" else 0))

    # Donald Trump
    if col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump"):
        print(
            '%s\t%s\t%s\t%s\t%s\t%s' % ("Donald Trump", col[3], col[4], 1 if col[5] == "Twitter Web App" else 0,
                                        1 if col[5] == "Twitter for iPhone" else 0,
                                        1 if col[5] == "Twitter for Android" else 0))

    # Joe Biden
    if col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"):
        print(
            '%s\t%s\t%s\t%s\t%s\t%s' % ("Joe Biden", col[3], col[4], 1 if col[5] == "Twitter Web App" else 0,
                                        1 if col[5] == "Twitter for iPhone" else 0,
                                        1 if col[5] == "Twitter for Android" else 0))
