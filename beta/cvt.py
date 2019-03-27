import subprocess

instr_beta = '''
            "bcb_3hhb18bqcandzueboeomyytqf6wgmxrt9twde3xbga79yhkozz88dr3qqhok",
            "bcb_3iarrwbi5fe7zp6adjgqx4fpopotbzxyo3659gebigxw79iny4qx8qz1i7zq",
            "bcb_3djb63zf4d7wexwthhroiahdyqincqymf896yks9kooh4o18iitbnguwmjzo",
            "bcb_11iqjc3h6we5emdbynf9mkxgxwx5skrqc1fcg4hehji6ib93nq6agwuudmm6",
            "bcb_1fqby8riam57frgpquoiur5363ufkgoddym7o74ff7u1zbrmtdgms6eoaxqk",
            "bcb_1peqzid67xyhronqheueoookpyqqg4c61eyxr8sdg8fqkk7iot1oiobf6pgg",
            "bcb_1mscbbq9qhamt1joz1g33wtffgqbdm9ce6g4w1iw9fo3w3cubuue1h4fi663",
            "bcb_1gu3i19ca83y53fatwb9xcnneei85pryi7tdni9emg1strk6s7oyhnasgj95",
            "bcb_1pk4qqykag14chpd89f83ykm55j5dkei8qr7z3j6ur3b6f83tymf4xh45e1y",
            "bcb_1qadj4837q3k7etgrxpgeezcgdr639xh1k3ygpj9fnj991xdtmz8gxsgszka"
'''

instr_live = '''

bcb_3zj11bh99obyehtr9cef3rxjy87psbg5xht8kpo9kxdinoxw7s3fqidqofwu
bcb_1ogwu5zqwyp7irteq34uk4ht8qxoks4tr8kn8fq6aittgi533sem9aukfxif
bcb_3b4hqx14n7kjr8nzh7cpqssgwhg7mma5orhqbwukwqwuow7ihfyi8xmz5zhc
bcb_1134anoxw3xn3mxd63rqdo35ce9g47rhm8rn1bzuak3dfrbo9yn344htqroh
bcb_34yaiodfrwpwmukzjadycgafb5dq9fjso8um6b438za7gmdiwjs8fhdjhenm
bcb_3iy9xzzci98edoswup6b79cy9d6nkhs5g4czj397izuknj6hu7atnu5i1j69
bcb_35ts8mzkx1ca1t781smecoqchyho8u8kir4o3r6qedumsirgmhuqn61x5d89
bcb_13431ny3r3qp4chyttrytttnu769yymceruw91cinsjw5zbe69byzr1skij6
'''

def cvt(s):
    # print(s)
    cmd = "/home/melnaquib/work/client/freelancer.com/bb/code/btcb_build_beta/btcb_node"
    # res = subprocess.run([cmd, '--account_get', '--key', s], stdout=subprocess.PIPE)
    res = subprocess.run([cmd, '--account_key', '--account', s], stdout=subprocess.PIPE)

    r = res.stdout.decode()
    r = r.replace("Account:", "").replace("Hex:", "").strip()
    return r


instr = instr_live
for s in instr.split("\n"):
    s = s.replace('"', '').replace(',', '').strip()
    if s:
        print('"' + cvt(s) + '",')