
#https://www.isc.upenn.edu/how-to/configuring-your-web-browser-allow-pop-windows#:~:text=Click%20the%20ellipsis%20icon%20(..,Pop%2Dups%20are%20now%20allowed.

from datetime import datetime
import pywhatkit
now = datetime.now()
hour=now.hour
minute=now.minute
second=now.second
minute=minute+1
pywhatkit.sendwhatmsg('+9050XXXXXXXX', 'Type your message here', hour, minute, second, True, 65)
#In 30 Seconds WhatsApp will open and after 15 Seconds Message will be Delivered!
