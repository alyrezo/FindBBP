from googlesearch import search
import time, os, argparse, requests, colorama , sys

colorama.init()

banner = colorama.Fore.RED + """
        ███████╗██╗███╗   ██╗██████╗   ██████╗ ██████╗ ██████╗ 
        ██╔════╝██║████╗  ██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗
        █████╗  ██║██╔██╗ ██║██║  ██║  ██████╔╝██████╔╝██████╔╝
        ██╔══╝  ██║██║╚██╗██║██║  ██║  ██╔══██╗██╔══██╗██╔═══╝ 
        ██║     ██║██║ ╚████║██████╔╝  ██████╔╝██████╔╝██║     
        ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝   ╚═════╝ ╚═════╝ ╚═╝     

        """ + colorama.Fore.CYAN + """Twitter:  @Alyrezo
        Github:  https://github.com/Alyrezo
        """

parser = argparse.ArgumentParser()
parser.add_argument('--silence',action="store_const",const=True,help="Not displaying the banner")
parser.add_argument('-n','--nonstop',action="store_const",const=True,help="non stop crawling")
parser.add_argument('-d','--dork',type=str,help="for using your custom dork")
parser.add_argument('-o','--output',type=str,help="result export as txt file")
parser.add_argument('-c','--count',type=int,help='count of domains it finds')
parser.add_argument('-t','--tld',type=str,help="for sort Top-Level Domain")
args = parser.parse_args()

if args.dork == None:
    dork = 'inurl:"security.txt" ext:txt -github -wikipedia'
    if args.tld != None:
        dork = f"site:{args.tld} " + dork
else:
    dork = str(args.dork).replace("'","")

if args.silence == None:
    print(banner)
    print(colorama.Fore.YELLOW + "[!] " + dork)

try:
    os.remove(".google-cookie")
except:
    pass

if args.output != None:
    file = args.output
    with open(file,'w') as tmp:
        tmp.close()

count = 0
try:
    for results in search(dork, tld="com", lang="en",num=5, start=0, stop=None, pause=2):
        if args.silence == None:
            print(colorama.Fore.GREEN +'[+] '+results[results.find('/',results.find('/'))+2:results.find('/',results.find('/')+2)])
            try:
                print(colorama.Fore.BLUE + requests.get(results,timeout=2).text+'\n\n')
            except:
                pass
        else:
            print(colorama.Fore.GREEN + results)

        if args.count != None:
            if count == args.count:
                break
            else:
                count += 1

        if args.output != None:
            with open(file,'a') as tmp:
                tmp.write(results + '\n')
        
        if args.nonstop or args.count or args.silence == None:
            print('\n' + colorama.Fore.YELLOW + '[!] continue...',end='')
            input()

        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()

