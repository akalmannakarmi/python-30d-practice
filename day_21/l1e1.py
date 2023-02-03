# Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

import statistics

class Data():
    def __init__(self,content):
        self.content = content
    def count(self):
        return len(self.content)
    def sum(self):
        s=0
        for item in self.content:
            s+=item
        return s
    def min(self):
        return min(self.content)
    def max(self):
        return max(self.content)
    def range(self):
        return max(self.content)-min(self.content)
    def mean(self):
        return statistics.mean(self.content)
    def median(self):
        return statistics.median(self.content)
    def mode(self):
        return statistics.mode(self.content)
    def count(self):
        return len(self.content)
    def count(self):
        return len(self.content)
    def std(self):
        return statistics.stdev(self.content)
    def var(self):
        return statistics.variance(self.content)
    def freq_dist(self):
        frequency_distribution = {}

        for c in self.content:
            if c not in frequency_distribution:
                frequency_distribution[c] = 1
            else:
                frequency_distribution[c] += 1
        return frequency_distribution

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Data(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]