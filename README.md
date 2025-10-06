# Game of Thrones Multi-Agent MCP Gradio App 🏰🐉

> **Discover your destiny in Westeros through the power of AI agents!**

Step into the world of Westeros and discover your true Game of Thrones character and dragon! This innovative project combines the fantasy realm of Game of Thrones with cutting-edge AI agent technology, using a multi-agent system powered by CrewAI, integrated with MCP (Model Context Protocol), and featuring beautiful web interfaces for interactive personality matching.

![Game of Thrones Banner](https://img.shields.io/badge/Game%20of%20Thrones-Character%20Matcher-red?style=for-the-badge&logo=game-of-thrones)
![AI Powered](https://img.shields.io/badge/AI-Multi--Agent%20System-blue?style=for-the-badge)
![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green?style=for-the-badge)

## ✨ Features

### 🤖 **Multi-Agent AI System**
- **CrewAI Orchestration**: Sophisticated AI agents working together
- **Sequential Processing**: Questioner → Character Matcher → Dragon Matcher → Story Presenter
- **Intelligent Analysis**: Deep personality trait matching with Game of Thrones lore

### 🌐 **Multiple Interfaces**
- **Gradio Web App**: Modern, shareable interface perfect for demos
- **Streamlit Dashboard**: Interactive interface with detailed controls
- **MCP Server**: Tool integration for AI workflows and VS Code

### 🎭 **Immersive Experience**
- **Storytelling**: Results presented as dramatic GoT-style narratives
- **Character Matching**: Detailed analysis with house affiliations and traits
- **Dragon Pairing**: Compatible dragon selection with historical context
- **Personalized Results**: Tailored responses based on your unique answers

## 🚀 Quick Start

### **Prerequisites**
- Python 3.10+ 
- Google Cloud Platform account (for AI models)
- Git

### **Installation**
```bash
# Clone the repository
git clone https://github.com/saishshinde15/Game_Of_Thrones_MultiAgent_Mcp_Gradio_App.git
cd Game_Of_Thrones_MultiAgent_Mcp_Gradio_App/crewai_gcp

# Install dependencies
pip install -r requirements.txt

# Set up Python path
export PYTHONPATH=$(pwd)/src
```

### **Google Cloud Setup**
```bash
# Authenticate with Google Cloud
gcloud auth application-default login

# Or use service account key
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/key.json
```

### **Run the Application**

**🎯 Gradio Interface (Recommended)**
```bash
cd crewai_gcp
PYTHONPATH=./src python gradio_app.py
# Open http://127.0.0.1:7860
```

**📊 Streamlit Interface**
```bash
cd crewai_gcp  
PYTHONPATH=./src streamlit run streamlit_app.py
# Open http://localhost:8501
```

**🔧 MCP Server**
```bash
cd crewai_gcp
PYTHONPATH=./src python mcp_server.py
```

## 🎮 Try the Demo

Run our interactive demo script to see the system in action:

```bash
python demo.py
```

The demo includes:
- **Sample personality profiles** to test the system
- **MCP integration testing**
- **Interface configuration validation**
- **Step-by-step analysis walkthrough**

## 🏗️ Project Architecture

```
Game_Of_Thrones_MultiAgent_Mcp_Gradio_App/
├── 📄 README.md                    # This file
├── 🎮 demo.py                      # Interactive demo script
├── 📁 docs/                        # Comprehensive documentation
│   ├── PROJECT_OVERVIEW.md         # Detailed project explanation
│   ├── TECHNICAL_DEEP_DIVE.md      # Architecture and implementation
│   ├── SETUP_DEPLOYMENT.md         # Setup and deployment guide
│   └── FAQ.md                      # Frequently asked questions
├── 📁 .vscode/
│   └── mcp.json                    # MCP configuration for VS Code
└── 📁 crewai_gcp/                  # Main application
    ├── 🌐 gradio_app.py            # Gradio web interface
    ├── 🌐 streamlit_app.py         # Streamlit interface
    ├── 🔧 mcp_server.py            # MCP server implementation
    ├── 📄 requirements.txt         # Dependencies
    ├── 📄 pyproject.toml           # Project configuration
    ├── 📁 knowledge/               # Sample data
    └── 📁 src/crewai_gcp/         # Core application code
        ├── 🤖 crew.py             # CrewAI multi-agent setup
        ├── 📁 config/
        │   ├── agents.yaml         # AI agent definitions
        │   └── tasks.yaml          # Task configurations
        └── 📁 tools/               # Custom tools
```

## 🎯 How It Works

### **1. Personality Analysis (7 Questions)**
- Leadership style and approach
- Core values (power, family, honor, knowledge)
- Conflict resolution methods
- Loyalty and trust patterns
- Decision-making preferences
- Core life motivations

### **2. AI Agent Pipeline**
```
User Responses → [Questioner Agent] → [Character Matcher] → [Dragon Matcher] → [Story Presenter] → Epic Reveal!
```

### **3. Results Generation**
- **Character Match**: Detailed personality analysis with house affiliation
- **Dragon Pairing**: Compatible dragon with historical context
- **Immersive Narrative**: Story-driven reveal in authentic GoT style
- **Fun Facts**: Hidden details only true fans would know

## 🌟 Deployment Options

### **🤗 Hugging Face Spaces (Easiest)**
1. Fork this repository
2. Create a new [Hugging Face Space](https://huggingface.co/spaces)
3. Select "Gradio" SDK and connect your repo
4. Add Google Cloud credentials in Space settings
5. Deploy automatically!

### **☁️ Cloud Platforms**
- **Google Cloud Run**: `gcloud run deploy`
- **AWS ECS/Fargate**: Container deployment
- **Azure Container Instances**: Docker deployment

### **🐳 Docker**
```bash
docker build -t got-matcher .
docker run -p 7860:7860 got-matcher
```

## 🔧 MCP Integration

### **VS Code Setup**
The project includes MCP configuration for VS Code integration:

```json
{
    "servers": {
        "GoT": {
            "type": "stdio", 
            "command": "uv",
            "args": ["--directory", "crewai_gcp", "run", "mcp_server.py"]
        }
    }
}
```

### **Claude Desktop Integration**
Add to your Claude Desktop configuration to use as an AI tool!

## 📚 Documentation

- **[📖 Project Overview](docs/PROJECT_OVERVIEW.md)** - Comprehensive project explanation
- **[🔧 Technical Deep Dive](docs/TECHNICAL_DEEP_DIVE.md)** - Architecture and implementation details  
- **[🚀 Setup & Deployment](docs/SETUP_DEPLOYMENT.md)** - Complete setup and deployment guide
- **[❓ FAQ](docs/FAQ.md)** - Frequently asked questions and troubleshooting

## 🛠️ Technologies Used

- **[CrewAI](https://github.com/joaomdmoura/crewai)** - Multi-agent AI orchestration
- **[Google Cloud AI Platform](https://cloud.google.com/ai-platform)** - AI model hosting
- **[Gradio](https://gradio.app)** - Modern web interface framework
- **[Streamlit](https://streamlit.io)** - Interactive web dashboard
- **[FastMCP](https://github.com/jlowin/fastmcp)** - Model Context Protocol implementation
- **Python 3.10+** - Core programming language

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Run the demo**: `python demo.py` to understand the system
3. **Read the docs**: Check out the technical documentation
4. **Make improvements**: Start with small enhancements
5. **Submit a PR**: We'll review and merge!

## 📊 Performance

- **Analysis Time**: 1-2 minutes per complete character matching
- **Scalability**: Designed for individual user interactions  
- **Requirements**: Internet connection for Google Cloud AI APIs

## 🎉 Credits & Acknowledgments

- **[CrewAI Team](https://github.com/joaomdmoura/crewai)** - Amazing multi-agent framework
- **George R.R. Martin** - Creating the incredible Game of Thrones universe
- **Google Cloud Platform** - Powerful AI infrastructure
- **Gradio & Streamlit** - Excellent UI frameworks
- **MCP Community** - Tool interoperability standards

## 📄 License

This project is open source. See the license file for details.

---

## 🏰 Ready to Discover Your Destiny?

**"When you play the game of thrones, you win or you die. There is no middle ground."**  
*- Cersei Lannister*

Whether you're a noble Stark, a cunning Lannister, a fierce Targaryen, or something entirely different, your destiny awaits in the world of Westeros. Fire up the application and let the AI agents reveal your true nature!

**May your dragon soar high above the clouds of Westeros!** 🐉

---

⭐ **Star this repository if you found it interesting!**  
🔄 **Share with fellow Game of Thrones fans!**  
🐛 **Report issues or suggest improvements!**
