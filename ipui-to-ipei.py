#ipui = '019B90BB43' #debug
ipui = input('Please enter IPUI: ')

if (len(ipui) == 10):
	emcHex = ipui[:5]
	psnHex = ipui[-5:]
	print('EMC: %s | PSN: %s (hex)' % (emcHex, psnHex))
	
	emc = str(int(emcHex, 16)).zfill(5)
	psn = str(int(psnHex, 16)).zfill(7)
	print('EMC: %s | PSN: %s (dec)' % (emc, psn))
	
	m = 1 #multiplier
	chksum = 0
	emcpsn = emc + psn
	
	for c in emcpsn:
		chksum += int(c)*m
		m += 1
		print('%s*%s' % (c,m))
	chkdgt = chksum % 11
	print('IPEI: %s %s %s' % (emc,psn,chkdgt))