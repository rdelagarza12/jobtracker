import { createContext, useContext, useState, useRef } from "react";


const appContext = createContext(null)

export const AppProvider = ({children}) => {
    const [loggedIn, setLoggedIn] = useState(false);
    const [library, setLibrary] = useState([]);
    const [tracker, setTracker] = useState([]);
    const [trackerId, setTrackerId] = useState([]);
    const [trackerName, setTrackerName] = useState("");
    const [job, setJob] = useState([]);


    return (
    <appContext.Provider value={{
        loggedIn, setLoggedIn,
        library, setLibrary,
        tracker, setTracker,
        trackerId, setTrackerId,
        trackerName, setTrackerName,
        job, setJob
    }}>
        {children}
    </appContext.Provider>
    )
}

export const useAppContext = () => {
    return useContext(appContext)
}