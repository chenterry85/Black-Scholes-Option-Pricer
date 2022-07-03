from math import log, sqrt

# param: S = spot price, K = strike price, r = interest rate, t = time to maturity, sigma = volatility of asset
def d1(S,K,r,t,sigma):
  return (log(S/K) + (r+(sigma**2/2.))*t) / (sigma * sqrt(t))

# param: S = spot price, K = strike price, r = interest rate, t = time to maturity, sigma = volatility of asset
def d2(S,K,r,t,sigma):
  return d1(S,K,r,t,sigma) - sigma * sqrt(t)

