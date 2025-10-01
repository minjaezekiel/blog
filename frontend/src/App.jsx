import { useState,useEffect } from 'react'
import axios from "axios"
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

const base_url = 'http://127.0.0.1:8000/'

function App() {
  const [data, setData] = useState([])
  const [loading,setLoading] = useState(true)
  const [error,setError] = useState(null)

  {/* using axios and useEffect to get post data from api  */}
useEffect(() => {
  axios.get(`${base_url}home`)
    .then((res) => {
      setData(res.data)
      setLoading(false)
    })
    .catch((err) => {
      setError(err.message)
      setLoading(false)
    })
}, [])

 
  if (loading) return <p>Loading posts...</p>
  if (error) return <p>Error: {error}</p>
  return (
    <>
     <h1>Latest Posts</h1>
     {data.length === 0 ?(<p>No posts found</p>)
     :
     (
        <ul>
          {data.map((post) => (
            <li key={post.id}>
              <h2>{post.title}</h2>
              <p>{post.content}</p>
              <small>Created: {new Date(post.created).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      )}
    </>
  )
}

export default App
