import React, { useEffect, useState } from 'react'
import DataTable from 'react-data-table-component'
import { getCustomerList } from '../../hooks/useCustomer'

const CustomerList = () => {
  const [customers, setCustomers] = useState({})
  const [loading, setLoading] = useState(true)
  const [totalRows, setTotalRows] = useState(0)
  const [page, setPage] = useState(1)
  const PER_PAGE = 20
  const handlePageChange = page => {
    setPage(page)
  }

  useEffect(() => {
    setLoading(true)
    getCustomerList(page).then(response => {
      setCustomers(response.data.results)
      setTotalRows(response.data.count)
      setLoading(false)
    })
  }, [page])

  useEffect(() => {
    getCustomerList(false).then(response => {
      setCustomers(response.data.results)
      setTotalRows(response.data.count)
      setLoading(false)
      console.log(response)
    })
  }, [])
  const columns = [
    {
      name: 'Id',
      selector: row => row.id
    },
    {
      name: 'email',
      selector: row => row.email
    }
  ]
  return (
    <DataTable
      title='customer List'
      columns={columns}
      data={customers}
      progressPending={loading}
      paginationRowsPerPageOptions={[PER_PAGE]}
      paginationPerPage={PER_PAGE}
      paginationServer
      paginationTotalRows={totalRows}
      onChangePage={handlePageChange}
      pagination
    />
  )
}

export default CustomerList
