## -*- coding: utf-8 -*-

Для каждого типа сервиса сделать тупо шаблоны, чтобы пользователю надо было вводить минимум данных.
После нажатия создать все необходимые записи будут создаваться автоматически

## https://support.godaddy.com/help/article/680/%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-dns-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%B0%D1%88%D0%B8%D1%85-%D0%B4%D0%BE%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D1%85-%D0%B8%D0%BC%D0%B5%D0%BD

web server
A
 CNAME
 AAAA
 TXT
NS

mail server
A record
MX record
 hostname  TTL RECORD_TYPE DESTINATION  PRIORITY
 Blank or @ 3600 MX   mx1.emailsrvr.com 10
 Blank or @ 3600 MX   mx2.emailsrvr.com 20
PTR record (Reverse DNS)
 100.0.168.192.in-addr.arpa. 6230INPTRmailserver.example.com.
SPF record (Sender Policy Framework)
 Blank or @ Lowest possible TXT "v=spf1 include:emailsrvr.com ~all"
Caller-ID record 
DKIM (DomainKeys Identified Mail)



jabber server
 A records
 SRV records
  _xmpp-client._tcp.example.com. 18000 IN SRV 0 5 5222 xmpp.example.com.
  _xmpp-server._tcp.example.com. 18000 IN SRV 0 5 5269 xmpp.example.com.

  parts to change:
   example.com.
   18000 TTL
   0 record's priority
   5 record's weight
   5222 port
   xmpp.example.com.

 TXT records
   the _xmppconnect as TXT record
 subdomains
   _xmpp-server._tcp.conference.example.com. 18000 IN SRV 0 5 5269 xmpp.example.com.

