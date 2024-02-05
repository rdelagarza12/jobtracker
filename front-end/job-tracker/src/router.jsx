import {createBrowserRouter} from "react-router-dom";
import App from "./App";
import Profile from "./pages/Profile";
import HomePage from "./pages/HomePage";
import Library from "./components/Library";
import SingleTracker from "./pages/SingleTracker";


const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />
            },
            {
                path: "profile",
                element: <Profile />,
                children: [
                    {
                        index: true,
                        element: <Library />
                    },
                    {
                        path: 'tracker',
                        element: <SingleTracker />
                    }
                ]
            },
        ]
    }
])

export default router