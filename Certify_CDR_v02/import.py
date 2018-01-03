import os
import datetime
import csv
from app import db, models


def main():
    fileList = os.path.join(os.getcwd(), 'inserts')
    for fileName in os.listdir(fileList):
        with open(fileList + "\\" + fileName, 'rt', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            rows = list(reader)
            f.close()
            os.remove(fileList + "\\" + fileName)

            for row in rows:
                if row[0][0] == "0" or row[0][0] == "1":
                    row[4] = datetime.datetime.utcfromtimestamp(  # Timestamp Convert
                        int(row[4])).strftime('%Y-%m-%d %H:%M:%S')

                    list_of_dec = [int(row[7]),
                                   int(row[13]),
                                   int(row[21]),
                                   int(row[28]),
                                   int(row[35]),
                                   int(row[43])]

                    x_list = [convert_ips(dec) for dec in list_of_dec]

                    [row[7],
                     row[13],
                     row[21],
                     row[28],
                     row[35],
                     row[43]] = x_list

                    rowInsert = models.CDR(
                        cdrRecordType=row[0],
                        globalCallID_callManagerId=row[1],
                        globalCallID_callId=row[2],
                        origLegCallIdentifier=row[3],
                        dateTimeOrigination=row[4],
                        origNodeId=row[5],
                        origSpan=row[6],
                        origIpAddr=row[7],
                        callingPartyNumber=row[8],
                        callingPartyUnicodeLoginUserID=row[9],
                        origCause_location=row[10],
                        origCause_value=row[11],
                        origPrecedenceLevel=row[12],
                        origMediaTransportAddress_IP=row[13],
                        origMediaTransportAddress_Port=row[14],
                        origMediaCap_payloadCapability=row[15],
                        origMediaCap_maxFramesPerPacket=row[16],
                        origMediaCap_g723BitRate=row[17],
                        origVideoCap_Codec=row[18],
                        origVideoCap_Bandwidth=row[19],
                        origVideoCap_Resolution=row[20],
                        origVideoTransportAddress_IP=row[21],
                        origVideoTransportAddress_Port=row[22],
                        origRSVPAudioStat=row[23],
                        origRSVPVideoStat=row[24],
                        destLegIdentifier=row[25],
                        destNodeId=row[26],
                        destSpan=row[27],
                        destIpAddr=row[28],
                        originalCalledPartyNumber=row[29],
                        finalCalledPartyNumber=row[30],
                        finalCalledPartyUnicodeLoginUserID=row[31],
                        destCause_location=row[32],
                        destCause_value=row[33],
                        destPrecedenceLevel=row[34],
                        destMediaTransportAddress_IP=row[35],
                        destMediaTransportAddress_Port=row[36],
                        destMediaCap_payloadCapability=row[37],
                        destMediaCap_maxFramesPerPacket=row[38],
                        destMediaCap_g723BitRate=row[39],
                        destVideoCap_Codec=row[40],
                        destVideoCap_Bandwidth=row[41],
                        destVideoCap_Resolution=row[42],
                        destVideoTransportAddress_IP=row[43],
                        destVideoTransportAddress_Port=row[44],
                        destRSVPAudioStat=row[45],
                        destRSVPVideoStat=row[46],
                        dateTimeConnect=row[47],
                        dateTimeDisconnect=row[48],
                        lastRedirectDn=row[49],
                        pkid=row[50],
                        originalCalledPartyNumberPartition=row[1],
                        callingPartyNumberPartition=row[1],
                        finalCalledPartyNumberPartition=row[1],
                        lastRedirectDnPartition=row[1],
                        duration=row[1],
                        origDeviceName=row[1],
                        destDeviceName=row[1],
                        origCallTerminationOnBehalfOf=row[1],
                        destCallTerminationOnBehalfOf=row[1],
                        origCalledPartyRedirectOnBehalfOf=row[1],
                        lastRedirectRedirectOnBehalfOf=row[1],
                        origCalledPartyRedirectReason=row[1],
                        lastRedirectRedirectReason=row[1],
                        destConversationId=row[1],
                        globalCallId_ClusterID=row[1],
                        joinOnBehalfOf=row[1],
                        comment=row[1],
                        authCodeDescription=row[1],
                        authorizationLevel=row[1],
                        clientMatterCode=row[1],
                        origDTMFMethod=row[1],
                        destDTMFMethod=row[1],
                        callSecuredStatus=row[1],
                        origConversationId=row[1],
                        origMediaCap_Bandwidth=row[1],
                        destMediaCap_Bandwidth=row[1],
                        authorizationCodeValue=row[1],
                        outpulsedCallingPartyNumber=row[1],
                        outpulsedCalledPartyNumber=row[1],
                        origIpv4v6Addr=row[1],
                        destIpv4v6Addr=row[1],
                        origVideoCap_Codec_Channel2=row[1],
                        origVideoCap_Bandwidth_Channel2=row[1],
                        origVideoCap_Resolution_Channel2=row[1],
                        origVideoTransportAddress_IP_Channel2=row[1],
                        origVideoTransportAddress_Port_Channel2=row[1],
                        origVideoChannel_Role_Channel2=row[1],
                        destVideoCap_Codec_Channel2=row[1],
                        destVideoCap_Bandwidth_Channel2=row[1],
                        destVideoCap_Resolution_Channel2=row[1],
                        destVideoTransportAddress_IP_Channel2=row[1],
                        destVideoTransportAddress_Port_Channel2=row[1],
                        destVideoChannel_Role_Channel2=row[1],
                        IncomingProtocolID=row[1],
                        IncomingProtocolCallRef=row[1],
                        OutgoingProtocolID=row[1],
                        OutgoingProtocolCallRef=row[1],
                        currentRoutingReason=row[1],
                        origRoutingReason=row[1],
                        lastRedirectingRoutingReason=row[1],
                        huntPilotPartition=row[1],
                        huntPilotDN=row[1],
                        calledPartyPatternUsage=row[1],
                        IncomingICID=row[1],
                        IncomingOrigIOI=row[1],
                        IncomingTermIOI=row[1],
                        OutgoingICID=row[1],
                        OutgoingOrigIOI=row[1],
                        OutgoingTermIOI=row[1],
                        outpulsedOriginalCalledPartyNumber=row[1],
                        outpulsedLastRedirectingNumber=row[1],
                        wasCallQueued=row[1],
                        totalWaitTimeInQueue=row[1],
                        callingPartyNumber_uri=row[1],
                        originalCalledPartyNumber_uri=row[1],
                        finalCalledPartyNumber_uri=row[1],
                        lastRedirectDn_uri=row[1],
                        mobileCallingPartyNumber=row[1],
                        finalMobileCalledPartyNumber=row[1],
                        origMobileDeviceName=row[1],
                        destMobileDeviceName=row[1],
                        origMobileCallDuration=row[1],
                        destMobileCallDuration=row[1],
                        mobileCallType=row[1],
                        originalCalledPartyPattern=row[1],
                        finalCalledPartyPattern=row[1],
                        lastRedirectingPartyPattern=row[1],
                        huntPilotPattern=row[1]
                    )
                    print(row)
                    db.session.add(rowInsert)


                elif row[0][0] == "2":
                    row[6] = datetime.datetime.utcfromtimestamp(
                        int(row[6])).strftime('%Y-%m-%d %H:%M:%S')

                    rowInsert = models.CMR(
                        cdrRecordType=row[0],
                        globalCallID_callManagerId=row[1],
                        globalCallID_callId=row[2],
                        nodeId=row[3],
                        directoryNum=row[4],
                        callIdentifier=row[5],
                        dateTimeStamp=row[6],
                        numberPacketsSent=row[7],
                        numberOctetsSent=row[8],
                        numberPacketsReceived=row[9],
                        numberOctetsReceived=row[10],
                        numberPacketsLost=row[11],
                        jitter=row[12],
                        latency=row[13],
                        pkid=row[14],
                        directoryNumPartition=row[15],
                        globalCallId_ClusterID=row[16],
                        deviceName=row[17],
                        varVQMetrics=row[18],
                        duration=row[19],
                        videoContentType=row[20],
                        videoDuration=row[21],
                        numberVideoPacketsSent=row[22],
                        numberVideoOctetsSent=row[23],
                        numberVideoPacketsReceived=row[24],
                        numberVideoOctetsReceived=row[25],
                        numberVideoPacketsLost=row[26],
                        videoAverageJitter=row[27],
                        videoRoundTripTime=row[28],
                        videoOneWayDelay=row[29],
                        videoReceptionMetrics=row[30],
                        videoTransmissionMetrics=row[31],
                        videoContentType_channel2=row[32],
                        videoDuration_channel2=row[33],
                        numberVideoPacketsSent_channel2=row[34],
                        numberVideoOctetsSent_channel2=row[35],
                        numberVideoPacketsReceived_channel2=row[36],
                        numberVideoOctetsReceived_channel2=row[37],
                        numberVideoPacketsLost_channel2=row[38],
                        videoAverageJitter_channel2=row[39],
                        videoRoundTripTime_channel2=row[40],
                        videoOneWayDelay_channel2=row[41],
                        videoReceptionMetrics_channel2=row[42],
                        videoTransmissionMetrics_channel2=row[43],
                    )
                    db.session.add(rowInsert)

    db.session.commit()

def convert_ips(signed32BitInt):
    if signed32BitInt == 0:
        return "0"
    hexValue = hex(signed32BitInt & (2**32-1))[2:10]
    if len(hexValue) == 7:
        hexValue = '0' + hexValue
    elif len(hexValue) == 6:
        hexValue = '00' + hexValue
    elif len(hexValue) == 5:
        hexValue = '000' + hexValue
    hexSwap = [hexValue[6:8], hexValue[4:6], hexValue[2:4], hexValue[0:2]]
    return '.'.join([str(int(n,16)) for n in hexSwap])

main()