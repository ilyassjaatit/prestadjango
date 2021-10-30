import React from 'react'
import SbTopNav from './SbTopNav'
import LayoutSideNav from './LayoutSideNav'
import Footer from './Footer'

const Layout = ({ children }) => {
  return (
    <>
      <SbTopNav />
      <div id='layoutSidenav'>
        <LayoutSideNav />
        <div id='layoutSidenav_content'>
          <main>
            <div className='container-fluid px-4'>
              {children}
            </div>
          </main>
          <Footer />
        </div>
      </div>

    </>
  )
}

export default Layout
