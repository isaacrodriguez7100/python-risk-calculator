upper_limit = 0
lower_limit = 0
while True:
    try:
        lower_limit = int(input("Lower limit: "))
        upper_limit = int(input("Upper limit: "))
    except ValueError:
        print("Please enter a number")
        continue
    if lower_limit >= upper_limit:
        print("Upper limit must be greater than Lower limit")
        continue
    else:
        break

middle_bound = (upper_limit - lower_limit)/2
stop_loss = upper_limit - middle_bound
value_per_mkt = middle_bound * 2
sell_gain_line = lower_limit - value_per_mkt
buy_gain_line = upper_limit + value_per_mkt

risk_target = 220
multiplier_guess = risk_target / value_per_mkt
start = int(multiplier_guess) -2
end = int(multiplier_guess) + 2
best_multiplier = 0
best_error = float("inf")
for multiplier in range(start, end):
    result = value_per_mkt * multiplier
    error = abs(result - risk_target)
    if error < best_error:
        best_error = error
        best_multiplier = multiplier
rec_exposure = value_per_mkt * best_multiplier

LINES = {
    "stop loss" : stop_loss,
    "value per market" : value_per_mkt,
    "sell gain line" : sell_gain_line,
    "buy gain line" : buy_gain_line,
    "Recommended amount of mrkt/s" : best_multiplier,
    "Recommended exposure" : rec_exposure
}

for label, value in LINES.items():
    print(f"{label.title()} is: {value}")