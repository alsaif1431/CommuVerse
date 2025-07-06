# 🌐 CommuVerse: A Global Community of Communities

**CommuVerse** is an AI-powered vibrant online platform where individuals from all walks of life can come together to explore their passions, connect with like-minded people, and engage with communities powered by cutting-edge AI technology.

## 🚀 Features

### Core Communities

1. **🎨 Hobby Hub** - Explore and share your hobbies with others
2. **📚 Study & Life Hack** - Boost your productivity with life hacks
3. **🧘‍♀️ Mental Health & Wellness** - Find mindfulness practices and self-care tips
4. **🍽️ Meal Planner** - Generate meal plans based on your ingredients
5. **🕴 Stranger Buddy** - Connect and share your thoughts with someone new
6. **💰 Finance for Beginners** - Start managing your finances smartly
7. **💅 Beauty & Skincare** - Explore beauty tips and skincare routines
8. **🎉 Event Finder** - Discover fun events and activities happening near you
9. **👗 Fashion & Style** - Get personalized fashion advice based on your mood

### Key Features

- **AI-Powered Conversations**: Each community has its own specialized AI assistant
- **Personalized Experience**: Tailored responses based on user preferences and needs
- **Interactive Chat Interface**: Real-time conversations with AI companions
- **Beautiful UI**: Modern, responsive design with intuitive navigation
- **Memory System**: Conversations are remembered across sessions
- **Search Integration**: Real-time information retrieval using Tavily Search

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/LLM**: Azure OpenAI (GPT models)
- **Search**: Tavily Search API
- **Memory**: LangChain Conversation Buffer
- **Styling**: Custom CSS with responsive design

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd CommuVerse
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file or configure Streamlit secrets with:

   ```
   AZURE_OPENAI_ENDPOINT=your_azure_endpoint
   AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_API_VERSION=your_api_version
   TAVILY_API_KEY=your_tavily_api_key
   ```

4. **Run the application**
   ```bash
   streamlit run Home.py
   ```

## 🏗️ Project Structure

```
CommuVerse/
├── Home.py                          # Main application entry point
├── pages/                           # Community pages
│   ├── 🎨 Hobby Hub.py
│   ├── 📚 Study & Life Hack.py
│   ├── 🧘‍♀️ Mental Health & Wellness.py
│   ├── 🍽️ Meal Planner.py
│   ├── 🕴 Stranger Buddy.py
│   ├── 💰 Finance for Beginners.py
│   ├── 💅 Beauty & Skincare.py
│   ├── 🎉 Event Finder.py
│   └── 👗 Fashion & Style.py
├── prompts/                         # AI system prompts
│   ├── hobbyHub.py
│   ├── strangerFriend.py
│   ├── mealPlanner.py
│   ├── studyLifeHacks.py
│   ├── mentalHealthWellness.py
│   ├── financeBeginners.py
│   ├── beautySkincare.py
│   ├── eventFinder.py
│   └── fashionStyle.py
├── services/                        # Core services and utilities
│   ├── constants.py
│   ├── footer.py
│   ├── html_css.py
│   ├── llmUtils.py
│   ├── models.py
│   └── utils.py
├── assets/                          # Static assets
│   ├── CommuVerse.png
│   └── HobbyHub.png
└── requirements.txt                 # Python dependencies
```

## 🎯 How It Works

### AI Integration

Each community page features:

- **Specialized AI Assistant**: Custom-trained prompts for specific domains
- **Conversation Memory**: Maintains context across chat sessions
- **Real-time Search**: Access to current information via Tavily Search
- **Personalized Responses**: Tailored advice based on user input

### User Experience

1. **Home Page**: Browse communities with beautiful card interface
2. **Community Pages**: Interactive chat with domain-specific AI assistants
3. **Navigation**: Seamless switching between communities
4. **Responsive Design**: Works on desktop and mobile devices

## 🔧 Configuration

### Environment Variables

- `AZURE_OPENAI_ENDPOINT`: Azure OpenAI service endpoint
- `AZURE_OPENAI_DEPLOYMENT_NAME`: Model deployment name
- `AZURE_OPENAI_API_KEY`: API key for authentication
- `AZURE_OPENAI_API_VERSION`: API version
- `TAVILY_API_KEY`: Tavily search API key

### Customization

- **Prompts**: Modify `prompts/` files to customize AI behavior
- **Styling**: Update `services/html_css.py` for UI changes
- **Communities**: Add new communities in `Home.py` and create corresponding pages

## 🚀 Deployment

### Local Development

```bash
streamlit run Home.py
```

### Cloud Deployment

1. **Streamlit Cloud**: Connect your GitHub repository
2. **Heroku**: Use the provided `requirements.txt`
3. **AWS/GCP**: Deploy as a containerized application

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Saif Pasha**

- Instagram: [@_al_sxif_](https://www.instagram.com/_al_sxif_/)
- Snapchat: [saif_pasha](https://snapchat.com/t/wNqTJk9Q)
- LinkedIn: [Saif Pasha](https://www.linkedin.com/in/saif-pasha-59643b197/)
- GitHub: [alsaif1431](https://github.com/alsaif1431)

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- Azure OpenAI for powerful language models
- LangChain for AI/LLM orchestration
- Tavily for real-time search capabilities

---

**© 2023 CommuVerse. All rights reserved.**
