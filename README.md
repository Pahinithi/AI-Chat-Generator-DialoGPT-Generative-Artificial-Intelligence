# AI Chat Generator - DialoGPT Generative Artificial Intelligence

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How to Use](#how-to-use)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **AI Chat Generator** is a conversational AI model built using Microsoft's **DialoGPT-large**. It allows users to interact with an AI-powered chatbot that generates dynamic, human-like responses. This project is designed using **FastAPI** for the backend and **Hugging Face's Transformers** library to harness the power of DialoGPT.

**GitHub Repository**: [AI Chat Generator - DialoGPT](https://github.com/Pahinithi/AI-Chat-Generator-DialoGPT-Generative-Artificial-Intelligence)

## Features
- Real-time dynamic text generation using **DialoGPT-large**.
- **FastAPI** integration for high-performance backend services.
- Clean and intuitive UI with a form-based interaction.
- AI responses generated based on user input, leveraging state-of-the-art NLP technology.

## Demo
Check out the demo here:  
[Live Demo](https://your-demo-link-here.com)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Pahinithi/AI-Chat-Generator-DialoGPT-Generative-Artificial-Intelligence.git
    cd AI-Chat-Generator-DialoGPT-Generative-Artificial-Intelligence
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have **PyTorch** and **transformers** installed, as they are essential for running the DialoGPT model.

4. To start the app, use the following command:
    ```bash
    uvicorn app:app --reload
    ```

## How to Run
Once you have installed the dependencies, you can start the application by running:
```bash
uvicorn app:app --reload
```

After running the command, navigate to `http://127.0.0.1:8000` in your web browser to start interacting with the AI chatbot.

## How to Use
1. Open your web browser and visit `http://127.0.0.1:8000`.
2. On the homepage, enter a question or statement into the input box.
3. Click "Generate Response" to see the AI-generated reply.
4. The generated response will be displayed below the input section.

## Screenshots

<img width="1728" alt="AI02" src="https://github.com/user-attachments/assets/058fa590-7d48-48f6-9199-2fce174a2ab3">


## Technologies Used
- **FastAPI**: Fast and efficient web framework for building APIs.
- **Transformers (Hugging Face)**: To utilize the DialoGPT model for generating responses.
- **PyTorch**: Backend for the deep learning model.
- **Jinja2**: For templating the HTML pages.
- **HTML/CSS**: For creating a responsive and user-friendly frontend.


## Contributing
If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are always welcome!

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact

For any questions or support, please contact:

- **Name**: Pahirathan Nithilan
- **Email**: [nithilan32@gmail.com](mailto:nithilan32@gmail.com)
- **GitHub**: [Pahinithi](https://github.com/Pahinithi)
