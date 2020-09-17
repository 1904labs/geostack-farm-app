import React, { Component } from 'react'

import {
  Map,
  Popup,
  Controls,
  loadDataLayer
} from '@bayer/ol-kit'

class MapView extends Component {

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

  createUSStatesLayer = async () => {
    const map = this.state.map
    const url = window.location.origin + '/api/geoserver/states';
    const layer = await loadDataLayer(map, url, { addToMap: false })
    layer.set('title', 'us-states')
    map.addLayer(layer)
  }

  onMapInit = (map) => {
    this.setState({ map: map })
    this.createUSStatesLayer()
  }

  render(){
    return (
        <Map onMapInit={this.onMapInit} className="vw-100 vh-100">
          <Controls />
          <Popup />
        </Map>
    )
  }
}

export default MapView
