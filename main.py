from math import log, sqrt, exp
from signal import signal
from scipy.stats import norm

# param: S = spot price, K = strike price, r = interest rate, t = time to maturity, sigma = volatility of asset

def d1(S,K,r,t,sigma):
  return (log(S/K) + (r+(sigma**2/2.))*t) / (sigma * sqrt(t))

def d2(S,K,r,t,sigma):
  return d1(S,K,r,t,sigma) - sigma * sqrt(t)

def call(S,K,r,t,sigma):
  return norm(d1(S,K,r,t,sigma)) * S - norm(d2(S,K,r,t,sigma)) * K * exp(-r * t)