# Setup and Deployment Guide

## 🚀 Quick Start

### **Prerequisites**
- Python 3.10-3.13
- Git
- Google Cloud Platform account (for AI models)
- Optional: UV package manager for faster dependency management

### **Installation**

#### **Method 1: Using pip (Standard)**
```bash
# Clone the repository
git clone https://github.com/saishshinde15/Game_Of_Thrones_MultiAgent_Mcp_Gradio_App.git
cd Game_Of_Thrones_MultiAgent_Mcp_Gradio_App/crewai_gcp

# Install dependencies
pip install -r requirements.txt

# Set Python path for proper imports
export PYTHONPATH=$(pwd)/src
```

#### **Method 2: Using UV (Recommended)**
```bash
# Clone the repository
git clone https://github.com/saishshinde15/Game_Of_Thrones_MultiAgent_Mcp_Gradio_App.git
cd Game_Of_Thrones_MultiAgent_Mcp_Gradio_App/crewai_gcp

# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies with UV
uv pip install -r requirements.txt

# Set Python path
export PYTHONPATH=$(pwd)/src
```

### **Configuration**

#### **Google Cloud Setup**
1. **Create a Google Cloud Project**
   ```bash
   # Install Google Cloud CLI
   curl https://sdk.cloud.google.com | bash
   exec -l $SHELL
   
   # Initialize gcloud
   gcloud init
   
   # Enable AI Platform API
   gcloud services enable aiplatform.googleapis.com
   ```

2. **Authentication Options**

   **Option A: Service Account Key**
   ```bash
   # Create service account
   gcloud iam service-accounts create got-matcher-sa \
       --display-name="Game of Thrones Matcher Service Account"
   
   # Grant necessary permissions
   gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
       --member="serviceAccount:got-matcher-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
       --role="roles/aiplatform.user"
   
   # Create and download key
   gcloud iam service-accounts keys create ~/got-matcher-key.json \
       --iam-account=got-matcher-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com
   
   # Set environment variable
   export GOOGLE_APPLICATION_CREDENTIALS=~/got-matcher-key.json
   ```

   **Option B: Application Default Credentials**
   ```bash
   gcloud auth application-default login
   ```

## 🌐 Running the Application

### **1. Gradio Interface (Recommended)**
```bash
cd crewai_gcp
PYTHONPATH=./src python gradio_app.py
```
- **Access**: http://127.0.0.1:7860
- **Features**: Modern web interface, easy sharing
- **Best for**: General use, demos, sharing

### **2. Streamlit Interface**
```bash
cd crewai_gcp
PYTHONPATH=./src streamlit run streamlit_app.py
```
- **Access**: http://localhost:8501
- **Features**: Interactive dashboard, detailed controls
- **Best for**: Data exploration, detailed analysis

### **3. MCP Server**
```bash
cd crewai_gcp
PYTHONPATH=./src python mcp_server.py
```
- **Protocol**: stdio (for MCP integration)
- **Usage**: Tool integration with MCP-compatible systems
- **Best for**: VS Code integration, workflow automation

## 🏗️ Deployment Options

### **Option 1: Hugging Face Spaces (Easiest)**

1. **Prepare Repository**
   ```bash
   # Ensure your repository structure is correct
   ls -la
   # Should show: gradio_app.py, requirements.txt, README.md, crewai_gcp/
   ```

