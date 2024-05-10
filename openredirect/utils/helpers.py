#!/usr/bin/env python

"""
 * Open Redirect
 * Open Redirect Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""

👋 Hey \033[96m{username}
   \033[92m                                                         v1.0
   ____                         ____           ___                __
  / __ \____  ___  ____        / __ \___  ____/ (_)_______  _____/ /_
 / / / / __ \/ _ \/ __ \______/ /_/ / _ \/ __  / / ___/ _ \/ ___/ __/
/ /_/ / /_/ /  __/ / / /_____/ _, _/  __/ /_/ / / /  /  __/ /__/ /_
\____/ .___/\___/_/ /_/     /_/ |_|\___/\__,_/_/_/   \___/\___/\__/
    /_/
                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mOpen Redirect : Bug scanner for WebPentesters and Bugbounty Hunters

\x1b[31;1m$ \033[92mOpen Redirect\033[0m [option]

Usage: \033[92mOpen Redirect\033[0m [options]

Options:
  -u, --url     URL to scan                                openredirect -u https://target.com
  -i, --input   <filename> Read input from txt             openredirect -i target.txt
  -o, --output  <filename> Write output in txt file        openredirect -i target.txt -o output.txt
  -c, --chatid  Creating Telegram Notification             openredirect --chatid yourid
  -b, --blog    To Read about Open Redirect Bug           openredirect -b
  -h, --help    Help Menu
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
      \033[92m                                                      v1.0
   ____                         ____           ___                __
  / __ \____  ___  ____        / __ \___  ____/ (_)_______  _____/ /_
 / / / / __ \/ _ \/ __ \______/ /_/ / _ \/ __  / / ___/ _ \/ ___/ __/
/ /_/ / /_/ /  __/ / / /_____/ _, _/  __/ /_/ / / /  /  __/ /__/ /_
\____/ .___/\___/_/ /_/     /_/ |_|\___/\__,_/_/_/   \___/\___/\__/
    /_/
                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mOpen Redirect : Bug scanner for WebPentesters and Bugbounty Hunters

\033[0m"""
    print(help_banner)
