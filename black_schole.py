from math import log, sqrt, exp
from scipy.stats import norm

def d1(S,K,r,t,sigma):
  return (log(S/K) + (r+(sigma**2/2.))*t) / (sigma * sqrt(t))

def d2(S,K,r,t,sigma):
  return d1(S,K,r,t,sigma) - sigma * sqrt(t)

# param: S = spot price, K = strike price, r = risk-free interest rate, t = time to maturity, sigma = volatility of asset
def call_price(S,K,r,t,sigma):
  return norm.cdf(d1(S,K,r,t,sigma)) * S - norm.cdf(d2(S,K,r,t,sigma)) * K * exp(-r * t)

# param: S = spot price, K = strike price, r = risk-free interest rate, t = time to maturity, sigma = volatility of asset
def put_price(S,K,r,t,sigma):
  return K*exp(-r * t) * norm.cdf(-d2(S,K,r,t,sigma)) - S * norm.cdf(-d1(S,K,r,t,sigma))