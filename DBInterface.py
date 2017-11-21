import os
import sqlite3
import csv

"""
DBInterface.py
Author: A.Nihiser, apnihiser@gmail.com, Github: https://github.com/merkkie/CUCMCDR

Purpose: Interface that connects a folder that is always being fed CDR, CMR data from CUCM.
I am running from an IIS server that will run this script to run at the top of every
hour via scheduled tasks. This ia place hold doc until I can figure out the web
front end that will serve as the GUI for this project. There we can pick times and dates
well as calling and called numbers.

Issues: I would like to point out that CUCM spits out CDR and CMR information in 129 or 44
columns at a time. This is why these sql creation and insertion commands are so massive. I'll
continue to research on what I can do about this. I have tried other methods to accomplish this
but due to sql inject and my nubbyness things have not worked according to plan. For now I'll
continue to tinker around to get a product up that can actually pull information from the web
GUI and display a file for downloading. Until then this will all be a bit of mess!! My
apologies.
"""

def main():

    conn = sqlite3.connect('car.db')

    c = conn.cursor()

    create_table_cdr(c)
    create_table_cmr(c)

    path = 'C:\dev\CUCM\IVC_CDR\CDR_Working_DIR'

    dirs = os.listdir( path )

    for files in dirs:

        path = "C:\dev\CUCM\IVC_CDR\CDR_Working_DIR\{}".format(files)

        with open(path, 'rt', newline='') as f:

            reader = csv.reader(f, delimiter=',')

            rows = list(reader)

            for row in rows:

                if row[0][0] == "0" or row[0][0] == "1":
                    data_entry_cdr(c, row)
                elif row[0][0] == "2":
                    data_entry_cmr(c, row)

    c.close()

    conn.commit()

    conn.close()


def create_table_cmr(c):
    c.execute("""CREATE TABLE IF NOT EXISTS cmrtable (
                    cdrRecordType INTEGER,
                    globalCallID_callManagerId INTEGER,
                    globalCallID_callId INTEGER,
                    nodeId INTEGER,
                    directoryNum VARCHAR(50),
                    callIdentifier INTEGER,
                    dateTimeStamp INTEGER,
                    numberPacketsSent INTEGER,
                    numberOctetsSent INTEGER,
                    numberPacketsReceived INTEGER,
                    numberOctetsReceived INTEGER,
                    numberPacketsLost INTEGER,
                    jitter INTEGER,
                    latency INTEGER,
                    pkid TEXT PRIMARY KEY,
                    directoryNumPartition VARCHAR(50),
                    globalCallId_ClusterID VARCHAR(50),
                    deviceName VARCHAR(129),
                    varVQMetrics VARCHAR(600),
                    duration INTEGER,
                    videoContentType VARCHAR(10),
                    videoDuration INTEGER,
                    numberVideoPacketsSent INTEGER,
                    numberVideoOctetsSent INTEGER,
                    numberVideoPacketsReceived INTEGER,
                    numberVideoOctetsReceived INTEGER,
                    numberVideoPacketsLost INTEGER,
                    videoAverageJitter INTEGER,
                    videoRoundTripTime INTEGER,
                    videoOneWayDelay INTEGER,
                    videoReceptionMetrics VARCHAR(600),
                    videoTransmissionMetrics VARCHAR(600),
                    videoContentType_channel2 VARCHAR(10),
                    videoDuration_channel2 INTEGER,
                    numberVideoPacketsSent_channel2 INTEGER,
                    numberVideoOctetsSent_channel2 INTEGER,
                    numberVideoPacketsReceived_channel2 INTEGER,
                    numberVideoOctetsReceived_channel2 INTEGER,
                    numberVideoPacketsLost_channel2 INTEGER,
                    videoAverageJitter_channel2 INTEGER,
                    videoRoundTripTime_channel2 INTEGER,
                    videoOneWayDelay_channel2 INTEGER,
                    videoReceptionMetrics_channel2 VARCHAR(600),
                    videoTransmissionMetrics_channel2 VARCHAR(600)
                    )""")


