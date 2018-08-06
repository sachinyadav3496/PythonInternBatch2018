#=================================================

# Problem: Market Basket Analysis using ARM - Apriori

#==================================================

# Required libraries/packages:

# arules


#==================================================================================
# Step1: - collecting data
# Our market basket analysis will utilize the purchase data collected from one month of
# operation at a real-world grocery store. The data contains 9,835 transactions or about
# 327 transactions per day (roughly 30 transactions per hour in a 12-hour business day),
# suggesting that the retailer is not particularly large, nor is it particularly small.


#==================================================================================
# 2. Explore and prepare the data
#==================================================================================

#setwd("/Users/rchowt/Desktop/2_ML/1_EXAMPLES/4_Classification")

library(arules)

# Open and read transactions
groceries <- read.transactions(file.choose(), sep = ",")

summary(groceries)

inspect(groceries[1:5])

# view the support level for the first three items in the grocery data:
itemFrequency(groceries[, 1:3])

#---------------------------------------------

# Visualizing item support - item frequency plots

#---------------------------------------------

itemFrequencyPlot(groceries, support = 0.1)

# If you would rather limit the plot to a specific number of items, the topN parameter
# can be used with itemFrequencyPlot():

itemFrequencyPlot(groceries, topN = 20)

#---------------------------------------------
# Visualizing the transaction data - plotting the sparse matrix
# The resulting diagram depicts a matrix with 5 rows and 169 columns, indicating the
# 5 transactions and 169 possible items we requested.
#--------------------------------------------
image(groceries[1:5])

# create random selection of 100 transactions is as follows:
# 100rows x 169 columns
image(sample(groceries, 100))

#===========================================================================
# Train the model
#===========================================================================

# In this case, if we attempt to use the default settings of support = 0.1 and
# confidence = 0.8, we will end up with a set of zero rules:
apriori(groceries)

# Set the parameters
groceryrules <- apriori(groceries, parameter = list(support =
                                                      0.006, confidence = 0.25, minlen = 2))
groceryrules

#===========================================================================
# Evaluate the model
#===========================================================================
summary(groceryrules)

inspect(groceryrules[1:3])

# Sorting the set of association rules
# Depending upon the objectives of the market basket analysis, the most useful rules
# might be the ones with the highest support, confidence, or lift.

inspect(sort(groceryrules, by = "lift")[1:5])

# Taking subsets of association rules
# Suppose that given the preceding rule, the marketing team is excited about the
# possibilities of creating an advertisement to promote berries, which are now in
# season.

berryrules <- subset(groceryrules, items %in% "berries")
inspect(berryrules)

# Saving association rules to a file or data frame
write(groceryrules, file = "groceryrules.csv",
      sep = ",", quote = TRUE, row.names = FALSE)

# convert the rules into an R data frame
groceryrules_df <- as(groceryrules, "data.frame")

str(groceryrules_df)

