import { useState } from "react";
import { updateSingleJob } from "../utilities";


export default function Job({keyProp, jobObject}) {
    const [updateJob, setUpdateJob] = useState(false)
    const [updatingData, setUpdatingData] = useState({})

    const {id, job_name, company_name, date_applied, application_status, contact_info, job_description } = jobObject;
    const tracker_id = localStorage.getItem('tracker')


    const [jobName, setJobName] = useState(job_name)
    const [companyName, setCompanyName] = useState(company_name)
    const [dateApplied, setDateApplied] = useState(date_applied)
    const [applicationStatus, setApplicationStatus] = useState(application_status)
    const [contactInfo, setContactInfo] = useState(contact_info)
    const [jobDescription, setJobDescription] = useState(job_description)
    const updateChange = (setter) => (e) => {
        const {name, value} = e.target;
        setUpdatingData((prevData) => ({...prevData, [keyProp] : {...prevData[keyProp], [name] : value}}))
        setUpdateJob(true)
        setter(value)
    }

    const handleSaveUpdate = async (e) => {
        const updatingJobData = updatingData[keyProp]
        try {
            await updateSingleJob(updatingJobData, tracker_id, keyProp)
            setUpdateJob(false)

        } catch (error) {
            console.error('Failed to handle saveUpdate')
            window.alert('Improper Input, failed to update')
        }
    }

    return (
        <div>
            <input type="text" name="job_name" placeholder="Job Title" value={jobName} onChange={updateChange(setJobName)}/>
            <input type="text" name="company_name" placeholder="Company Name" value={companyName} onChange={updateChange(setCompanyName)}/>
            <input type="date" name="date_applied" value={dateApplied} onChange={updateChange(setDateApplied)}/>
            <select name="application_status" className={applicationStatus.toLowerCase()} value={applicationStatus} onChange={updateChange(setApplicationStatus)}>
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
            <input type="text" name="contact_info" placeholder="Contact Information" value={contactInfo} onChange={updateChange(setContactInfo)}/>
            <input type="text" name="job_description" placeholder="Job Description" value={jobDescription} onChange={updateChange(setJobDescription)}/>
            {updateJob && <button onClick={handleSaveUpdate}>Update Job</button>}
        </div>
    )
}