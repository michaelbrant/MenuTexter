# MenuTexter
Automatically sends texts of Widener University's cafeteria Lunch and Dinner menus.
The HTML is parsed from https://widener.campusdish.com/Commerce/Catalog/Menus.aspx?LocationId=213 using a python library called Beautiful Soup 4


### To Install the MenuTexter:
You can remotely connect via SSH into ec2-52-207-132-210.compute-1.amazonaws.com with the username ec2-user and the private key that
I'm not going to post here. This already has the MenuTexter installed using the email menutexter@gmail.com 

-OR, If you want your own server-
1. Launch a t2.micro Amazon Linux AMI EC2 instance and run the following commands:
```sh
$ sudo yum update
$ sudo easy_install bs4
$ sudo easy_install configparser
$ sudo yum install git-all
```
2. git clone https://github.com/michaelbrant/MenuTexter
3. edit config.cfg with either your own gmail account or add the password that I will give to you. (I'm not posting that here)

### Running the MenuTexter
Send a text to the gmail saying Start, if you did not add your own then it is menutexter@gmail.com

Next, run 
```sh
$ python checkMail.py 
```
Then,
```sh
$ nano emailList.txt 
```
and you should see your phone number in the list.


At this point running:
```sh
$ python MenuTexter.py L
```
will send a text of today's lunch menu to whatever phone numbers are in emailList.txt

```sh
$ python MenuTexter.py D 
```
will send a text of the dinner menu.

If you are not receiving a text it is quite possible that there is no lunch/dinner menu for today.
Uncomment the three lines in pullMenu.py to test specific days that you know have lunch or dinner menus

### Make the MenuTexter Automatic
```sh
$ crontab -e
```
add the following code:
```
00 14 * * 1-5 python MenuTexter.py D
00 14 * * 1-5 python MenuTexter.py L
* * * * * python checkMail.py
```
This will run MenuTexter.py D and MenuTexter.py L every day Monday-Friday during school months at 10AM
It will also run checkMail.py every minute.
