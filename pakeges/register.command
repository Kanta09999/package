pkill python
cd `dirname $0`
source activate dev
python reg.py
pkill python
exit