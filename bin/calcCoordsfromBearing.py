import math, sys, csv, logging
import splunk.Intersplunk

logger = logging.getLogger("calcCoordsfromBearing")
logger.setLevel(logging.DEBUG)


def main():
	lat1 = float(sys.argv[1]) #51.13276
	lon1 = float(sys.argv[2]) #0.0
	bearing = float(sys.argv[3]) #45
	distance = float(sys.argv[4]) #1.5

	bearingRad = math.cos(math.radians(bearing))
	R = 6378.1 #Radius of the Earth

	outfile = sys.stdout

	fieldnames = ['lat','lon','bearing','distance','lat2','lon2']
	w = csv.DictWriter(outfile, fieldnames=fieldnames)

	lat1r = math.radians(lat1) #Current lat point converted to radians
	lon1r = math.radians(lon1) #Current long point converted to radians

	lat2 = math.asin( math.sin(lat1r)*math.cos(distance/R) +
		math.cos(lat1r)*math.sin(distance/R)*math.cos(bearingRad))

	lon2 = lon1r + math.atan2(math.sin(bearingRad)*math.sin(distance/R)*math.cos(lat1r),
        	math.cos(distance/R)-math.sin(lat1r)*math.sin(lat2))

	lat2 = math.degrees(lat2)
	lon2 = math.degrees(lon2)

	w.writerow({'lat':'lat','lon':'lon','bearing':'bearing','distance':'distance','lat2':'lat2','lon2':'lon2'})	
	w.writerow({'lat':str(lat1),'lon':str(lon1),'bearing':str(bearing),'distance':str(distance),'lat2':str(lat2),'lon2':str(lon2)})

try:
     main()
except Exception, e:
     # Catch any exception, log it and also return a simplified version back to splunk (should be displayed in red at the top of the page)
     logger.exception("Unhanded top-level exception")
     splunk.Intersplunk.generateErrorResults("Exception! %s (See python.log)" % (e,))

