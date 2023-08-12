ax1,ay1,ax2,ay2,bx1,by1,bx2,by2 = -2,-2,2,2,-2,-2,2,2
Area1 = (ay2-ay1)*(ax2-ax1)
print(Area1)
Area2 = (bx2-bx1)*(by2-by1)
print(Area2)
overlap_x = max(0, min(ax2, bx2) - max(ax1, bx1))
overlap_y = max(0, min(ay2, by2) - max(ay1, by1))
common = overlap_x * overlap_y
result = Area1+Area2
x=result-common
print(x)
