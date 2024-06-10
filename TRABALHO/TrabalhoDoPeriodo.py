import RPi.GPIO as GPIO
import time
import random

GPIO.setwarnings(False)

LED_PIN = 17
BUTTON_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
    reaction_times = []

    try:
        for attempt in range(5):
            GPIO.output(LED_PIN, GPIO.LOW)

            delay = random.uniform(1, 5)
            time.sleep(delay)

            GPIO.output(LED_PIN, GPIO.HIGH)

            start_time = time.time()
            
            while GPIO.input(BUTTON_PIN) == GPIO.LOW:
                time.sleep(0.01) 
            
            reaction_time = time.time() - start_time
            reaction_times.append(reaction_time)
            GPIO.output(LED_PIN, GPIO.LOW)
            print("Botão pressionado. Tempo de reação: {:.3f} segundos".format(reaction_time))

            time.sleep(2)
        
        average_time = sum(reaction_times) / len(reaction_times)
        max_time = max(reaction_times)
        min_time = min(reaction_times)

        print("\nResumo das tentativas:")
        print("Tempo médio de reação: {:.3f} segundos".format(average_time))
        print("Tempo máximo de reação: {:.3f} segundos".format(max_time))
        print("Tempo mínimo de reação: {:.3f} segundos".format(min_time))

    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    except Exception as e:
        print("Ocorreu um erro: {}".format(e))
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()