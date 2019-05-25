S = input()

former = S[0:2]
latter = S[2:4]

is_former_month = False
is_latter_month = False
if 1 <= int(former) <= 12:
    is_former_month = True
if 1 <= int(latter) <= 12:
    is_latter_month = True

if is_former_month and is_latter_month:
    print("AMBIGUOUS")
elif is_former_month:
    print("MMYY")
elif is_latter_month:
    print("YYMM")
else:
    print("NA")
