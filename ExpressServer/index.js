const express  = require('express')
const cors = require('cors')
const mongoose = require('mongoose')
require("dotenv").config();
mongoose.set('strictQuery', false);

const app = express();

app.use(cors());
app.use(express.json());
