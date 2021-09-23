# These methods allow access to various CPU key performance indicators
import psutil as cpu
# Displays only
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


#Converts seconds to hours,minutes and seconds
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

#Print runtime for all CPU threads based on category
def printCPURuntime():
	cpuTime = cpu.cpu_times()
	#print(cpuTime)
	tags = ['User Runtime','System Runtime', 'Idle Runtime','Interrupt Runtime','DPC Runtime']
	for i,j in enumerate(tags):
		print(j + ': ' + convert(cpuTime[i]))
#printCPURuntime()

#Get current CPU load
def getCPULoad():
	print(cpu.cpu_percent(interval =1))
	return cpu.cpu_percent(interval = 1)

#Get number of threads and cores
def getCPUCount():
	print('Number of Logical Cores (threads): ' + str(cpu.cpu_count()))
	print('Number of True Cores: ' + str(cpu.cpu_count(logical = False)))
	return cpu.cpu_count()

#Get current CPU clockrate
def getCPUClock():
	print(cpu.cpu_freq())
	return str(cpu.cpu_freq()[0]/1000) + "GHz"


getCPULoad()
print(getCPUCount())
print(getCPUClock())