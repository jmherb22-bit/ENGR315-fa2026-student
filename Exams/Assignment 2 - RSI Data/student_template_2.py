"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel, norm, chisquare, t, sem #import t_test, normal distribution, chisquare test, t distribution, and standard error

data_path = 'data/drop-jump/all_participant_data_rsi.csv' #relative path to data file
alpha = 0.05 #alpha value 

"""
Two Sided Tests for Two Samples
"""
def load_data(path: str) -> pd.DataFrame:
    """
    Load the RSI data 
    :param path: Relative path to the csv file
    :return: DataFrame with columns trial, force_plate_rsi, accelerometer_rsi, percent_error, participant
    """
    df = pd.read_csv(path) #read file 
    df['participant'] = df['trial'].str.split('_').str[0] #isolate participant letter to allow for filtering
    return df

def paired_t_test(force: np.ndarray, accel: np.ndarray, _alpha: float):
    """
    Conduct a two-sided paired t-test with both methods
    H0: mean dif(force plate - accel) = 0
    Ha:mean dif != 0
    :return: (t statistic, p-value, reject) where reject is True if H0 is rejected

    """

    t_stat, p_value = ttest_rel(force, accel) #Use t_test fxn to compare 
    return t_stat, p_value, p_value < _alpha


"""
Chi-Square Goodness of Fit
"""


def expected_normal_counts(bins, mu, std, num_samples):
    """
    Expected number of samples in each bin if the samples come from a normal distribution
    :param _bins: A numpy array of bin edges (may start with -np.inf and end with np.inf)
    :param _mu: Mean of the normal distribution
    :param _std: Standard deviation of the normal distribution
    :param _num_samples: Total number of samples
    :return: A numpy array of expected counts, one per bin (one fewer than the number of edges)
    """
    
    probs = norm.cdf(bins[1:], mu, std) - norm.cdf(bins[:-1], mu, std) #determine probablity of landing in bin by subtracting lower from upper CDF
    return probs*num_samples


def normal_fit_test(samples, alpha):
    """
    Test whether samples could come from a normal distribution, using the fitted mean and standard deviation
    :param _samples: A numpy array of samples
    :param _alpha: Level of significance, e.g. 0.05
    :return: A tuple (chi2 statistic, p-value, reject) where reject is True if the null hypothesis is rejected
    """

    # Step 1: fit normal distribution 
    mu, std = norm.fit(samples)
    # Step 2: 9 evenly spaced edges from mean - 2*std to mean + 2*std, plus -inf and +inf so outer bins catch tails
    bins = np.r_[-np.inf, np.linspace(mu - 2*std, mu + 2*std, 9), np.inf]
    # Step 3: count samples in each bin
    observed, _ = np.histogram(samples, bins)
    # Step 4: count expected for normal 
    expected = expected_normal_counts(bins, mu, std, len(samples))
    # Step 5: chisquare test after mean and std estimation
    chi_stat, p_value = chisquare(observed, expected, ddof=2)

    return chi_stat, p_value, p_value < alpha, mu, std, observed, expected

"""
Dataframe 95% Confidence 
"""

def confidence_int(samples: np.ndarray, confidence: float = 0.95):
    """
    Confidence interval for the mean using the t distribution
    :param samples: A numpy array of measurements
    :param confidence: Confidence level, default 95%
    :return: (mean, lower bound, upper bound)
    """

    mean = np.mean(samples) #define mean var as interval center
    lower, upper = t.interval(confidence, df=len(samples)-1, loc = mean, scale = sem(samples)) #range around mean, df = n -1, scale is standard error 
    return mean, lower, upper

if __name__ == "__main__":

    #load data and set RSI columns as arrays 
    data = load_data(data_path)
    force = data['force_plate_rsi'].to_numpy()
    accel = data['accelerometer_rsi'].to_numpy()

    """Task 1"""

    print('*'*20)
    print('Task 1:' )
    print('_'*20)
    t_stat, p_val, reject = paired_t_test(force, accel, alpha) #run t_test
    #print sample size , means, hypothisis, results, and decision 
    print(f'Number of trials: {len(data)}')
    print(f'Mean force plate RSI: {force.mean():.4f}')
    print(f'Mean accel RSI: {accel.mean():.4f}')
    print('H0: mean(force plate - accel) = 0 (methods agree)')
    print('Ha: mean(force plate - accel) != 0 (methods agree)')
    print(f't_value: {t_stat:.4f}')
    print(f'p_value: {p_val:.4f}')
    print(f'Reject H0 at alpha = {alpha}? {reject}')

    """Task 2"""

    print()
    print('*'*20)
    print('Task 2:' )
    print('_'*20)
    chi_stat, p_chi, reject_chi, mu, std, observed, expected = normal_fit_test(accel, alpha) #accel normal distribution, run chisquare test
    # print fit paraps, bin counts, p_value
    print(f'Fitted normal: mean = {mu:.4f}, {std:.4f}')
    print('H0: accel RSI follows normal distribution')
    print(f'Actual bin count: {observed}')
    print(f'Predicted bin counts: {np.round(expected, 2)}')
    print(f'p_value: {p_chi:.4f}')
    print('Fit accuracy: ' + ('BAD' if reject_chi else 'GOOD'))#Determine if data is good based on H0 reject accept

    #Graph of data with scaling to match density  
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(accel, bins=15, density=True, alpha=0.6, color='gray', edgecolor='black',
            label='Accel RSI')
    #adjust x range to wider than data
    x = np.linspace(accel.min() - 0.2, accel.max() + 0.2, 400)
    #Add normal probability and density fxn 
    ax.plot(x, norm.pdf(x, mu, std), 'r-', linewidth=2,
            label=f'Normal fit (mean={mu:.2f}, std={std:.2f})')
    #Axis labels 
    ax.set_xlabel('Accel RSI')
    ax.set_ylabel('Probability density')
    ax.set_title('Accelerometer RSI with fitted normal distribution')
    ax.legend()
    fig.tight_layout()
    fig.savefig('accel_rsi_histogram.png', dpi=150) #save graph
    

    """Task 3"""

    print()
    print('*'*20)
    print('Task 3:' )
    print('_'*20)
    #Keep participant F trils and reset index
    participant_f = data[data['participant'] == 'F'].reset_index(drop=True)
    print(participant_f)
    #95% and mean measurement method
    for label, col in [('Force plate', 'force_plate_rsi'), ('Accel', 'accelerometer_rsi')]:
        values = participant_f[col].to_numpy()
        mean, lower, upper = confidence_int(values, 0.95)
        print(f'{label} mean RSI: {mean:.4f}')
        print(f'{label} 95% CI: ({lower:.4f}, {upper:.4f})')
    plt.show()#Open graph 



