import React from "react";
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Home from "./Components/Home";
import AddNewData from "./Components/VillageProfile/AddNewData";
import PendingData from "./Components/VillageProfile/PendingData";
import VillageProfileHome from "./Components/VillageProfileHome";
import "./App.css"
import { db } from "./db/db";

export default function App() {
  db.open();
  return (
    <Router>
      <Switch>
        <Route path="/vpapp/add-new">
          <AddNewData />
        </Route>
        <Route path="/vpapp/pending">
          <PendingData />
        </Route>
        <Route path="/vpapp">
          <VillageProfileHome />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}
