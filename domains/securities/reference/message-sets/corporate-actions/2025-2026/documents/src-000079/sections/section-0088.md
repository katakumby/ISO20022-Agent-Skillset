---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionCancellationAdvice seev.039.00x.13"]
content_origin: "source-transcription"
---

# CorporateActionCancellationAdvice seev.039.00x.13

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionCancellationAdvice seev.039.00x.13.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1467** CorporateActionCancellationAdvice seev.039.00x.13

**P1468** Description

**P1469** This example describes a CorporateActionCancellationAdvice sent by an account servicer to inform the account owners that the previously announced corporate action event has been dropped by the issuer. This corporate action cancellation advice sample message illustrates the cancellation of the event previously announced by the message illustrated in the example 1 of the CorporateActionNotification section.

**P1470** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P1471** Business Data

**P1472** Issue name

**P1473** Glaxo Holdings

**P1474** ISIN GB0007123466

**P1475** Terms

**P1476** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P1477** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P1478** Relative dates

**P1479** Ex date - 01 September 2010

**P1480** Record date - 07 September 2010

**P1481** Dividend payment date - 02 October 2010

**P1482** Response deadline date - 23 September 2010

**P1483** Transaction description

**P1484** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P1485** Message Instance (with application header)

**P1486** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P1487** 	<Fr>

**P1488** 		<FIId>

**P1489** 			<FinInstnId>

**P1490** 				<BICFI>ABCDBEBBXXX</BICFI>

**P1491** 			</FinInstnId>

**P1492** 		</FIId>

**P1493** 	</Fr>

**P1494** 	<To>

**P1495** 		<FIId>

**P1496** 			<FinInstnId>

**P1497** 				<BICFI>WXYZFRPP666</BICFI>

**P1498** 			</FinInstnId>

**P1499** 		</FIId>

**P1500** 	</To>

**P1501** 	<BizMsgIdr>LOCCUS000000008</BizMsgIdr>

**P1502** 	<MsgDefIdr>seev.039.001.13</MsgDefIdr>

**P1503** 	<CreDt>2010-08-17T08:30:00Z</CreDt>

**P1504** </AppHdr>

**P1505** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.039.001.13" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P1506** <CorpActnCxlAdvc>

**P1507** 	<CxlAdvcGnlInf>

**P1508** 		<CxlRsnCd>WITH</CxlRsnCd>

**P1509** 		<PrcgSts>

**P1510** 				<EvtCmpltnsSts>COMP</EvtCmpltnsSts>

**P1511** 				<EvtConfSts>CONF</EvtConfSts>

**P1512** 		</PrcgSts>

**P1513** 	</CxlAdvcGnlInf>

**P1514** 	<CorpActnGnlInf>

**P1515** 		<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P1516** 		<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1517** 		<EvtTp>

**P1518** 			<Cd>DVOP</Cd>

**P1519** 		</EvtTp>

**P1520** 		<MndtryVlntryEvtTp>

**P1521** 			<Cd>CHOS</Cd>

**P1522** 		</MndtryVlntryEvtTp>

**P1523** 		<FinInstrmId>

**P1524** 			<ISIN>GB0007123466</ISIN>

**P1525** 			<Desc>GLAXO HOLDINGS</Desc>

**P1526** 		</FinInstrmId>

**P1527** 	</CorpActnGnlInf>

**P1528** 	<AcctsDtls>

**P1529** 		<ForAllAccts>

**P1530** 			<IdCd>GENR</IdCd>

**P1531** 		</ForAllAccts>

**P1532** 	</AcctsDtls>

**P1533** </CorpActnCxlAdvc>

**P1534** </Document>

**P1535**   


