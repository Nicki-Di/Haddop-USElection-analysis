#!/usr/bin/env python

import sys

word = None
current_word = None
current_likes = 0
current_retweets = 0
current_web = 0
current_iphone = 0
current_android = 0

for line in sys.stdin:
    line.strip()
    word, likes, retweets, web, iphone, android = line.split("\t")
    likes = int(float(likes))
    retweets = int(float(retweets))
    web = int(float(web))
    iphone = int(float(iphone))
    android = int(float(android))

    if current_word == word:
        current_likes += likes
        current_retweets += retweets
        current_web += web
        current_iphone += iphone
        current_android += android
    else:
        if current_word:
            print(
                '%s\t%s\t%s\t%s\t%s\t%s' % (current_word, current_likes, current_retweets, current_web, current_iphone, current_android))
        current_word = word
        current_likes = likes
        current_retweets = retweets
        current_web = web
        current_iphone = iphone
        current_android = android
if current_word == word:
    print('%s\t%s\t%s\t%s\t%s\t%s' % (current_word, current_likes, current_retweets, current_web, current_iphone, current_android))
