import { useState } from "react";
import axios from "axios";
import "../styles/Header.css";
import { Link } from "react-router-dom";

export default function Header() {
  const [categories, setCategories] = useState();

  if (!categories) {
    axios.get("http://127.0.0.1:8000/api/categories/").then((res) => {
      setCategories(res.data);
    });
  }

  return !categories ? (
    <>
      <p>loading</p>
    </>
  ) : (
    <div className="header">
      <Link to="/">
        <h1>Cooking Recipes for Every Day!</h1>
      </Link>
      <div className="categories-container">
        {categories.map((c) => (
          <Link to={`/category/${c.slug}`} key={c.id}>
            <span key={c.id}>{c.name}</span>
          </Link>
        ))}
        <Link to="/api">
          <span>API</span>
        </Link>
      </div>
    </div>
  );
}
