#!/usr/bin/env python
# coding: utf-8

# In[84]:


from abc import ABC, abstractmethod

class IStrategy(ABC):            
    @abstractmethod
    def realPrice(self, consumePrice):
        pass
    
    @abstractmethod
    def strategyName(self):
        pass
    
class RebateStrategy(IStrategy):    #6折商品促销策略
    @classmethod
    def realPrice(self, consumePrice):
        return consumePrice * 0.6

    def strategyName(self):
        return "RebateStrategy"

class PromotionalStrategy(IStrategy):  #150以上打5折商品促销策略
    @classmethod
    def realPrice(self, consumePrice):
        if consumePrice > 150:
            consumePrice = 150 + (consumePrice-150) * 0.5
        return consumePrice

    def strategyName(self):
        return "PromotionalStrategy"

class ReduceStrategy(IStrategy):  #满100元减40元，满200减90元，满300元减150元商品促销案策略
    @classmethod
    def realPrice(self, consumePrice):
        if consumePrice >= 100 and consumePrice < 200:
            consumePrice -= 40
        elif consumePrice >= 200 and consumePrice <300:
            consumePrice -= 90
        elif consumePrice >= 300:
            consumePrice -= 150
        return consumePrice

    def strategyName(self):
        return "ReduceStrategy"

class Context:
    def __init__(self, strategy = None):
        self.strategy = strategy

    def setStrategy(self, strategy):
        self.strategy = strategy

    def cul(self, consumePrice):
        realPrice = self.strategy.realPrice(consumePrice)
        print(('打折策略：{}\n打折前：{}\n打折后：{}').format(self.strategy.strategyName(self), consumePrice, realPrice))

class Client:
    def __init__(self, name = None, price = None):
        self.name = name
        self.price = price
        
    def setname(self, name):
        self.name = name

    def setprice(self, price):
        self.price = price
    
    def printResult(self):
        print(('用户名:{}').format(self.name))
        self.context = Context()
        self.context.setStrategy(RebateStrategy)
        self.context.cul(self.price)
        self.context.setStrategy(PromotionalStrategy)
        self.context.cul(self.price)
        self.context.setStrategy(ReduceStrategy)
        self.context.cul(self.price)
        
client = Client()
client.setname('Tom')
client.setprice(200)
client.printResult()


# In[ ]:




