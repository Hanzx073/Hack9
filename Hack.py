import random
import requests
import json

# Fungsi untuk mengambil issueNumber dari API
def get_issue_number():
    url = "https://newapi.55lottertttapi.com/api/webapi/GetGameIssue"
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNzQwO>"
    }
    data = {
        "typeId": 30,
        "language": 1,
        "random": "9ba2756f3d6f4fe18eb701b2b1c879c8",
        "signature": "974836932C9A148CB9C8456D363A412B",
        "timestamp": 1740906221
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = response.json()
        return response_json["data"]["issueNumber"]
    else:
        print("Error fetching issue number.")
        return None

# Fungsi untuk memprediksi angka
def prediksi_angka():
    angka_acak = random.randint(0, 9)
    if angka_acak <= 4:
        keterangan = "small"
    else:
        keterangan = "big"
    return angka_acak, keterangan

# Fungsi utama
def main():
    while True:
        # Meminta input dari pengguna
        user_input = input("angka terakhir keluar: ")

        # Validasi input pengguna
        if not user_input.isdigit():
            print("Tolong masukkan angka yang valid.")
            continue

        tebakan = int(user_input)

        # Menampilkan hasil prediksi angka acak dan keterangan
        angka_acak, keterangan = prediksi_angka()
        print(f"hasil prediksi: {angka_acak} ({keterangan})")

        # Ambil issue number dari API dan tampilkan setelah hasil tebakan
        issue_number = get_issue_number()
        if issue_number:
            print(f"periode: {issue_number}\n")

if __name__ == "__main__":
    main()
  
