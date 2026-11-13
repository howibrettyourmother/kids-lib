# Copy kids.js into a game's source folder with a provenance header. Usage: python3 vendor.py /workspace/<game>/src
import os,sys,subprocess
D=os.path.dirname(os.path.abspath(__file__));dst=sys.argv[1]
rev=subprocess.run(['git','-C',D,'rev-parse','--short','HEAD'],capture_output=True,text=True).stdout.strip() or 'local'
src=open(f'{D}/kids.js').read()
open(os.path.join(dst,'kids.js'),'w').write(f'/* vendored from howibrettyourmother/kids-lib @{rev} — edit the lib, then re-vendor */\n'+src)
print('vendored kids.js @',rev,'->',dst)
