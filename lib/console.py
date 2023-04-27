from colorama import Fore, init; init()
import threading, json, os
config = json.load(open('./input/config.json', 'r+'))
lock = threading.Lock()
class Console:
    def __init__(self) -> None:
        pass

    def debug(content: str):
            if config['debug']:
                lock.acquire()
                print(f'[DEBUG] {content}{Fore.RESET}'.replace('[+]', f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}]').replace('[*]', f'[{Fore.LIGHTYELLOW_EX}*{Fore.RESET}]').replace('[>]', f'[{Fore.CYAN}>{Fore.RESET}]').replace('[-]', f'[{Fore.RED}-{Fore.RESET}]'))
                lock.release()
    def printl(content: str):
            lock.acquire()
            print(f'{content}{Fore.RESET}'.replace('[+]', f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}]').replace('[*]', f'[{Fore.LIGHTYELLOW_EX}*{Fore.RESET}]').replace('[>]', f'[{Fore.CYAN}>{Fore.RESET}]').replace('[-]', f'[{Fore.RED}-{Fore.RESET}]'))
            lock.release()
    def logo():
        os.system(f"title Guilded AIO ^| v1.2.0 ^| by xKian ^| Improved by daddy m ^| Tokens loaded: {len(open('./output/cookies.txt', 'r+').read().splitlines())}")
        print(Fore.RED + f"""


                        ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗      █████╗ ██╗ ██████╗ 
                       ██╔════╝ ██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║██╔═══██╗
                       ██║  ███╗██║   ██║██║██║     ██║  ██║█████╗  ██║  ██║    ███████║██║██║   ██║
                       ██║   ██║██║   ██║██║██║     ██║  ██║██╔══╝  ██║  ██║    ██╔══██║██║██║   ██║
                       ╚██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██████╔╝    ██║  ██║██║╚██████╔╝
                        ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝     ╚═╝  ╚═╝╚═╝ ╚═════╝ 

                                                {Fore.RESET}by xKian - Improved by daddy m

                                    {Fore.RED}[{Fore.RESET}1{Fore.RED}]{Fore.RESET} Account Creator       {Fore.RED}[{Fore.RESET}5{Fore.RED}]{Fore.RESET} Set Profile Picture
                                    {Fore.RED}[{Fore.RESET}2{Fore.RED}]{Fore.RESET} Server Joiner         {Fore.RED}[{Fore.RESET}6{Fore.RED}]{Fore.RESET} Spammer
                                    {Fore.RED}[{Fore.RESET}3{Fore.RED}]{Fore.RESET} Onliner               {Fore.RED}[{Fore.RESET}7{Fore.RED}]{Fore.RESET} Token Checker      
                                    {Fore.RED}[{Fore.RESET}4{Fore.RED}]{Fore.RESET} Set Status            {Fore.RED}[{Fore.RESET}8{Fore.RED}]{Fore.RESET} Coming soon...                                        

""")