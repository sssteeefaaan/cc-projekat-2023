const {Student} = require("../models/student")
const studentErrors = require("../models/studentErrors").errors

function parseError(error){
    // Unique constraint is validated on the mongo server side, so mongoose cannot read that error (11000)
    if (error.code == "11000"){
        const field = Object.keys(error.keyValue)[0]
        const key = field.split(".")
        let inner = studentErrors
        for (k of key){
            if(inner == null)
                break
            inner = inner[k]
        }
        return inner.unique || `${field} must be unique!`
    }else{
        let message = ""
        for(er of Object.keys(error.errors))
            message += error.errors[er].properties.message + "\n"
        return message
    }
}

async function registerStudent(data){
    console.log("Register student")
    console.log(data)
    try{
        await Student.create(data)
        return { message: "Success", status: 200 }
    }catch(e){
        const errorMessage = parseError(e)
        console.log(errorMessage)
        return { message: errorMessage, status: 400 }
    }
}

async function registerProfessor(data){
    console.log("Register professor", data)
}

module.exports = {
    registerStudent,
    registerProfessor
}