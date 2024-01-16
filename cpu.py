from controlUnit import ControlUnit

cpu = ControlUnit()
cpu.execute('9,2')
cpu.execute('2,3')
cpu.execute('7,4')
cpu.execute('6,5')
cpu.execute('5,6')
cpu.execute('4,7')
cpu.execute('3,9')
cpu.execute('ADD,8,2,3')
cpu.execute('ADDI,10,8,78')
cpu.execute('SUB,13,6,7')