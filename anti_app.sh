# a little bash script for mac that stops an app from starting. just a little prank script I use on technicly challenged friends
#USAGE: ./anti_app.sh [APP]
while :
do
  pkill $1
done
