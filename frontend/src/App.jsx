import { useState,useEffect, useCallback } from 'react'
import axios from "axios"
import CreatePost from './components/create_post'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


const base_url = 'http://127.0.0.1:8000/'

function App() {
  const [data, setData] = useState([])
  const [loading,setLoading] = useState(true)
  const [error,setError] = useState(null)

  // ✅ useCallback to prevent redefining fetchPosts on every render
  const fetchPosts = useCallback(async () => {
    try {
      const res = await axios.get(`${base_url}home`);
      setData(res.data);
      setError(null);
    } catch (err) {
      console.error("Error fetching posts:", err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  // ✅ Fetch posts initially + refresh every 15 seconds
  useEffect(() => {
    fetchPosts(); // initial load

    const interval = setInterval(() => {
      fetchPosts(); // re-fetch every 15s
    }, 15000);

    return () => clearInterval(interval); // cleanup
  }, [fetchPosts]);



 
  if (loading) return <p>Loading posts...</p>
  if (error) return <p>Error: {error}</p>
  return (
    <>
    {/* ✅ Add your CreatePost component here */}
    <CreatePost />
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
