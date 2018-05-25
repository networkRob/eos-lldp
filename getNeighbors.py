#!/usr/bin/python

from jsonrpclib import Server
import argparse

#credentials to login to device
eUser = 'arista'
ePwd = 'arista'

def cSwitch(hIP):
        return(Server('https://{0}:{1}@{2}/command-api'.format(eUser,ePwd,hIP)))


def runCMDS(hIP,*rcmd):
        return(cSwitch(hIP).runCmds(1,rcmd))


def tEnable(hIP):
        try:
            	runCMDS(hIP,'enable')
                return(1)
        except Exception as e:
                print("Unable to run 'enable' on switch", e)
                return(0)


def getIntD(hIP,sINT):
        eint = runCMDS(hIP,'show interfaces {0}'.format(sINT))[0]['interfaces']
        ekey = eint.keys()[0]
        return(eint[ekey]['description'])


def getLLDPN(hIP):
        return(runCMDS(hIP,'show lldp neighbors')[0]['lldpNeighbors'])


def updateDesc(hIP,sINT,nDes):
        runCMDS(hIP,'enable','configure','interface {0}'.format(sINT),'description {0}'.format(nDes))


#Code starts
def upDLLDP(hIP):
        for r1 in getLLDPN(hIP):
                cint = r1['port']
                cintN = r1['neighborDevice']
                cintNP = r1['neighborPort']
                cDes = getIntD(hIP,cint)
                pDes = '{0} - {1}'.format(cintN,cintNP)
                if cDes != pDes:
                        print('Previous {0}: {1}'.format(cint,getIntD(hIP,cint)))
                        updateDesc(hIP,cint,'{0} - {1}'.format(cintN,cintNP))
                        print('New {0}: {1}'.format(cint,getIntD(hIP,cint)))
                else:
                     	print('{0} no change'.format(cint))


def main():
	parser = argparse.ArgumentParser(description="Edit Arista Interface Descriptions with LLDP Neighbor Information")
        parser.add_argument("--host",help="IP address of the target switch")
        args = parser.parse_args()
        if args.host == None:
                args.host = '127.0.0.1'
	if tEnable(args.host) == 1:
        	upDLLDP(args.host)


if __name__ == '__main__':
        main()