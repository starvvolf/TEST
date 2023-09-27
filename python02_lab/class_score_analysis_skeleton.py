

def read_data(filename):
    # TODO) Read `filename` as a list of integer numbers
    data = []
    f=open(filename,'r')
    for line in f.readlines():
        if line.startswith('#'):
            continue
        values=[int(word)for word in line.split(',')]
        data.append(values)
    return data

def calc_weighted_average(data_2d, weight):
    # TODO) Calculate the weighted averages of each row of `data_2d`
    average = []
    for idx in range(len(data_2d)):
        avg=data_2d[idx][0]*weight[0]+data_2d[idx][1]*weight[1]
        average.append(avg)
    return average

def analyze_data(data_1d):
    # TODO) Derive summary of the given `data_1d`
    # Note) Please don't use NumPy and other libraries. Do it yourself.
    mean = 0
    var = 0
    median = 0
    sum=0
    sqsum=0
    for idx in range(len(data_1d)):
        sum=sum+data_1d[idx]
        sqsum=sqsum+data_1d[idx]**2
    mean=sum/len(data_1d)
    var=sqsum/len(data_1d)-mean**2
    
    if len(data_1d)%2==0:
        median=(sorted(data_1d)[len(data_1d)/2]+sorted(data_1d)[len(data_1d)/2-1])/2
    else:
        median=sorted(data_1d)[len(data_1d)/2+0.5]
    
    
    return mean, var, median, min(data_1d), max(data_1d)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        average = calc_weighted_average(data, [40/125, 60/100])

        # Write the analysis report as a markdown file
        with open('class_score_analysis.md', 'w') as report:
            report.write('### Individual Score\n\n')
            report.write('| Midterm | Final | Total |\n')
            report.write('| ------- | ----- | ----- |\n')
            for ((m_score, f_score), a_score) in zip(data, average):
                report.write(f'| {m_score} | {f_score} | {a_score:.3f} |\n')
            report.write('\n\n\n')

            report.write('### Examination Analysis\n')
            data_columns = {
                'Midterm': [m_score for m_score, _ in data],
                'Final'  : [f_score for _, f_score in data],
                'Average': average }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f'* {name}\n')
                report.write(f'  * Mean: **{mean:.3f}**\n')
                report.write(f'  * Variance: {var:.3f}\n')
                report.write(f'  * Median: **{median:.3f}**\n')
                report.write(f'  * Min/Max: ({min_:.3f}, {max_:.3f})\n')