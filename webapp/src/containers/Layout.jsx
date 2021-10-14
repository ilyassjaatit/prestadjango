import React from "react";
import SbTopNav from "./SbTopNav";
import LayoutSideNav from "./LayoutSideNav";

const Layout = ({children}) => {
    return (
        <React.Fragment>
            <SbTopNav/>
            <div id="layoutSidenav">
                <LayoutSideNav/>
                <div id="layoutSidenav_content">
                    <main>
                        <div className="container-fluid px-4">
                            {children}
                        </div>
                    </main>
                    <footer className="py-4 bg-light mt-auto">
                        <div className="container-fluid px-4">
                            <div className="d-flex align-items-center justify-content-between small">
                                <div className="text-muted">Copyright &copy; Ilyass Jaatit 2021</div>
                            </div>
                        </div>
                    </footer>
                </div>
            </div>

        </React.Fragment>
    );
}

export default Layout;