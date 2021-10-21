import React, {useContext, useEffect, useState} from "react";
import DataTable from 'react-data-table-component';
import axios from "axios";
import AppContext from "../context/AppContext";

const API_URL = process.env.REACT_APP_API_ENDPOIN + "products/"

const ProductList = () => {
    const {state} = useContext(AppContext)
    const [productsData, setProductsData] = useState({})
    useEffect(() => {
        const config = {
            method: 'get',
            url: API_URL,
            headers: {
                'Authorization': 'Token ' + state.auth_token
            }
        };
        axios(config).then(response => {
            setProductsData(response.data)
        })

    }, [])
    const columns = [
        {
            name: 'Id',
            selector: row => row.id,
        },
        {
            name: 'Name',
            selector: row => row.name,
        },
        {
            name: 'Sku',
            selector: row => row.sku,
        },
    ];

    return (
        <DataTable
            title="Product List"
            columns={columns}
            data={productsData.results}
            pagination
        />
    );
}
export default ProductList