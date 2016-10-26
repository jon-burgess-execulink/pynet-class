import snmp_helper

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
routers = ( '184.105.247.70', '184.105.247.71')
oids = ('1.3.6.1.2.1.1.5.0','1.3.6.1.2.1.1.1.0',)

for i in routers:
    print "\n" + i + " queries:"
    for j in oids:
        query = (i, COMMUNITY_STRING, SNMP_PORT)
        data = snmp_helper.snmp_get_oid(query,j)
        output = snmp_helper.snmp_extract(data)
        print output + "\n"
    print "\n"
