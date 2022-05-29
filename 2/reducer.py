#!/usr/bin/env python

import sys

state = None
current_state = None
current_both = 0
current_trump = 0
current_biden = 0
current_total = 0

for line in sys.stdin:
    line.strip()
    state, both, trump, biden, total = line.split("\t")
    both = int(float(both))
    trump = int(float(trump))
    biden = int(float(biden))
    total = int(float(total))

    if current_state == state:
        current_both += both
        current_trump += trump
        current_biden += biden
        current_total += total

    else:
        if current_state:
            print('%s\t%s\t%s\t%s\t%s' % (
                current_state, (current_both / current_total), (current_biden / current_total),
                (current_trump / current_total), current_total))
        current_state = state
        current_both = both
        current_trump = trump
        current_biden = biden
        current_total = total
if current_state == state:
    print('%s\t%s\t%s\t%s\t%s' % (
        current_state, (current_both / current_total), (current_biden / current_total),
        (current_trump / current_total), current_total))
