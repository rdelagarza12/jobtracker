import React, { useEffect, useState } from 'react';
import { fetchLibrary, createTracker, deleteSingleTracker} from '../utilities';
import { useAppContext } from '../context';
import { Link } from 'react-router-dom';

export default function Library() {
const [addTracker, setAddTracker] = useState(false)
const [deleteTracker, setDeleteTracker] = useState(false)
// const [updatingTrackerName, setUpdatingTrackerName] = useState(false)

  const {library, setLibrary} = useAppContext()




  useEffect(() => {
    // Fetch library data from the backend when the component mounts
    fetchLibrary(setLibrary);
  }, []); // Empty dependency array ensures the effect runs only once on mount


  const handleClick = (itemId) => {
    localStorage.setItem('tracker', itemId)
  }

  const handleDeleteTracker = async (item_id) => {
    try {
      const response = await deleteSingleTracker(item_id)
    } 
    catch (error) {
      console.error('Failed to delete tracker', error)
    }
    setLibrary(prevLibrary => prevLibrary.filter(tracker => tracker.id !== item_id))
    setDeleteTracker(false)
  }

  const saveTracker = async (e) => {
    e.preventDefault()
    const newTrackerName = e.target.trackername.value
    const newTrackerObject = await createTracker(newTrackerName)
    setLibrary(prevLibrary => [...prevLibrary, newTrackerObject])
    setAddTracker(false)
  }


  return (
    <div className='trackerLibrary'>
      <h2>Library</h2>
      <ol>
        {library.map((item) => (
          <li key={item.id}>
          <Link to='/profile/tracker' onClick={() => handleClick(item.id)}>
            <div className="trackers">
              <strong>{item.name}</strong>{' '}-{' '}<strong>Applied Jobs:</strong> {item.applied_jobs} 
            </div>
          </Link>
          {deleteTracker && <button onClick={() => handleDeleteTracker(item.id)}>DELETE</button>}
          {/* {updatingTrackerName && <button>CHANGE NAME</button>} */}
        </li>
        ))}
      </ol>
      {addTracker && (<form onSubmit={saveTracker}>
                        <input name ="trackername" placeholder='Tracker Name'/>
                        <button type="submit">SAVE</button>
                      </form>)
      }
      <div className="buttonContainer">
      {addTracker ? <button className="addTrackerButton" onClick={() => setAddTracker(false)}>CANCEL TRACKER</button> 
      : <button className="addTrackerButton"onClick={() => setAddTracker(true)}>ADD TRACKER</button>}
        {!deleteTracker ? <button className="deleteTrackerButton" onClick={() => setDeleteTracker(true)}>DELETE TRACKER</button>
        : <button className="deleteTrackerButton" onClick={() => setDeleteTracker(false)}>CANCEL DELETE</button>}
        {/* {!updatingTrackerName ? <button onClick={() => setUpdatingTrackerName(true)}>UPDATE NAMES</button> 
        : <button onClick={() => setUpdatingTrackerName(false)}>CANCEL UPDATE</button>} */}
      </div>
    </div>
  );
}

