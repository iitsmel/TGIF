#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/random.html
# https://docs.python.org/3/library/secrets.html#module-secrets

import random
import secrets
import string

# random

# knowhow
# bookkeeping
random.seed(123)
internal_state = random.getstate()
random.setstate(internal_state)

# bytes
random_bytes = random.randbytes(5)
print(f"randbytes           : {random_bytes}")

# integers
random_range_value = random.randrange(1, 10, 2)
random_integer = random.randint(1, 10)
random_bits = random.getrandbits(8)
print(f"randrange           : {random_range_value}")
print(f"randint             : {random_integer}")
print(f"getrandbits         : {random_bits}")

# sequences
random_choice = random.choice(['a', 'b', 'c'])
random_choices = random.choices(['a', 'b', 'c'], weights=[10,5,1], k=3)
list_to_shuffle = [1, 2, 3, 4]
random.shuffle(list_to_shuffle)
random_sample = random.sample(range(20), 5, counts=[1]*20)
print(f"choice              : {random_choice}")
print(f"choices             : {random_choices}")
print(f"shuffle             : {list_to_shuffle}")
print(f"sample              : {random_sample}")

# discrete distributions
binomial_value = random.binomialvariate(10, 0.5)
print(f"binomialvariate     : {binomial_value}")

# real-valued distributions
random_value = random.random()
uniform_value = random.uniform(1.0, 5.0)
triangular_value = random.triangular(1.0, 10.0, 5.0)
beta_value = random.betavariate(0.5, 0.5)
exponential_value = random.expovariate(1.0)
gamma_value = random.gammavariate(1.0, 1.0)
gaussian_value = random.gauss(0, 1)
normal_value = random.normalvariate(0, 1)
lognormal_value = random.lognormvariate(0, 1)
vonmises_value = random.vonmisesvariate(0, 1)
pareto_value = random.paretovariate(1.5)
weibull_value = random.weibullvariate(1, 1)
print(f"random              : {random_value}")
print(f"uniform             : {uniform_value}")
print(f"triangular          : {triangular_value}")
print(f"betavariate         : {beta_value}")
print(f"expovariate         : {exponential_value}")
print(f"gammavariate        : {gamma_value}")
print(f"gauss               : {gaussian_value}")
print(f"normalvariate       : {normal_value}")
print(f"lognormvariate      : {lognormal_value}")
print(f"vonmisesvariate     : {vonmises_value}")
print(f"paretovariate       : {pareto_value}")
print(f"weibullvariate      : {weibull_value}")

# payload automation
proceed = input("Proceed to payload automation? (y/n): ").strip().lower()
if proceed == 'y':
    digits = string.digits
    letters = string.ascii_letters
    specials = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    payload = [
        random.choice(digits),                       
        *[random.choice(letters) for _ in range(4)],  
        random.choice(specials),                     
        random.choice(digits),                       
        *[random.choice(letters) for _ in range(3)]  
    ]

    random_sequence = ''.join(payload)
    print(random_sequence)

    all_chars = string.ascii_letters + string.digits + specials
    random_sequence2 = ''.join(random.choice(all_chars) for _ in range(10))
    print(random_sequence2)


print()


# secrets
secret_token_bytes = secrets.token_bytes(16)
secret_token_hex = secrets.token_hex(16)
secret_token_urlsafe = secrets.token_urlsafe(16)
secret_choice = secrets.choice(['one', 'two', 'three'])
secret_randbelow = secrets.randbelow(100)
secret_randbits = secrets.randbits(16)
print(f"secrets.token_bytes  : {secret_token_bytes}")
print(f"secrets.token_hex    : {secret_token_hex}")
print(f"secrets.token_urlsafe: {secret_token_urlsafe}")
print(f"secrets.choice       : {secret_choice}")
print(f"secrets.randbelow    : {secret_randbelow}")
print(f"secrets.randbits     : {secret_randbits}")

# https://docs.python.org/3/library/secrets.html#recipes-and-best-practices
# 8-character alphanumeric password
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for _ in range(12))
print(f"secure password      : {password}")

# 10-character password with conditions
while True:
    complex_password = ''.join(secrets.choice(alphabet) for _ in range(12))
    if (any(c.islower() for c in complex_password)
            and any(c.isupper() for c in complex_password)
            and sum(c.isdigit() for c in complex_password) >= 3):
        break
print(f"complex password     : {complex_password}")
