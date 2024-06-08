"use strict";

const Hapi = require("@hapi/hapi");
const Inert = require("@hapi/inert");
const routes = require("./routes");
const Path = require("path");
const Nunjucks = require("nunjucks");

const init = async () => {
  const server = Hapi.server({
    port: process.env.PORT,
    host: "0.0.0.0",
    routes: {
      cors: {
        origin: ["*"],
      },
    },
  });
  // Konfigurasi Nunjucks
  Nunjucks.configure(Path.join(__dirname, "templates"), {
    autoescape: true,
    noCache: true,
  });

  // Register Inert plugin
  await server.register(Inert);

  // Define routes
  server.route(routes);

  // Start the server
  await server.start();
  console.log(`Server berjalan pada ${server.info.uri}`);
};

init();
