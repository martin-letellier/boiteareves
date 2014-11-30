#!/bin/bash
i=1
while true; do
  url="http://www.la-boite-a-reves.fr/reves/$i?print=true" 
  code=`curl -s -o /dev/null -w "%{http_code}" $url`
  if [ $code -ne 200 ]; then
    break;
  fi
  echo $i
  phantomjs rasterize.js $url "reve-$(echo $i).png" 384px
  i=$((i+1))
done
