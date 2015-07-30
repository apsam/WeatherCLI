#!/bin/sh

echo "City:"
read city_name
echo "State:"
read state_name
#echo "$city_name is in $state_name" 

python getweather.py $city_name $state_name
