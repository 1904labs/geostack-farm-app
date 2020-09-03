import React from "react";
import TopNav from './TopNav'
import MapView from './MapView'
import ListView from './ListView'
import ListItemForm from './ListItemForm'
import {
  HashRouter as Router,
  Route,
  Switch
} from "react-router-dom";

const App = () => {
  return (
    <Router>
        <TopNav/>
        <Switch>
          <Route exact path="/" ><MapView /></Route>
          <Route path="/list"><ListView /></Route>
          <Route path="/sell"><ListItemForm /></Route>
        </Switch>
    </Router>
  );
}

export default App;