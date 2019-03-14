# bouncing_balls.py

# author: awakenedhaki

def bouncingBall(h: float, bounce: float, window: float) -> int:
    views = 1
    if (h <= 0) or (h <= window) or not (0 < bounce < 1):
        return -1
    else:
        h *= bounce
        while h >= window:
            views += 2
            h *= bounce
        return views
