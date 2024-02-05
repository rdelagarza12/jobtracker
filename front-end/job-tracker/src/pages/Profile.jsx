import { Outlet, useNavigate,} from "react-router-dom"
import { signOut } from "../utilities"



export default function Profile() {
    const navigate = useNavigate()

    const handleSignOut = async () => {
        try {
            const signOutResponse = await signOut()
            if (signOutResponse == "204") {
                localStorage.clear();
                navigate('/')
            }
        } catch (error) {
            console.error('Failed to logout', error)
        }
    }

    return (
        <div className="profile">
            <button className="logoutButton" onClick={handleSignOut}>LOGOUT</button>
            <Outlet />
        </div>
    )
}