# Frequently Asked Questions (FAQ)

## 🏰 General Questions

### **Q: What exactly does this application do?**
**A:** This application is a personality matching system that uses AI agents to analyze your responses to personality questions and matches you with a Game of Thrones character and dragon. It provides an immersive, story-driven experience that makes you feel like you're discovering your destiny in the world of Westeros.

### **Q: How accurate are the character matches?**
**A:** The matching is based on personality trait analysis using sophisticated AI models. While it's designed to be entertaining and engaging, the accuracy depends on the comprehensiveness of your answers and the AI model's understanding of Game of Thrones characters. It's primarily for fun and entertainment!

### **Q: How long does the analysis take?**
**A:** Typically 1-2 minutes. The system uses multiple AI agents working sequentially to analyze your responses, match characters, select dragons, and create the final immersive narrative.

## 🔧 Technical Questions

### **Q: Why do I get "ModuleNotFoundError: No module named 'crewai_gcp'"?**
**A:** This is a Python path issue. You need to set the PYTHONPATH environment variable:
```bash
export PYTHONPATH=/path/to/your/project/crewai_gcp/src
```
Then run your script. For permanent solution, add this to your `~/.bashrc` or `~/.zshrc`.

### **Q: What's the difference between Gradio and Streamlit interfaces?**
**A:** 
- **Gradio**: Simpler, more modern web interface. Better for sharing and general use. Easier to deploy to Hugging Face Spaces.
- **Streamlit**: More interactive dashboard-style interface. Better for data exploration and detailed controls.

Both provide the same core functionality but with different user experiences.

### **Q: Do I need Google Cloud Platform to run this?**
**A:** Yes, the application uses Google Cloud AI Platform for the underlying AI models. You'll need:
- A Google Cloud Platform account
- AI Platform API enabled
- Service account credentials or application default credentials
- Some API calls may incur small costs

### **Q: Can I run this without Google Cloud?**
**A:** The current implementation requires Google Cloud AI Platform. However, you could modify the code to use other AI providers like OpenAI, Anthropic, or local models, but this would require code changes.

## 🛠️ Setup and Deployment

### **Q: I'm getting authentication errors with Google Cloud. What should I do?**
**A:** Check these steps:
1. Verify your Google Cloud project is set up correctly
2. Ensure AI Platform API is enabled
3. Check your authentication method:
   ```bash
   # For service account
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/key.json
   
   # For application default credentials
   gcloud auth application-default login
   ```
4. Test authentication:
   ```bash
   python -c "from google.cloud import aiplatform; print('Success')"
   ```

### **Q: How do I deploy this to Hugging Face Spaces?**
**A:** 
1. Push your code to a GitHub repository
2. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
3. Create a new Space, select "Gradio" as SDK
4. Connect to your GitHub repository
5. Set up environment variables for Google Cloud credentials
6. The Space will automatically deploy

### **Q: Can I run this locally without internet?**
**A:** No, the application requires internet connectivity to access Google Cloud AI Platform APIs. It's designed as a cloud-based AI application.

### **Q: What ports does the application use?**
**A:** 
- **Gradio**: Port 7860 (default)
- **Streamlit**: Port 8501 (default)
- **MCP Server**: Uses stdio protocol (no HTTP port)

## 🔍 MCP Integration

### **Q: What is MCP and why should I care?**
**A:** MCP (Model Context Protocol) is a standardized way for AI tools to communicate. It allows this Game of Thrones matcher to be used as a tool within other AI systems like VS Code with AI extensions or Claude Desktop, making it part of larger AI workflows.

### **Q: How do I set up MCP integration with VS Code?**
**A:** 
1. Ensure you have the MCP extension installed in VS Code
2. Configure the `.vscode/mcp.json` file (already included in the project)
3. Start the MCP server:
   ```bash
   cd crewai_gcp
   PYTHONPATH=./src python mcp_server.py
   ```
4. The Game of Thrones matcher should now be available as a tool in VS Code

### **Q: Can I use the MCP server with other applications?**
**A:** Yes! Any MCP-compatible application can use the server. This includes Claude Desktop, some AI coding assistants, and other tools that support the MCP protocol.

