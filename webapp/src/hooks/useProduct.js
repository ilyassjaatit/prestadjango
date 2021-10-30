import axios from 'axios'

async function _prepareGetProduct (url) {
  const authToken = window.localStorage.getItem('auth_token')
  const config = {
    method: 'get',
    url: url,
    headers: {
      Authorization: 'Token ' + authToken
    }
  }
  return axios(config)
}

async function getProductDetail (id) {
  const API_URL = process.env.REACT_APP_API_ENDPOIN + 'products/' + id + '/'
  return _prepareGetProduct(API_URL)
}

async function getProductList (page = false) {
  let API_URL = process.env.REACT_APP_API_ENDPOIN + 'products/'
  if (page !== false) {
    API_URL = API_URL + '?page=' + page
  }
  return _prepareGetProduct(API_URL)
}

export { getProductList, getProductDetail }
