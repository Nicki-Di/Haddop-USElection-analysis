#!/usr/bin/env python

import sys
import csv

cols = csv.reader(sys.stdin)
next(cols)
for col in cols:
    # Both
    if (col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump")) and ((
            col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"))):
        print('%s\t%s' % ("BothCandidatesLikes", col[3]))
        print('%s\t%s' % ("BothCandidatesRetweets", col[4]))
        if col[5] == "Twitter Web App":
            print('%s\t%s' % ("BothCandidatesWeb", 1))
        elif col[5] == "Twitter for iPhone":
            print('%s\t%s' % ("BothCandidatesiPhone", 1))
        elif col[5] == "Twitter for Android":
            print('%s\t%s' % ("BothCandidatesAndroid", 1))

    # Donald Trump
    if col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump"):
        print('%s\t%s' % ("DonaldTrumpLikes", col[3]))
        print('%s\t%s' % ("DonaldTrumpRetweets", col[4]))
        if col[5] == "Twitter Web App":
            print('%s\t%s' % ("DonaldTrumpWeb", 1))
        elif col[5] == "Twitter for iPhone":
            print('%s\t%s' % ("DonaldTrumpiPhone", 1))
        elif col[5] == "Twitter for Android":
            print('%s\t%s' % ("DonaldTrumpAndroid", 1))

    # Joe Biden
    if col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"):
        print('%s\t%s' % ("JoeBidenLikes", col[3]))
        print('%s\t%s' % ("JoeBidenRetweets", col[4]))
        if col[5] == "Twitter Web App":
            print('%s\t%s' % ("JoeBidenWeb", 1))
        elif col[5] == "Twitter for iPhone":
            print('%s\t%s' % ("JoeBideniPhone", 1))
        elif col[5] == "Twitter for Android":
            print('%s\t%s' % ("JoeBidenAndroid", 1))

##################################


# !/usr/bin/env python

import sys
import csv

cols = csv.reader(sys.stdin)
next(cols)
for col in cols:
    # Both
    if (col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump")) and ((
            col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"))):
        print('%s\t%s' % ("BothCandidatesLikes", col[3]))
        print('%s\t%s' % ("BothCandidatesRetweets", col[4]))
        if col[5] == "Twitter Web App":
            print('%s\t%s' % ("BothCandidatesWeb", 1))
        elif col[5] == "Twitter for iPhone":
            print('%s\t%s' % ("BothCandidatesiPhone", 1))
        elif col[5] == "Twitter for Android":
            print('%s\t%s' % ("BothCandidatesAndroid", 1))

    # Donald Trump
    if col[2].lower().__contains__("#trump") or col[2].lower().__contains__("#donaldtrump"):
        print('%s\t%s' % ("DonaldTrumpLikes", col[3]))
        print('%s\t%s' % ("DonaldTrumpRetweets", col[4]))
        if col[5] == "Twitter Web App":
            print('%s\t%s' % ("DonaldTrumpWeb", 1))
        elif col[5] == "Twitter for iPhone":
            print('%s\t%s' % ("DonaldTrumpiPhone", 1))
        elif col[5] == "Twitter for Android":
            print('%s\t%s' % ("DonaldTrumpAndroid", 1))

    # Joe Biden
    if col[2].lower().__contains__("#biden") or col[2].lower().__contains__("#joebiden"):
        print('%s\t%s' % ("JoeBidenLikes", col[3]))
        print('%s\t%s' % ("JoeBidenRetweets", col[4]))
        if col[5] == "Twitter Web App":
            print('%s\t%s' % ("JoeBidenWeb", 1))
        elif col[5] == "Twitter for iPhone":
            print('%s\t%s' % ("JoeBideniPhone", 1))
        elif col[5] == "Twitter for Android":
            print('%s\t%s' % ("JoeBidenAndroid", 1))
