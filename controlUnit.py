from cache import Cache

class ControlUnit():
  def __init__(self) -> None:
    self.cache = Cache()

  def execute(self, command: str):
    elements = command.split(',')
    instruction = elements[0]
    operands = elements[1:]

    if instruction.isnumeric():
      self.saveToCache(instruction, int(operands[0]))
    elif instruction == 'ADD':
      self.add(int(operands[0]), int(operands[1]), int(operands[2]))
    elif instruction == 'ADDI':
      self.addi(int(operands[0]), int(operands[1]), int(operands[2]))
    elif instruction == 'SUB':
      self.sub(int(operands[0]), int(operands[1]), int(operands[2]))

  def saveToCache(self, value: int, target: int):
    self.cache.write(target, value)

  def add(self, reg1: int, reg2: int, reg3: int):
    value1 = int(self.cache.read(reg2))
    value2 = int(self.cache.read(reg3))
    res = value1 + value2
    self.cache.write(reg1, res)
    print('ADD', reg1, ",", reg2, ':', value1, ",", reg3, ':', value2, '=', res, sep = "")

  def addi(self, reg1, reg2, immd):
    value1 = self.cache.read(reg2)
    res = value1 + immd
    self.cache.write(reg1, res)
    print('ADDI', reg1, ",", reg2, ':', value1, ',immd:', immd, '=', res, sep = "")

  
  def sub(self, reg1: int, reg2: int, reg3: int):
    value1 = int(self.cache.read(reg2))
    value2 = int(self.cache.read(reg3))
    res = value1 - value2
    self.cache.write(reg1, res)
    print('SUB', reg1, ",", reg2, ':', value1, ",", reg3, ':', value2, '=', res, sep = "")


