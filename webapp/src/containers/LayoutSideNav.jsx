import React from 'react'
import { Link } from 'react-router-dom'

const LayoutSideNav = () => {
  return (
    <>
      <div id='layoutSidenav_nav'>
        <nav className='sb-sidenav accordion sb-sidenav-dark' id='sidenavAccordion'>
          <div className='sb-sidenav-menu'>
            <div className='nav'>
              <div className='sb-sidenav-menu-heading'>Core</div>
              <Link className='nav-link' to='/'>
                <div className='sb-nav-link-icon'><i className='fas fa-tachometer-alt' /></div>
                Dashboard
              </Link>
              <div className='sb-sidenav-menu-heading'>Catalog</div>
              <a
                className='nav-link collapsed' href='#' data-bs-toggle='collapse'
                data-bs-target='#collapseLayouts' aria-expanded='false'
                aria-controls='collapseLayouts'
              >
                <div className='sb-nav-link-icon'><i className='fas fa-columns' /></div>
                Products
                <div className='sb-sidenav-collapse-arrow'><i className='fas fa-angle-down' />
                                    </div>
              </a>
              <div
                className='collapse' id='collapseLayouts' aria-labelledby='headingOne'
                data-bs-parent='#sidenavAccordion'
              >
                <nav className='sb-sidenav-menu-nested nav'>
                  <Link className='nav-link' to='products'>Products</Link>
                  <Link className='nav-link' to=''>Add Products</Link>
                </nav>
              </div>

              <div className='sb-sidenav-menu-heading'>Statistics</div>
              <a className='nav-link' href=''>
                <div className='sb-nav-link-icon'><i className='fas fa-chart-area' /></div>
                Sales
              </a>
            </div>
          </div>
          <div className='sb-sidenav-footer'>
            <div className='small'>Logged in as:</div>
            admin
          </div>
        </nav>
      </div>
    </>
  )
}

export default LayoutSideNav
