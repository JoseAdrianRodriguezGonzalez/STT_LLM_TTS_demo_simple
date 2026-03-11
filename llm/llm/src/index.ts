import express from "express"
import { getLlama, LlamaChatSession } from "node-llama-cpp"

const app = express()
app.use(express.json())

let session

async function init(){

  const llama = await getLlama()

  const model = await llama.loadModel({
    modelPath: "./models/hf_mradermacher_Meta-Llama-3.1-8B-Instruct.Q4_K_M.gguf"
  })

  const context = await model.createContext()

  session = new LlamaChatSession({
    contextSequence: context.getSequence()
  })
}

app.post("/chat", async (req,res)=>{

  const prompt = req.body.text

  const response = await session.prompt(prompt)

  res.json({response})
})

await init()

app.listen(3000,()=>console.log("LLM server running"))