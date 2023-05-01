import os

input_file = input("Enter the location of the input file: ")
if not os.path.isfile(input_file):
    print(f"Error: {input_file} does not exist.")
    exit()

for domain in open(input_file, "r"):
    domain = domain.strip()

    use_cewl = input(f"Do you want to use CeWL for {domain}? (y/n): ")
    if use_cewl.lower() == "y":
        cewl_output_file = f"{domain}_CeWL.txt"
        os.system(f"cewl {domain} -w {cewl_output_file}")

       

    use_harvester = input(f"Do you want to use theHarvester for {domain}? (y/n): ")
    if use_harvester.lower() == "y":
        harvester_output_file = f"{domain}_theHarvester.txt"
        os.system(f"theHarvester -d {domain} -l 500 -b all -f {harvester_output_file}")

    use_dnsrecon = input(f"Do you want to use dnsrecon for {domain}? (y/n): ")
    if use_dnsrecon.lower() == "y":
        wordlist = input(f"Enter the location of the wordlist to use for dnsrecon for {domain} (press enter to skip): ")
        if os.path.isfile(wordlist):
            dnsrecon_output_file = f"{domain}_dnsrecon.txt"
            os.system(f"dnsrecon -d {domain} -w {wordlist} -t brt -a -c -j -o {dnsrecon_output_file}")

    use_nmap = input(f"Do you want to use nmap for {domain}? (y/n): ")
    if use_nmap.lower() == "y":
        nmap_output_file = f"{domain}_nmap.txt"
        os.system(f"nmap -p- --script vuln {domain} -oN {nmap_output_file}")

        wordlist = input(f"Enter the location of the wordlist to use for subfinder for {domain} (press enter to skip): ")
        if os.path.isfile(wordlist):
            subfinder_output_file = f"{domain}_subfinder.txt"
            os.system(f"subfinder -d {domain} -w {wordlist} -o {subfinder_output_file}")
        if os.path.isfile(cewl_output_file):
            subfinder_output_file = f"{domain}_subfinder_CeWL.txt"
            os.system(f"subfinder -d {domain} -w {cewl_output_file} -o {subfinder_output_file}")
