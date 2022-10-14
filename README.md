# AttendanceBot

This repository contains the python source code for a discord attendance bot. It is capable of tracking attendee names and dates in a CSV file and has some admin commands to retrieve this file and change the password for sign in.

# Usage

With the discord bot set up on a server, the following commands are possible through direct messages or in it's specified channel:

 - Attendee sign in: **@Bot *(password) (name)***
 - Retrieve CSV file: **@Bot *(get_csv_code)***
 - Change the password: **@Bot *(set_pass_code) (new_password)***

Make sure to remove the parenthesis when filling in the command. *get_csv_code* and *set_pass_code* are private keys required to use admin commands. They are set in a secrets file associated with the main script. If you wish to keep the attendance sheet private, only use the command in direct messages with the bot.

The password is only reset temporarily until the server is restarted.
In rare occurrences, the server may restart when attendance is being taken.

A .CSV file will be created automatically when first used. Please avoid changing this file, as it can stop the bot from saving data properly.

## CSV Format

The CSV file can be downloaded from Discord **with the admin key** and used as an excel file for tracking attendance and other operations. The CSV file cannot be written to on the server side without manual access to the hosting platform. The columns represent dates, and the rows attendees.

## MSU SRT Specific Details

The bot is named SolarAttendance on the associated discord server. Head to the **#attendance** channel under the **Information** tab to use the commands listed above or direct message the AttendanceBot. Commands work the exact same when direct messaging the bot.

The bot is hosted by me (Vetri Vijay). If changes need to be made to the currently running bot when I'm not on the team, feel free to reach out.

## Resources Used

https://www.youtube.com/watch?v=SPTfmiYiuok&t=12s
