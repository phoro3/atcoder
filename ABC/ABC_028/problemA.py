#coding:utf-8

score = int(raw_input())

if score <= 59:
    print "Bad"
elif score >= 60 and score <= 89:
    print "Good"
elif score >= 90 and score <= 99:
    print "Great"
elif score == 100:
    print "Perfect"
