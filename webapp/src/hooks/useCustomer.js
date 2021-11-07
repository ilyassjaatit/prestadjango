import axios from 'axios'

async function _prepareGetCustomer (url) {
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

async function getCustomerDetail (id) {
  const API_URL = process.env.REACT_APP_API_ENDPOIN + 'customers/' + id + '/'
  return _prepareGetCustomer(API_URL)
}

async function getCustomerList (page = false) {
  let API_URL = process.env.REACT_APP_API_ENDPOIN + 'customers/'
  if (page !== false) {
    API_URL = API_URL + '?page=' + page
  }
  return _prepareGetCustomer(API_URL)
}

export { getCustomerList, getCustomerDetail }
