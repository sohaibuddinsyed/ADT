# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound

# App modules
from app import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):

    try:
        f = open("app/log.txt","r")
        dateline = f.readline()
        startdate = dateline[19:30]
        startdate  = startdate .replace(", ","-")
        f.close()
        
        LOG = tracker("app/log.txt", startdate)
        # LOG = LOG + tracker("app/log2.txt", startdate)
        
        print()
        print()
        # Detect the current page
        segment = get_segment( request )
        print("-"*100)
        # for item in LOG:
        #     print(item)
        totalVisitCount = 0
        for key, val in totalVisits.items():
            totalVisitCount += val
            print(key,val)
        # Serve the file (if exists) from app/templates/FILE.html
        return render_template(  path, hi="Hello",log_global = LOG,totalVisits = totalVisits, 
        cameras = cameras, people = people,totalVisitCount = totalVisitCount,segment=segment)
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404

def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
totalVisits=dict({'agentOne':0, 'agentTwo':0, 'president':0})
people = list([])
cameras = list([])

def tracker(file, startdate):
    f = open(file,"r")
    LOG = []
    prev = {'agentOne':0, 'agentTwo':0, 'president':0}
    localdate = None
    
    for line in f.readlines():
        log_dict = dict({'date':None, 'time':None, 'people':[], 'location':None, 'startdate':startdate, 'enddate':None, 
        'count':{'agentOne':0, 'agentTwo':0, 'president':0}})
        
        print()
        print()
        # if("Unknown" in line):
        #     log_dict['people'].append("unknown")
        #     log_dict['count'].append
        if('Agent1' in line):
            log_dict['people'].append("Agent 1")
            if('Agent1' not in people):
                people.append('Agent1')
            log_dict['count']['agentOne'] = log_dict['count']['agentOne'] + 1
        
        if('Agent2' in line):
            log_dict['people'].append("Agent 2")
            if('Agent2' not in people):
                people.append('Agent2')
            log_dict['count']['agentTwo'] = log_dict['count']['agentTwo'] + 1
        
        if('President' in line):
            log_dict['people'].append("President")
            if('President' not in people):
                people.append('President')
            log_dict['count']['president'] = log_dict['count']['president'] + 1
        
        if("Camera1" in line):
            log_dict['location']="Cam-1"
            if('Cam-1' not in cameras):
                cameras.append("Cam-1")
        
        if("Camera2" in line):
            log_dict['location']="Cam-2"
            if('Cam-2' not in cameras):
                cameras.append("Cam-2")
        # alist = list(line)
        localdate = line[19:30]
        localdate = localdate.replace(", ","-")
        log_dict['date'] = localdate
        time = line[32:41]
        time = time.replace(", ",":")
        log_dict['time'] = time
        for key, val in log_dict.items():
            print(key,val)
        for key, val in totalVisits.items():
            print(key,val)
        LOG.append(log_dict)
        LOG.append('*');
        for val in people:
            print(val)
        for val in cameras:
            print(val)
    
        if( prev['agentOne'] > log_dict['count']['agentOne'] ):
            totalVisits['agentOne'] += 1
     
        if( prev['agentTwo'] > log_dict['count']['agentTwo'] ):
            totalVisits['agentTwo'] += 1

        if( prev['president'] > log_dict['count']['president'] ):
            totalVisits['president'] += 1
        
        
        prev = log_dict['count']

    return LOG