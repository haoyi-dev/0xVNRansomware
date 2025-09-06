import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
import threading
import time
import random
import sys
import os
import winsound
from datetime import datetime, timedelta

class FakeRansomware:
    def __init__(self):
        self.root = tk.Tk()
        self.esc_count = 0
        self.colors = ['#FF0000', '#FF3333', '#FF6666', '#FF9999', '#FFCCCC']
        self.current_color_index = 0
        self.encrypted_files = []
        self.progress_value = 0
        self.deadline = datetime.now() + timedelta(days=3)
        self.setup_window()
        self.setup_ui()
        self.start_animations()
        self.play_startup_sound()
        
    def setup_window(self):
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.configure(bg='#8B0000')
        self.root.title("0xVN Ransomware")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind('<Escape>', self.on_escape)
        self.root.focus_set()
        
    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg='#8B0000')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        header_frame = tk.Frame(main_frame, bg='#000000', relief='raised', bd=2)
        header_frame.pack(fill='x', pady=(0, 10))
        
        title_frame = tk.Frame(header_frame, bg='#000000')
        title_frame.pack(pady=10)
        
        skull_label = tk.Label(title_frame, text="💀", font=("Arial", 48), fg="red", bg="black")
        skull_label.pack(side='left', padx=10)
        
        self.title_label = tk.Label(
            title_frame,
            text="0xVN Ransomware",
            font=("Arial", 32, "bold"),
            fg="#FF0000",
            bg="black"
        )
        self.title_label.pack(side='left', padx=10)
        
        content_frame = tk.Frame(main_frame, bg='#8B0000')
        content_frame.pack(fill='both', expand=True)
        
        left_panel = tk.Frame(content_frame, bg='#000000', relief='sunken', bd=2)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        tk.Label(left_panel, text="Tệp Đã Mã Hóa:", font=("Arial", 14, "bold"), 
                fg="white", bg="black").pack(pady=5)
        
        self.file_listbox = scrolledtext.ScrolledText(
            left_panel, 
            height=15, 
            width=50,
            bg='black', 
            fg='#00FF00',
            font=("Courier", 10),
            state='disabled'
        )
        self.file_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        right_panel = tk.Frame(content_frame, bg='#000000', relief='sunken', bd=2)
        right_panel.pack(side='right', fill='y', padx=(10, 0))
        
        payment_frame = tk.Frame(right_panel, bg='black')
        payment_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(payment_frame, text="💰 YÊU CẦU THANH TOÁN 💰", 
                font=("Arial", 16, "bold"), fg="yellow", bg="black").pack()
        
        tk.Label(payment_frame, text="Số Tiền: $300 USD", 
                font=("Arial", 14), fg="white", bg="black").pack(pady=5)
        
        tk.Label(payment_frame, text="Địa Chỉ Bitcoin:", 
                font=("Arial", 12), fg="white", bg="black").pack()
        
        bitcoin_entry = tk.Entry(payment_frame, width=35, font=("Courier", 10))
        bitcoin_entry.insert(0, "1Fake0xVN123BitcoinAddress456VN")
        bitcoin_entry.config(state='readonly')
        bitcoin_entry.pack(pady=5)
        
        countdown_frame = tk.Frame(right_panel, bg='black')
        countdown_frame.pack(fill='x', padx=10, pady=20)
        
        tk.Label(countdown_frame, text="⏰ THỜI GIAN CÒN LẠI:", 
                font=("Arial", 14, "bold"), fg="red", bg="black").pack()
        
        self.countdown_label = tk.Label(
            countdown_frame,
            text="72:00:00",
            font=("Arial", 24, "bold"),
            fg="#FF0000",
            bg="black"
        )
        self.countdown_label.pack(pady=10)
        
        warning_frame = tk.Frame(right_panel, bg='black')
        warning_frame.pack(fill='x', padx=10, pady=10)
        
        warnings = [
            "⚠️ KHÔNG được khởi động lại máy tính!",
            "⚠️ KHÔNG được xóa chương trình này!",
            "⚠️ Tệp sẽ bị mất sau khi hết thời gian!"
        ]
        
        for warning in warnings:
            tk.Label(warning_frame, text=warning, font=("Arial", 10, "bold"), 
                    fg="orange", bg="black", wraplength=200).pack(pady=2)
        
        progress_frame = tk.Frame(main_frame, bg='#000000', relief='raised', bd=2)
        progress_frame.pack(fill='x', pady=10)
        
        tk.Label(progress_frame, text="Tiến Trình Mã Hóa:", 
                font=("Arial", 12, "bold"), fg="white", bg="black").pack(pady=5)
        
        self.progress_bar = ttk.Progressbar(
            progress_frame, 
            length=600, 
            mode='determinate',
            style='Red.Horizontal.TProgressbar'
        )
        self.progress_bar.pack(pady=5)
        
        self.progress_label = tk.Label(
            progress_frame,
            text="Đang mã hóa tệp... 0%",
            font=("Arial", 10),
            fg="lime",
            bg="black"
        )
        self.progress_label.pack(pady=5)
        
        self.secret_label = tk.Label(
            main_frame,
            text="ESC x3 to exit prank",
            font=("Arial", 8),
            fg="#330000",
            bg="#8B0000"
        )
        self.secret_label.pack(side="bottom", anchor="se")
        
    def start_animations(self):
        self.animate_colors()
        self.fake_countdown()
        self.update_progress()
        self.show_encrypted_files()
        self.configure_progress_style()
        
    def animate_colors(self):
        color = self.colors[self.current_color_index]
        self.title_label.configure(fg=color)
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        self.root.after(300, self.animate_colors)
        
    def fake_countdown(self):
        current_time = self.countdown_label.cget("text")
        hours, minutes, seconds = map(int, current_time.split(':'))
        
        if seconds > 0:
            seconds -= 1
        elif minutes > 0:
            minutes -= 1
            seconds = 59
        elif hours > 0:
            hours -= 1
            minutes = 59
            seconds = 59
        else:
            hours, minutes, seconds = 71, 59, 59
            
        new_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.countdown_label.configure(text=new_time)
        
        if hours == 0:
            current_color = self.countdown_label.cget("fg")
            new_color = "#FFFF00" if current_color == "#FF0000" else "#FF0000"
            self.countdown_label.configure(fg=new_color)
        
        self.root.after(1000, self.fake_countdown)
        
    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += random.randint(1, 3)
            if self.progress_value > 100:
                self.progress_value = 100
                
        self.progress_bar['value'] = self.progress_value
        self.progress_label.configure(text=f"Đang mã hóa tệp... {self.progress_value}%")
        
        if self.progress_value >= 100:
            self.root.after(2000, lambda: setattr(self, 'progress_value', 0))
        
        self.root.after(200, self.update_progress)
        
    def show_encrypted_files(self):
        fake_files = [
            "C:\\Users\\Documents\\anh_gia_dinh.jpg.0xvn",
            "C:\\Users\\Desktop\\tai_lieu_quan_trong.pdf.0xvn", 
            "C:\\Users\\Downloads\\video_du_lich.mp4.0xvn",
            "C:\\Windows\\System32\\drivers\\audio.sys.0xvn",
            "C:\\Program Files\\Microsoft Office\\excel.exe.0xvn",
            "C:\\Users\\Music\\bai_hat_yeu_thich.mp3.0xvn",
            "C:\\Users\\Pictures\\anh_cuoi.png.0xvn",
            "D:\\Backup\\ho_so_tai_chinh.xlsx.0xvn",
            "C:\\Users\\Documents\\luan_van.docx.0xvn",
            "C:\\Games\\Steam\\game_saves.dat.0xvn"
        ]
        
        if len(self.encrypted_files) < len(fake_files):
            new_file = fake_files[len(self.encrypted_files)]
            self.encrypted_files.append(new_file)
            
            self.file_listbox.config(state='normal')
            self.file_listbox.insert('end', f"[ĐÃ MÃ HÓA] {new_file}\n")
            self.file_listbox.see('end')
            self.file_listbox.config(state='disabled')
            
        delay = random.randint(1000, 3000)
        self.root.after(delay, self.show_encrypted_files)
        
    def configure_progress_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Red.Horizontal.TProgressbar", 
                       background='red',
                       troughcolor='darkred',
                       borderwidth=1,
                       lightcolor='red',
                       darkcolor='darkred')
        
    def play_startup_sound(self):
        try:
            winsound.MessageBeep(winsound.MB_ICONHAND)
            self.root.after(2000, lambda: winsound.MessageBeep(winsound.MB_ICONEXCLAMATION))
        except:
            pass
        
    def on_escape(self, event):
        self.esc_count += 1
        print(f"ESC pressed {self.esc_count} times")
        
        if self.esc_count == 1:
            self.show_warning("Nhấn ESC thêm 2 lần nữa để thoát...")
        elif self.esc_count == 2:
            self.show_warning("Nhấn ESC thêm 1 lần nữa để thoát...")
        elif self.esc_count >= 3:
            self.exit_program()
            
    def show_warning(self, message):
        warning_label = tk.Label(
            self.root,
            text=message,
            font=("Arial", 14),
            fg="white",
            bg="red"
        )
        warning_label.place(x=10, y=10)
        self.root.after(2000, warning_label.destroy)
        
    def exit_program(self):
        reveal_window = tk.Toplevel(self.root)
        reveal_window.title("Trò Đùa Bị Phát Hiện!")
        reveal_window.geometry("500x400")
        reveal_window.configure(bg='#00FF00')
        reveal_window.attributes('-topmost', True)
        
        reveal_window.geometry("+{}+{}".format(
            int(reveal_window.winfo_screenwidth()/2 - 250),
            int(reveal_window.winfo_screenheight()/2 - 200)
        ))
        
        tk.Label(reveal_window, text="🎉 ĐÃ LỪA ĐƯỢC! 🎉", 
                font=("Arial", 32, "bold"), fg="red", bg="#00FF00").pack(pady=20)
        
        tk.Label(reveal_window, text="Đây chỉ là một trò đùa vô hại!", 
                font=("Arial", 16, "bold"), fg="black", bg="#00FF00").pack(pady=10)
        
        tk.Label(reveal_window, text="✅ Không có tệp nào bị mã hóa\n✅ Không gây hại cho máy tính\n✅ Hoàn toàn an toàn và có thể phục hồi", 
                font=("Arial", 12), fg="darkgreen", bg="#00FF00", justify="left").pack(pady=10)
        
        tk.Label(reveal_window, text="Hy vọng bạn đã vui! 😄\nHãy nhớ: Không bao giờ tin tưởng các chương trình đáng nghi!", 
                font=("Arial", 14), fg="black", bg="#00FF00", justify="center").pack(pady=20)
        
        try:
            winsound.MessageBeep(winsound.MB_OK)
        except:
            pass
            
        tk.Button(reveal_window, text="Đóng Trò Đùa", font=("Arial", 14, "bold"),
                 bg="red", fg="white", command=self.close_all).pack(pady=20)
        
        reveal_window.after(10000, self.close_all)
        
    def close_all(self):
        self.root.destroy()
        sys.exit()
        
    def on_closing(self):
        pass
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ransomware = FakeRansomware()
    ransomware.run()
