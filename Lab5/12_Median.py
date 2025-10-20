
def median(data):
    sort_val = sorted(data)
    n = len(data)
    if n % 2 == 0:
        mid1 = sort_val[n // 2 - 1]
        mid2 = sort_val[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sort_val[n // 2]

data_odd = [1, 2, 3, 4, 5]
data_even = [1, 2, 3, 4, 5, 6]
median_odd = median(data_odd)
median_even = median(data_even)
print(f"Median for odd: {median_odd}")
print(f"Median for even: {median_even}")


