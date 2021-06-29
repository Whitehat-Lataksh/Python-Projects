# School 1 With Z SCORE

Rawschool1Data = pd.read_csv('./DataVisualization/intervention/School 1 Orignal.csv')
School1Data = Rawschool1Data["Math_score"].tolist()

PopulationMean = statistics.mean(School1Data)

def mean(counter):
    dataSet100 = []
    for i in range(0, counter):
        number = random.randint(0, len(School1Data)-1)
        dataSet100.append(School1Data[number])

    mean = statistics.mean(dataSet100)
    SD = statistics.stdev(dataSet100)
    return mean

def mean1000():
    dataSet1000 = []
    for i in range(0, 100):
        raw_data = mean(30)
        dataSet1000.append(raw_data)
    meanOfSample1000 = statistics.mean(dataSet1000)

    SDofSample1000 = statistics.stdev(dataSet1000)
    SampleMean, SampleSD = readInterventions()

    zScore = (meanOfSample1000 - SampleMean) / SDofSample1000
    print("ZScore of school 1  is " + zScore.__str__())


def readInterventions():
    rawintervention1 = pd.read_csv('./DataVisualization/intervention/School1Sample.csv')
    intervention1 = rawintervention1["Math_score"].tolist()

    SDIntervention1 = statistics.stdev(intervention1)
    meanIntervention1 = statistics.mean(intervention1)
    return meanIntervention1, SDIntervention1


if __name__ == '__main__':
    mean1000()




# School 2 With Z SCORE

Rawschool2Data = pd.read_csv('./DataVisualization/intervention/School 2 Orignal .csv')
School2Data = Rawschool2Data["Math_score"].tolist()

PopulationMean = statistics.mean(School2Data)

def mean(counter):
    dataSet100 = []
    for i in range(0, counter):
        number = random.randint(0, len(School2Data)-1)
        dataSet100.append(School2Data[number])

    mean = statistics.mean(dataSet100)
    SD = statistics.stdev(dataSet100)
    return mean

def mean1000():
    dataSet1000 = []
    for i in range(0, 100):
        raw_data = mean(30)
        dataSet1000.append(raw_data)
    meanOfSample1000 = statistics.mean(dataSet1000)

    SDofSample1000 = statistics.stdev(dataSet1000)

    SampleMean, SampleSD = readInterventions()



    zScore = (SampleMean - PopulationMean ) / SDofSample1000

    print("ZScore of school 2 is " + zScore.__str__())


def readInterventions():
    rawintervention1 = pd.read_csv('./DataVisualization/intervention/School2Sample.csv')
    intervention1 = rawintervention1["Math_score"].tolist()
    SDIntervention1 = statistics.stdev(intervention1)
    meanIntervention1 = statistics.mean(intervention1)
    return meanIntervention1, SDIntervention1


if __name__ == '__main__':
    mean1000()

    # School 3 With Z SCORE

Rawschool3Data = pd.read_csv('./DataVisualization/intervention/School 3 Orignal.csv')
School3Data = Rawschool2Data["Math_score"].tolist()

PopulationMean = statistics.mean(School3Data)

def mean(counter):
    dataSet100 = []
    for i in range(0, counter):
        number = random.randint(0, len(School3Data)-1)
        dataSet100.append(School3Data[number])

    mean = statistics.mean(dataSet100)
    SD = statistics.stdev(dataSet100)
    return mean

def mean1000():
    dataSet1000 = []
    for i in range(0, 100):
        raw_data = mean(30)
        dataSet1000.append(raw_data)
    meanOfSample1000 = statistics.mean(dataSet1000)

    SDofSample1000 = statistics.stdev(dataSet1000)

    SampleMean, SampleSD = readInterventions()

    zScore = (SampleMean - PopulationMean ) / SDofSample1000

    print("ZScore of school 3 is " + zScore.__str__())


def readInterventions():
    rawintervention1 = pd.read_csv('./DataVisualization/intervention/School3Sample.csv')
    intervention1 = rawintervention1["Math_score"].tolist()
    SDIntervention1 = statistics.stdev(intervention1)
    meanIntervention1 = statistics.mean(intervention1)
    return meanIntervention1, SDIntervention1


if __name__ == '__main__':
    mean1000()