---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionMovementReversalAdvice seev.037.00x.17"]
content_origin: "source-transcription"
---

# CorporateActionMovementReversalAdvice seev.037.00x.17

Source: [src-000079](../../../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Locator: heading path Business Examples / CorporateActionMovementReversalAdvice seev.037.00x.17.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1293** CorporateActionMovementReversalAdvice seev.037.00x.17

**P1294** Description

**P1295** This example describes a CorporateActionMovementReversalAdvice sent by an account servicer after payment date and the confirmation of the movements of a dividend option event. The reason for the reversal is that the funds to be distributed have not been received.

**P1296** This CorporateActionMovementReversalAdvice sample message illustrates the reversal of the movement confirmation message illustrated in the example 1 of the CorporateActionMovementConfirmation section.

**P1297** The corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash.

**P1298** Business Data

**P1299** Issue name

**P1300** Glaxo Holdings

**P1301** ISIN GB0007123466

**P1302** Terms

**P1303** Final dividend of GBP 0,017 per share, OR one ordinary share for every 37 shares held. Elections cannot be made on holdings of less than 37 shares.

**P1304** Elections which give rise to fractional entitlements will be rounded down to the nearest whole multiple of 37 shares; the full cash dividend of GBP 0,017 per share will be paid on the remainder of the holding.

**P1305** Relative dates

**P1306** Ex date - 01 September 2010

**P1307** Record date - 07 September 2010

**P1308** Dividend payment date - 02 October 2010

**P1309** Response deadline date - 23 September 2010

**P1310** Transaction description

**P1311** A/C 98-0112441-05 has an underlying balance of 80,000 shares.

**P1312** Message Instance (with application header)

**P1313** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P1314** 	<Fr>

**P1315** 		<FIId>

**P1316** 			<FinInstnId>

**P1317** 				<BICFI>ABCDBEBBXXX</BICFI>

**P1318** 			</FinInstnId>

**P1319** 		</FIId>

**P1320** 	</Fr>

**P1321** 	<To>

**P1322** 		<FIId>

**P1323** 			<FinInstnId>

**P1324** 				<BICFI>WXYZFRPP666</BICFI>

**P1325** 			</FinInstnId>

**P1326** 		</FIId>

**P1327** 	</To>

**P1328** 	<BizMsgIdr>LOCCUS00000000239</BizMsgIdr>

**P1329** 	<MsgDefIdr>seev.037.001.17</MsgDefIdr>

**P1330** 	<CreDt>2010-10-04T14:39:00Z</CreDt>

**P1331** </AppHdr>

**P1332** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.037.001.17" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P1333** 	<CorpActnMvmntRvslAdvc>

**P1334** 		<MvmntConfId>

**P1335** 			<Id>LOCCUS0000000198</Id>

**P1336** 		</MvmntConfId>

**P1337** 		<RvslRsn>

**P1338** 			<Rsn>

**P1339** 				<Cd>FNRC</Cd>

**P1340** 			</Rsn>

**P1341** 		</RvslRsn>

**P1342** 		<CorpActnGnlInf>

**P1343** 			<CorpActnEvtId>DIVGLAX125</CorpActnEvtId>

**P1344** 			<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1345** 			<EvtTp>

**P1346** 				<Cd>DVOP</Cd>

**P1347** 			</EvtTp>

**P1348** 			<FinInstrmId>

**P1349** 				<ISIN>GB0007123466</ISIN>

**P1350** 				<Desc>GLAXO HOLDINGS</Desc>

**P1351** 			</FinInstrmId>

**P1352** 		</CorpActnGnlInf>

**P1353** 		<AcctDtls>

**P1354** 			<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P1355** 			<ConfdBal>

**P1356** 				<Bal>

**P1357** 					<ShrtLngPos>LONG</ShrtLngPos>

**P1358** 					<QtyChc>

**P1359** 						<Qty>

**P1360** 							<Unit>80000</Unit>

**P1361** 						</Qty>

**P1362** 					</QtyChc>

**P1363** 				</Bal>

**P1364** 			</ConfdBal>

**P1365** 		</AcctDtls>

**P1366** 		<CorpActnConfDtls>

**P1367** 			<OptnNb>

**P1368** 				<Nb>002</Nb>

**P1369** 			</OptnNb>

**P1370** 			<OptnTp>

**P1371** 				<Cd>SECU</Cd>

**P1372** 			</OptnTp>

**P1373** 			<SctiesMvmntDtls>

**P1374** 				<FinInstrmId>

**P1375** 					<ISIN>GB0007633421</ISIN>

**P1376** 					<Desc>GLAXO WELLCOME</Desc>

**P1377** 				</FinInstrmId>

**P1378** 				<CdtDbtInd>CRDT</CdtDbtInd>

**P1379** 				<PstngQty>

**P1380** 					<Qty>

**P1381** 						<Unit>2162</Unit>

**P1382** 					</Qty>

**P1383** 				</PstngQty>

**P1384** 				<PstngDt><Dt>2010-10-03</Dt></PstngDt>

**P1385** 				<OrgnlPstngDt><Dt>2010-10-02</Dt></OrgnlPstngDt>

**P1386** 			</SctiesMvmntDtls>

**P1387** 			<CshMvmntDtls>

**P1388** 				<CdtDbtInd>CRDT</CdtDbtInd>

**P1389** 				<PstngDt><Dt>2010-10-03</Dt></PstngDt>

**P1390** 				<OrgnlPstngDt><Dt>2010-10-02</Dt>2010-10-02</OrgnlPstngDt>

**P1391** 				<PstngAmt Ccy="GBP">0.10</PstngAmt>

**P1392** 			</CshMvmntDtls>

**P1393** 		</CorpActnConfDtls>

**P1394** 	</CorpActnMvmntRvslAdvc>

**P1395** </Document>

**P1396**   


