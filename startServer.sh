portValue=`grep PORT ./config.py`

port=`echo $portValue | cut -d " " -f 3`
python3 httpServer.py $port &
echo $! > .tmp.txt
echo "Started Server"