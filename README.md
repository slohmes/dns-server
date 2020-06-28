# dns-server
Toy recursive DNS server written in Python!

Created with <3 alongside the Recurse Center community: recurse.com 

Still WIP.

TODO for MVP:
* replace UDP packets saved in example-packets with actual DNS messages, 
  probably sent via `dig` and intercepted via `nc`.
* Finish parsing DNS messages -- don't necessarily need to parse everything properly, 
  could read just the `question` and `answer` fields, as appropriate.
* Implement logic to send and interpret requests to root server, TLD (top-level domain) servers, and name authority servers.

Stretch goals:
* add caching (this is arguably MVP, but this also a toy implementation purely for fun)

Resources:
* Julia Evans' great blog post: https://jvns.ca/blog/how-updating-dns-works/
* The official RFC (section 4.1 is where the DNS message format is defined): https://tools.ietf.org/html/rfc1035
* An extremely cute comic on how DNS works! https://howdns.works/
