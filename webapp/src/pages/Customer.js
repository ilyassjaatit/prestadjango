import { Route, useRouteMatch, Link } from 'react-router-dom'
import { CustomerDetail, CustomerList } from '../containers/customer'

const Customer = () => {
  const { path } = useRouteMatch()
  return (
    <>
      <Route path={`${path}/:customerId`} component={CustomerDetail} />
      <Route exact path={path}>
        <h1 className='mt-4'>Products</h1>
        <ol className='breadcrumb mb-4'>
          <li className='breadcrumb-item'><Link to='/'>Home</Link></li>
          <li className='breadcrumb-item active'>Customers</li>
        </ol>
        <CustomerList />
      </Route>
    </>
  )
}

export default Customer
