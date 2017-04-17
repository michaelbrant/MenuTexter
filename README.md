# MenuTexter
Automatically sends texts of Widener University's cafeteria Lunch and Dinner menus

To Run the MenuTexter:
1. Launch a t2.micro Amazon Linux AMI EC2 instance.
2. sudo yum update
3. sudo easy_install bs4
4. sudo easy_install configparser
5. Move all code to /home/ec2-user
6. edit config.cfg with either your own gmail account or add the password that I will give to you. (I'm not posting that here)

Send a text to the gmail saying Start, if you did not add your own then it is cafemenuemail@gmail.com
Next, run python checkMail.py. nano emailList.txt and you should see your phone number in the list.
At this point running:
$python MenuTexter.py L
will send a text of today's lunch menu to whatever phone numbers are in emailList.txt

python MenuTexter.py D will send a text of the dinner menu.

If you are not receiving a text it is quite possible that there is no lunch/dinner menu for today.
https://widener.campusdish.com/Commerce/Catalog/Menus.aspx?LocationId=213

nano pullMenu.py and uncomment out the three lines to test specific days that you know have lunch or dinner menus

crontab -e

