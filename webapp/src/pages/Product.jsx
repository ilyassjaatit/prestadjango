import React, {useContext, useEffect, useState} from "react";
import {Route, useRouteMatch} from "react-router-dom";
import {Link} from "react-router-dom";
import {ProductList, ProductDetail} from '../containers/product';

const Product = () => {
    const {path} = useRouteMatch();
    return (
        <React.Fragment>
            <Route path={`${path}/:productId`} component={ProductDetail}/>
            <Route exact path={path}>
                <h1 className="mt-4">Products</h1>
                <ol className="breadcrumb mb-4">
                    <li className="breadcrumb-item"><Link to="/">Home</Link></li>
                    <li className="breadcrumb-item active">Products</li>
                </ol>
                <ProductList/>
            </Route>
        </React.Fragment>
    );
}

export default Product;