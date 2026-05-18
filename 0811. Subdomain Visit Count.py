def subdomainVisits(self, cpdomains):
        domain_count = {}

        for entry in cpdomains:
            count_str, domain = entry.split(" ")
            count = int(count_str)
            parts = domain.split(".")

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])

                if subdomain not in domain_count:
                    domain_count[subdomain] = 0

                domain_count[subdomain] += count

        result = []
        for domain, cnt in domain_count.items():
            result.append(str(cnt) + " " + domain)

        return result