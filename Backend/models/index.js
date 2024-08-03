const mongoose = require("mongoose");
require("dotenv").config();

const uri = process.env.MONGODB_URI;

if (!uri) {
  console.error("Error: MONGODB_URI is not defined in the .env file");
  process.exit(1);
}

function main() {
  mongoose
    .connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => {
      console.log("Successful");
    })
    .catch((err) => {
      console.log("Error: ", err);
    });
}

module.exports = { main };