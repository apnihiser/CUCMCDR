import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_PASSWORD_SALT = 'sdf8y79pawhfo8h983hfp[98f4845jnfnjrgf859j34fji9f3j9'
    SECURITY_USER_IDENTITY_ATTRIBUTES = 'name'

    advancedCallInfo = [
        "authCodeDescription",
        "authorizationCodeValue",
        "authorizationLevel",
        "calledPartyPatternUsage",
        "callingPartyNumber_uri",
        "callingPartyNumberPartition",
        "callSecuredStatus",
        "clientMatterCode",
        "comment",
        "currentRoutingReason",
        "destCallTerminationOnBehalfOf",
        "destCause_location",
        "destCause_value",
        "destConversationId",
        "destDeviceName",
        "finalCalledPartyNumber_uri",
        "finalCalledPartyNumberPartition",
        "finalCalledPartyPattern",
        "globalCallId_ClusterID",
        "huntPilotDN",
        "huntPilotPartition",
        "huntPilotPattern",
        "joinOnBehalfOf",
        "lastRedirectDn",
        "lastRedirectDn_uri",
        "lastRedirectDnPartition",
        "lastRedirectingPartyPattern",
        "lastRedirectingRoutingReason",
        "lastRedirectRedirectOnBehalfOf",
        "lastRedirectRedirectReason",
        "origCalledPartyRedirectOnBehalfOf",
        "origCalledPartyRedirectReason",
        "origCallTerminationOnBehalfOf",
        "origCause_location",
        "origCause_value",
        "origConversationId",
        "origDeviceName",
        "originalCalledPartyNumber_uri",
        "originalCalledPartyNumberPartition",
        "originalCalledPartyPattern",
        "origRoutingReason",
        "outpulsedCalledPartyNumber",
        "outpulsedCallingPartyNumber",
        "outpulsedLastRedirectingNumber",
        "outpulsedOriginalCalledPartyNumber",
        "totalWaitTimeInQueue",
        "wasCallQueued",
    ]

    protocolInfo = [
        "cdrRecordType",
        "globalCallID_callManagerId",
        "globalCallID_callId",
        "origLegCallIdentifier",
        "origNodeId",
        "origSpan",
        "origIpAddr",
        "origMediaTransportAddress_IP",
        "origMediaTransportAddress_Port",
        "origMediaCap_payloadCapability",
        "origMediaCap_maxFramesPerPacket",
        "origMediaCap_g723BitRate",
        "destLegIdentifier",
        "destNodeId",
        "destSpan",
        "destIpAddr",
        "destMediaTransportAddress_IP",
        "destMediaTransportAddress_Port",
        "destMediaCap_payloadCapability",
        "destMediaCap_maxFramesPerPacket",
        "destMediaCap_g723BitRate",
        "destVideoCap_Codec",
        "destVideoCap_Bandwidth",
        "destVideoCap_Resolution",
        "destVideoTransportAddress_IP",
        "destVideoTransportAddress_Port",
        "origDTMFMethod",
        "destDTMFMethod",
        "origMediaCap_Bandwidth",
        "destMediaCap_Bandwidth",
        "origIpv4v6Addr",
        "destIpv4v6Addr",
        "IncomingProtocolID",
        "IncomingProtocolCallRef",
        "OutgoingProtocolID",
        "OutgoingProtocolCallRef"
    ]

