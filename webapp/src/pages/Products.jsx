import React, {useContext, useEffect, useState} from "react";
import {Link} from "react-router-dom";
import ProductList from '../containers/product/ProductList';

const Products = () => {
    return (
        <React.Fragment>
            <h1 className="mt-4">Products</h1>
            <ol className="breadcrumb mb-4">
                <li className="breadcrumb-item"><Link to="/">Home</Link></li>
                <li className="breadcrumb-item active">Products</li>
            </ol>
            <ProductList/>
        </React.Fragment>
    );
}

export default Products;