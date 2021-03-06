import React, { Component } from 'react'
import { Route, Switch } from 'react-router-dom'

import Layout from './hoc/Layout/Layout'
import Home from './containers/Home/Home'
import Catalog from './containers/Catalog/Catalog'

class App extends Component {
  render() {
    return(
      <Layout>
        <Switch>
          <Route path='/' exact component={ Home } />
          <Route path='/catalog' exact component={ Catalog } />
        </Switch>
      </Layout>
    )
  }
}

export default App;
