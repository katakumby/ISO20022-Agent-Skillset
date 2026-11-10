---
template: false
document_kind: "source-discrepancies"
title: "Clearing and settlement example differences"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.002.001.16", "pacs.003.001.12", "pacs.004.001.15", "pacs.007.001.14", "pacs.008.001.14", "pacs.009.001.13", "pacs.010.001.06", "pacs.028.001.07"]
message_families: ["pacs.002", "pacs.003", "pacs.004", "pacs.007", "pacs.008", "pacs.009", "pacs.010", "pacs.028"]
source_locations: [{"source_id": "src-000162", "locator": "Business Examples; T28–T47 and P650–P2615; exact cells/paragraphs listed"}]
issue_ids: ["issue-000059"]
source_editions: ["March 2026"]
---

# Clearing and settlement example differences

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

The entries below preserve disagreements between supplied Business Data tables, narrative and XML. They do not silently repair the source or override the exact XSD. Each payload validates only after the separately documented namespace/Document envelope is applied; schema validity does not imply equality with its narrative/table.

| Example | Table locator | Literal table cell | Compared locator | Finding |
| --- | --- | --- | --- | --- |
| 1 | T28 row28 cell2 | &lt;RtrdIntrBkSttlmAmt&gt; | P697 | Table XML tag &lt;RtrdIntrBkSttlmAmt&gt;; instance uses &lt;IntrBkSttlmAmt&gt; in OrgnlTxRef. |
| 2 | T29 row27 cell3 | 2015-07-13 | P735 | Narrative requested collection date is 13 July 20102; table and XML use 2015-07-13. |
| 3 | T30 row21 cell3 | CCCC/151122-PR007/1 | P872 | Table ReturnIdentification CCCC/151122-PR007/1; XML RtrId CCCC/151122-PR007. |
| 4 | T31 row43 cell2 | &lt;AddtlRtrRsnInf&gt; | P963 | Table tag &lt;AddtlRtrRsnInf&gt;; XML RtrRsnInf/AddtlInf. |
| 5 | T32 row3 cell3 | BBBBUS39-RETURN-0213 | P977 | Table MsgId BBBBUS39-RETURN-0213; XML BBBBUS39-RETURN-0123. |
| 5 | T32 row20 cell2 | &lt;OrgnlEndToEnd&gt; | P1001 | Table OriginalEndToEndIdentification &lt;OrgnlEndToEnd&gt; VA060327/0123; instance assigns that value to OrgnlInstrId, not OrgnlEndToEndId. |
| 6 | T33 row20 cell3 | VA060327/0123 | Complete example instance | Table OriginalEndToEndIdentification VA060327/0123; complete XML P1067–P1159 contains no OrgnlEndToEndId or equivalent populated original end-to-end field. |
| 8 | T35 row29 cell3 | 2015-09-28T15:45:00 | Complete example instance | Table AcceptanceDateTime 2015-09-28T15:45:00; complete XML P1284–P1392 contains no AccptncDtTm. |
| 9 | T36 row3 cell3 | BBBB/150928-CCT/EUR/912 | P1399 | Table MsgId BBBB/150928-CCT/EUR/912; XML BBBB/150928-CT/EUR/912. |
| 11 | T38 row4 cell3 | 12-09-29T09:00:00 | P1681 | Table CreationDateTime 12-09-29T09:00:00; XML 2015-09-29T09:00:00. |
| 13 | T40 row18 cell3 | BBBB/151109-CBJ056/1 | P1938 | Table InstrId BBBB/151109-CBJ056/1; XML BBBB/151109/-CBJ056/1. |
| 14 | T41 row18 cell3 | BBBB/150928-CCT/JPY/123/1 | P2059 | Table TxId BBBB/150928-CCT/JPY/123/1; XML BBBB/150928-CCT/123/1. |
| 14 | T41 row58 cell3 | EC3R7NE | P2114 | Table underlying creditor postcode EC3R7NE; XML EC3RZNE. |
| 18 | T45 row11 cell3 | 24538877443 | P2368 | Table settlement account24538877443; XML245388877443. P2209 also states24538877443. |
| 19 | T46 row12 cell2 | &lt;CdtTrfTxInf&gt; | P2441 | Table CreditInstruction tag &lt;CdtTrfTxInf&gt;; XML root child &lt;CdtInstr&gt;. |
| 1 | T28 row43 cell2 | &lt;Name&gt; | P707 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 5 | T32 row19 cell2 | &lt;RtnId&gt; | P1000 | Table tag &lt;RtnId&gt; is retained literally; corresponding instance vocabulary uses RtrId. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 6 | T33 row19 cell2 | &lt;RtnId&gt; | P1092 | Table tag &lt;RtnId&gt; is retained literally; corresponding instance vocabulary uses RtrId. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 6 | T33 row57 cell2 | &lt;Name&gt; | P1135 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 7 | T34 row21 cell2 | &lt;OrgnlEndToEnd&gt; | P1195 | Table tag &lt;OrgnlEndToEnd&gt; is retained literally; corresponding instance vocabulary uses OrgnlEndToEndId. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 8 | T35 row50 cell2 | &lt;Name&gt; | P1326 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 8 | T35 row67 cell2 | &lt;Type&gt; | P1376 | Table tag &lt;Type&gt; is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 9 | T36 row54 cell2 | &lt;Name&gt; | P1446 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 9 | T36 row69 cell2 | &lt;RfrdDocType&gt; | P1493 | Table tag &lt;RfrdDocType&gt; is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 9 | T36 row87 cell2 | &lt;Name&gt; | P1446 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 9 | T36 row105 cell2 | &lt;Name&gt; | P1446 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 10 | T37 row44 cell2 | &lt;Name&gt; | P1605 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 10 | T37 row61 cell2 | &lt;RfrdDocType&gt; | P1655 | Table tag &lt;RfrdDocType&gt; is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 11 | T38 row56 cell2 | &lt;Name&gt; | P1730 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 11 | T38 row71 cell2 | &lt;Type&gt; | P1777 | Table tag &lt;Type&gt; is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 12 | T39 row50 cell2 | &lt;Name&gt; | P1835 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 12 | T39 row64 cell2 | &lt;Type&gt; | P1891 | Table tag &lt;Type&gt; is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 13 | T40 row57 cell2 | &lt;Name&gt; | P1955 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 13 | T40 row71 cell2 | &lt;Type&gt; | P2011 | Table tag &lt;Type&gt; is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 14 | T41 row69 cell2 | &lt;RfrdDocType&gt; | P2130 | Table tag &lt;RfrdDocType&gt; is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 14 | T41 row72 cell2 | &lt;RfrdDocNb&gt; | P2135 | Table tag &lt;RfrdDocNb&gt; is retained literally; corresponding instance vocabulary uses Nb. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 16 | T43 row33 cell2 | &lt;BIC&gt; | P2230 | Table tag &lt;BIC&gt; is retained literally; corresponding instance vocabulary uses BICFI. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |
| 20 | T47 row56 cell2 | &lt;Name&gt; | P2566 | Table tag &lt;Name&gt; is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration. |


## Narrative qualifications

- P655 writes AAAUS29 once, then AAAAUS29 in the same sentence; no unsupported alias is created.
- P1260 says four messages sent by BBBBUS33; P1264 and P1674 explicitly show the fourth sent by EEEEDEFF. The fourth exchange retains EEEEDEFF as initiator.
- P1278 supplies an insurance-premium due date in 2006; surrounding message creation dates are2015. Both historical dates are retained.
- P1798 dates the invoice13October2010; T39 and its XML give related-document date2015-10-13. Both source claims remain visible.
- P2204 calls the final FFFFSESS→DDDDLULL leg second; headingP2352 calls it third. Ordered exchanges follow the three explicit source legs, retaining this wording difference.
- P2508 refers to section7.6.1. Word filep92 actually labels the first customer credit-transfer example7.6.1, so this cross-reference is not classified as an error. Paragraph-heading text omits automatic numbering.

Blank table cells, case, spaces, punctuation, and leading zeros are preserved. Dot grouping in amounts is not automatically interpreted as a decimal separator or a source error. Names in table XML-tag columns are evidence labels and are not a replacement for schema declarations.
