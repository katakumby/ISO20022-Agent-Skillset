---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionInstructionCancellationRequestStatusAdvice seev.041.00x.15"]
content_origin: "source-transcription"
---

# CorporateActionInstructionCancellationRequestStatusAdvice seev.041.00x.15

Source: [src-000079](../../../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Locator: heading path Business Examples / CorporateActionInstructionCancellationRequestStatusAdvice seev.041.00x.15.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1610** CorporateActionInstructionCancellationRequestStatusAdvice seev.041.00x.15

**P1611** Description

**P1612** This example describes a CorporateActionInstructionCancellationRequestStatusAdvice sent by an account servicer to report the status of the corporate action instruction cancellation request previously received from the account owner. The instruction cancellation request status advice informs the account owner that instruction cancellation has been completed.

**P1613** This CorporateActionInstructionCancellationRequestStatusAdvice sample message illustrates the status of the instruction cancellation request message illustrated in the example 1 of the CorporateActionInstructionCancellationRequest section.

**P1614** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P1615** Business Data

**P1616** Issue name

**P1617** Glaxo Holdings

**P1618** ISIN GB0007123466

**P1619** Terms

**P1620** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P1621** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P1622** Relative dates

**P1623** Ex date - 01 September 2010

**P1624** Record date - 07 September 2010

**P1625** Dividend payment date - 02 October 2010

**P1626** Response deadline date - 23 September 2010

**P1627** Transaction description

**P1628** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P1629** Message Instance (with application header)

**P1630** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P1631** 	<Fr>

**P1632** 		<FIId>

**P1633** 			<FinInstnId>

**P1634** 				<BICFI>ABCDBEBBXXX</BICFI>

**P1635** 			</FinInstnId>

**P1636** 		</FIId>

**P1637** 	</Fr>

**P1638** 	<To>

**P1639** 		<FIId>

**P1640** 			<FinInstnId>

**P1641** 				<BICFI>WXYZFRPP666</BICFI>

**P1642** 			</FinInstnId>

**P1643** 		</FIId>

**P1644** 	</To>

**P1645** 	<BizMsgIdr>LOCCUS0000000099</BizMsgIdr>

**P1646** 	<MsgDefIdr>seev.041.001.15</MsgDefIdr>

**P1647** 	<CreDt>2010-10-03T17:30:00Z</CreDt>

**P1648** </AppHdr>

**P1649** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.041.001.15" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P1650** <CorpActnInstrCxlReqStsAdvc>

**P1651** 	<InstrCxlReqId>

**P1652** 		<Id>GLOCUS0000000018</Id>

**P1653** 	</InstrCxlReqId>

**P1654** 	<CorpActnGnlInf>

**P1655** 		<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P1656** 		<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1657** 		<EvtTp>

**P1658** 			<Cd>DVOP</Cd>

**P1659** 		</EvtTp>

**P1660** 	</CorpActnGnlInf>

**P1661** 	<InstrCxlReqSts>

**P1662** 		<CxlCmpltd>

**P1663** 			<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1664** 		</CxlCmpltd>

**P1665** 	</InstrCxlReqSts>

**P1666** 	<CorpActnInstr>

**P1667** 		<OptnNb>

**P1668** 			<Nb>002</Nb>

**P1669** 		</OptnNb>

**P1670** 		<OptnTp>

**P1671** 			<Cd>SECU</Cd>

**P1672** 		</OptnTp>

**P1673** 			<StsQty>

**P1674** 				<Qty>

**P1675** 					<Unit>80000</Unit>

**P1676** 				</Qty>

**P1677** 			</StsQty>

**P1678** 	</CorpActnInstr>

**P1679** </CorpActnInstrCxlReqStsAdvc>

**P1680** </Document>

**P1681**   