2. **Create Hugging Face Space**
   - Go to [Hugging Face Spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose "Gradio" as the SDK
   - Link to your GitHub repository

3. **Configure Space**
   ```yaml
   # Create spaces_config.yaml (optional)
   title: "Game of Thrones Character & Dragon Matcher"
   emoji: "🏰"
   colorFrom: "blue"
   colorTo: "purple"
   sdk: "gradio"
   app_file: "crewai_gcp/gradio_app.py"
   ```

4. **Environment Variables**
   - Set `GOOGLE_APPLICATION_CREDENTIALS` in Space settings
   - Upload service account key as a file

### **Option 2: Local Server Deployment**

#### **Production Setup with Gunicorn**
```bash
# Install production dependencies
pip install gunicorn uvicorn

# Create Gunicorn configuration
cat > gunicorn.conf.py << EOF
bind = "0.0.0.0:8000"
workers = 2
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 300
keepalive = 2
EOF

# Run with Gunicorn
cd crewai_gcp
PYTHONPATH=./src gunicorn -c gunicorn.conf.py gradio_app:iface
```

#### **Docker Deployment**
```dockerfile
# Create Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY crewai_gcp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY crewai_gcp/ ./crewai_gcp/

# Set Python path
ENV PYTHONPATH=/app/crewai_gcp/src

# Expose port
EXPOSE 7860

# Run application
CMD ["python", "crewai_gcp/gradio_app.py"]
```

```bash
# Build and run Docker container
docker build -t got-matcher .
docker run -p 7860:7860 -e GOOGLE_APPLICATION_CREDENTIALS=/app/key.json got-matcher
```

### **Option 3: Cloud Platform Deployment**

#### **Google Cloud Run**
```bash
# Create Cloud Run service
gcloud run deploy got-matcher \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --memory 2Gi \
    --timeout 300
```

#### **AWS ECS/Fargate**
```yaml
# ecs-task-definition.json
{
  "family": "got-matcher",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "1024",
  "memory": "2048",
  "executionRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "got-matcher",
      "image": "your-ecr-repo/got-matcher:latest",
      "portMappings": [
        {
          "containerPort": 7860,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "GOOGLE_APPLICATION_CREDENTIALS",
          "value": "/app/key.json"
        }
      ]
    }
  ]
}
```

## 🔧 MCP Integration Setup

### **VS Code Integration**
1. **Install MCP Extension** (if available)
2. **Configure MCP Server**
   ```json
   // .vscode/mcp.json
   {
       "servers": {
           "GoT": {
               "type": "stdio",
               "command": "uv",
               "args": [
                   "--directory",
                   "crewai_gcp",
                   "run",
                   "mcp_server.py"
               ]
           }
       }
   }
   ```

3. **Test MCP Integration**
   ```bash
   # Start MCP server manually for testing
   cd crewai_gcp
   PYTHONPATH=./src python mcp_server.py
   ```

### **Claude Desktop Integration**
```json
// claude_desktop_config.json
{
  "mcpServers": {
    "got-matcher": {
      "command": "python",
      "args": ["/path/to/crewai_gcp/mcp_server.py"],
      "env": {
        "PYTHONPATH": "/path/to/crewai_gcp/src",
        "GOOGLE_APPLICATION_CREDENTIALS": "/path/to/key.json"
      }
    }
  }
}
```

## 🐛 Troubleshooting

### **Common Issues**

#### **Import Errors**
```bash
# Problem: ModuleNotFoundError: No module named 'crewai_gcp'
# Solution: Set Python path correctly
export PYTHONPATH=/path/to/crewai_gcp/src

# Verify path is correct
python -c "import crewai_gcp.crew; print('Success')"
```

#### **Google Cloud Authentication**
```bash
# Problem: Authentication errors
# Solution: Check credentials setup
gcloud auth list
gcloud config list

# Test authentication
python -c "from google.cloud import aiplatform; print('Auth successful')"
```

#### **Gradio/Streamlit Issues**
```bash
# Problem: Interface won't start
# Solution: Check port availability
netstat -tulpn | grep :7860  # For Gradio
netstat -tulpn | grep :8501  # For Streamlit

# Try different port
python gradio_app.py --server-port 7861
```

#### **Performance Issues**
```bash
# Problem: Slow responses
# Solutions:
# 1. Check internet connection
# 2. Verify Google Cloud quotas
# 3. Monitor CPU/memory usage
htop
# 4. Check logs for errors
tail -f ~/.cache/gradio/logs/gradio.log
```

### **Debugging Tips**

#### **Enable Verbose Logging**
```python
# Add to your Python scripts
import logging
logging.basicConfig(level=logging.DEBUG)

# For CrewAI debugging
crew_instance = crew.crew()
crew_instance.verbose = True
```

#### **Test Individual Components**
```python
# Test CrewAI setup
from crewai_gcp.crew import GotCharacterMatcher
crew = GotCharacterMatcher()
print("CrewAI setup successful")

# Test Google Cloud connection
from google.cloud import aiplatform
aiplatform.init(project="your-project-id")
print("Google Cloud connection successful")
```

## 🔐 Security Considerations

### **Production Security**
- **Environment Variables**: Never commit credentials to version control
- **Network Security**: Use HTTPS in production
- **Access Control**: Implement authentication if needed
- **Rate Limiting**: Consider request rate limits for public deployments

### **Secrets Management**
```bash
# Use environment variables for sensitive data
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_APPLICATION_CREDENTIALS="/secure/path/to/key.json"

# For production, use secret management services:
# - Google Secret Manager
# - AWS Secrets Manager
# - Azure Key Vault
# - HashiCorp Vault
```

## 📊 Monitoring & Analytics

### **Application Monitoring**
```python
# Add basic analytics to your apps
import time
from datetime import datetime

def log_usage(user_responses):
    timestamp = datetime.now().isoformat()
    print(f"Usage at {timestamp}: {len(user_responses)} responses")
    # Add more sophisticated logging as needed
```

### **Performance Monitoring**
```bash
# Monitor system resources
pip install psutil

# Add to your application
import psutil
print(f"CPU: {psutil.cpu_percent()}%")
print(f"Memory: {psutil.virtual_memory().percent}%")
```

This guide should help you deploy and run the Game of Thrones Character Matcher in various environments, from local development to production cloud deployments.