
DD=docker
ST=start
SP=stop
PL=pull

INIMG=-i jolly-clarke

TCIMG=teamcity-server-instance
MDBIMG=mongo
SWIMG=reverent_murdock

IN:
	${DD} ${ST} ${INIMG}

TC:
	${DD} ${ST} ${TCIMG}

TCSP:
	${DD} ${SP} ${TCIMG}

MDB:
	${DD} ${ST} ${MDBIMG}

MDBSP:
	${DD} ${SP} ${MDBIMG}

SW:
	${DD} ${ST} ${SWIMG}

SWSP:
	${DD} ${SP} ${SWIMG}


