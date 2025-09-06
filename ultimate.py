import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
import threading
import time
import random
import sys
import os
import winsound
from datetime import datetime, timedelta

class WannaCryPrankUltimate:
    def __init__(self):
        self.root = tk.Tk()
        self.esc_count = 0
        self.colors = ['#FF0000', '#FF3333', '#FF6666', '#FF9999', '#FFCCCC']
        self.current_color_index = 0
        self.encrypted_files = []
        self.progress_value = 0
        self.matrix_chars = "01"
        self.matrix_drops = []
        self.setup_window()
        self.setup_ui()
        self.start_animations()
        self.play_startup_sound()
        self.create_matrix_effect()
        
    def setup_window(self):
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.configure(bg='#000000')
        self.root.title("0xVN Ransomware - ULTIMATE")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind('<Escape>', self.on_escape)
        self.root.focus_set()
        
    def create_matrix_effect(self):

        self.matrix_canvas = tk.Canvas(
            self.root, 
            width=self.root.winfo_screenwidth(),
            height=self.root.winfo_screenheight(),
            bg='black',
            highlightthickness=0
        )
        self.matrix_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        

        cols = self.root.winfo_screenwidth() // 10
        for i in range(cols):
            self.matrix_drops.append(0)
            
        self.animate_matrix()
        
    def animate_matrix(self):
        self.matrix_canvas.delete("matrix")
        

        for i in range(len(self.matrix_drops)):
            text = random.choice(self.matrix_chars)
            x = i * 10
            y = self.matrix_drops[i] * 10
            

            color = f"#00{random.randint(50, 255):02x}00"
            
            self.matrix_canvas.create_text(
                x, y, text=text, fill=color, 
                font=("Courier", 10), tags="matrix"
            )
            

            if y > self.root.winfo_screenheight() and random.random() > 0.975:
                self.matrix_drops[i] = 0
            else:
                self.matrix_drops[i] += 1
                
        self.root.after(50, self.animate_matrix)
        
    def setup_ui(self):

        main_frame = tk.Frame(self.root, bg='#8B0000', relief='raised', bd=5)
        main_frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)
        

        self.main_frame = main_frame
        self.flash_border()
        

        header_frame = tk.Frame(main_frame, bg='#000000', relief='raised', bd=3)
        header_frame.pack(fill='x', pady=(0, 10))
        
        title_frame = tk.Frame(header_frame, bg='#000000')
        title_frame.pack(pady=15)
        
        skull_frame = tk.Frame(title_frame, bg='#000000')
        skull_frame.pack(side='left', padx=20)
        
        self.skull_labels = []
        skull_emojis = ["💀", "☠️", "💀", "☠️", "💀"]
        for i, emoji in enumerate(skull_emojis):
            skull = tk.Label(skull_frame, text=emoji, font=("Arial", 24), fg="red", bg="black")
            skull.pack(side='top', pady=2)
            self.skull_labels.append(skull)
        
        title_container = tk.Frame(title_frame, bg='#000000')
        title_container.pack(side='left', padx=20)
        
        shadow_title = tk.Label(
            title_container,
            text="0xVN Ransomware",
            font=("Impact", 36, "bold"),
            fg="#330000",
            bg="black"
        )
        shadow_title.place(x=3, y=3)
        
        self.title_label = tk.Label(
            title_container,
            text="0xVN Ransomware",
            font=("Impact", 36, "bold"),
            fg="#FF0000",
            bg="black"
        )
        self.title_label.pack()
        
        danger_frame = tk.Frame(title_frame, bg='#000000')
        danger_frame.pack(side='right', padx=20)
        
        danger_symbols = ["⚠️", "☢️", "⚡", "🔥", "💥"]
        self.danger_labels = []
        for symbol in danger_symbols:
            danger = tk.Label(danger_frame, text=symbol, font=("Arial", 24), fg="yellow", bg="black")
            danger.pack(side='top', pady=2)
            self.danger_labels.append(danger)
        

        content_frame = tk.Frame(main_frame, bg='#8B0000')
        content_frame.pack(fill='both', expand=True, padx=10)
        
    
        left_panel = tk.Frame(content_frame, bg='#000000', relief='sunken', bd=3)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 5))
        
        tk.Label(left_panel, text="🔒 TỆP ĐÃ MÃ HÓA 🔒", 
                font=("Arial", 14, "bold"), fg="red", bg="black").pack(pady=5)
        
        self.file_listbox = scrolledtext.ScrolledText(
            left_panel, height=12, width=45, bg='black', fg='#00FF00',
            font=("Courier", 9), state='disabled', wrap='word'
        )
        self.file_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        

        middle_panel = tk.Frame(content_frame, bg='#000000', relief='sunken', bd=3)
        middle_panel.pack(side='left', fill='y', padx=5)
        
    
        payment_header = tk.Frame(middle_panel, bg='black')
        payment_header.pack(fill='x', padx=10, pady=10)
        
        self.payment_title = tk.Label(payment_header, text="💰 PAYMENT REQUIRED 💰", 
                font=("Arial", 16, "bold"), fg="yellow", bg="black")
        self.payment_title.pack()
            
        tk.Label(middle_panel, text="Số tiền: 1000000 VNĐ   ", 
                font=("Arial", 14, "bold"), fg="white", bg="black").pack(pady=5)
        
        tk.Label(middle_panel, text="Phương thức thanh toán: Bitcoin Only", 
                font=("Arial", 12), fg="red", bg="black").pack(pady=2)
        

        tk.Label(middle_panel, text="Địa chỉ Bitcoin:", 
                font=("Arial", 12, "bold"), fg="white", bg="black").pack(pady=(10, 2))
        
        bitcoin_frame = tk.Frame(middle_panel, bg='black')
        bitcoin_frame.pack(pady=5)
        
        self.bitcoin_entry = tk.Entry(bitcoin_frame, width=30, font=("Courier", 10),
                                     bg='#333333', fg='yellow', state='readonly')
        self.bitcoin_entry.pack(side='left', padx=2)
        self.bitcoin_entry.insert(0, "HaoyiDeveloper")
        
        copy_btn = tk.Button(bitcoin_frame, text="📋", font=("Arial", 10),
                           bg='red', fg='white', command=self.copy_bitcoin)
        copy_btn.pack(side='left', padx=2)
        

        qr_frame = tk.Frame(middle_panel, bg='white', width=120, height=120)
        qr_frame.pack(pady=10)
        qr_frame.pack_propagate(False)
        

        qr_text = "█ ▄▀█▄ █\n▄ █▀▄▀ ▄\n█▄ ▀█▀ █\n ▀▄█▄▀▄ \n█ ▄▀█▄ █"
        tk.Label(qr_frame, text=qr_text, font=("Courier", 8), bg='white').pack(expand=True)
        

        right_panel = tk.Frame(content_frame, bg='#000000', relief='sunken', bd=3)
        right_panel.pack(side='right', fill='y', padx=(5, 0))
        
    
        countdown_frame = tk.Frame(right_panel, bg='black')
        countdown_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(countdown_frame, text="⏰ TIME REMAINING ⏰", 
                font=("Arial", 14, "bold"), fg="red", bg="black").pack()
        
        self.countdown_label = tk.Label(
            countdown_frame, text="72:00:00", font=("Digital-7", 28, "bold"),
            fg="#FF0000", bg="black", relief='sunken', bd=2
        )
        self.countdown_label.pack(pady=10)
        
    
        threat_frame = tk.Frame(right_panel, bg='black')
        threat_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(threat_frame, text="🚨 THREAT LEVEL 🚨", 
                font=("Arial", 12, "bold"), fg="red", bg="black").pack()
        
        self.threat_label = tk.Label(threat_frame, text="CRITICAL", 
                font=("Arial", 20, "bold"), fg="red", bg="black")
        self.threat_label.pack()
        

        warning_frame = tk.Frame(right_panel, bg='black')
        warning_frame.pack(fill='x', padx=10, pady=10)
        
        warnings = [
            "⚠️ Files will be deleted in 72h",
            "🚫 Do NOT restart computer", 
            "🔒 Do NOT close this program",
            "💻 Do NOT disconnect internet",
            "📞 Do NOT contact authorities"
        ]
        
        for warning in warnings:
            label = tk.Label(warning_frame, text=warning, font=("Arial", 9, "bold"), 
                           fg="orange", bg="black", wraplength=180, justify='left')
            label.pack(pady=1, anchor='w')
        

        progress_frame = tk.Frame(main_frame, bg='#000000', relief='raised', bd=3)
        progress_frame.pack(fill='x', pady=10)
        

        tk.Label(progress_frame, text="🔄 SYSTEM STATUS 🔄", 
                font=("Arial", 12, "bold"), fg="white", bg="black").pack(pady=5)
        

        encryption_frame = tk.Frame(progress_frame, bg='black')
        encryption_frame.pack(fill='x', padx=10, pady=2)
        
        tk.Label(encryption_frame, text="Encryption:", font=("Arial", 10), 
                fg="white", bg="black").pack(side='left')
        
        self.encryption_progress = ttk.Progressbar(
            encryption_frame, length=300, mode='determinate'
        )
        self.encryption_progress.pack(side='left', padx=10)
        
        self.encryption_label = tk.Label(encryption_frame, text="0%", 
                font=("Arial", 10), fg="lime", bg="black")
        self.encryption_label.pack(side='right')
        

        key_frame = tk.Frame(progress_frame, bg='black')
        key_frame.pack(fill='x', padx=10, pady=2)
        
        tk.Label(key_frame, text="Key Generation:", font=("Arial", 10), 
                fg="white", bg="black").pack(side='left')
        
        self.key_progress = ttk.Progressbar(
            key_frame, length=300, mode='indeterminate'
        )
        self.key_progress.pack(side='left', padx=10)
        self.key_progress.start(20)
        
        tk.Label(key_frame, text="Active", font=("Arial", 10), 
                fg="yellow", bg="black").pack(side='right')
        

        self.secret_label = tk.Label(
            main_frame, text="ESC x3", font=("Arial", 6),
            fg="#220000", bg="#8B0000"
        )
        self.secret_label.place(relx=0.99, rely=0.99, anchor='se')
        
    def flash_border(self):

        colors = ['#8B0000', '#FF0000', '#8B0000', '#AA0000']
        color = colors[random.randint(0, len(colors)-1)]
        self.main_frame.configure(bg=color)
        self.root.after(500, self.flash_border)
        
    def copy_bitcoin(self):

        messagebox.showwarning("Clipboard", "Bitcoin address copied!\n(Just kidding, this is fake!)")
        
    def start_animations(self):
        self.animate_colors()
        self.fake_countdown()
        self.update_progress()
        self.show_encrypted_files()
        self.animate_skulls()
        self.animate_payment()
        self.animate_threat()
        
    def animate_colors(self):
        color = self.colors[self.current_color_index]
        self.title_label.configure(fg=color)
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        self.root.after(200, self.animate_colors)
        
    def animate_skulls(self):

        for skull in self.skull_labels:
            if random.random() > 0.7:
                current_color = skull.cget("fg")
                new_color = "white" if current_color == "red" else "red"
                skull.configure(fg=new_color)
        self.root.after(300, self.animate_skulls)
        
    def animate_payment(self):

        colors = ["yellow", "orange", "red", "yellow"]
        color = colors[random.randint(0, len(colors)-1)]
        self.payment_title.configure(fg=color)
        self.root.after(400, self.animate_payment)
        
    def animate_threat(self):

        levels = ["CRITICAL", "MAXIMUM", "EXTREME", "CRITICAL"]
        colors = ["red", "orange", "yellow", "red"]
        index = random.randint(0, len(levels)-1)
        self.threat_label.configure(text=levels[index], fg=colors[index])
        self.root.after(800, self.animate_threat)
        
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
        

        if hours == 0 and minutes < 30:
            colors = ["#FF0000", "#FFFF00", "#FF0000"]
            color = colors[seconds % 3]
            self.countdown_label.configure(fg=color)
            
        self.root.after(1000, self.fake_countdown)
        
    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += random.randint(1, 4)
            if self.progress_value > 100:
                self.progress_value = 100
                
        self.encryption_progress['value'] = self.progress_value
        self.encryption_label.configure(text=f"{self.progress_value}%")
        
        if self.progress_value >= 100:
            self.root.after(3000, lambda: setattr(self, 'progress_value', 0))
            
        self.root.after(150, self.update_progress)
        
    def show_encrypted_files(self):
        fake_files = [
            "🔒 C:\\Users\\Documents\\ky_uc_gia_dinh_2023.jpg.0xvn",
            "🔒 C:\\Users\\Desktop\\bai_thuyet_trinh_quan_trong.pptx.0xvn",
            "🔒 C:\\Users\\Downloads\\phim_yeu_thich.mp4.0xvn", 
            "🔒 D:\\Photos\\album_cuoi\\*.jpg.0xvn",
            "🔒 C:\\Program Files\\Steam\\saves\\*.dat.0xvn",
            "🔒 C:\\Users\\Music\\nhac_yeu_thich\\*.mp3.0xvn",
            "🔒 C:\\Users\\Documents\\du_an_cong_viec.docx.0xvn",
            "🔒 C:\\Backup\\ho_so_tai_chinh.xlsx.0xvn",
            "🔒 C:\\Users\\Pictures\\anh_thoi_tho_au\\*.png.0xvn",
            "🔒 D:\\Games\\Minecraft\\worlds\\*.mcworld.0xvn",
            "🔒 C:\\Users\\Desktop\\vi_tien_dien_tu.dat.0xvn",
            "🔒 C:\\Users\\Documents\\mat_khau.txt.0xvn"
        ]
        
        if len(self.encrypted_files) < len(fake_files):
            new_file = fake_files[len(self.encrypted_files)]
            self.encrypted_files.append(new_file)
            
            self.file_listbox.config(state='normal')
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.file_listbox.insert('end', f"[{timestamp}] {new_file}\\n")
            self.file_listbox.see('end')
            self.file_listbox.config(state='disabled')
            
        delay = random.randint(2000, 5000)
        self.root.after(delay, self.show_encrypted_files)
        
    def play_startup_sound(self):
        try:

            winsound.MessageBeep(winsound.MB_ICONHAND)
            self.root.after(1000, lambda: winsound.MessageBeep(winsound.MB_ICONEXCLAMATION))
            self.root.after(2000, lambda: winsound.MessageBeep(winsound.MB_ICONHAND))
        except:
            pass
            
    def on_escape(self, event):
        self.esc_count += 1
        
        if self.esc_count == 1:
            self.show_warning("⚠️ Nhấn ESC thêm 2 lần nữa để thoát...")
        elif self.esc_count == 2:
            self.show_warning("⚠️ Nhấn ESC thêm 1 lần nữa để thoát...")

            try:
                winsound.MessageBeep(winsound.MB_ICONQUESTION)
            except:
                pass
        elif self.esc_count >= 3:
            self.exit_program()
            
    def show_warning(self, message):
        warning_label = tk.Label(
            self.root, text=message, font=("Arial", 16, "bold"),
            fg="white", bg="red", relief='raised', bd=3
        )
        warning_label.place(relx=0.5, y=50, anchor='center')
        self.root.after(3000, warning_label.destroy)
        
    def exit_program(self):

        reveal_window = tk.Toplevel(self.root)
        reveal_window.title("🎉 TRÙM TÙM PHÁT HIỆN! 🎉")
        reveal_window.geometry("600x500")
        reveal_window.configure(bg='#00AA00')
        reveal_window.attributes('-topmost', True)
        

        reveal_window.geometry("+{}+{}".format(
            int(reveal_window.winfo_screenwidth()/2 - 300),
            int(reveal_window.winfo_screenheight()/2 - 250)
        ))
        
        title_frame = tk.Frame(reveal_window, bg='#00AA00')
        title_frame.pack(pady=20)
        
        tk.Label(title_frame, text="🎉🎊🎉🎊🎉", font=("Arial", 24), 
                fg="gold", bg="#00AA00").pack()
        
        tk.Label(title_frame, text="GOTCHA!", font=("Impact", 42, "bold"), 
                fg="red", bg="#00AA00").pack()
        
        tk.Label(title_frame, text="🎊🎉🎊🎉🎊", font=("Arial", 24), 
                fg="gold", bg="#00AA00").pack()
        
    
        info_frame = tk.Frame(reveal_window, bg='white', relief='raised', bd=3)
        info_frame.pack(pady=20, padx=40, fill='x')
        
        tk.Label(info_frame, text="HAHAHAHHA", 
                font=("Arial", 18, "bold"), fg="green", bg="white").pack(pady=10)
        
        details = """
✅ No files were actually encrypted fake
✅ No damage to your computer  
✅ No data was accessed or stolen fake
✅ Completely safe and reversible fake
✅ No internet connection was made fake
✅ No malware was installed fake

This is an educational demonstration of what 
ransomware LOOKS like - but this is 100% fake!
        """
        
        tk.Label(info_frame, text=details, font=("Arial", 11), 
                fg="darkgreen", bg="white", justify="left").pack(pady=10)
        
        tk.Label(reveal_window, text="Hy vọng bạn đã vui! 😄\\nLuôn cẩn thận với các chương trình sus!", 
                font=("Arial", 14, "bold"), fg="black", bg="#00AA00", justify="center").pack(pady=20)
        

        try:
            winsound.MessageBeep(winsound.MB_OK)
            reveal_window.after(500, lambda: winsound.MessageBeep(winsound.MB_OK))
        except:
            pass
            

        button_frame = tk.Frame(reveal_window, bg='#00AA00')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Close Prank", font=("Arial", 14, "bold"),
                 bg="red", fg="white", command=self.close_all, width=12).pack(side='left', padx=10)
        
        tk.Button(button_frame, text="Run Again", font=("Arial", 14, "bold"), 
                 bg="blue", fg="white", command=self.restart_prank, width=12).pack(side='left', padx=10)
        

        reveal_window.after(15000, self.close_all)
        
    def restart_prank(self):
        self.root.destroy()
        new_prank = WannaCryPrankUltimate()
        new_prank.run()
        
    def close_all(self):
        self.root.destroy()
        sys.exit()
        
    def on_closing(self):
        pass
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    prank = WannaCryPrankUltimate()
    prank.run()
