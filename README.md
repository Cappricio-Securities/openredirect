
<div align="center">
  <img src="https://blogs.cappriciosec.com/uploaders/openredirect.png" alt="logo">
</div>


## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![PyPI - Version](https://img.shields.io/pypi/v/openredirect)
![PyPI - Downloads](https://img.shields.io/pypi/dm/openredirect)
![GitHub all releases](https://img.shields.io/github/downloads/Cappricio-Securities/openredirect/total)
<a href="https://github.com/Cappricio-Securities/openredirect/releases/"><img src="https://img.shields.io/github/release/Cappricio-Securities/openredirect"></a>![Profile_view](https://komarev.com/ghpvc/?username=Cappricio-Securities&label=Profile%20views&color=0e75b6&style=flat)
[![Follow Twitter](https://img.shields.io/twitter/follow/cappricio_sec?style=social)](https://twitter.com/cappricio_sec)
<p align="center">

<p align="center">







## License

[MIT](https://choosealicense.com/licenses/mit/)



## Installation 

1. Install Python3 and pip [Instructions Here](https://www.python.org/downloads/) (If you can't figure this out, you shouldn't really be using this)

   - Install via pip
     - ```bash
          pip install openredirect 
        ```
   - Run bellow command to check
     - `openredirect -h`

## Configurations 
2. We integrated with the Telegram API to receive instant notifications for vulnerability detection.
   
   - Telegram Notification
     - ```bash
          openredirect --chatid <YourTelegramChatID>
        ```
   - Open your telegram and search for [`@CappricioSecuritiesTools_bot`](https://web.telegram.org/k/#@CappricioSecuritiesTools_bot) and click start

## Usages 
3. This tool has multiple use cases.
   
   - To Check Single URL
     - ```bash
          openredirect -u http://example.com 
        ```
   - To Check List of URL 
      - ```bash
          openredirect -i urls.txt 
        ```
   - Save output into TXT file
      - ```bash
          openredirect -i urls.txt -o out.txt
        ```
   - Want to Learn about [`openredirect`](https://blogs.cappriciosec.com/application/143/Open%20Redirection%20-%20A%20Deceptive%20Detour%20for%20Users%20and%20a%20Vulnerability%20for%20Applications)? Then Type Below command
      - ```bash
          openredirect -b
        ```
     
<p align="center">
  <b>🚨 Disclaimer</b>
  
</p>
<p align="center">
<b>This tool is created for security bug identification and assistance; Cappricio Securities is not liable for any illegal use. 
  Use responsibly within legal and ethical boundaries. 🔐🛡️</b></p>


## Working PoC Video

[![asciicast](https://blogs.cappriciosec.com/uploaders/Screenshot%202024-05-19%20at%204.46.23%20PM.png)](https://asciinema.org/a/fU7dHRjZagrF65cCf8yz2ZhW4)




## Help menu

#### Get all items

```bash
👋 Hey Hacker
                                                            v1.0
   ____                         ____           ___                __
  / __ \____  ___  ____        / __ \___  ____/ (_)_______  _____/ /_
 / / / / __ \/ _ \/ __ \______/ /_/ / _ \/ __  / / ___/ _ \/ ___/ __/
/ /_/ / /_/ /  __/ / / /_____/ _, _/  __/ /_/ / / /  /  __/ /__/ /_
\____/ .___/\___/_/ /_/     /_/ |_|\___/\__,_/_/_/   \___/\___/\__/
    /_/
                              Developed By https://cappriciosec.com

openredirect : Bug scanner for WebPentesters and Bugbounty Hunters 

$ openredirect [option]

Usage: openredirect [options]
```


| Argument | Type     | Description                | Examples |
| :-------- | :------- | :------------------------- | :------------------------- |
| `-u` | `--url` | URL to scan | openredirect -u https://target.com |
| `-i` | `--input` | filename Read input from txt  | openredirect -i target.txt | 
| `-o` | `--output` | filename Write output in txt file | openredirect -i target.txt -o output.txt |
| `-c` | `--chatid` | Creating Telegram Notification | openredirect --chatid yourid |
| `-b` | `--blog` | To Read about openredirect Bug | openredirect -b |
| `-h` | `--help` | Help Menu | openredirect -h |



## 🔗 Links
[![Website](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cappriciosec.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karthikeyan--v/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/karthithehacker)



## Author

- [@karthithehacker](https://github.com/karthi-the-hacker/)



## Feedback

If you have any feedback, please reach out to us at contact@karthithehacker.com
