import csv

print("\n🏠 घरभाडेकरूंसाठी वीज बिल कॅल्क्युलेटर 💡")
print("--------------------------------------------------")

# ---- पायरी १: मुख्य मीटरची माहिती ----
main_prev = int(input("मुख्य मीटरची जुनी रीडिंग टाका: "))
main_curr = int(input("मुख्य मीटरची नवीन रीडिंग टाका: "))
total_bill = int(input("या महिन्याचे एकूण बिल (₹): "))

main_units = main_curr - main_prev
print(f"\nमुख्य मीटरच्या एकूण युनिट: {main_curr} - {main_prev} = {main_units} युनिट")

# ---- पायरी २: प्रती युनिट दर (फ्लोअर व्हॅल्यू) ----
unit_value = int(total_bill / main_units)
print(f"या महिन्याचा प्रती युनिट दर: ₹{total_bill} ÷ {main_units} = ₹{unit_value} (फ्लोअर व्हॅल्यू)\n")

# ---- पायरी ३: भाडेकरू १ - योगिता चौव्हाण ----
print("भाडेकरू १️⃣ - योगिता चौव्हाण")
a_prev = int(input("जुनी रीडिंग: "))
a_curr = int(input("नवीन रीडिंग: "))
a_units = a_curr - a_prev
a_amount = a_units * unit_value
print(f"योगिता चौव्हाण यांच्या युनिट: {a_curr} - {a_prev} = {a_units} युनिट")
print(f"योगिता चौव्हाण यांचे बिल: {a_units} × ₹{unit_value} = ₹{a_amount}\n")

# ---- पायरी ४: भाडेकरू २ - गीता गोरे ----
print("भाडेकरू २️⃣ - गीता गोरे")
b_prev = int(input("जुनी रीडिंग: "))
b_curr = int(input("नवीन रीडिंग: "))
b_units = b_curr - b_prev
b_amount = b_units * unit_value
print(f"गीता गोरे यांच्या युनिट: {b_curr} - {b_prev} = {b_units} युनिट")
print(f"गीता गोरे यांचे बिल: {b_units} × ₹{unit_value} = ₹{b_amount}\n")

# ---- पायरी ५: भाडेकरू ३ - कृष्णा (उरलेली युनिट) ----
print("भाडेकरू ३️⃣ - कृष्णा (उरलेली युनिट)")
c_units = main_units - (a_units + b_units)
if c_units < 0:
    print("⚠️ त्रुटी: रीडिंगमध्ये काहीतरी चूक आहे. कृपया पुन्हा तपासा.")
    exit()
c_amount = c_units * unit_value
print(f"कृष्णा यांच्या युनिट: {main_units} - ({a_units} + {b_units}) = {c_units} युनिट")
print(f"कृष्णा यांचे बिल: {c_units} × ₹{unit_value} = ₹{c_amount}\n")

# ---- पायरी ६: एकूण सारांश ----
print("--------------------------------------------------")
print("💰 अंतिम बिल सारांश:")
print(f"योगिता चौव्हाण: ₹{a_amount}")
print(f"गीता गोरे: ₹{b_amount}")
print(f"कृष्णा: ₹{c_amount}")

total_sum = a_amount + b_amount + c_amount
diff = total_bill - total_sum
print(f"\nएकूण मिळून: ₹{total_sum}")
if diff == 0:
    print("✅ सर्व ठीक आहे — कुठलाही फरक नाही.")
else:
    print(f"⚠️ सूचना: एकूण बिलातून ₹{diff} चा फरक आहे (rounding मुळे).")

# ---- पायरी ७: निकाल CSV फाईलमध्ये जतन करा ----
with open('parinam_rounded_final_marathi.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["भाडेकरू नाव", "वापरलेल्या युनिट", "प्रती युनिट ₹", "एकूण बिल ₹"])
    writer.writerow(["योगिता चौव्हाण", a_units, unit_value, a_amount])
    writer.writerow(["गीता गोरे", b_units, unit_value, b_amount])
    writer.writerow(["कृष्णा", c_units, unit_value, c_amount])
    writer.writerow(["एकूण", a_units + b_units + c_units, "", total_sum])

print("\n📁 परिणाम 'parinam_rounded_final_marathi.csv' नावाने जतन केला आहे.")
print("--------------------------------------------------")

