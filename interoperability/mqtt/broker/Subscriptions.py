# Subscriptions model - produced from XML source

import time, logging
 
class Subscriptions:

  def __init__(self, aClientid, aTopic):
    self.__clientid = aClientid
    self.__topic = aTopic
    self.__timestamp = time.clock()

  def getClientid(self):
    return self.__clientid

  def getTopic(self):
    return self.__topic

  def resubscribe(self):
    logging.info("[MQTT-1.1.0-1] resubscription for client %s on topic %s", self.__clientid, self.__topic)
    self.__timestamp = time.clock()

  def getTimestamp(self):
    return self.__timestamp

  def __repr__(self):
    return repr((self.__clientid, self.__topic, self.__timestamp))
 
