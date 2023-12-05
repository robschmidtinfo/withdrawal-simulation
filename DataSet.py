import random 

class DataSet:

    @staticmethod
    def createRandom(stockValues, 
                bondValues, 
                inflationValues, 
                assetAllocationStocks, 
                numYears, 
                correctionPercent=0.0):
        
        dataSet = []

        for year in range(1, numYears + 1):
            stockPercent = round(random.choice(stockValues) + correctionPercent, 2)
            bondPercent = round(random.choice(bondValues) + correctionPercent, 2)
            inflationValue = round(random.choice(inflationValues), 2)

            portfolioValue = round((assetAllocationStocks / 100) * stockPercent + \
                              ((100 - assetAllocationStocks) / 100) * bondPercent, 2)

            dataSet.append({
                'year': year,
                'portfolioValue': portfolioValue,
                'inflationValue': inflationValue
            })

        return dataSet
