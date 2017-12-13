from app import db,models
import os


#numType = input('Search by Calling or Called number?:  ')
#numVar = input('Which number?:  ')
#
#if numType == 'Calling':
#    calling = models.CDR.query.filter_by(callingPartyNumber=numVar).all()
#    print(calling)
#
#elif numType == 'Called':
#    called = models.CDR.query.filter_by(originalCalledPartyNumber=numVar).all()
#    for i in called:
#        print(called)
#
#    for i in cdrrecord:
#        print(i.originalCalledPartyNumber,i.originalCalledPartyNumber,i.duration)
#
#    for i in cmrrecord:
#        print(i.varVQMetrics)called = models.CDR.query.filter_by(originalCalledPartyNumber=numVar).all()

#def dbquery():

#header = models.CDR.query.column_descriptions()   ????

#dateQ = models.CDR.query.filter(models.CDR.dateTimeOrigination >= '1511190039').filter(
#    models.CDR.dateTimeOrigination <= '1511190058').filter_by(callingPartyNumber='1530')

#for row in dateQ:
#    dict = row.__dict__
#    del dict['_sa_instance_state']
#z   print(json.dumps(dict))

#    dateQ = models.CDR.query.filter(models.CDR.dateTimeOrigination >= '').filter(models.CDR.dateTimeOrigination <= '')

#    dicts = [(row.__dict__) for row in dateQ]
#    print(dicts)
#    for dict in dicts:
#        del dict['_sa_instance_state']
#    print(dicts)


#    for row in dateQ:
#        dicts = []
#        dict = row.__dict__
#        del dict['_sa_instance_state']

#        dicts.append(dict)
#    print(dicts)


#query = models.CDR.query.all() #print entire database
#for q in query: #iterate across each row object from table
#    print(q.__dict__) #.values(), .keys(), or .items() from __dict__ to extract values from row objects.

