import React, { useEffect, useState } from 'react'
import { useParams, Redirect } from 'react-router-dom'
import Spinner from 'react-bootstrap/Spinner'
import { getCustomerDetail } from '../../hooks/useCustomer'

const CustomerDetail = () => {
  const { customerId } = useParams()
  const [customer, setCustomer] = useState({})
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)
  useEffect(() => {
    getCustomerDetail(customerId).then(response => {
      setCustomer(response.data)
      setLoading(false)
    }).catch(error => {
      console.log(error)
      setError(true)
    })
  }, [])
  if (error) {
    return (<Redirect to='/404-not-found' />)
  }

  if (loading) {
    return (
      <Spinner animation='border' role='status'>
        <span className='sr-only'>Loading...</span>
      </Spinner>
    )
  } else {
    return (
      <div>
        <h1>{customer.email}</h1>
      </div>
    )
  }
}

export default CustomerDetail
