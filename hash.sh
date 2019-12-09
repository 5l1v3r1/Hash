#!/bin/bash

echo ""
echo " 01) Encode String"
echo " 02) Decode Hash"
echo ""
read -p " Menu : " act;

if [ $act == '1' ]
then
	php en.php
elif [ $act == '2' ]
then
	python3 de.py
fi