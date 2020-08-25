import React, { Component } from 'react'
import { 
  Map, 
  Popup, 
  Controls, 
  LayerPanel, 
  loadDataLayer 
} from '@bayer/ol-kit'

class App extends Component {

  addLayerOnLoaded = async (ev) => {
    const map = this.state.map
    const fileName =  ev.target.fileName
    const content = ev.target.result
    const layer = await loadDataLayer(map, content, { addToMap: false })
    layer.set('title', fileName)
    map.addLayer(layer)
  }
  

  addLayerFromFile = (file) => {
    const fileData = new FileReader()
    fileData.fileName = file.name
    fileData.onloadend = this.addLayerOnLoaded
    fileData.readAsText(file)
  }

  onMapInit = (map) => {
    this.setState({ map: map });
  }

  render(){
    return (
      <Map onMapInit={this.onMapInit} >
        <Controls />
        <Popup />
        <LayerPanel onFileImport={this.addLayerFromFile} />
      </Map>
    )
  }
}

export default App
