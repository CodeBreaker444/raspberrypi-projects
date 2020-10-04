#!/bin/sh

#MESSAGE=$(systemctl status reverse-ssh | grep url)
MESSAGE=$(date && cat /lib/systemd/system/output.txt | grep url)
if [ $MESSAGE -eq "" ]; then
MESSAGE="Not_Assigned_URL"
fi
echo $MESSAGE
C_ID=$CHAT_ID
TOKEN=$TELEGRAM_BOT_TOKEN
URL="https://api.telegram.org/bot$TOKEN/sendMessage"
curl -s -X POST $URL -d chat_id=$C_ID -d text="$MESSAGE"
#echo $MESSAGE
if [ $? -eq 0 ]; then
	echo Sent
else
	echo Failed to sent
fi
