import axios from "axios";


async function _prepareGetProduct(url) {
    const auth_token = localStorage.getItem("auth_token")
    const config = {
        method: 'get',
        url: url,
        headers: {
            'Authorization': 'Token ' + auth_token
        }
    };
    return axios(config)
}

async function getProductDetail(id) {
    let API_URL = process.env.REACT_APP_API_ENDPOIN + "products/" + id + "/";
    return _prepareGetProduct(API_URL)
}


async function getProductList(page = false) {
    let API_URL = process.env.REACT_APP_API_ENDPOIN + "products/";
    if (page !== false) {
        API_URL = API_URL + "?page=" + page
    }
    return _prepareGetProduct(API_URL)
}


export {getProductList, getProductDetail};