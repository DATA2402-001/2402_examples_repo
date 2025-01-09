amts = [100.00, 50.00, 'missing', 25.00, 75.00, None]

# write a loop that computes gst amounts for each value in amts
# but uses 0.0 where that's not possible due to bad values
# [5.0, 2.5, 0.0, 1.25, 3.75, 0.0]

GST = 0.05

gst_amts = []

for value in amts:
    try:
        gst_amts.append(value * GST)
    except:
        gst_amts.append(0.0)

print(gst_amts)