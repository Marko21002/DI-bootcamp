const db = require("knex")({
  client: "pg",
  connection: {
    host: "127.0.0.1",
    port: 5432,
    user: "postgres",
    password: "m210702g",
    database: "auth",
  },
});

module.exports = db;
