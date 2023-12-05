from DataSet import DataSet
from HistoricalValues import HistoricalValues

class Main:

    @staticmethod
    def simulate(times): 

        results = []

        for i in range(times): 
            # create the unique dataset for simulation 
            stockValues = HistoricalValues.getStockValues() 
            bondValues = HistoricalValues.getBondValues()
            inflationValues = HistoricalValues.getInflationValues()

            dataSet = DataSet.createRandom(stockValues, 
                                    bondValues, 
                                    inflationValues, 
                                    assetAllocationStocks=50.0, 
                                    numYears=5, 
                                    correctionPercent=0.0)
            

            # must iterate over the dataset and use different withdrawal ideas
            account = 1000000
            for year in dataSet:
                account = account * (1 + year['portfolioValue'])  # first add this years growth
                # amountToWithdraw = WithdrawalMethod()
                account = account - 0

            results.append(account)

        # must show the results 
        return results
        
result = Main.simulate(10000) #10000
print(result)

# müssten hier sehen können, 
# bei welchen Konstellationen das ganze negativ wird. Also z.B. wenn zig Jahre hintereinander Minuswerte sind