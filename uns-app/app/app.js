// Requirements
const express = require("express")
const path = require("path")
const env = process.env
const ejs = require("ejs")

// Variables
const port = env["SERVER_PORT"] || 8000

// Server instance
const app = express()
app.use(express.json())

// Views engine setup 'EJS'
app.engine('.ejs',ejs.__express)
app.set('view engine', 'ejs')
app.set("views", path.join(".", "views"))

// Static files setup
app.use(express.static(path.join(".", 'public')))

// root route
app.get('/', (req, res) => {
  res.render("index")
})

// uns routes
app.use('/uns', require("./routes/uns"))

// listening
app.listen(port, () => {
  console.log(`Server successfully started! (On port ${port})`)
})