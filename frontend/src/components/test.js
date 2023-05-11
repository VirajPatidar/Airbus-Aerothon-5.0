import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Test = () => {

    const [data, setData] = useState(null);

    useEffect(() => {
        axios.get(`http://localhost:8000/api/test`)
            .then((res) => {
                console.log(res);
                setData(res.data);
            })
            .catch(err => {
                console.log(err)
            });
    }, [])

    return (
        <>
            <h1>{data && data.resp}</h1>
        </>
    );
}

export default Test;