import React, {useState, useRef, useContext, Fragment} from "react";
import Footer from "../containers/Footer";
import "@scss/pages/_login.scss"
import Alert from 'react-bootstrap/Alert'
import AppContext from "../context/AppContext";
import {auth} from "../hooks/useAuth"


const LoginErrors = ({httpError}) => {
    if (httpError) {
        if (httpError.message) {
            return (
                <Alert variant="danger">
                    {httpError.message}
                </Alert>
            )
        }
    }
    return (<Fragment></Fragment>)

}

const Login = () => {
    const { addUser, addAuthToken } = useContext(AppContext)
    const [httpError, setHttpError] = useState()

    const form = useRef(null)
    const handleSubmit = (event) => {
        event.preventDefault()
        const formData = new FormData(form.current)
        const data = {
            username: formData.get('username'),
            password: formData.get('password'),
        }
        auth(data, setHttpError, addUser, addAuthToken)


    }
    return (
        <React.Fragment>
            <div id="layoutAuthentication">
                <div id="layoutAuthentication_content">
                    <main>
                        <div className="container">
                            <div className="row justify-content-center">
                                <div className="col-lg-5">
                                    <div className="card shadow-lg border-0 rounded-lg mt-5">
                                        <div className="card-header"><h3
                                            className="text-center font-weight-light my-4">Login</h3></div>
                                        <div className="card-body">
                                            <form action="/" ref={form}>
                                                <div className="form-floating mb-3">
                                                    <input className="form-control" name="username" type="text"
                                                           placeholder="Your username"/>
                                                    <label htmlFor="username">Username</label>
                                                </div>
                                                <div className="form-floating mb-3">
                                                    <input className="form-control" name="password" type="password"
                                                           placeholder="Password"/>
                                                    <label htmlFor="password">Password</label>
                                                </div>
                                                <div
                                                    className="d-flex align-items-center justify-content-between mt-4 mb-0">
                                                    <button type="submit" onClick={handleSubmit}
                                                            className="btn btn-primary">Login
                                                    </button>
                                                </div>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </main>
                </div>
                <div id="layoutAuthentication_footer">
                    <Footer></Footer>
                </div>
            </div>

        </React.Fragment>
    );

}

export default Login