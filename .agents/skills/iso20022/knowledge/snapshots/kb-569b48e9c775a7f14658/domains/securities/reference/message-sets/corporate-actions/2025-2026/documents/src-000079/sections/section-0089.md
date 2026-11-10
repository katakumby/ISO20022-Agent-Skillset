---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionInstructionCancellationRequest seev.040.00x.013"]
content_origin: "source-transcription"
---

# CorporateActionInstructionCancellationRequest seev.040.00x.013

Source: [src-000079](../../../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Locator: heading path Business Examples / CorporateActionInstructionCancellationRequest seev.040.00x.013.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1536** CorporateActionInstructionCancellationRequest seev.040.00x.013

**P1537** Description

**P1538** This example describes a CorporateActionInstructionCancellationRequest sent by an account owner to cancel its previously sent instruction and indicating its intent to replace it by another instruction.

**P1539** This CorporateActionInstructionCancellationRequest sample message illustrates the cancellation of the instruction message illustrated in the example 1 of the CorporateActionInstructionSection.

**P1540** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P1541** Business Data

**P1542** Issue name

**P1543** Glaxo Holdings

**P1544** ISIN GB0007123466

**P1545** Terms

**P1546** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P1547** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P1548** Relative dates

**P1549** Ex date - 01 September 2010

**P1550** Record date - 07 September 2010

**P1551** Dividend payment date - 02 October 2010

**P1552** Response deadline date - 23 September 2010

**P1553** Transaction description

**P1554** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P1555** Message Instance (with application header)

**P1556** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P1557** 	<Fr>

**P1558** 		<FIId>

**P1559** 			<FinInstnId>

**P1560** 				<BICFI>WXYZFRPP666</BICFI>

**P1561** 			</FinInstnId>

**P1562** 		</FIId>

**P1563** 	</Fr>

**P1564** 	<To>

**P1565** 		<FIId>

**P1566** 			<FinInstnId>

**P1567** 				<BICFI>ABCDBEBBXXX</BICFI>

**P1568** 			</FinInstnId>

**P1569** 		</FIId>

**P1570** 	</To>

**P1571** 	<BizMsgIdr>GLOCUS0000000018</BizMsgIdr>

**P1572** 	<MsgDefIdr>seev.040.001.13</MsgDefIdr>

**P1573** 	<CreDt>2010-10-03T15:30:00Z</CreDt>

**P1574** </AppHdr>

**P1575** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.040.001.13" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P1576** <CorpActnInstrCxlReq>

**P1577** 	<InstrId>

**P1578** 		<Id>GLOCUS0000000001</Id>

**P1579** 	</InstrId>

**P1580** 	<CorpActnGnlInf>

**P1581** 		<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P1582** 		<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1583** 		<EvtTp>

**P1584** 			<Cd>DVOP</Cd>

**P1585** 		</EvtTp>

**P1586** 		<FinInstrmId>

**P1587** 			<ISIN>GB0007123466</ISIN>

**P1588** 			<Desc>GLAXO HOLDINGS</Desc>

**P1589** 		</FinInstrmId>

**P1590** 	</CorpActnGnlInf>

**P1591** 	<AcctDtls>

**P1592** 		<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P1593** 	</AcctDtls>

**P1594** 	<CorpActnInstr>

**P1595** 		<OptnNb>

**P1596** 			<Nb>002</Nb>

**P1597** 		</OptnNb>

**P1598** 		<OptnTp>

**P1599** 			<Cd>SECU</Cd>

**P1600** 		</OptnTp>

**P1601** 			<InstdQty>

**P1602** 				<Qty>

**P1603** 					<Unit>80000</Unit>

**P1604** 				</Qty>

**P1605** 			</InstdQty>

**P1606** 	</CorpActnInstr>

**P1607** </CorpActnInstrCxlReq>

**P1608** </Document>

**P1609**   


