from servers.chill_palace import chill_palace 
from servers.pfp import pfp
from servers.mmmm import mmmm
from multiprocessing import Process

is_pfp = True
is_chill_palace = True
is_mmmm = True

if __name__=='__main__':
  pfp_fun = Process(target = pfp.run)
  chill_palace_fun = Process(target = chill_palace.run)
  mmmm_fun = Process(target = mmmm.run)

  if is_pfp:
    print("PFP TRUE")
    pfp_fun.start()

  if is_chill_palace:
    print("CHILL PALACE TRUE")  
    chill_palace_fun.start()

  if is_mmmm:
    print("MMMM TRUE")  
    mmmm_fun.start()
