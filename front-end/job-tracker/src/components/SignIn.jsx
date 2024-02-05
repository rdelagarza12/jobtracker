import { useState } from "react";
import { useAppContext } from "../context";
import { api } from "../utilities";
import { useNavigate } from 'react-router-dom';


export default function SignIn() {

    const {loggedIn, setLoggedIn} = useAppContext()
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate()


    const logInUser = async (e) => {
        e.preventDefault()
        try {
            const response = await api.post('users/login/', {
                email: username,
                password: password
            })
            let token = response.data.token;
            localStorage.setItem("token", token)
            setLoggedIn(true)
            navigate('profile');
        } catch (error) {
            window.alert('Invalid Username or Password, please try again')
        }
    }




    return (
        <div className="signIn">
            <h2>SIGN IN</h2>
            <form className="signInForm" onSubmit={logInUser}>
                <input
                type="email"
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Email Address"
                />
                <input
                type="password"
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                />
                <button type="submit">SIGN IN</button>
            </form>
        </div>
    )
}