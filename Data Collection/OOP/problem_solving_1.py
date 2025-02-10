cake_bf = "Black Forest"
cake_vc = "Vanilla Cake"
cake_rv = "Red Velvet"
cake_ls = "Lemon Sponge Cake"
cake_chocolate = "Chocolate Cake"

print("• " + cake_bf, cake_vc, cake_rv, cake_ls, cake_chocolate, sep="\n• ")

#materials cost
materials_bf_each_pound = 180
materials_vc_each_pound = 150
materials_rv_each_pound = 220
materials_ls_each_pound = 165
materials_chocolate_each_pound = 170

#transportation
transportation_cost = 150 

#utility 
utility_bf_each_pound = (materials_bf_each_pound+ transportation_cost) * 0.03
utility_vc_each_pound = (materials_vc_each_pound+ transportation_cost) * 0.03
utility_rv_each_pound = (materials_rv_each_pound+ transportation_cost) * 0.03
utility_ls_each_pound = (materials_ls_each_pound+ transportation_cost) * 0.03
utility_chocolate_each_pound = (materials_chocolate_each_pound+ transportation_cost) * 0.03

space_cost = 50
staff_cost = 60

print(sep="\n")

total_inventory_cost_bf = materials_bf_each_pound+transportation_cost+utility_bf_each_pound+space_cost+staff_cost
total_inventory_cost_vc = materials_vc_each_pound+transportation_cost+utility_vc_each_pound+space_cost+staff_cost
total_inventory_cost_rv = materials_rv_each_pound+transportation_cost+utility_rv_each_pound+space_cost+staff_cost
total_inventory_cost_ls = materials_ls_each_pound+transportation_cost+utility_ls_each_pound+space_cost+staff_cost
total_inventory_cost_chocolate = materials_chocolate_each_pound+transportation_cost+utility_chocolate_each_pound+space_cost+staff_cost

print(total_inventory_cost_bf,total_inventory_cost_vc,total_inventory_cost_rv,total_inventory_cost_ls,total_inventory_cost_chocolate,sep="\n")

print(sep="\n")

#selling price
selling_price_bf_each_pound = 780
selling_price_vc_each_pound = 600
selling_price_rv_each_pound = 800
selling_price_ls_each_pound = 650
selling_price_chocolate_cake_each_pound = 660

print(selling_price_bf_each_pound,selling_price_vc_each_pound,selling_price_rv_each_pound,selling_price_ls_each_pound,selling_price_chocolate_cake_each_pound,sep="\n")

print(sep="\n")

discounted_selling_price_bf_each_pound = 780-(780 * 0.05)
discounted_selling_price_vc_each_pound = 600-(600 * 0.05)
discounted_selling_price_rv_each_pound = 800-(800 * 0.05)
discounted_selling_price_ls_each_pound = 650-(650 * 0.07)
discounted_selling_price_chocolate_cake_each_pound = 600-(600 * 0.07)

print(discounted_selling_price_bf_each_pound,discounted_selling_price_vc_each_pound,discounted_selling_price_rv_each_pound,discounted_selling_price_ls_each_pound,discounted_selling_price_chocolate_cake_each_pound,sep="\n")

print(sep="\n")

profit_for_bf = discounted_selling_price_bf_each_pound-total_inventory_cost_bf
profit_for_vc = discounted_selling_price_vc_each_pound-total_inventory_cost_vc
profit_for_rv = discounted_selling_price_rv_each_pound-total_inventory_cost_rv
profit_for_ls = discounted_selling_price_ls_each_pound-total_inventory_cost_ls
profit_for_chocolate_cake = discounted_selling_price_chocolate_cake_each_pound-total_inventory_cost_chocolate


print(profit_for_bf,profit_for_vc,profit_for_rv,profit_for_ls,profit_for_chocolate_cake,sep="\n")
print(sep="\n")

total_profit = profit_for_bf+profit_for_vc+profit_for_rv+profit_for_ls+profit_for_chocolate_cake
print(total_profit)

profit_percentage_bf= (profit_for_bf / total_inventory_cost_bf) * 100
profit_percentage_vc= (profit_for_vc / total_inventory_cost_vc) * 100
profit_percentage_rv= (profit_for_rv / total_inventory_cost_rv) * 100
profit_percentage_ls= (profit_for_ls / total_inventory_cost_ls) * 100
profit_percentage_chocolate_cake= (profit_for_chocolate_cake / total_inventory_cost_chocolate) * 100

print(sep="\n")

print(profit_percentage_bf,profit_percentage_vc,profit_percentage_rv,profit_percentage_ls,profit_percentage_chocolate_cake,sep="\n")