import axios from "axios";
import { useLoaderData } from "react-router-dom";
import "../styles/Category.css";
import { Link } from "react-router-dom";

export async function getRecipes({ params }) {
  const categoryData = await axios
    .get(`http://127.0.0.1:8000/api/categories/${params.categoryName}`)
    .then((res) => {
      return res.data;
    });
  return { categoryData };
}

function Category() {
  const data = useLoaderData().categoryData;
  const recipes = data.recipes;
  console.log(data);

  const title = data.name;
  const raiting = (r) => {
    const rounded = Math.floor(r);
    let stars = "★".repeat(rounded);
    if (Math.round(r) !== rounded) {
      stars += "+";
    }
    return stars;
  };
  return !recipes.length ? (
    <>
      <h3>{title}</h3>
      <p>No recipes in this category</p>
    </>
  ) : (
    <div className="category-container">
      <h3>{title}</h3>
      <div className="recipes-grid">
        {recipes.map((r) => (
          <div className="recipe-container" key={r.id}>
            <div className="recipe-grid-image-container">
              <Link to={`/recipe/${r.slug}`}>
                <img
                  alt={`dish-${r.id}`}
                  className="recipe-grid"
                  src={`http://127.0.0.1:8000${r.image}`}
                ></img>
              </Link>
            </div>
            <h4>{r.name}</h4>
            <p className="rating">
              {raiting(r.rating) + " "}
              {r.rating}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Category;
