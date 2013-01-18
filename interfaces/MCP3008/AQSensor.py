import MCP3008

class AQSensor:
	adc = None
	adcPin = 0
	
	def __init__(self, adc, adcNumber):
		self.adc = adc
		self.adcPin = adcNumber
	
	def get_quality(self):
		result = self.adc.readADC(self.adcPin) + 1
		vout = float(result)/1023 * 3.3
		rs = ((5.0 - vout) / vout)
		return rs
