from phi.playground import Playground
from ai_agent import image_text_agent

app = Playground(agents=[image_text_agent]).get_app()

if __name__ == "__main__":
    from phi.playground import serve_playground_app
    serve_playground_app("playground:app", reload=True)
