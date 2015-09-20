# https://www.reddit.com/r/dailyprogrammer/comments/3i99w8/20150824_challenge_229_easy_the_dottie_number/

import math

eps = 0.001
dottle = 0.74

curr = 1
prev = 0

while abs(curr - prev) > eps:
	prev = curr
	curr = math.cos(curr)

print x
