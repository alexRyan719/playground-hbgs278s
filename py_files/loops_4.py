# Multiplication
to_mult = 5
mult_times = 10
mult_ans = to_mult

for num_m in range(1,mult_times):
    mult_ans += to_mult

print(mult_ans)

# Division
to_div = 50
div_times = 5
div_ans = div_times
div_count = 0

while div_ans <= to_div:
    div_ans += div_times
    div_count += 1

print(div_count)
