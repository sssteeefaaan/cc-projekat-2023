const router = require("express").Router()
const {registerStudent, registerProfessor} = require("../utils/register")
const {loginStudent, loginProfessor} = require("../utils/login")

router.get('/', async (req, res) => {
    res.render('uns/index')
})

router.post("/register", async(req, res) => {
    try{
        const content = req.body
        let result;
        switch (content.type){
            case("student"):{
                result = await registerStudent(content.data)
                break
            }
            case("professor"):{
                result = await registerProfessor(content.data)
                break
            }
            default: {
                result.message = `Unknown registration type '${content.type}'`
                result.status = 400
            }
        }
        return res.status(result.status).send({message: result.message})
    }catch(e){
        console.log(e)
        res.send({
            status: "Failed",
            reason: e
        }).status(500)
    }
})

router.post("/login", async(req, res)=>{
    try{
        const content = req.body
        let result = { message: null, status: null, content: null}
        switch (content.type){
            case("student"):{
                result = await loginStudent(content.data)
                break
            }
            case("professor"):{
                result = await loginProfessor(content.data)
                break
            }
            default: {
                result.message = `Unknown login type '${content.type}'`
                result.status = 400
                result.content = null
            }
        }
        return res.status(result.status).send({ message: result.message, content: result.content })

    }catch(e){
        console.log(e)
        res.status(500).send({message: "Failed", reason: e})
    }
})

module.exports = router