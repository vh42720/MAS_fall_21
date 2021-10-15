from utils.ci_helper import create_ci_mean, create_ci_proportion
from scipy.stats import t

alpha_list = [0.01]

# confidence intervals for mean
print('Mean CI')
ret_dict = create_ci_mean(alphas=alpha_list, x_bar=273.04, n=25, s=56.2, df=24)
for k, v in ret_dict.items():
    print(k, v)
print('--------------')

# confidence intervals for proportion
print('Proportion CI')
ret_dict = create_ci_proportion(alphas=alpha_list, p_hat=0.55, n=600)
for k, v in ret_dict.items():
    print(k, v)
print('--------------')

# t value
t_value = t.isf(alpha_list[0]/2, 35)
print(t_value)