## 🎮 Usage and Features

### **Q: What personality questions does the app ask?**
**A:** The app asks 7 key questions:
1. Leadership style (commanding, diplomatic, strategic)
2. Core values (power, family, honor, knowledge)
3. Conflict handling approach
4. Loyalty and trust approach
5. Decision-making style (logic, emotions, intuition)
6. Core motivation (power vs. security)

### **Q: Can I get different results if I answer the questions differently?**
**A:** Absolutely! The AI analyzes your specific responses to match you with the most appropriate character and dragon. Different answers will lead to different matches.

### **Q: Which Game of Thrones characters and dragons are included?**
**A:** The system has knowledge of major characters and dragons from the series. The AI draws from its training data about Game of Thrones, so it includes most well-known characters and dragons from both the books and TV series.

### **Q: Can I save or share my results?**
**A:** Currently, results are displayed in the interface but not automatically saved. You can:
- Copy and paste the results
- Take a screenshot
- The Gradio interface has sharing capabilities if you enable them

## 🔧 Customization and Development

### **Q: Can I add more characters or dragons?**
**A:** The character and dragon knowledge comes from the AI model's training data. To add more specific characters, you would need to modify the agent prompts and task descriptions in the YAML configuration files to include more detailed information about specific characters.

### **Q: How can I modify the personality questions?**
**A:** Edit the question prompts in:
- `gradio_app.py` for the Gradio interface
- `streamlit_app.py` for the Streamlit interface
- Update the `tasks.yaml` file if you want to change how responses are processed

### **Q: Can I change the storytelling style of the results?**
**A:** Yes! Modify the `present_results` task in `src/crewai_gcp/config/tasks.yaml`. You can change the tone, style, format, and content of the final narrative output.

### **Q: How do I add more agents to the system?**
**A:** 
1. Add new agent definitions to `config/agents.yaml`
2. Create corresponding tasks in `config/tasks.yaml`
3. Add the new agent and task methods to the `GotCharacterMatcher` class in `crew.py`
4. Update the task dependencies and workflow as needed

## 🐛 Troubleshooting

### **Q: The application is running but responses are very slow or timing out.**
**A:** This could be due to:
- High Google Cloud API latency
- Network connectivity issues
- API rate limits or quota issues
- The sequential agent processing taking longer than expected

Try:
- Checking your internet connection
- Verifying Google Cloud quotas and billing
- Running the demo script to test individual components

### **Q: I get errors about missing dependencies.**
**A:** Run:
```bash
pip install -r requirements.txt
```

If you're still having issues, try creating a fresh virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### **Q: The Gradio interface won't start.**
**A:** Check:
1. Port availability: `netstat -tulpn | grep :7860`
2. Python path: `export PYTHONPATH=/path/to/crewai_gcp/src`
3. Dependencies: Ensure Gradio is installed
4. Try a different port: Modify the `launch()` call in `gradio_app.py`

### **Q: I want to contribute to the project. How do I get started?**
**A:** 
1. Fork the repository on GitHub
2. Set up your local development environment
3. Run the demo script to understand the system
4. Read through the technical documentation
5. Start with small improvements or bug fixes
6. Submit pull requests for review

## 💡 Tips and Best Practices

### **Q: How do I get the best character matches?**
**A:** 
- Be honest and detailed in your responses
- Think about how you would actually behave in challenging situations
- Consider your core values and motivations carefully
- Don't just answer what you think sounds "cool" - authenticity gives better matches

### **Q: Can I run multiple instances simultaneously?**
**A:** Yes, but be aware of:
- Google Cloud API rate limits
- Port conflicts (use different ports for each instance)
- Resource usage on your machine

### **Q: What's the recommended development workflow?**
**A:** 
1. Set up your environment with proper Python paths
2. Test individual components with the demo script
3. Make small changes and test frequently
4. Use the Gradio interface for quick testing
5. Use the Streamlit interface for more detailed analysis
6. Test MCP integration separately

This FAQ should help you understand and work with the Game of Thrones Character Matcher effectively! If you have additional questions, check the technical documentation or run the demo script for hands-on exploration.