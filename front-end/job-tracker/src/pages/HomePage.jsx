import Login from "../components/Login"

export default function HomePage() {
    return (
        <>
            <div className="homePage">
                <h1>JOB PILOT</h1>
                <div className="homePageLoginDiv">
                    <div className="login">
                        <Login />
                    </div>
                </div>
            </div>
        </>
    )
}