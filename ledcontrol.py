class LedControl:
  def __init__(self,pins,gpio):
    self.leds = list()
    for x in pins:
      self.leds.append(Led(gpio,x['pin'],x['name']))
  def getNames(self):
    ret = list()
    for x in self.leds:
      ret.append(x.name)
    return ret

class Led:
  def __init__(self,gpio,pin,name):
    self.__gpio = gpio
    self.__state = self.__gpio.LOW
    self.pin = pin
    self.name = name
    self.__gpio.digitalWrite(pin,self.__state)
  def setState(self,state):
    if(state != 0 or state != 1):
      raise ValueError
    self.__state = self.__gpio.HIGH if state == 1 else self.__gpio.LOW
    self.__gpio.digitalWrite(self.pin,self.__state)
  def getState(self):
    return self.__state
  def toggleState(self):
    self.__state = self.__gpio.HIGH if self.__state ==self.__gpio.LOW else self.__gpio.LOW
    self.__gpio.digitalWrite(self.pin,self.__state)

class wiringx86_dummy:
  HIGH = 1
  LOW = 0
  INPUT = 1
  OUTPUT = 0
  __pins = dict()
  __states = dict()
  def pinMode(self,pin,mode):
    self.__checkEntry(pin)
    self.__pins[pin] = mode
  def digitalRead(self,pin):
    self.__checkEntry(pin)
    return self.__states[pin]
  def digitalWrite(self,pin,state):
    self.__states[pin] = state
  def __checkEntry(self,pin):
    if not pin in self.__states:
      self.__states[pin] = 0
