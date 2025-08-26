study_hours = [1, 2, 3, 4, 5, 6, 7]
test_scores = [1, 2, 3, 4, 5, 6, 7]

sum_x = sum(study_hours)
sum_y = sum(test_scores)

running_sum = 0
i = 0  # (you need to initialize i)
while i < 7:
    running_sum += study_hours[i] * test_scores[i]
    i += 1
sum_xy = running_sum

n = len(study_hours)

running_sum2 = 0
i = 0
while i < 7:
    running_sum2 += (study_hours[i])**2
    i += 1
sum_x2 = running_sum2

slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
intercept = (sum_y - slope * sum_x) / n

print(sum_x)
print(sum_y)
print(sum_xy)
print(n)
print(sum_x2)
print(slope)
print(intercept)

