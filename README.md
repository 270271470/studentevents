# Student Events Project
## Setup Instructions

### Prerequisites
- Python 3.x
- Node.js and npm

### Set Up Python Environment
python -m venv venv
source venv\Scripts\activate

pip install -r requirements.txt

### Clone the Repository
git clone https://github.com/270271470/studentevents.git

cd flask_app

### Set Up Node.js Environment
npm install

### To Run while developing
watchmedo auto-restart --patterns="*.py;*.html" --recursive -- flask run

### If new Vue components are added OR current ones updated also run
npm run buildvite

### If any CSS changes are made, it must be compiled from the input.css to the output.css, so run this
npm run buildcss
