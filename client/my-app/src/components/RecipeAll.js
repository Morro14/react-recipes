import axios from "axios";
import { useLoaderData } from "react-router-dom";
import "../styles/RecipeAll.css";
import { Link } from "react-router-dom";

export async function getAllRecipes({ params }) {
  const data = await axios
    .get(`http://127.0.0.1:8000/api/recipes`)
    .then((res) => {
      console.log("Sending request: all recipes ");
      return res.data;
    });
  return { data };
}

function RecipeAll() {
  const recipes = useLoaderData();

  const raiting = (r) => {
    const rounded = Math.floor(r);
    let stars = "★".repeat(rounded);
    if (Math.round(r) !== rounded) {
      stars += "+";
    }
    return stars;
  };
  return !recipes ? (
    <>loading</>
  ) : (
    <div className="recipes-all-container">
      <h3>
        Speedy weeknight dinners, 5-ingredient dishes, quick and easy meals,
        plus kid-pleasing snacks and desserts.{" "}
      </h3>
      <div className="recipes-grid">
        {recipes.data.map((r) => (
          <div className="recipe-container" key={r.id}>
            <div className="recipe-grid-image-container">
              <Link to={`/recipe/${r.slug}`}>
                <img className="recipe-grid-image" src={`${r.image}`}></img>
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

export default RecipeAll;
