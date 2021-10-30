import React, { useEffect, useState } from 'react'
import DataTable from 'react-data-table-component'
import { getProductList } from '../../hooks/useProduct'

const ProductList = () => {
  const [products, setProducts] = useState({})
  const [loading, setLoading] = useState(true)
  const [totalRows, setTotalRows] = useState(0)
  const [page, setPage] = useState(1)
  const PER_PAGE = 20
  const handlePageChange = page => {
    setPage(page)
  }

  useEffect(() => {
    setLoading(true)
    getProductList(page).then(response => {
      setProducts(response.data.results)
      setTotalRows(response.data.count)
      setLoading(false)
    })
  }, [page])

  useEffect(() => {
    getProductList(false).then(response => {
      setProducts(response.data.results)
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
      name: 'Name',
      selector: row => row.name
    },
    {
      name: 'Sku',
      selector: row => row.sku
    }
  ]

  return (
    <DataTable
      title='Product List'
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
  )
}
export default ProductList
