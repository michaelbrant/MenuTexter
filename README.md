# MenuTexter
Automatically sends texts of Widener University's cafeteria Lunch and Dinner menus

To Run the MenuTexter:
1. Launch a t2.micro Amazon Linux AMI EC2 instance.
2. sudo yum update
3. sudo easy_install bs4
4. sudo easy_install configparser
5. Move all code to /home/ec2-user
6. edit config.cfg with either your own gmail account or add the password that I will give to you. (I'm not posting that here)

At this point running 
$python MenuTexter.py L
will send a text of today's lunch menu to whatever phone number is in emailList.txt
