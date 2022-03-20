if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Nivedhhm/LuciferMoringstar-Robot/DarkSnyder-Robot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /DarkSnyder-Robot
fi
cd /DarkSnyder-Robot
pip3 install -U -r requirements.txt
echo "Starting DarkSnyder RoBot...."
python3 main.py
