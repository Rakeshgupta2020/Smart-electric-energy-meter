import alexa_conf
import json,time,requests
from boltiot import Bolt, Sms
mybolt=Bolt(alexa_conf.API_KEY,alexa_conf.DEVICE_ID)
sms=Sms(alexa_conf.SID,alexa_conf.AUTH_TOKEN,alexa_conf.TO_NUMBER,alexa_conf.FROM_NUMBER)
R1=30000
R2=7500
while True:
  print ("Reading voltage sensor value")
  response = mybolt.analogRead('A0')
  data = json.loads(response)
  data_val=int(data['value'])
  try:
   print ("Sensor value is: ",data_val)
   adc_voltage=float(data_val)*(1/1024.0)
   print(adc_voltage)
   voltage=adc_voltage/(R2/(R1+R2))
   print(voltage)
   print("Voltage value in Volts is {:.4f}".format(voltage))
   I=0.00454
   pwr=voltage*I
   print("power consumed by LED in Watts is {:.4f}".format(pwr))
   if (voltage >0.05):
    sms.send_sms("Someone switched ON the device: and power consumed was:{:.4f}".format(pwr))
   else:
    sms.send_sms("Someone switched OFF the device: and power consumed was:{:.4f}".format(pwr))

  except Exception as e:
    print ("Error occured: Below are the details")
    print (e)
time.sleep(30)
