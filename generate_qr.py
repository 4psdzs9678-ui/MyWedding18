"""
Генерирует QR-код со ссылкой на вашего бота.
Отсканировав его, гость сразу откроет чат с ботом и запустит /start.

Использование:
    python generate_qr.py your_bot_username
"""
import sys
import qrcode

def main():
    if len(sys.argv) < 2:
        print("Использование: python generate_qr.py <username_бота_без_@>")
        sys.exit(1)

    bot_username = sys.argv[1].lstrip("@")
    start_param = "wedding"  # можно изменить/убрать
    link = f"https://t.me/{bot_username}?start={start_param}"

    img = qrcode.make(link)
    out_path = "wedding_qr.png"
    img.save(out_path)
    print(f"Готово! Ссылка: {link}")
    print(f"QR-код сохранён в {out_path} — можно печатать.")

if __name__ == "__main__":
    main()
