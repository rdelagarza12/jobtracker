import { useEffect, useState } from "react";
import { useAppContext } from "../context";
import { fetchTracker, createJob, defaultDate, deleteSingleJob} from "../utilities";
import Job from "./Job";

export default function Tracker() {
    const [formData, setFormData] = useState({
        "job_name" : "",
        "company_name" : "",
        "date_applied" : defaultDate(),
        "job_description" : "",
        "contact_info" : "",
        "application_status" : "",

    })
    const tracker_id = localStorage.getItem('tracker')


    // USE STATES TO TRACK WHETHER IM ADDING A NEW JOB OR DELETING ONE
    const [addJob, setAddJob] = useState(false)    
    const [deleteJob, setDeleteJob] = useState(false)
    const [updatingJob, setUpdatingJob] = useState(false)


    // CONTEXT IMPORTED TO KEEP TRACKE OF WHAT TRACKER IM USING AND THE NAME, SO IT PERSISTS WHEN I REFRESH
    const {tracker, setTracker, trackerName, setTrackerName } = useAppContext();


    // LOADS THE INITIAL TRACKER BY GRABBING THE ID FROM LOCALSTORAGE
    useEffect(() => {
        // const tracker_id = localStorage.getItem('tracker')
        fetchTracker(setTracker, setTrackerName, tracker_id);


    }, [tracker_id]); // Refetch tracker data when trackerId changes


    // THIS METHOD ALLOWS ME UP TO UPDATE MY FORM INPUTS REALS TIME
    const handleFormChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevFormData) => ({...prevFormData, [name]: value}));
    };


    // LOGIC TO USE A POST METHOD TO CREATE A NEW JOB
    const createJobApplication = async (e) => {
        e.preventDefault();

        try {
            const jobId = await createJob(tracker_id, formData);
            const newJobObject = {...formData, id: jobId}
            setTracker((prevTracker) => [...prevTracker, newJobObject]);
            setFormData({
                "job_name": "",
                "company_name": "",
                "date_applied": defaultDate(),
                "job_description": "",
                "contact_info": "",
                "application_status": "",
            });
            setAddJob(false)
        } catch (error) {
            console.error('Failed to create job', error);
        }
    };

    // DELETES A SINGLE JOB
    const handleDeleteJob = async (jobId) => {
        let job_endpoint
        if (typeof jobId === 'object' && jobId !== null) {
            job_endpoint = jobId.data
        } else {
            job_endpoint = jobId
        }
        try {
            await deleteSingleJob(tracker_id, job_endpoint);
            setTracker(prevTracker => prevTracker.filter(job => job.id !== jobId));
        } catch (error) {
            console.error('Failed to delete job', error);
        }
    };
// <----------------------------------------- ACTUAL COMPONENT --------------------------- >
    return (
        <div>
                <div className="tracker">
                    <h1>{trackerName}</h1>
                    <ol>
                        {tracker.map((job, index) => (
                            <li key={index} className="job">
                                <div className="jobAndDeleteButtonContainer">
                                    <Job key={job.id} keyProp={job.id} jobObject={job} onDelete={() => handleDeleteJob(job.id)}/>
                                    {updatingJob && <button>Update</button>}
                                    {deleteJob && <button className="deleteJobButton" onClick={() => handleDeleteJob(job.id)}>DELETE</button>}
                                </div>
                            </li>
                        ))}
                    </ol>
                </div>
                <div className="addOrDeleteJobContainer">
                    {addJob && (<>
                    <form onSubmit={createJobApplication}>
                        <input type="text" name="job_name" placeholder="Job Title" value={formData.job_name} onChange={handleFormChange}/>
                        <input type="text" name="company_name" placeholder="Company Name" value={formData.company_name} onChange={handleFormChange}/>
                        <input type="date" name="date_applied" value={formData.date_applied} onChange={handleFormChange}/>
                        <select name="application_status" className={formData.application_status.toLowerCase()} value={formData.application_status} onChange={handleFormChange}>
                            <option className="applied">
                                APPLIED
                            </option>
                            <option className="rejected">
                                REJECTED
                            </option>
                            <option className="under-review">
                                UNDER-REVIEW
                            </option>
                            <option className="interviewing">
                                INTERVIEWING
                            </option>
                            <option className="accepted">
                                ACCEPTED
                            </option>
                        </select>
                        <input type="text" name="contact_info" placeholder="Contact Information" value={formData.contact_info} onChange={handleFormChange}/>
                        <input type="text" name="job_description" placeholder="Job Description" value={formData.job_description} onChange={handleFormChange}/>
                        <button className="saveButton" type="submit">SAVE</button>
                    </form>
                    </>)}
                    {addJob && <button onClick={() => setAddJob(false)} className="addJobButton">CANCEL</button>}
                    { !addJob && !deleteJob &&<button onClick={() => setAddJob(true)} className="addJobButton">ADD</button>}
                    {deleteJob && <button onClick={() => setDeleteJob(false)} className="deleteJobButton">STOP DELETING</button>}
                    {!deleteJob && !addJob && <button onClick={() => setDeleteJob(true)} className="deleteJobButton">DELETE</button>}
                </div>
        </div>
    );
}
