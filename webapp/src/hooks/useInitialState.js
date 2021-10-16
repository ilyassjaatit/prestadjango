import {useState} from "react"

const initialState = {
    user: {}
}

const useInitialState = () => {
    const [state, setState] = useState(initialState)
    const addUser = (payload) => {
        setState({...state, user: payload})
    }

    return {
        state,
        addUser
    }
}

export default useInitialState;