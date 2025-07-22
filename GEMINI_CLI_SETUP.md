# Gemini CLI Installation and Configuration Guide

This guide will walk you through installing and configuring the Gemini CLI, a command-line AI workflow tool that connects to your tools, understands your code, and accelerates your development workflows.

## What is Gemini CLI?

The Gemini CLI is a powerful command-line tool that allows you to:

- 🔍 **Query and edit large codebases** in and beyond Gemini's 1M token context window
- 🎨 **Generate new apps** from PDFs or sketches using Gemini's multimodal capabilities  
- ⚙️ **Automate operational tasks** like querying pull requests or handling complex rebases
- 🛠️ **Use tools and MCP servers** to connect new capabilities, including media generation with Imagen, Veo, or Lyria
- 🔍 **Ground your queries** with the Google Search tool, built into Gemini

---

## Installation Options

You have two main options to install the Gemini CLI:

### Option 1: Install with Node.js (Recommended)

#### Prerequisites
- Ensure you have **Node.js version 20 or higher** installed
- Check your version: `node --version`

#### Installation Methods

**Method A: Run directly with npx (no installation required)**
```bash
npx https://github.com/google-gemini/gemini-cli
```

**Method B: Global installation with npm**
```bash
npm install -g @google/gemini-cli
```

After global installation, you can run the CLI from anywhere:
```bash
gemini
```

### Option 2: Install with Homebrew (macOS/Linux)

#### Prerequisites
- Ensure you have **Homebrew** installed
- Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

#### Installation
```bash
brew install gemini-cli
```

After installation, run the CLI from anywhere:
```bash
gemini
```

---

## Configuration Steps

### 1. Initial Setup

When you first run `gemini`, you'll be prompted to complete the initial configuration:

1. **Pick a color theme** for your CLI interface
2. **Authentication** (see options below)

### 2. Authentication Options

You have three main authentication methods:

#### Option A: Personal Google Account (Easiest)
- **Free tier**: Up to 60 model requests per minute and 1,000 requests per day
- Simply sign in with your personal Google account when prompted
- No additional setup required

#### Option B: Gemini API Key (More Control)
Best for users who want more control over their usage and higher rate limits.

**Benefits:**
- Free tier: 100 requests per day using Gemini 2.5 Pro
- Control over which model you use
- Access to higher rate limits with paid plans

**Setup Steps:**
1. **Generate an API key** from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. **Set environment variable** in your terminal:
   ```bash
   export GEMINI_API_KEY="YOUR_API_KEY"
   ```
   Replace `YOUR_API_KEY` with your actual generated key.

3. **(Optional)** Upgrade to a paid plan on the [API key page](https://aistudio.google.com/app/apikey) to unlock Tier 1 rate limits

#### Option C: Vertex AI API Key (Enterprise)
Best for enterprise users or those needing the highest rate limits.

**Benefits:**
- Free tier using express mode for Gemini 2.5 Pro
- Control over which model you use
- Highest rate limits with billing account

**Setup Steps:**
1. **Generate a key** from [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. **Set environment variables**:
   ```bash
   export GOOGLE_API_KEY="YOUR_API_KEY"
   export GOOGLE_GENAI_USE_VERTEXAI=true
   ```
3. **(Optional)** Add a billing account to your project for higher usage limits

---

## Environment Variable Setup

### For Bash/Zsh users:
Add to your `~/.bashrc` or `~/.zshrc`:
```bash
# Gemini API Configuration
export GEMINI_API_KEY="your-api-key-here"
# OR for Vertex AI:
# export GOOGLE_API_KEY="your-api-key-here"
# export GOOGLE_GENAI_USE_VERTEXAI=true
```

Then reload your shell:
```bash
source ~/.bashrc  # or ~/.zshrc
```

### For Fish shell users:
```fish
set -gx GEMINI_API_KEY "your-api-key-here"
```

---

## Quick Start Examples

Once installed and configured, you can start using the Gemini CLI immediately:

### Starting a New Project
```bash
cd new-project/
gemini
```
Then ask something like:
```
> Write me a Gemini Discord bot that answers questions using a FAQ.md file I will provide
```

### Working with Existing Code
```bash
git clone https://github.com/google-gemini/gemini-cli
cd gemini-cli
gemini
```
Then ask:
```
> Give me a summary of all of the changes that went in yesterday
```

### BookBot Tutorial Integration
For this BookBot tutorial, you can use Gemini CLI to help with implementation:
```bash
cd bookbot-project/
gemini
```
Ask questions like:
```
> Help me implement the word counting function in stats.py
> How can I improve the character frequency analysis?
> Debug this file reading error in my main.py
```

---

## Verification

Test your installation by running:
```bash
gemini --version
```

Or start an interactive session:
```bash
gemini
```

You should see the Gemini CLI interface with your chosen color theme.

---

## Troubleshooting

### Common Issues

**1. "Command not found: gemini"**
- Make sure you installed globally: `npm install -g @google/gemini-cli`
- Or use npx: `npx https://github.com/google-gemini/gemini-cli`

**2. "Authentication failed"**
- Check your API key is correctly set: `echo $GEMINI_API_KEY`
- Verify the key is valid in Google AI Studio
- Make sure you're using the correct environment variable name

**3. "Rate limit exceeded"**
- Consider upgrading to a paid plan
- Switch to Vertex AI for higher limits
- Wait for the rate limit to reset

**4. Node.js version issues**
- Update Node.js: `npm install -g n && n stable`
- Or use a Node version manager like nvm

### Getting Help

For more authentication methods and advanced configuration, see the [official authentication guide](https://github.com/google-gemini/gemini-cli).

---

## Next Steps

Now that you have Gemini CLI installed and configured:

1. ✅ **Complete this BookBot tutorial** using Gemini CLI for assistance
2. 🚀 **Explore advanced features** like MCP servers and tool integrations  
3. 🤝 **Join the community** and share your workflows
4. 📖 **Read the documentation** for more advanced use cases

Happy coding with Gemini CLI! 🎉