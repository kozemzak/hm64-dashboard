import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import Home from './Home.js'
import Tools from './Tools.js'
import GirlsRivals from './GirlsRivals.js'
import Animals from './Animals.js'

class AppRouter extends Component{ 
  render() {
    return (
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/girls_rivals/">Girls and Rivals</Link>
              </li>
              <li>
                <Link to="/animals/">Animals</Link>
              </li>
              <li>
                <Link to="/tools/">Tools</Link>
              </li>
            </ul>
          </nav>
          <Route path="/" exact component={Home} />
          <Route path="/girls_rivals/" component={GirlsRivals} />
          <Route path="/animals/" component={Animals} />
          <Route path="/tools/" component={Tools} />
        </div>
      </Router>
    );
  }
}

export default AppRouter;
