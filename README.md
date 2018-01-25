# ipui-to-ipei
IPUI to IPEI converter for Siemens Gigaset dect phones

**Example:**</br>
IPUI = 0 19B9 0BB43 hex</br>
IPEI = 19B9 0BB43 hex</br>
</br>
EMC = 06585 (0 + 19B9 in dec)</br>
PSN = 0047939 (0 + 0BB43 in dec)</br>
</br>
06585 0047939</br>
</br>
Checksum = 0\*1+6\*2+5\*3+8\*4+5\*5+0\*6+0\*7+4\*8+7\*9+9\*10+3\*11+9\*12 => 410</br>
Check digit = 3 (410 mod 11)</br>
</br>
IPEI = EMC + PSN + CHECKSUM_RESULT</br>
IPEI = 06585 0047939 3
