import os
import elm
path = os.path.dirname(elm.__file__) 
ELM_COMPILER_EXECUTABLE = "runghc "+ path + "/bin/elmToJS.hs"
