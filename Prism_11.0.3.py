import struct

print("Нужна версия призмы кароче 11.0.3 иначе нон ворк")
patches = {
    0xB5B60: bytes([0xB0, 0x01, 0xC3, 0x24, 0x08]),
    0xEB18D: bytes([0x90, 0x90]),
    0xEB196: bytes([0xE9, 0x9F, 0x00, 0x00, 0x00, 0x90]),
}
with open("prismlauncher.exe", "rb") as f:
    data = bytearray(f.read())
for offset, new_bytes in patches.items():
    data[offset:offset+len(new_bytes)] = new_bytes
with open("prismlauncher.exe", "wb") as f:
    f.write(data)
