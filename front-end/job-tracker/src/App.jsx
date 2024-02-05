import './App.css'
import { AppProvider } from './context'
import HomePage from './pages/HomePage'
import { Outlet } from 'react-router-dom'
import Profile from './pages/Profile'

export default function App() {
  return (
    <AppProvider>
      <Outlet />
    </AppProvider>
  )
}


