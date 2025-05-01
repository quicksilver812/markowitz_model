import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import scipy.optimize as optimization

# Declare constants
NUM_TRADING_DAYS = 252
NUM_PORTFOLIOS = 10000

# Select stocks
stocks = ['AAPL', 'GE', 'WMT', 'AMZN', 'TSLA', 'DB']

# Select start and end dates
start_date = '2012-01-01'
end_date = '2017-01-01'

# Download data
def download_data():
    data = {}
    for stock in stocks:
        ticker = yf.Ticker(stock)
        data[stock] = ticker.history(start = start_date, end = end_date)['Close']

    return pd.DataFrame(data)

# Visualise data
def show_data(data):
    data.plot(figsize = (12,8))
    plt.show()

# Calculate Returns
def calculate_returns(data):
    log_returns = np.log(data/data.shift(1))
    return log_returns[1:]

# Performance calculator
def performance_calculator(weights, returns):
    portfolio_return = np.sum(returns.mean()*weights)*NUM_TRADING_DAYS
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*NUM_TRADING_DAYS, weights)))
    return portfolio_return, portfolio_volatility

# Generate portfolios
def generate_portfolios(returns):
    portfolio_weights = []
    portfolio_returns = []
    portfolio_volatilities = []
    portfolio_sharpe_ratios = []

    for _ in range(NUM_PORTFOLIOS):
        w = np.random.rand(len(stocks))
        w /= np.sum(w)
        portfolio_weights.append(w)
        portfolio_return, portfolio_volatility = performance_calculator(w, returns)
        portfolio_returns.append(portfolio_return)
        portfolio_volatilities.append(portfolio_volatility)
        portfolio_sharpe_ratios.append(portfolio_return/portfolio_volatility)

    return np.array(portfolio_weights), np.array(portfolio_returns), np.array(portfolio_volatilities), np.array(portfolio_sharpe_ratios)

# Visualise portfolios
def show_portfolios(returns, volatilities, sharpe_ratios, opt, log_returns):
    plt.figure(figsize = (12,8))
    plt.scatter(volatilities, returns, c = sharpe_ratios, cmap = 'viridis', marker = 'o', alpha = 0.5)
    plt.title('Random Portfolio Performance')
    plt.xlabel('Risk')
    plt.ylabel('Return')
    plt.colorbar(label = 'Sharpe Ratio')
    plt.grid(True)
    portfolio_return, portfolio_volatility = performance_calculator(opt['x'].round(3), log_returns)
    plt.scatter(portfolio_volatility, portfolio_return, color = 'red', marker='*', s=120)
    plt.show()

# min_sharpe_function
def min_sharpe_function(weights, returns):
    portfolio_return, portfolio_volatility = performance_calculator(weights, returns)
    return -portfolio_return/portfolio_volatility

# Optimise portfolios
def optimise_portfolio(weights, returns):
    constraints = ({'type':'eq', 'fun': lambda x: np.sum(x)-1})
    bounds = tuple((0,1) for _ in range(len(stocks)))
    initial_guess = weights[0]
    optimum = optimization.minimize(
        fun=min_sharpe_function,
        x0=initial_guess,
        method='SLSQP',
        args=(returns,),
        bounds=bounds,
        constraints = constraints
    )
    return optimum

# Print optimised weights
def print_optimum_portfolio(opt, returns):
    print('Optimum portfolio weights: ', opt['x'].round(3))
    portfolio_return, portfolio_volatility = performance_calculator(opt['x'].round(3), returns)
    print('Optimum portfolio returns: ', portfolio_return)
    print('Optimum portfolio risk: ', portfolio_volatility)
    print('Optimum portfolio Sharpe Ratio: ', portfolio_return/portfolio_volatility)

# Main method
if __name__ == '__main__':
    dataset = download_data()
    log_daily_returns = calculate_returns(dataset)
    p_weights, p_returns, p_volatilities, p_sharpe_ratios = generate_portfolios(log_daily_returns)
    optimum_portfolio = optimise_portfolio(p_weights, log_daily_returns)
    print_optimum_portfolio(optimum_portfolio, log_daily_returns)
    show_portfolios(p_returns, p_volatilities, p_sharpe_ratios, optimum_portfolio, log_daily_returns)