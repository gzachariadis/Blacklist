# Top Level Domains (TLDs)

This folder contains a curated list of known malicious or suspicious **Top-level domains (TLDs)** sourced from various reputable threat intelligence and security organizations.

These TLDs are commonly associated with malicious activities such as **phishing**, **malware distribution**, **spam**, and other types of cyber threats.

## Introduction

Top-level domains (TLDs) are the final segment of a domain name, appearing after the last dot (e.g., .com, .org, .xyz). 

Certain TLDs are frequently abused by malicious actors due to their permissive registration policies, low costs, or lack of proper oversight.

The list is updated periodically based on new data and reports from various sources.

## Sources

The list of malicious TLDs has been sourced from the following trusted threat intelligence providers:

- Source: [Spamhaus](https://www.spamtitan.com/)
- Source: [SpamTitan](https://www.spamtitan.com/)
- Source: [Interisle](https://interisle.net/)
- Source: [DomainTools](https://whois.domaintools.com/)

## File Format

The TLDs are stored in text format, with one TLD per line, formatted as a regex to be used for [Pihole](https://pi-hole.net/).

Below is an example format:

```
(^|\.)cam$
(^|\.)club$
```

## Making use

This list of malicious TLDs can be used for a variety of cybersecurity applications, such as:

- Blocking or filtering access to known malicious TLDs.
- Integrating the TLD list into threat detection systems or firewalls.
- Enriching domain reputation checks or security monitoring systems.
- Enhancing phishing detection and mitigation strategies.

To integrate the list into your system, you can download the file and parse the TLDs for further use in any way you like.

## License

This repository is licensed under the MIT License. Use it freely for personal, educational, and professional purposes, but please credit the sources and contributors.
