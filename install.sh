#pkg update && pkg upgrade
#pkg install python
pkg install figlet
cd
cd ../usr/etc                                                              
echo "alias clock='cd && cd simple-clock && python clock.py'" >> bash.bashrc
cd 
echo "Terminal shortcut successfully created"
echo "If not working this shortcut, Please Restart termux app"
echo "Next time just type: "
echo "clock"
echo