def data_entry_cmr(c, cmr_data_row):
    c.execute("""INSERT INTO cmrtable (
                    cdrRecordType,
                    globalCallID_callManagerId,
                    globalCallID_callId,
                    nodeId,
                    directoryNum,
                    callIdentifier, 
                    dateTimeStamp, 
                    numberPacketsSent, 
                    numberOctetsSent, 
                    numberPacketsReceived, 
                    numberOctetsReceived, 
                    numberPacketsLost,
                    jitter,
                    latency, 
                    pkid,
                    directoryNumPartition,
                    globalCallId_ClusterID, 
                    deviceName, 
                    varVQMetrics, 
                    duration, 
                    videoContentType, 
                    videoDuration, 
                    numberVideoPacketsSent, 
                    numberVideoOctetsSent, 
                    numberVideoPacketsReceived, 
                    numberVideoOctetsReceived, 
                    numberVideoPacketsLost, 
                    videoAverageJitter, 
                    videoRoundTripTime, 
                    videoOneWayDelay, 
                    videoReceptionMetrics, 
                    videoTransmissionMetrics, 
                    videoContentType_channel2, 
                    videoDuration_channel2, 
                    numberVideoPacketsSent_channel2, 
                    numberVideoOctetsSent_channel2, 
                    numberVideoPacketsReceived_channel2, 
                    numberVideoOctetsReceived_channel2, 
                    numberVideoPacketsLost_channel2, 
                    videoAverageJitter_channel2, 
                    videoRoundTripTime_channel2, 
                    videoOneWayDelay_channel2, 
                    videoReceptionMetrics_channel2, 
                    videoTransmissionMetrics_channel2 
                    ) VALUES (
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?
                    )""", (cmr_data_row))


