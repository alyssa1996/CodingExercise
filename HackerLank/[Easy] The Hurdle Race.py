def hurdleRace(k, height):
    if max(height)<=k:
        return 0
    else:
        return max(height)-k
