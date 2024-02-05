import { useState } from "react"
import SignIn from "./SignIn"
import SignUp from "./SignUp"



export default function Login() {
    const [login, setLogin] = useState(false)
    const [signup, setSignup] = useState(false)

    return (
        <div className="login">
            {!login && !signup && (
                            <div>
                                <h2>
                                    Already a User?
                                </h2>
                                <button className="loginButtons" onClick={() => setLogin(true)}>LOG IN</button>
                                <h2>
                                    Or create an account
                                </h2>
                                <button className="loginButtons" onClick={() => setSignup(true)}>SIGN UP</button>
                            </div>
            )}
            {login && <SignIn />}
            {signup && <SignUp />}
            {(login || signup) && (<button className="loginReturn" onClick={(e) => {setLogin(false); setSignup(false)}}>RETURN</button>)}

        </div>
    )
}