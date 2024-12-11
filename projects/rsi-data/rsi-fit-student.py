import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
### YOUR CODE HERE
path_to_data_folder = "../../data/drop-jump/"
filename = "all_participant_data_rsi.csv"
full_path_to_file = path_to_data_folder + filename
data = pd.read_csv(full_path_to_file) # load data from csv using pandas

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

### YOUR CODE HERE
force_plate = data["force_plate_rsi"].to_numpy() # use pandas to select force plate column then convert to numpy
acceleration = data["accelerometer_rsi"].to_numpy() # use pandas to select acceleration column then convert to numpy

# calculate and report the distribution parameters (mu and std) for the force plate using numpy
mu_fp = np.mean(force_plate)
std_fp = np.std(force_plate)
print("The distribution parameter for the force plate are mu = " + str(mu_fp) + " and std = " + str(std_fp))

# calculate and report the distribution parameters (mu and std) for the acceleration using numpy
mu_accel = np.mean(acceleration)
std_accel = np.std(acceleration)
print("The distribution parameter for the acceleration are mu = " + str(mu_accel) + "and std = " + str(std_accel))

# I learned the following code from the distribution-fit.py lecture example in module 6
plt.figure(figsize=(8, 6))
# use lin space to make a vector with a linear spacing between start (min) and stop (max) points then use the normal
# distribution probability density function to generate results for both force plate and acceleration
x_fp = np.linspace(start=np.min(force_plate), stop=np.max(force_plate), num=10000)
y_fp = norm.pdf(x_fp, loc=mu_fp, scale=std_fp)
x_accel = np.linspace(start=np.min(acceleration), stop=np.max(acceleration), num=10000)
y_accel = norm.pdf(x_accel, loc=mu_accel, scale=std_accel)

# plot the distribution of force plate and acceleration with appropriate labels
plt.plot(x_fp, y_fp, label='Force Plate')
plt.plot(x_accel, y_accel, label="Acceleration")
plt.title("Probability Density Function for Force Plate and Acceleration Data")
plt.xlabel("Value")
plt.ylabel("Probability Distribution")
plt.legend()
plt.show()


"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the binds. An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

"""
Acceleration
"""
### YOUR CODE HERE
# The following code was learned from the chi-square-dist-fit.py lecture example in module 6
# bin the examples
bins = np.linspace(0, 2, 9) # generate 9 bins between [0,2)
bins = np.r_[-np.inf, bins, np.inf] # append _inf and +inf to both ends of the bins
# place observations into bins, density = false so results will contain the number of samples in each bin (from numpy documentation)
observed_counts_accel, observed_edges_accel = np.histogram(acceleration, bins=bins, density=False)

expected_prob_accel = np.diff(norm.cdf(bins, loc=mu_accel, scale=std_accel)) # use CDF for probabilities for each bin
expected_accel = expected_prob_accel * len(acceleration) # Expected frequency for each bin

alpha = 0.05 # set alpha to 0.05
(chi_stat_accel, p_value_accel) = chisquare(f_obs=observed_counts_accel, f_exp=expected_accel) # Conduct chi2 test
print('Chi2 stat: ', str(chi_stat_accel), 'p-value: ', str(p_value_accel))
if p_value_accel < alpha:
    print('Reject null hypothesis. Acceleration data does not fit the normal distribution.')
else:
    print('Accept null hypothesis. Acceleration data fits the normal distribution')


"""
Force Plate
"""
### YOUR CODE HERE
# Repeat previous code for force plate data
observed_counts_fp, observed_edges_fp = np.histogram(force_plate, bins=bins, density=False)

expected_prob_fp = np.diff(norm.cdf(bins, loc=mu_fp, scale=std_fp))
expected_fp = expected_prob_fp * len(force_plate)

(chi_stat_fp, p_value_fp) = chisquare(f_obs=observed_counts_fp, f_exp=expected_fp)
print('Chi2 stat: ', str(chi_stat_fp), 'p-value: ', str(p_value_fp))
if p_value_fp < alpha:
    print('Reject null hypothesis. Force Plate data does not fit the normal distribution.')
else:
    print('Accept null hypothesis. Force Plate data fits the normal distribution')


"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE
# To help with my understanding of this code, I looked at examples 5 and 6 in the hypothesis-test.py example in module 5
# use ttest_ind to compare the datasets with two-sided test
# from scipy documentation, alternative='two-sided' means the means of the distributions underlying the samples are unequal.
t_test, p_value = ttest_ind(acceleration, force_plate, alternative='two-sided')
print("The p-value is " + str(p_value) + " and the t-test statistic is " + str(t_test))
if p_value < alpha:
    print("Reject the null hypothesis. The RSI values for the acceleration and force plate data are not equivalent.")
else:
    print("Accept the null hypothesis. The RSI values for acceleration and force plate data are equivalent.")



"""
Question 4 (Bonus): Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE
# I learned how to answer this question based on part 3 of the distribution-fit example in module 6
rsi_error = force_plate - acceleration # difference between force plate and accelerometer
mu_error = np.mean(rsi_error) # mean of RSI error between force plate and accelerometer
std_error = np.std(rsi_error) # standard deviation of RSI error between force plate and accelerometer

plt.figure(figsize=(8, 6))
plt.hist(rsi_error, bins=16, label="RSI Error") # histogram of the data with 16 bins

rsi_min = min(rsi_error) # use min to find start for linspace
rsi_max = max(rsi_error) # use max to find stop for linspace
# use lin space to make a vector with a linear spacing of points between start and stop
x_rsi = np.linspace(rsi_min, rsi_max, 100)
rsi_pdf = norm.pdf(x_rsi, mu_error, std_error) # use the normal distribution probability density function to generate results
plt.plot(x_rsi, rsi_pdf, label="Normal Curve") # plot the sampled distribution

plt.title("RSI Error Distribution To Fitted Normal Curve")
plt.xlabel("RSI Error")
plt.ylabel("Density")
plt.legend()
plt.show()

