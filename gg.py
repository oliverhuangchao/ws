import subprocess
import sys

HOST="node1847"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="bash -l /home/wei6/wei6Project3/probabilitySearch/nodeRun.bash"

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result