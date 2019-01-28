pkill python

cd `dirname $0`
source activate dev
python dev.py

pkill python

python main.py
pkill python
exit