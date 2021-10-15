"""Helper functions to create confidence interval"""

from scipy.stats import t, norm
import numpy as np


def create_ci_mean(alphas, x_bar, n, s, df):
    """
    Calculate the confidence interval of the point estimate (mean)
    :param alphas: list - a list of alpha
    :param x_bar: numeric
    :param n: integer - number of samples
    :param s: numeric - standard error
    :param df: integer - degree of freedom
    :return: a dictionary of confidence interval
    """
    ret_val = {}
    for alpha in alphas:
        ci = (x_bar - t.isf(alpha/2, df) * (s/np.sqrt(n)),
              x_bar + t.isf(alpha/2, df) * (s/np.sqrt(n)))
        ret_val[f'{(1-alpha)*100}%-CI'] = ci
    return ret_val


def create_ci_proportion(alphas, p_hat, n):
    """
    Calculate the confidence interval of the point estimate (proportion)
    :param alphas: list - a list of alpha
    :param p_hat: number - must be between 0 and 1
    :param n: integer - number of samples
    :return: a dictionary of confidence interval
    """
    ret_val = {}
    for alpha in alphas:
        ci = (p_hat - norm.isf(alpha/2) * np.sqrt(p_hat * (1-p_hat) / n),
              p_hat + norm.isf(alpha/2) * np.sqrt(p_hat * (1-p_hat) / n))
        ret_val[f'{(1-alpha)*100}%-CI'] = ci
    return ret_val
