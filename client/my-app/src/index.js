import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./index.css";

import { getRecipes as categoryLoader } from "./components/Category";
import { getAllRecipes as recipesLoader } from "./components/RecipeAll";
import { getRecipe as recipeLoader } from "./components/Recipe";
import { RouterProvider, createBrowserRouter } from "react-router-dom";

import ErrorPage from "./error-page";
import Main from "./components/Main";
import Category from "./components/Category";
import Recipe from "./components/Recipe";
import RecipeAll from "./components/RecipeAll";
import SwaggerUI from "./components/SwaggerUI";

const container = document.getElementById("root");
const root = createRoot(container);

export const serverURL = "http://127.0.0.1:8000";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <Main />,
        children: [
          {
            path: "/category/:categoryName",
            loader: categoryLoader,
            element: <Category />,
          },
          {
            path: "/",
            loader: recipesLoader,
            element: <RecipeAll />,
          },
          {
            path: "/recipe/:recipeName",
            element: <Recipe />,
            loader: recipeLoader,
          },
        ],
      },
    ],
  },
  {
    path: "/api",
    element: <SwaggerUI />,
  },
]);

root.render(
  <React.StrictMode>
    {/* <Provider store={store}> */}
    <RouterProvider router={router} />
    {/* </Provider> */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