def create_table_cdr(c):
    c.execute("""CREATE TABLE IF NOT EXISTS cdrtable (
                    cdrRecordType INTEGER,
                    globalCallID_callManagerId INTEGER,
                    globalCallID_callId INTEGER,
                    origLegCallIdentifier INTEGER,
                    dateTimeOrigination INTEGER,
                    origNodeId INTEGER,
                    origSpan INTEGER,
                    origIpAddr INTEGER,
                    callingPartyNumber VARCHAR(50),
                    callingPartyUnicodeLoginUserID VARCHAR(128),
                    origCause_location INTEGER,
                    origCause_value INTEGER,
                    origPrecedenceLevel INTEGER,
                    origMediaTransportAddress_IP INTEGER,
                    origMediaTransportAddress_Port INTEGER,
                    origMediaCap_payloadCapability INTEGER,
                    origMediaCap_maxFramesPerPacket INTEGER,
                    origMediaCap_g723BitRate INTEGER,
                    origVideoCap_Codec INTEGER,
                    origVideoCap_Bandwidth INTEGER,
                    origVideoCap_Resolution INTEGER,
                    origVideoTransportAddress_IP INTEGER,
                    origVideoTransportAddress_Port INTEGER,
                    origRSVPAudioStat VARCHAR(64),
                    origRSVPVideoStat VARCHAR(64),
                    destLegIdentifier INTEGER,
                    destNodeId INTEGER,
                    destSpan INTEGER,
                    destIpAddr INTEGER,
                    originalCalledPartyNumber VARCHAR(50),
                    finalCalledPartyNumber VARCHAR(50),
                    finalCalledPartyUnicodeLoginUserID VARCHAR(128),
                    destCause_location INTEGER,
                    destCause_value INTEGER,
                    destPrecedenceLevel INTEGER,
                    destMediaTransportAddress_IP INTEGER,
                    destMediaTransportAddress_Port INTEGER,
                    destMediaCap_payloadCapability INTEGER,
                    destMediaCap_maxFramesPerPacket INTEGER,
                    destMediaCap_g723BitRate INTEGER,
                    destVideoCap_Codec INTEGER,
                    destVideoCap_Bandwidth INTEGER,
                    destVideoCap_Resolution INTEGER,
                    destVideoTransportAddress_IP INTEGER,
                    destVideoTransportAddress_Port INTEGER,
                    destRSVPAudioStat VARCHAR(64),
                    destRSVPVideoStat VARCHAR(64),
                    dateTimeConnect INTEGER,
                    dateTimeDisconnect INTEGER,
                    lastRedirectDn VARCHAR(50),
                    pkid TEXT PRIMARY KEY,
                    originalCalledPartyNumberPartition VARCHAR(50),
                    callingPartyNumberPartition VARCHAR(50),
                    finalCalledPartyNumberPartition VARCHAR(50),
                    lastRedirectDnPartition VARCHAR(50),
                    duration INTEGER,origDeviceName VARCHAR(129),
                    destDeviceName VARCHAR(129),
                    origCallTerminationOnBehalfOf INTEGER,
                    destCallTerminationOnBehalfOf INTEGER,
                    origCalledPartyRedirectOnBehalfOf INTEGER,
                    lastRedirectRedirectOnBehalfOf INTEGER,
                    origCalledPartyRedirectReason INTEGER,
                    lastRedirectRedirectReason INTEGER,
                    destConversationId INTEGER,
                    globalCallId_ClusterID VARCHAR(50),
                    joinOnBehalfOf INTEGER,
                    comment VARCHAR(2048),
                    authCodeDescription VARCHAR(50),
                    authorizationLevel INTEGER,
                    clientMatterCode VARCHAR(32),
                    origDTMFMethod INTEGER,
                    destDTMFMethod INTEGER,
                    callSecuredStatus INTEGER,
                    origConversationId INTEGER,
                    origMediaCap_Bandwidth INTEGER,
                    destMediaCap_Bandwidth INTEGER,
                    authorizationCodeValue VARCHAR(32),
                    outpulsedCallingPartyNumber VARCHAR(50),
                    outpulsedCalledPartyNumber VARCHAR(50),
                    origIpv4v6Addr VARCHAR(64),
                    destIpv4v6Addr VARCHAR(64),
                    origVideoCap_Codec_Channel2 INTEGER,
                    origVideoCap_Bandwidth_Channel2 INTEGER,
                    origVideoCap_Resolution_Channel2 INTEGER,
                    origVideoTransportAddress_IP_Channel2 INTEGER,
                    origVideoTransportAddress_Port_Channel2 INTEGER,
                    origVideoChannel_Role_Channel2 INTEGER,
                    destVideoCap_Codec_Channel2 INTEGER,
                    destVideoCap_Bandwidth_Channel2 INTEGER,
                    destVideoCap_Resolution_Channel2 INTEGER,
                    destVideoTransportAddress_IP_Channel2 INTEGER,
                    destVideoTransportAddress_Port_Channel2 INTEGER,
                    destVideoChannel_Role_Channel2 INTEGER,
                    IncomingProtocolID INTEGER,
                    IncomingProtocolCallRef VARCHAR(32),
                    OutgoingProtocolID INTEGER,
                    OutgoingProtocolCallRef VARCHAR(32),
                    currentRoutingReason INTEGER,
                    origRoutingReason INTEGER,
                    lastRedirectingRoutingReason INTEGER,
                    huntPilotPartition VARCHAR(50),
                    huntPilotDN VARCHAR(50),
                    calledPartyPatternUsage INTEGER,
                    IncomingICID VARCHAR(50),
                    IncomingOrigIOI VARCHAR(50),
                    IncomingTermIOI VARCHAR(50),
                    OutgoingICID VARCHAR(50),
                    OutgoingOrigIOI VARCHAR(50),
                    OutgoingTermIOI VARCHAR(50),
                    outpulsedOriginalCalledPartyNumber VARCHAR(50),
                    outpulsedLastRedirectingNumber VARCHAR(50),
                    wasCallQueued INTEGER,
                    totalWaitTimeInQueue INTEGER,
                    callingPartyNumber_uri VARCHAR(255),
                    originalCalledPartyNumber_uri VARCHAR(255),
                    finalCalledPartyNumber_uri VARCHAR(255),
                    lastRedirectDn_uri VARCHAR(255),
                    mobileCallingPartyNumber VARCHAR(50),
                    finalMobileCalledPartyNumber VARCHAR(50),
                    origMobileDeviceName VARCHAR(129),
                    destMobileDeviceName VARCHAR(129),
                    origMobileCallDuration INTEGER,
                    destMobileCallDuration INTEGER,
                    mobileCallType INTEGER,
                    originalCalledPartyPattern VARCHAR(50),
                    finalCalledPartyPattern VARCHAR(50),
                    lastRedirectingPartyPattern VARCHAR(50),
                    huntPilotPattern VARCHAR(50)
                    )""")


