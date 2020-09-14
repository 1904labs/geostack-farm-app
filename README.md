# Geospatial hackathon collaboration project  
Farm to Consumer Application
See extended documentation here:  
https://1904labs.github.io/geohack-collab-project/index.html  

## Prerequisites  
1. pyenv:  
    1. Install the required build packages here:  
       https://github.com/pyenv/pyenv/wiki/Common-build-problems  
    2. Install pyenv via the instructions here:  
       https://github.com/pyenv/pyenv-installer  
2. pipenv: Install pipenv via the instructions here:  
https://pypi.org/project/pipenv/  
3. node/npm: Install node.js and npm per the instructions here:  
https://www.npmjs.com/get-npm  

## Setup  
__1. Install your python environement__
```bash
pipenv install
```

__2. Install your node environment__
```bash
npm install
```

__3. Build your react app__
```bash
npm run build
```

__4. Run the dev server__
Lauch the webpack dev server on http://localhost:3000  
A browser window should open automatically  
```bash
npm run start
```
Alternately to lauch the flask dev server on http://localhost:5000  
```bash
npm run flask
```

