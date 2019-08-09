import time
import random
import hashlib

quasi_prime = 1153.5
wave_generation = 10
universal_integer = 42
time_entanglement = time.time()
octonian_symmetry_enabled = True
musical_resonance = 261.6256
shakespeare_reference_count = 37

def get_quantum_integer():
    print '[-] Generating Quantum Integer'
    time.sleep(3)
    feline_heart_rate = random.randint(140, 220)
    quantum_observation = random.randint(0,1)
    return feline_heart_rate * quantum_observation

def entangle_quasi_prime():
    print '[-] Initiating Entanglement of Quasi-Prime'
    time.sleep(2)
    print '[-] Applying Muscial Resonance'
    time.sleep(1)
    return (quasi_prime * time_entanglement * wave_generation) / musical_resonance

def artificial_intelligence_factorization(unintelligent_quasi_prime):
    print '[-] Connecting to AI ...'
    time.sleep(3)
    print '[-] AI Connected'
    time.sleep(1)
    print '[-] Populating HAL Model'
    time.sleep(3)
    print '[-] Deductive Factorization of Quasi Prime Complete'
    time.sleep(3)
    ai_initialization_vector = hashlib.md5(b'SGV5IFNpcmk=').hexdigest()[3]
    return int(ai_initialization_vector) * unintelligent_quasi_prime

def get_quantum_prime():
    entangled_quasi_prime = entangle_quasi_prime()
    intelligent_quasi_prime = artificial_intelligence_factorization(entangled_quasi_prime)
    quantum_addition = get_quantum_integer()
    quantum_prime = intelligent_quasi_prime + quantum_addition + shakespeare_reference_count
    return str(int(quantum_prime))

def encrypt_string(a, b):
    print '[-] Encrypting data ...'
    time.sleep(3)
    print '[-] 50% Progress'
    time.sleep(3)
    print '[-] Encryption complete.'
    time.sleep(1)
    f = lambda ss,cc: ''.join(chr(ord(s)^ord(c)) for s,c in zip(ss,cc*100))
    return f(a,b)

print 'CS Quantum AI Encryption'
print '========================'
clear_data = raw_input('Enter text to encrypt: ')
quantum_prime_key = get_quantum_prime()
encrypted_data = encrypt_string(clear_data, quantum_prime_key)

print '\n\nQuantum AI Encrypted Data Results'
print '================================='
print map(ord,encrypted_data)
