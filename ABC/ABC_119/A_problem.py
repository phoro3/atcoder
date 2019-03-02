from datetime import datetime as dt

S = input()

tdatetime = dt.strptime(S, "%Y/%m/%d")
end_h = dt.strptime("2019/04/30", "%Y/%m/%d")

if tdatetime <= end_h:
    print("Heisei")
else:
    print("TBD")
