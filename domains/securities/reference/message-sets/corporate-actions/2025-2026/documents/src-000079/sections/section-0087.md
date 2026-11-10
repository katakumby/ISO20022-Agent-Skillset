---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionNarrative seev.038.00x.09"]
content_origin: "source-transcription"
---

# CorporateActionNarrative seev.038.00x.09

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionNarrative seev.038.00x.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1397** CorporateActionNarrative seev.038.00x.09

**P1398** Description

**P1399** This example describes a CorporateActionNarrative sent by an account servicer and containing specific registration details for a corporate action event.

**P1400** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P1401** Business Data

**P1402** Issue name

**P1403** Glaxo Holdings

**P1404** ISIN GB0007123466

**P1405** Terms

**P1406** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P1407** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P1408** Relative dates

**P1409** Ex date - 01 September 2010

**P1410** Record date - 07 September 2010

**P1411** Dividend payment date - 02 October 2010

**P1412** Response deadline date - 23 September 2010

**P1413** Transaction description

**P1414** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P1415** Message Instance (with application header)

**P1416** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P1417** 	<Fr>

**P1418** 		<FIId>

**P1419** 			<FinInstnId>

**P1420** 				<BICFI>ABCDBEBBXXX</BICFI>

**P1421** 			</FinInstnId>

**P1422** 		</FIId>

**P1423** 	</Fr>

**P1424** 	<To>

**P1425** 		<FIId>

**P1426** 			<FinInstnId>

**P1427** 				<BICFI>WXYZFRPP666</BICFI>

**P1428** 			</FinInstnId>

**P1429** 		</FIId>

**P1430** 	</To>

**P1431** 	<BizMsgIdr>LOCCUS00000000398</BizMsgIdr>

**P1432** 	<MsgDefIdr>seev.038.001.09</MsgDefIdr>

**P1433** 	<CreDt>2010-10-09T10:30:00Z</CreDt>

**P1434** </AppHdr>

**P1435** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.038.001.09" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P1436** <CorpActnNrrtv>

**P1437** 	<AcctDtls>

**P1438** 		<AcctsListAndBalDtls>

**P1439** 			<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P1440** 			<ConfdBal>

**P1441** 				<Bal>

**P1442** 					<ShrtLngPos>LONG</ShrtLngPos>

**P1443** 					<QtyChc>

**P1444** 						<Qty>

**P1445** 							<Unit>80000</Unit>

**P1446** 						</Qty>

**P1447** 					</QtyChc>

**P1448** 				</Bal>

**P1449** 			</ConfdBal>

**P1450** 		</AcctsListAndBalDtls>

**P1451** 	</AcctDtls>

**P1452** 	<UndrlygScty>

**P1453** 		<ISIN>GB0007123466</ISIN>

**P1454** 		<Desc>GLAXO HOLDINGS</Desc>

**P1455** 	</UndrlygScty>

**P1456** 	<CorpActnGnlInf>

**P1457** 		<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P1458** 		<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1459** 		<NrrtvTp>

**P1460** 			<Cd>REGI</Cd>

**P1461** 		</NrrtvTp>

**P1462** 	</CorpActnGnlInf>

**P1463** 	<AddtlInf>Registration information are described extensively here. </AddtlInf>

**P1464** </CorpActnNrrtv>

**P1465** </Document>

**P1466**   


