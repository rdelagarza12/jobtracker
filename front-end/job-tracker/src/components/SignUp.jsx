import { useState } from "react"
import { api } from "../utilities"
import { useAppContext } from "../context"
import { useNavigate } from "react-router-dom"

export default function SignUp() {

    const {loggedIn, setLoggedIn} = useAppContext()
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate();

    const signUpUser = async (e) => {
        e.preventDefault()
        try {
            const response = await api.post('users/signup/', {
                email : username,
                password: password,
            })
            let token = response.data.token
            localStorage.setItem("token", token);
            setLoggedIn(true);
            navigate('profile');
        } catch (error) {
            window.alert('The Username or Password is either taken or it is invalid')
        }

    }

    return (
        <div className="signIn">
            <form className="signInForm" onSubmit={signUpUser}>
                <h3>CREATE YOUR ACCOUNT</h3>
                <input
                type="email"
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Email Address"
                />
                <input 
                type="password"
                onChange={(e) => setPassword(e.target.value)}
                placeholder="password"
                />
                <button type="submit">SIGN UP</button>
            </form>
        </div>
    )
}