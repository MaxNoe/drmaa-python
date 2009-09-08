#!/usr/bin/env python

import DRMAA
import os

def main():
    """Submit a job, then kill it.
    Note, need file called sleeper.sh in home directory. An example:
    echo 'Hello World $1'
    """
    s=DRMAA.Session()
    s.init()

    print 'Creating job template'
    jt = s.createJobTemplate()
    jt.remoteCommand = os.getcwd() + '/sleeper.sh'
    jt.args = ['42','Simon says:']
    jt.joinFiles=True
    jt.outputPath=":"+DRMAA.JobTemplate.HOME_DIRECTORY+'/tmp/DRMAA_JOB_OUT'
    
    jobid = s.runJob(jt)
    print 'Your job has been submitted with id ' + jobid
    # options are: SUSPEND, RESUME, HOLD, RELEASE, TERMINATE
    s.control(jobid,DRMAA.Session.TERMINATE)

    print 'Cleaning up'
    s.deleteJobTemplate(jt)
    s.exit()
    
if __name__=='__main__':
    main()
