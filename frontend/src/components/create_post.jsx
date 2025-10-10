import React, { useState } from "react";
import axios from "axios";

const CreatePost = ({ onPostCreated }) => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);

  const base_url = "http://127.0.0.1:8000/";

  const createPost = async () => {
    if (!title.trim() || !content.trim()) {
      return alert("Please fill all the fields");
    }

    try {
      setLoading(true);
      const res = await axios.post(`${base_url}create/`, { title, content });

      // ✅ Clear inputs
      setTitle("");
      setContent("");

      // ✅ Notify parent about the new post
      if (onPostCreated) onPostCreated(res.data);

      console.log("✅ Post created:", res.data);
    } catch (err) {
      console.error("❌ Error creating post:", err);
      alert("Something went wrong while posting...");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginBottom: 20 }}>
      <h2>🖋 Create New Post</h2>

      <input
        type="text"
        placeholder="Title"
        value={title}
        readOnly={loading}
        onChange={(e) => setTitle(e.target.value)}
        style={{
          width: "100%",
          marginBottom: 10,
          padding: 8,
          border: "1px solid #ccc",
          borderRadius: 6,
        }}
      />

      <textarea
        placeholder="Write your post content..."
        value={content}
        readOnly={loading}
        onChange={(e) => setContent(e.target.value)}
        rows={5}
        style={{
          width: "100%",
          padding: 10,
          border: "1px solid #ccc",
          borderRadius: 6,
          fontSize: "1rem",
        }}
      ></textarea>

      <br />

      <button
        onClick={createPost}
        disabled={loading}
        style={{
          marginTop: 10,
          padding: "8px 16px",
          backgroundColor: loading ? "#999" : "#007bff",
          color: "white",
          border: "none",
          borderRadius: 6,
          cursor: loading ? "not-allowed" : "pointer",
          fontWeight: "bold",
        }}
      >
        {loading ? "Posting..." : "Post"}
      </button>
    </div>
  );
};

export default CreatePost;
