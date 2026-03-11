from stt import test
from api import ask_llm
from tts import speak 
def main():
    print("Hello from tts!")
 #   print(sys.path)
    while True:
        text_user=test()
        print(text_user)
        response=ask_llm(text_user)
        print(response)
        speak(response)
        key = input("Presiona Enter para continuar o 'q' para salir: ")
        if key.lower() == "q":
            break
if __name__ == "__main__":
    main()
