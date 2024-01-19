import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { useEffect } from 'react';


function Applications() {
  let[rec,setRec] = useState([])
  async function showData(){
    await axios.get('http://127.0.0.1:8000/applications/').then((response)=>{
      setRec(response.data)
      console.log(response.data)
    }).catch((error)=>{
      alert('server down.....')
    })
  }
useEffect(()=>{showData()},[])

  return (
    <div className='container'>
        <div className='row'>
              <div class="table-responsive">
                <table className='table table-striped table-dark '>
                    < thead>
                    <tr>
                        <th>USER</th>
                        <th>ADHAAR NO</th>
                        <th>PAN NO</th>
                        <th>EMPLOYEMENT TYPE</th>
                        <th>BUSINESS TITLE</th>
                        <th>BUSINESS TYPE</th>
                        <th>BUSINESS ADDRESS</th>
                        <th>GST REG NO</th>
                        <th>BUSINESS LICENSE NO</th>
                        <th>EXPECTED AVG ANNUAL TURNOVER</th>
                        <th>YEARS OF CURRENT BUSINESS</th>
                        <th>COLLATERAL</th>
                        <th>STATUS</th>
                        <th>APPLICATION TIMESTAMP</th>
                        <th>REMARK</th>
                        <th>CREDIT SCORE</th>
                    </tr>
                    </thead>
                    <tbody>
                    {rec.map((obj)=>{
                            return (
                              <tr>
                                <td>{obj.user}</td>
                                <td>{obj.aadhaar_no}</td>
                                <td>{obj.pan_no}</td>
                                <td>{obj.type_of_employment}</td>
                                <td >{obj.business_title}</td>
                                <td>{obj.business_type}</td>
                                <td>{obj.business_address}</td>
                                <td>{obj.gst_registration_no}</td>
                                <td>{obj.business_license_no}</td>
                                <td>{obj.expected_average_annual_turnover}</td>
                                <td>{obj.years_in_current_business}</td>
                                <td>{obj.collateral}</td>
                                <td>{obj.status}</td>
                                <td>{new Date(obj.application_timestamp).toLocaleString()}</td>
                                <td>{obj.remark}</td>
                                <td>{obj.credit_score}</td>
                              </tr>)}
                    )}
                    </tbody>
                </table>
            </div>
        </div>
  </div>
)}
export default Applications