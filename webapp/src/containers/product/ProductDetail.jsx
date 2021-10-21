import React, {useContext, useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import axios from "axios";
import AppContext from "../../context/AppContext";

const ProductDetail = () => {
    let {productId} = useParams();
    console.log(productId)
    return (<div>
        <h1>test </h1>

    </div>);
}

export default ProductDetail
