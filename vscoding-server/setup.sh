# Reset
O='\e[0m'       # Text Reset

# Regular Colors
R='\e[31m'          # Red
G='\e[32m'        # Green
Y='\e[33m'       # Yellow
B='\e[34m'         # Blue

echo -e "${B}CB-CodeServer Script${O} "    
echo -e "Checking Depedencies "
if command -v nodejs >/dev/null 2>&1 ; then
    echo -e "${G}nodejs found "
    echo -e "version: $(nodejs -v) "
else
    echo -e "${R}nodejs not found "
    exit 1
fi
if command -v n code-server >/dev/null 2>&1 ; then
    echo -e "${G}Code-Server found "
    echo -e "Version: $(code-server -v) "
else
    echo -e "${R}Code-Server not found! Install through NPM "
    exit 1
fi
if command -v ngrok >/dev/null 2>&1 ; then
    echo -e "${G}Ngrok found "
    echo -e "version: $(ngrok -v)${O} "
else
    echo -e "${R}Ngrok not found! Download from ngrok.com or snap install ngrok${O} "
    exit 1
fi
echo -e -n "Enter Telegram Bot Token: "
read token
echo -e -n "Enter Chat ID of the bot"
read chatid
export CHAT_ID=$chatid
export TELEGRAM_BOT_TOKEN=$token
echo -e "export TELEGRAM_BOT_TOKEN=$token CHAT_ID=$chatid " >> /etc/profile
echo -e "Copying Files to /lib/systemd/system/ "
cp reverse* /lib/systemd/system/
cp code-server* /lib/systemd/system/
touch /lib/systemd/system/output.txt
echo -e "${G}Done copying! "
echo -e "Enabling Code-Server, Reverse-SSH Services "
systemctl daemon-reload
systemctl enable code-server
systemctl enable reverse-ssh
systemctl start code-server
systemctl start reverse-ssh
echo -e "{$}Done!"
