def calculate_total(exp_list):
    total=0
    for exp in exp_list:
        total+=exp
    return total

tom_exp_list=[2100,3400,3500]
joe_exp_list=[200,500,700]

print("Tom's total: ",calculate_total(tom_exp_list))
print("Joe's total: ",calculate_total(joe_exp_list))