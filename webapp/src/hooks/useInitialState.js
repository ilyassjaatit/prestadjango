import { useState } from 'react'

const userIsLogged = () => {
  const user = JSON.parse(window.sessionStorage.getItem('user'))
  if (user) {
    return user
  }
  return {}
}

const initialState = {
  app_name: process.env.REACT_APP_NAME,
  user: userIsLogged(),
  auth_token: window.localStorage.getItem('auth_token')
}

const useInitialState = () => {
  const [state, setState] = useState(initialState)
  const addUser = (payload) => {
    setState({ ...state, user: payload })
  }
  const addAuthToken = (payload) => {
    setState({ ...state, auth_token: payload })
  }
  return {
    state,
    addUser,
    addAuthToken
  }
}

export default useInitialState
