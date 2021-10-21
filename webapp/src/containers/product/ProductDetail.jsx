import React, {useEffect, useState} from "react";
import {useParams, Redirect} from "react-router-dom";
import Spinner from "react-bootstrap/Spinner";
import {getProductDetail} from "../../hooks/useProduct";
import NotFound from "../../pages/NotFound";

const ProductDetail = () => {
    const {productId} = useParams();
    const [product, setProduct] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);
    useEffect(() => {
        getProductDetail(productId).then(response => {
            setProduct(response.data)
            setLoading(false)
        }).catch(error => {
            console.log(error)
            setError(true)
        })
    }, []);

    if (error) {
        return (<Redirect to="/404-not-found"/>)
    }

    if (loading) {
        return (
            <Spinner animation="border" role="status">
                <span className="sr-only">Loading...</span>
            </Spinner>
        );
    } else {
        return (<div>
            <h1>{product.name}</h1>
        </div>);
    }

}

export default ProductDetail
