const path = require('path');
const rewireReactHotLoader = require('react-app-rewire-hot-loader')

module.exports = {
    config: function (config, env) {        
  	return rewireReactHotLoader(config, env)
    },
    paths: function (paths, env) {        
        paths.appSrc = path.resolve(__dirname, 'app/src');
        paths.appBuild = path.resolve(__dirname, 'app/dist');
        paths.appPublic = path.resolve(__dirname, 'app/public');
        paths.appIndexJs = path.resolve(__dirname, 'app/src/index.js');
        paths.appHtml = path.resolve(__dirname, 'app/public/index.html');
        paths.testsSetup = path.resolve(__dirname, 'app/src/setupTests.js');
        paths.proxySetup = path.resolve(__dirname, 'app/src/setupProxy.js');
        paths.swSrc = path.resolve(__dirname, 'app/src/service-worker.js');
        return paths;
    }
}
