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

## General info
The top level of this project contains project resource files, the application 
itself resides in the "app" folder and has both a server side component 
and a frontend component. The server side component uses the popular python 
microframework flask. The frontend uses react.js and utilizes ol-kit for the 
map component and the bootstrap4 css framework. Relevant links are below:  
- ol-kit: https://ol-kit.com/  
- React: https://reactjs.org/  
- React-Bootstrap: https://react-bootstrap.github.io/  
- Bootstrap: https://getbootstrap.com/docs/4.5/getting-started/introduction/  
- Flask: https://flask.palletsprojects.com/en/1.1.x/  

## Docker and docker-compose 
The Dockerfile file at the root of the project defines an alpine based  container image for the web components of the project.  The docker-compose 
file utilizes this container image as well as providing a geoserver container
and a postgis container.  These can be found here:  
- Geoserver: 
  - https://hub.docker.com/r/1904labs/geoserver  
  - https://github.com/1904labs/docker-geoserver  
- PostGis:  
  - https://hub.docker.com/r/postgis/postgis
  - https://github.com/postgis/docker-postgis  

## Related  
This project is built from this base    
- flask-react-base: https://github.com/1904labs/flask-react-base  

The mapview portion started out as a standalone container, it is useful 
for experimenting with map layers and can be found here: 
- docker-ol-kit: 
  - https://hub.docker.com/r/1904labs/ol-kit  
  - https://github.com/1904labs/docker-ol-kit  
