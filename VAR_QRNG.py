
def VaR_PRNG(stock, S, start, end, c, period, iterations):
    data = pdr.get_data_yahoo(stock, start=start, end=end)['Adj Close']
    returns = (data / data.shift(1)) - 1
    returns.dropna(inplace=True)
    mu = returns.mean()
    sigma = returns.std()
    z = np.random.normal(0, 1, [1, iterations])
    ST = S * np.exp(period * (mu - 0.5 * sigma ** 2) + sigma * np.sqrt(period) * z)
    ST = np.sort(ST)
    Spc = np.percentile(ST, (1 - c) * 100)
    var = S - Spc
    return str(int(var))

def VaR_QRNG(stock, S, start, end, c, period, iterations):
    data = pdr.get_data_yahoo(stock, start=start, end=end)['Adj Close']
    returns = (data / data.shift(1)) - 1
    returns.dropna(inplace=True)
    mu = returns.mean()
    sigma = returns.std()
    #quantum_engine = MainEngine()
    #z = np.array([0])
    z = np.array([])
    rand_array = np.array([])
    max = 2
    iterations = 0
    min = 1
    is_number_generated = True
    leading_zero = ""
    diff = len(bin(max)[2:]) - len(bin(min)[2:])
    for zero in range(diff):
        leading_zero += "0"

    if (min > max or max - min < 2 or min < 0 or max < 0):
        is_number_generated = False
        z = -1
    for w in range(iterations):
        # Range
        is_number_generated = True
        # print(len(bin(100)[2:]))
        random_fraction = get_random_number(diff, leading_zero + str(bin(min)[2:]), bin(max)[2:])

    m=getPstaticRandomNum()
    min_rand = np.amin(m)
    max_rand = np.amax(m, axis=0)
    print(max_rand)
    print(min_rand)
    for i in m:
       normalized_rand = ( i - min_rand )/ (max_rand - min_rand)
       rand_array= np.append(rand_array,normalized_rand)
    ST = S * np.exp(period * (mu - 0.5 * sigma ** 2) + sigma * np.sqrt(period) * rand_array)
    ST = np.sort(ST)
    Spc = np.percentile(ST, (1 - c) * 100)
    var = S - Spc
    return str(int(var))