def data_entry_cdr(c, cdr_data_row):
    c.execute("""INSERT INTO cdrtable (
                    cdrRecordType,
                    globalCallID_callManagerId,
                    globalCallID_callId,
                    origLegCallIdentifier,
                    dateTimeOrigination,
                    origNodeId,
                    origSpan,
                    origIpAddr,
                    callingPartyNumber,
                    callingPartyUnicodeLoginUserID,
                    origCause_location,
                    origCause_value,
                    origPrecedenceLevel,
                    origMediaTransportAddress_IP,
                    origMediaTransportAddress_Port,
                    origMediaCap_payloadCapability,
                    origMediaCap_maxFramesPerPacket,
                    origMediaCap_g723BitRate,
                    origVideoCap_Codec,
                    origVideoCap_Bandwidth,
                    origVideoCap_Resolution,
                    origVideoTransportAddress_IP,
                    origVideoTransportAddress_Port,
                    origRSVPAudioStat,
                    origRSVPVideoStat,
                    destLegIdentifier,
                    destNodeId,
                    destSpan,
                    destIpAddr,
                    originalCalledPartyNumber,
                    finalCalledPartyNumber,
                    finalCalledPartyUnicodeLoginUserID,
                    destCause_location,
                    destCause_value,
                    destPrecedenceLevel,
                    destMediaTransportAddress_IP,
                    destMediaTransportAddress_Port,
                    destMediaCap_payloadCapability,
                    destMediaCap_maxFramesPerPacket,
                    destMediaCap_g723BitRate,
                    destVideoCap_Codec,
                    destVideoCap_Bandwidth,
                    destVideoCap_Resolution,
                    destVideoTransportAddress_IP,
                    destVideoTransportAddress_Port,
                    destRSVPAudioStat,
                    destRSVPVideoStat,
                    dateTimeConnect,
                    dateTimeDisconnect,
                    lastRedirectDn,
                    pkid,
                    originalCalledPartyNumberPartition,
                    callingPartyNumberPartition,
                    finalCalledPartyNumberPartition,
                    lastRedirectDnPartition,
                    duration,
                    origDeviceName,
                    destDeviceName,
                    origCallTerminationOnBehalfOf,
                    destCallTerminationOnBehalfOf,
                    origCalledPartyRedirectOnBehalfOf,
                    lastRedirectRedirectOnBehalfOf,
                    origCalledPartyRedirectReason,
                    lastRedirectRedirectReason,
                    destConversationId,
                    globalCallId_ClusterID,
                    joinOnBehalfOf,
                    comment,
                    authCodeDescription,
                    authorizationLevel,
                    clientMatterCode,
                    origDTMFMethod,
                    destDTMFMethod,
                    callSecuredStatus,
                    origConversationId,
                    origMediaCap_Bandwidth,
                    destMediaCap_Bandwidth,
                    authorizationCodeValue,
                    outpulsedCallingPartyNumber,
                    outpulsedCalledPartyNumber,
                    origIpv4v6Addr,
                    destIpv4v6Addr,
                    origVideoCap_Codec_Channel2,
                    origVideoCap_Bandwidth_Channel2,
                    origVideoCap_Resolution_Channel2,
                    origVideoTransportAddress_IP_Channel2,
                    origVideoTransportAddress_Port_Channel2,
                    origVideoChannel_Role_Channel2,
                    destVideoCap_Codec_Channel2,
                    destVideoCap_Bandwidth_Channel2,
                    destVideoCap_Resolution_Channel2,
                    destVideoTransportAddress_IP_Channel2,
                    destVideoTransportAddress_Port_Channel2,
                    destVideoChannel_Role_Channel2,
                    IncomingProtocolID,
                    IncomingProtocolCallRef,
                    OutgoingProtocolID,
                    OutgoingProtocolCallRef,
                    currentRoutingReason,
                    origRoutingReason,
                    lastRedirectingRoutingReason,
                    huntPilotPartition,
                    huntPilotDN,
                    calledPartyPatternUsage,
                    IncomingICID,
                    IncomingOrigIOI,
                    IncomingTermIOI,
                    OutgoingICID,
                    OutgoingOrigIOI,
                    OutgoingTermIOI,
                    outpulsedOriginalCalledPartyNumber,
                    outpulsedLastRedirectingNumber,
                    wasCallQueued,
                    totalWaitTimeInQueue,
                    callingPartyNumber_uri,
                    originalCalledPartyNumber_uri,
                    finalCalledPartyNumber_uri,
                    lastRedirectDn_uri,
                    mobileCallingPartyNumber,
                    finalMobileCalledPartyNumber,
                    origMobileDeviceName,
                    destMobileDeviceName,
                    origMobileCallDuration,
                    destMobileCallDuration,
                    mobileCallType,
                    originalCalledPartyPattern,
                    finalCalledPartyPattern,
                    lastRedirectingPartyPattern,
                    huntPilotPattern
                    ) VALUES (
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                    )""", (cdr_data_row))


if __name__ == '__main__':
    main()
