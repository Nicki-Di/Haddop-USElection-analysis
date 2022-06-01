#!/usr/bin/env python

import sys
import csv

cols = csv.reader(sys.stdin)
next(cols)
for col in cols:
    # (kind, Likes, Retweets, Web, iPhone, Android)

    # Both
    if (col[2].__contains__("#Trump") or col[2].__contains__("#DonaldTrump")) and ((
            col[2].__contains__("#Biden") or col[2].__contains__("#JoeBiden"))):
        print(
            '%s\t%s\t%s\t%s\t%s\t%s' % ("Both Candidates", col[3], col[4], 1 if col[5] == "Twitter Web App" else 0,
                                        1 if col[5] == "Twitter for iPhone" else 0,
                                        1 if col[5] == "Twitter for Android" else 0))

    # Donald Trump
    elif col[2].__contains__("#Trump") or col[2].__contains__("#DonaldTrump"):
        print(
            '%s\t%s\t%s\t%s\t%s\t%s' % ("Donald Trump", col[3], col[4], 1 if col[5] == "Twitter Web App" else 0,
                                        1 if col[5] == "Twitter for iPhone" else 0,
                                        1 if col[5] == "Twitter for Android" else 0))

    # Joe Biden
    elif col[2].__contains__("#Biden") or col[2].__contains__("#JoeBiden"):
        print(
            '%s\t%s\t%s\t%s\t%s\t%s' % ("Joe Biden", col[3], col[4], 1 if col[5] == "Twitter Web App" else 0,
                                        1 if col[5] == "Twitter for iPhone" else 0,
                                        1 if col[5] == "Twitter for Android" else 0))
