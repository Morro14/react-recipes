import SwaggerUI from "swagger-ui-react";
import "swagger-ui-react/swagger-ui.css";

function apiUI() {
  return <SwaggerUI url="http://127.0.0.1:8000/api/schema" />;
}

export default apiUI;
