import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']


# total number of people who answered 'Ceballos'
total_ceballos = sum([1 for x in survey_responses if x == 'Ceballos'])
print(total_ceballos)

# survey length
survey_length = float(len(survey_responses))

# percentage of people in the survey who voted for Ceballos
percentage_ceballos = total_ceballos / survey_length
print(percentage_ceballos)

# Task 4
# In the real election, 54% of the 10,000 town population voted for Cynthia Ceballos. Your supervisors are concerned because this is a very different outcome than what the poll predicted. They want you to determine if there is something wrong with the poll or if given the sample size, it was an entirely reasonable result.

possible_surveys = np.random.binomial(survey_length, .54, size=10000) / survey_length

plt.hist(possible_surveys, range=(0,1), bins=20)
plt.show()

# As we saw, 47% of people we surveyed said they would vote for Ceballos, but 54% of people voted for Ceballos in the actual election.

# Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% of the vote and save it to the variable ceballos_loss_surveys.
possible_surveys_length = float(len(possible_surveys))
incorrect_predictions = len(possible_surveys[possible_surveys < .5])
ceballos_loss_surveys = incorrect_predictions / possible_surveys_length
print(ceballos_loss_surveys)

large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length, .54, size=10000) / large_survey_length

incorrect_predictions = len(large_survey[large_survey < .5])
ceballos_loss_new = incorrect_predictions / large_survey_length
print(ceballos_loss_new)
