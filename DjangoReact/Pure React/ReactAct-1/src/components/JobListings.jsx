import React, { useEffect, useState } from 'react'
import jobs from '../jobs.json';
import JobListing from './JobListing';

// const JobListings = ({ isHome = false }) => {
//     // const JobListings = isHome ? jobs.slice(0,3):jobs;
//     const [jobs, setJobs] = useState([]);
//     const [loading, setLoading] = useState([]);
//     useEffect(() => {
//         const fetchjobs = async () => {
//             try {
//                 const res = await fetch('http://localhost:8000/jobs')
//                 const data = await res.json();
//                 setJobs(data);

//             } catch (error) {
//                 console.log("Error Fetching Data", error);

//             } finally {
//                 setLoading(false);

//             }
//         };
//         fetchjobs();
//     }, []);
const JobListings = ({ isHome = false }) => {
    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(true);
  
    useEffect(() => {
      const fetchJobs = async () => {
        const apiUrl = isHome ? '/api/jobs?_limit=3' : '/api/jobs';
        try {
          const res = await fetch(apiUrl);
          const data = await res.json();
          setJobs(data);
        } catch (error) {
          console.log('Error fetching data', error);
        } finally {
          setLoading(false);
        }
      };
  
      fetchJobs();
    }, []);
    return (
        <section className="bg-blue-50 px-4 py-10">
            <div className="container-xl lg:container m-auto">
                <h2 className="text-3xl font-bold text-indigo-500 mb-6 text-center">
                    {isHome ? "Recent Jobs" : "Browse Jobs"}
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    {/* <!-- Job Listing 1 --> */}
                    {loading ? (<h1>Loading...</h1>) : (<>
                        {jobs.map((jobs) =>
                        (

                            <JobListing key={jobs.id} job={jobs} />

                        ))}
                    </>)}


                    {/* <!-- Job Listing 2 --> */}


                </div>
            </div>
        </section >
    )
}

export default JobListings
