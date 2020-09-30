import os
import glob
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

MAXFILES = 50

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

# Define MPI message tags
tags = enum('READY', 'DONE', 'EXIT', 'START')

if rank == 0:
  
    # Get directory listing for data directory
    
    loc = os.path.expanduser(os.environ['DATADIR'])
    files = glob.glob(os.path.join(loc,"*.sgy"))
    
    files = files[0:min(MAXFILES,len(files))]
    
    for file in files:
        
        status = MPI.Status()
        comm.recv(tag=tags.READY,status=status)        
        sender = status.Get_source()        
        comm.send(file,dest=sender,tag=tags.START)
        
    for rnk in range(1,size):
    
        status = MPI.Status()
        comm.recv(tag=tags.READY,status=status)        
        sender = status.Get_source()
        comm.send([],dest=sender,tag=tags.EXIT)
        
else:

    tag = tags.START
    
    while True:
    
        comm.send([],dest=0,tag=tags.READY)
        
        status = MPI.Status()
        file = comm.recv(source=0,tag=MPI.ANY_TAG,status=status)
        tag = status.Get_tag()
        
        if tag == tags.EXIT:
            break
        
        print("rank %d, tag %d: %s" % (rank, tag, file))
        
