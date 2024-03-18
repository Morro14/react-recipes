import React from "react";

import "./App.css";
import { Outlet } from "react-router-dom";
import Header from "./components/Header";

function App() {
  return (
    <>
      <div className="App">
        <Header />
        <Outlet></Outlet>
      </div>
    </>
  );
}
export default App;