import matplotlib.pyplot as plt
target = int(float(input('please enter the target profit $ ')))
print('-proft target:${}'.format(target))
# starting_balance = 31000.00
# current_balance = 31000.00
# sim_balance = 51000.00
starting_balance = int(float(input('please enter the balance your account started with $')))
current_balance = int(float(input('please enter your current balance $')))
print('-current balance: ${}'.format(current_balance))
loss = starting_balance - current_balance
# sim_loss = starting_balance-sim_balance
print('-loss: ${}'.format(loss))
#total_contracts = 3
total_contracts = int(input('please enter the amount of contracts you would like to trade'))
print('-total_contracts:',total_contracts)
# contracts = {'cl':54.06,
#               'es':2980.00,
#               'rty':1526.90}
# print('-contracts:',contracts)
# contracts_price_10 = 54.06
# print('-contracts_price:',contracts_price_10)
max_risk = current_balance*.01/3
print('----max risk: ${}'.format(max_risk))
contracts_tick_value_31 = 31.25 *total_contracts
contracts_tick_value_12 = 12.50 * total_contracts
contracts_tick_value_10 = 10.00 * total_contracts
contracts_tick_value_6 = 6.25 * total_contracts
contracts_tick_value_5 = 5.00 *total_contracts

print('-contracts_tick_value 31:${:.2f}'.format(contracts_tick_value_31))
print('-contracts_tick_value 12:${:.2f}'.format(contracts_tick_value_6))
print('-contracts_tick_value 10:${:.2f}'.format(contracts_tick_value_10))
print('-contracts_tick_value 6:${:.2f}'.format(contracts_tick_value_6))
print('-contracts_tick_value 5:${:.2f}'.format(contracts_tick_value_5))

if current_balance < starting_balance:
    print('-current balance is Less than starting balance .. continuing to perform risk analysis to reach target profit')
    current_balance = starting_balance-loss
    print('-current_balance: ${:.2f}'.format(current_balance))
    current_target_loss = target - current_balance
    print('-current loss from target profit: ${:.2f}'.format(current_target_loss))
    daily_target = current_target_loss/12
    print('-daily target: ${:.2f}'.format(daily_target))
    hourly_target = daily_target/4
    print('-hourly target: ${:.2f}'.format(hourly_target))
#     for contract in contracts:
    print('-Target contract size in each market to reach daily target')
    profit_size31 = daily_target/contracts_tick_value_31
    print('-profit size for $31 tick size: ',profit_size31)
    max_loss31 = profit_size31 *.015
    print('max loss: $',max_loss31*daily_target)
    profit_size12 = daily_target/contracts_tick_value_6
    print('-profit size for $12 tick size:',profit_size12)
    max_loss12 = profit_size12 *.015
    print('max loss: $',max_loss12*daily_target)
    profit_size10 = daily_target/contracts_tick_value_10
    print('-profit size for $10 tick size:',profit_size10)
    max_loss10 = profit_size10 *.015
    print('max loss: $',max_loss10*daily_target)
    profit_size6 = daily_target/contracts_tick_value_6
    print('-profit size for $6 tick size:',profit_size6)
    max_loss6 = profit_size6 *.015
    print('max loss: $',max_loss6*daily_target)
    profit_size5 = daily_target/contracts_tick_value_5
    print('-profit size for $5 tick size: ',profit_size5)
    max_loss5 = profit_size5 *.015
    print('max loss: $',max_loss5*daily_target)
elif current_balance == starting_balance:
    print('-current balance is Less than starting balance .. continuing to perform risk analysis to reach target profit')
    current_balance = starting_balance-loss
    print('-current_balance: ${:.2f}'.format(current_balance))
    current_target_loss = target - current_balance
    print('-current loss from target profit: ${:.2f}'.format(current_target_loss))
    daily_target = current_target_loss/12
    print('-daily target: ${:.2f}'.format(daily_target))
    hourly_target = daily_target/4
    print('-hourly target: ${:.2f}'.format(hourly_target))
#     for contract in contracts:
    print('-Target contract size in each market to reach daily target')
    profit_size31 = daily_target/contracts_tick_value_31
    print('-profit size for $31 tick size: ',profit_size31)
    max_loss31 = profit_size31 *.015
    print('max loss: $',max_loss31*daily_target)
    profit_size12 = daily_target/contracts_tick_value_6
    print('-profit size for $12 tick size:',profit_size12)
    max_loss12 = profit_size12 *.015
    print('max loss: $',max_loss12*daily_target)
    profit_size10 = daily_target/contracts_tick_value_10
    print('-profit size for $10 tick size:',profit_size10)
    max_loss10 = profit_size10 *.015
    print('max loss: $',max_loss10*daily_target)
    profit_size6 = daily_target/contracts_tick_value_6
    print('-profit size for $6 tick size:',profit_size6)
    max_loss6 = profit_size6 *.015
    print('max loss: $',max_loss6*daily_target)
    profit_size5 = daily_target/contracts_tick_value_5
    print('-profit size for $5 tick size: ',profit_size5)
    max_loss5 = profit_size5 *.015
    print('max loss: $',max_loss5*daily_target)


elif current_balance >= starting_balance:
    print('-current balance is Less than starting balance .. continuing to perform risk analysis to reach target profit')
    current_balance = starting_balance-loss
    print('-current_balance: ${:.2f}'.format(current_balance))
    current_target_loss = target - current_balance
    print('-current loss from target profit: ${:.2f}'.format(current_target_loss))
    daily_target = current_target_loss/12
    print('-daily target: ${:.2f}'.format(daily_target))
    hourly_target = daily_target/4
    print('-hourly target: ${:.2f}'.format(hourly_target))
#     for contract in contracts:
    print('-Target contract size in each market to reach daily target')
    profit_size31 = daily_target/contracts_tick_value_31
    print('-profit size for $31 tick size: ',profit_size31)
    max_loss31 = profit_size31 *.015
    print('max loss: $',max_loss31*daily_target)
    profit_size12 = daily_target/contracts_tick_value_6
    print('-profit size for $12 tick size:',profit_size12)
    max_loss12 = profit_size12 *.015
    print('max loss: $',max_loss12*daily_target)
    profit_size10 = daily_target/contracts_tick_value_10
    print('-profit size for $10 tick size:',profit_size10)
    max_loss10 = profit_size10 *.015
    print('max loss: $',max_loss10*daily_target)
    profit_size6 = daily_target/contracts_tick_value_6
    print('-profit size for $6 tick size:',profit_size6)
    max_loss6 = profit_size6 *.015
    print('max loss: $',max_loss6*daily_target)
    profit_size5 = daily_target/contracts_tick_value_5
    print('-profit size for $5 tick size: ',profit_size5)
    max_loss5 = profit_size5 *.015
    print('max loss: $',max_loss5*daily_target)
