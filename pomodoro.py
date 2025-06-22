import time
import os
import sys
import platform
import threading

try:
    import winsound
except ImportError:
    winsound = None

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def beep():
    if winsound:
        winsound.Beep(1000, 500)
    else:
        # macOS, Linux
        print('\a', end='', flush=True)

def input_with_default(prompt, default):
    s = input(f"{prompt} (기본값: {default}): ")
    return int(s) if s.strip().isdigit() else default

def format_time(seconds):
    m, s = divmod(seconds, 60)
    return f"{m:02d}:{s:02d}"

def pomodoro_timer(work_min=25, short_break_min=5, long_break_min=15, cycles=4):
    session = 0
    try:
        while True:
            for i in range(1, cycles + 1):
                session += 1
                # Work session
                for t in range(work_min * 60, -1, -1):
                    clear_screen()
                    print(f"\n===== 뽀모도로 타이머 =====\n")
                    print(f"현재 세션: {session} / {cycles}")
                    print(f"집중 시간: {format_time(t)} 남음")
                    print("\nCtrl+C로 언제든 종료할 수 있습니다.")
                    time.sleep(1)
                beep()
                clear_screen()
                print(f"\n집중 세션 {session} 종료! 5분간 휴식하세요.")
                beep()
                time.sleep(2)
                # Short break
                if i < cycles:
                    for t in range(short_break_min * 60, -1, -1):
                        clear_screen()
                        print(f"\n===== 뽀모도로 타이머 =====\n")
                        print(f"현재 세션: {session} / {cycles}")
                        print(f"짧은 휴식: {format_time(t)} 남음")
                        print("\nCtrl+C로 언제든 종료할 수 있습니다.")
                        time.sleep(1)
                    beep()
                    clear_screen()
                    print(f"\n짧은 휴식 종료! 다시 집중하세요.")
                    beep()
                    time.sleep(2)
            # Long break
            clear_screen()
            print(f"\n{cycles}번의 뽀모도로가 끝났습니다! 15분간 긴 휴식 시간입니다.")
            beep()
            for t in range(long_break_min * 60, -1, -1):
                clear_screen()
                print(f"\n===== 뽀모도로 타이머 =====\n")
                print(f"긴 휴식: {format_time(t)} 남음")
                print("\nCtrl+C로 언제든 종료할 수 있습니다.")
                time.sleep(1)
            beep()
            clear_screen()
            print("\n긴 휴식이 끝났습니다! 뽀모도로 사이클이 모두 완료되었습니다. 수고하셨습니다!\n")
            beep()
            time.sleep(3)
            break
    except KeyboardInterrupt:
        clear_screen()
        print("\n뽀모도로 타이머가 안전하게 종료되었습니다. 수고하셨습니다!\n")
        beep()
        sys.exit(0)

def main():
    print("\n===== 뽀모도로 타이머 설정 =====\n")
    work_min = input_with_default("작업 시간(분)", 25)
    short_break_min = input_with_default("짧은 휴식 시간(분)", 5)
    long_break_min = input_with_default("긴 휴식 시간(분)", 15)
    cycles = input_with_default("긴 휴식까지의 작업 횟수", 4)
    print("\n설정이 완료되었습니다. 타이머를 시작합니다!\n")
    time.sleep(1)
    pomodoro_timer(work_min, short_break_min, long_break_min, cycles)

if __name__ == "__main__":
    main()
