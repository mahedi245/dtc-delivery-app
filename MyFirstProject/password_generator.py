import random
import string

def generate_password(length=12):
    print('-----------------------------------')
    print('   ✨ পাসওয়ার্ড জেনারেটর ✨   ')
    print('-----------------------------------')
    
    # পাসওয়ার্ডের জন্য অক্ষর, সংখ্যা এবং চিহ্ন
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # পছন্দমতো দৈঘ্যের পাসওয়ার্ড তৈরি
    password = ''.join(random.choice(chars) for _ in range(length))
    
    print(f'\nВаш новый надежный пароль / Your New Strong Password: \n\n➡️  {password}  ⬅️\n')
    print('-----------------------------------')

if __name__ == '__main__':
    generate_password(16)
