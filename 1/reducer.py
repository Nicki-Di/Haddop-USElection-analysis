#!/usr/bin/env python

import sys

kind = None
current_kind = None
current_likes = 0
current_retweets = 0
current_web = 0
current_iphone = 0
current_android = 0

for line in sys.stdin:
    line.strip()
    kind, likes, retweets, web, iphone, android = line.split("\t")
    likes = int(float(likes))
    retweets = int(float(retweets))
    web = int(float(web))
    iphone = int(float(iphone))
    android = int(float(android))

    if current_kind == kind:
        current_likes += likes
        current_retweets += retweets
        current_web += web
        current_iphone += iphone
        current_android += android
    else:
        if current_kind:
            print(
                '%s\t%s\t%s\t%s\t%s\t%s' % (current_kind, current_likes, current_retweets, current_web, current_iphone, current_android))
        current_kind = kind
        current_likes = likes
        current_retweets = retweets
        current_web = web
        current_iphone = iphone
        current_android = android
if current_kind == kind:
    print('%s\t%s\t%s\t%s\t%s\t%s' % (current_kind, current_likes, current_retweets, current_web, current_iphone, current_android))
