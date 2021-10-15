from scipy.stats import t, norm

# constants
b_1 = 0.5056
se = 0.0219
n = 507
alpha = 0.95

t_statistic = b_1 / se
print(f't_statistic is {t_statistic}')

critical_value = t.ppf(q=0.975, df=48)
print(f'critical value is {t.ppf(q=0.975, df=48)}')

p = 2*(1 - t.cdf(t_statistic, 49))
print(f'P value is {p}')

ci = [b_1 - critical_value * se, b_1 + critical_value * se]
print(f'CI is {ci}')
