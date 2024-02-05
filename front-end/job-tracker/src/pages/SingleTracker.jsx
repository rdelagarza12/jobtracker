import { Link } from "react-router-dom"
import Tracker from "../components/Tracker"

export default function SingleTracker() {



    return (
        <div className="singleTrackerPage">
            <Link to='/profile'>
                <button className="returnButton">RETURN TO LIBRARY</button>
            </Link>
            <Tracker />
        </div>
    )
}