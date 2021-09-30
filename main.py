import chill_palace
import pfp
from multiprocessing import Process

is_pfp = True
is_chill_palace = True

if __name__=='__main__':
  pfp_fun = Process(target = pfp.run)
  chill_palace_fun = Process(target = chill_palace.run)

  if is_pfp:
    print("PFP TRUE")
    pfp_fun.start()

  if is_chill_palace:
    print("CHILL PALACE TRUE")  
    chill_palace_fun.start()