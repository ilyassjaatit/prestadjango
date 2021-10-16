import React from 'react';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Layout from "../containers/Layout";
import AppContext from "../context/AppContext";
import useInitialState from "../hooks/useInitialState";
import Home from "@pages/Home";
import NotFound from "@pages/NotFound";
import Login from "@pages/Login";
import '../scss/styles.scss'


const App = () => {
    const initialState = useInitialState()
    if (!initialState.state.user.id) {
        return (<Login></Login>);
    }
    return (
        <AppContext.Provider value={initialState}>
            <BrowserRouter>
                <Layout>
                    <Switch>
                        <Route exact path="/" component={Home}/>
                        <Route path="/login" component={Login}/>
                        <Route path="*" component={NotFound}/>
                    </Switch>
                </Layout>
            </BrowserRouter>
        </AppContext.Provider>

    );
}

export default App;