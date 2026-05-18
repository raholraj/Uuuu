[app]

# (str) गेम का नाम
title = MyGame

# (str) पैकेज का नाम (इसमें स्पेस नहीं होना चाहिए)
package.name = mygame

# (str) पैकेज का डोमेन
package.domain = org.adarsh

# (str) तुम्हारे कोड की डायरेक्टरी (यहाँ . का मतलब है वही फोल्डर)
source.dir = .

# (list) कौन-सी फाइलें गेम में शामिल करनी हैं
source.include_exts = py,png,jpg,jpeg,ttf,wav,mp3,ogg

# (str) गेम का वर्ज़न
version = 0.1

# (list) गेम चलाने के लिए ज़रूरी चीज़ें (एकदम पक्की सेटिंग्स)
requirements = python3, pygame-ce, cffi, pycparser, pymunk

# (str) स्क्रीन कैसी रहेगी (landscape या portrait)
orientation = landscape

# (bool) क्या गेम फुलस्क्रीन में चलेगा (1 = हाँ, 0 = ना)
fullscreen = 1

# (list) Android आर्किटेक्चर (सिर्फ 64-bit मॉडर्न फोन्स के लिए)
android.archs = arm64-v8a

# (str) NDK वर्ज़न (क्रैश रोकने के लिए)
android.ndk = 25b

# (bool) Android SDK लाइसेंस को अपने आप Yes करने के लिए
android.accept_sdk_license = True
