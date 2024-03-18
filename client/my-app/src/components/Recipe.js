import axios from "axios";
import { useLoaderData } from "react-router-dom";
import "../styles/Recipe.css";
import { serverURL } from "../index.js";

export async function getRecipe({ params }) {
  const data = await axios
    .get(`${serverURL}/api/recipes/${params.recipeName}`)
    .then((res) => {
      return res.data;
    });
  return { data };
}

function Recipe() {
  const recipe = useLoaderData();
  return !recipe ? (
    <>loading</>
  ) : (
    <div className="recipe-one-container">
      <h3>{recipe.data.name}</h3>
      <div className="recipe-image-text-container">
        <img className="recipe-image" src={`${recipe.data.image}`}></img>
        <div className="recipe-description">{recipe.data.description}</div>
      </div>
      <h4>Ingridients</h4>
      <p className="recipe-ingridients">
        <span>{recipe.data.ingridients}</span>
      </p>
      <h4>Directions</h4>
      <p className="recipe-directions">
        <span>{recipe.data.directions}</span>
      </p>
    </div>
  );
}

export default Recipe;
