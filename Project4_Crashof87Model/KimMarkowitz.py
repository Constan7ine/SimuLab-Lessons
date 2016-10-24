import random
import time
import matplotlib.pyplot as plt

orders = []	
random.seed(time.time())
totalTradesOnDay = 0

class Agent(object):

	stocks = 500.0
	stockprice = 100.0

	cash = 50000.0

	# 0: Rebalancer, 1: Portfolio Insurers
	investorType = 0

	floor = 0.0
	k = 2.0

	bankrupt = False

	nextReviewCountdown = 0
	nextInvestCountdown = 0

	openOrders = 0

	def Wealth(self):
		return self.stocks*self.stockprice + self.cash

	def __init__(self, investorType):
		self.investorType = investorType
		self.floor = 0.75 * self.Wealth() # 0.75 is insurance level
		self.nextReviewCountdown = round(random.expovariate(1.0/5.0))
		self.nextInvestCountdown = round(random.expovariate(1.0/10.0))

	# Look at assets and decide if a bid will be put in
	def ReviewPortfolio(self):
		# We now need to estimate a price, based on the bids placed, however it's not clear how this is fair since people who review first have no bids available
		nbuying, nselling = DetermineSupplyDemand()
		
		if nselling == 0 and nbuying != 0:
			self.stockprice = 1.01*FindHighestBuyPrice()
		elif nbuying == 0 and nselling != 0:
			self.stockprice = 0.99*FindLowestSellPrice()
		elif nbuying != 0 and nselling != 0:
			self.stockprice = 0.5*(FindHighestBuyPrice() + FindLowestSellPrice())
		else:
			self.stockprice = self.stockprice
		#print("My Stock Price: {0}".format(self.stockprice))
		#print("Current Highest Buying Price: {0}".format(FindHighestBuyPrice()))
		#print("Current Lowest Selling Price: {0}".format(FindLowestSellPrice()))

		if self.investorType == 0:
			if (self.stocks*self.stockprice)/self.Wealth() > 0.5:
				#print("I'd like to sell")
				self.PlaceSaleOrder()
			elif (self.stocks*self.stockprice)/self.Wealth() < 0.5:
				#print("I'd like to buy")
				self.PlaceBuyOrder()	
		elif self.investorType == 1:
			if (self.stocks*self.stockprice)/(self.Wealth()-self.floor) > self.k:
				#print("I'd like to sell")
				self.PlaceSaleOrder()
			if (self.stocks*self.stockprice)/(self.Wealth()-self.floor) < self.k:
				#print("I'd like to buy")
				self.PlaceBuyOrder()		

	def PlaceSaleOrder(self):
		newOrder = Order(0.99*self.stockprice, self, 0)
		self.openOrders += 1
		for order in orders:
			if round(order.bidprice, 0) == round(newOrder.bidprice, 0) and order.orderType == 1:
				order.Execute(newOrder)
				#print("Sale Complete")
				del newOrder
				return
		orders.append(newOrder)
		# Check the master list for a sell order at that price, if one exists, execute the trade
		# Otherwise place order in master list

	def PlaceBuyOrder(self):
		newOrder = Order(1.01*self.stockprice, self, 1)
		self.openOrders += 1
		for order in orders:
			if round(order.bidprice, 0) == round(newOrder.bidprice, 0) and order.orderType == 0:
				order.Execute(newOrder)
				#print("Purchase Complete")
				del newOrder
				return
		orders.append(newOrder)
		# Check for matching counter offer and execute if possible
		# Place order in list for future processing

	def MaybeReviewPortfolio(self):
		self.nextReviewCountdown -= 1
		if self.nextReviewCountdown <= 0 or self.openOrders > 0:
			self.nextReviewCountdown = round(random.expovariate(1.0/5.0))
			#print("Reviewing portfolio of Type {0}".format(self.investorType))
			self.ReviewPortfolio()
			#print("Finished Review")

	def MaybeInvestMoney(self):
		self.nextInvestCountdown -= 1
		if self.nextInvestCountdown <=- 0:
			self.nextInvestCountdown = round(random.expovariate(1.0/10.0))
			investment = random.uniform(-8000.0, 8000.0)
			self.cash += investment
			#print("Investing {0}".format(investment))

class Order(object):
	bidprice = 0
	bidder = Agent(0)
	orderType = 0 # 0 for sale, 1 for buy, -1 for executed order
	def __init__(self, bidprice, bidder, orderType):
		self.bidprice = bidprice
		self.bidder = bidder
		self.orderType = orderType

	def Execute(self, other):
		global totalTradesOnDay
		if self.orderType == 0:
			totalTradesOnDay += 1
			self.bidder.stocks -= 1
			self.bidder.cash += self.bidprice
			self.bidder.openOrders -= 1
			other.bidder.stocks += 1
			other.bidder.cash -= self.bidprice
			other.bidder.openOrders -=1
		elif self.orderTypeMy pixx == 1:
			totalTradesOnDay += 1
			self.bidder.stocks += 1
			self.bidder.cash -= self.bidprice
			self.bidder.openOrders -= 1
			other.bidder.stocks -= 1
			other.bidder.cash += self.bidprice
			other.bidder.openOrders -=1
		self.orderType = -1
		other.orderType = -1

agents = []
for i in range(150):
	if i > 50:
		agent = Agent(1)
		agents.append(agent)
	else:
		agent = Agent(0)
		agents.append(agent)
random.shuffle(agents)

def DetermineSupplyDemand():
	nselling = 0
	nbuying = 0
	for order in orders:
		if order.orderType == 0:
			nselling += 1
		elif order.orderType == 1:
			nbuying += 1
	return nbuying, nselling

def FindHighestBuyPrice():
	highest = -1000
	for order in orders:
		if order.bidprice > highest and order.orderType == 1:
			highest = order.bidprice
	return highest

def FindLowestSellPrice():
	lowest = 100000000
	for order in orders:
		if order.bidprice < lowest and order.orderType == 0:
			lowest = order.bidprice
	return lowest

# What's the cycle of this model? It's one day.

tradeVolumeRecord = []
insurancePeriodCountdown = 65
# This represents each day. What happens each day?
for x in range(800):
	# A random (exp dist mean of 5 days) selection of agents will review their portfolios + agents from the previous day with open buy/sell orders
	# Randomly (exponential dist mean of 10) random (uniform between 8000 and +8000) amounts of cash are deposited in each investors account
	# At the end of each insurance period floor needs to be recalculated to new insurance period starts
	# If wealth is 0 agent is eliminated
	insurancePeriodCountdown -= 1
	for agent in agents:
		if agent.bankrupt == False:
			agent.MaybeReviewPortfolio()
			agent.MaybeInvestMoney()
			if insurancePeriodCountdown <= 0 and agent.investorType == 1:
				agent.floor = 0.75 * agent.Wealth()
				insurancePeriodCountdown = 65
			if agent.Wealth() <= 0:
				agent.bankrupt = True
				print("BANKRUIPT!")

	# for order in orders:
	# 	if order.orderType == -1:
	# 		del order
	
	# Maybe clear all orders from the previous day
	nbuying, nselling = DetermineSupplyDemand()
	#print("nbuying {0}, nselling {1}".format(nbuying, nselling))
	tradeVolumeRecord.append(totalTradesOnDay)
	totalTradesOnDay = 0
	orders = []
	# Day ends when every agent who reviewed their portfolio and has had the chance to place an order
	#pass

days = range(800)
plt.plot(days, tradeVolumeRecord)
plt.show()