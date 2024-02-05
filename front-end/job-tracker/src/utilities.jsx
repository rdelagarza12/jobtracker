import React from "react"
import axios from "axios";

export const api = axios.create({
    baseURL:"http://127.0.0.1:8000/api/"
})

export const defaultDate = () => {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0'); // Month is zero-based
    const day = String(today.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  };


export const fetchLibrary = async (setLibrary) => {
    try {
        const response = await api.get('library/', {
            headers: {
                'Authorization' : `Token ${localStorage.getItem('token')}`
            }
        })
        setLibrary(response.data.active_trackers)
    } catch (error) {
        console.error('Error fetching library data: ', error)
    }
};

// GRAB A SINGLE TRACKER
export const fetchTracker = async (setTracker, setTrackerName, tracker_id) => {
    try {
        const response = await api.get(`trackers/${tracker_id}/`, {
            headers: {
                'Authorization' : `Token ${localStorage.getItem('token')}`
            }
        })
        setTracker(response.data.applied_jobs)
        setTrackerName(response.data.name)
    } catch (error) {
        console.error("Failed to fetch Tracker", error)
    }
}

// CREATE A NEW TRACKER 
export const createTracker = async (tracker_name) => {

    try {
        const response = await api.post(`library/`,
        {
            name : tracker_name
        },
        {
            headers: {
                'Authorization' : `Token ${localStorage.getItem('token')}`
            }
        })
        return response.data
    } catch (error) {
        console.error('Failed to create a new Tracker', error)
    }
}

// DELETE A TRACKER
export const deleteSingleTracker = async (tracker_id) => {
    try {
        const response = await api.delete(`library/${tracker_id}/`, {
            headers : {
                'Authorization' : `Token ${localStorage.getItem('token')}`
            }
        })
        return response
    } catch (error) {
        console.error('Failed to Delete Tracker', error)
    }
}

// GRAB ONLY ONE JOB
export const fetchJob = async ( job_id) => {
    try {
        const response = await api.post(`jobs/${job_id}/`, {
            headers: {
                'Authorization' : `Token ${localStorage.getItem('token')}`
            }
        })
        return response
    } catch (error) {
        console.error('Failed to fetch job', error)
    }
}

// CREATE A SINGLE JOB
export const createJob = async (tracker_id, job_data) => {
    try {
        const response = await api.post(
            `trackers/${tracker_id}/`,
            {
                job_name: job_data.job_name,
                company_name: job_data.company_name,
                job_description: job_data.job_description,
                date_applied: job_data.date_applied,
                contact_info: job_data.contact_info,
                application_status: job_data.application_status
            },
            {
                headers: {
                    Authorization: `Token ${localStorage.getItem('token')}`
                }
            }
        ); return response
    } catch (error) {
        console.error('Failed to Create Job', error);
    }
};

// UPDATE A JOB
export const updateSingleJob = async (job_data,tracker_id, job_id) => {
    try {
        const response = await api.put(`trackers/${tracker_id}/${job_id}/`, 
        {
            job_name : job_data.job_name,
            company_name : job_data.company_name,
            date_applied : job_data.date_applied,
            application_status : job_data.application_status,
            contact_info : job_data.contact_info,
            job_description : job_data.job_description
        },
        {
            headers : {
                'Authorization' : `Token ${localStorage.getItem('token')}`
            }
        })
        return response
    } catch (error) {
        console.error('Failed to update Job', error)
    }
}

// DELETE A JOB
export const deleteSingleJob = async (tracker_id, job_id) => {
    try {
        const response = await api.delete(`trackers/${tracker_id}/${job_id}/`, {
            headers : {
                'Authorization' : `Token ${localStorage.getItem('token')}`
            }
        })
        return response
    } catch (error) {
        console.error('Failed to Delete Job', error)
    }

}

// SIGN OUT

export const signOut = async () => {
    try {
        const response = await api.post(
            'users/logout/',
            {},
            {
                headers: {
                    Authorization: `Token ${localStorage.getItem('token')}`
                }
            }
        );
        return response.status;
    } catch (error) {
        console.error('Failed to Sign out', error);
        throw error; // Optionally, you can re-throw the error to handle it elsewhere
    }
};