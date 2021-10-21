import React, {useContext, useEffect, useState} from "react";
import DataTable from 'react-data-table-component';
import axios from "axios";
import AppContext from "../../context/AppContext";

async  function getProducts(page=false, state) {
    let API_URL = process.env.REACT_APP_API_ENDPOIN + "products/"
    if (page !== false) {
        API_URL = API_URL + "?page=" + page
    }
    const config = {
            method: 'get',
            url: API_URL,
            headers: {
                'Authorization': 'Token ' + state.auth_token
            }
        };
    const response = await axios(config)
    return response
}

const ProductList = () => {
    const {state} = useContext(AppContext)
    const [products, setProducts] = useState({});
    const [loading, setLoading] = useState(true);
    const [totalRows, setTotalRows] = useState(0);
    const [page, setPage] = useState(1);
    const PER_PAGE = 20;
    const handlePageChange = page => {
        setPage(page)
    };


    useEffect(() => {
        setLoading(true)
        getProducts(page, state).then(response => {
            setProducts(response.data.results)
            setTotalRows(response.data.count)
            setLoading(false)
        })
    }, [page])


    useEffect(() => {
        getProducts(false, state).then(response => {
            setProducts(response.data.results)
            setTotalRows(response.data.count)
            setLoading(false)
            console.log(response)
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
            data={products}
            progressPending={loading}
            paginationRowsPerPageOptions={[PER_PAGE]}
            paginationPerPage={PER_PAGE}
            paginationServer
            paginationTotalRows={totalRows}
            onChangePage={handlePageChange}
            pagination
        />
    );
}
export default ProductList