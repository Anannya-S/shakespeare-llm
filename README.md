# shakespeare-llm
This project fine-tunes a base LLM to speak in the style of William Shakespeare using Unsloth. The resulting model is exported to Ollama for efficient local inference, and a Gradio app is built to demo the model and provide an interactive front end.

# Workflow
1. **Fine-tuning**  
   - Used Unsloth to fine-tune a base model on a Shakespeare-style dataset.  
   - Dataset consisted of prompt–response pairs in Elizabethan English.  

2. **Deployment**  
   - Converted the fine-tuned model into Ollama’s `Modelfile` format.  
   - Loaded it locally with Ollama for efficient inference.  

3. **Web App**  
   - Built a Gradio app titled *Ask Shakespeare*.  
   - Users can ask free-form questions or use pre-set buttons for inspiration.  

---

# Dataset
The dataset consists of custom Shakespearean prompt–response pairs.  

