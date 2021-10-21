import React from "react";
import "../scss/pages/_error.scss"
import {Link} from "react-router-dom";
const NotFound = () => {
    return (
        <div id="layoutError">
            <div id="layoutError_content">
                <main>
                    <div className="container">
                        <div className="row justify-content-center">
                            <div className="col-lg-6">
                                <div className="text-center mt-4">
                                    <h1 className="display-1">404</h1>
                                    <p className="lead">404 Not Found</p>
                                    <p>page not found</p>
                                    <Link to="/">
                                        <i className="fas fa-arrow-left me-1"></i>
                                        Return to Dashboard
                                    </Link>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
            <div id="layoutError_footer">
                <footer className="py-4 bg-light mt-auto">
                    <div className="container-fluid px-4">
                        <div className="d-flex align-items-center justify-content-between small">
                            <div className="text-muted">Copyright &copy; ilyass jaatit</div>
                        </div>
                    </div>
                </footer>
            </div>
        </div>
    );
}

export default NotFound;