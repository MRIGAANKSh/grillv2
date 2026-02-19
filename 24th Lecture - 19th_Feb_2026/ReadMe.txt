Steps to install dlib for face detection (Python Version = 3.10)

STEP 1) Create a virtual environment
python -m venv myenv

STEP 2) Activate your created virtual environment
source myenv/bin/activate

STEP 3) Upgrade pip
pip install --upgrade pip

STEP 4) Install additional libraries to work on videos
sudo apt update -y && sudo apt install ffmpeg libsm6 libxext6 -y

STEP 5) Install additional libraries for dlib and face_recognition
sudo apt install cmake libboost-all-dev -y
sudo apt install build-essential -y

STEP 6) Install project required libraries
pip install -r requirement.txt
