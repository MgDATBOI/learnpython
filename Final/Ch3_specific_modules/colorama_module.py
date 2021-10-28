from colorama import Fore, Back, Style, init

init()

MVG = f"{Fore.WHITE}{Style.BRIGHT}[{Fore.CYAN}M{Fore.BLUE}V{Fore.MAGENTA}G{Fore.WHITE}]{Fore.RESET}{Style.NORMAL}"
Q = f"{Fore.WHITE}{Style.BRIGHT}[{Fore.BLUE}?{Fore.WHITE}]{Fore.RESET}{Style.NORMAL}"
INFO = f"{Fore.WHITE}{Style.BRIGHT}[{Fore.CYAN}-{Fore.WHITE}]{Fore.RESET}{Style.NORMAL}"
WARN = (
    f"{Fore.WHITE}{Style.BRIGHT}[{Fore.YELLOW}*{Fore.WHITE}]{Fore.RESET}{Style.NORMAL}"
)
CRIT = f"{Fore.WHITE}{Style.BRIGHT}[{Fore.RED}!{Fore.WHITE}]{Fore.RESET}{Style.NORMAL}"
OK = f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}+{Fore.WHITE}]{Fore.RESET}{Style.NORMAL}"

print(MVG)
print(Q)
print(INFO)
print(WARN)
print(CRIT)
print(OK)
