---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionAllegementReport semt.019.001.12"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionAllegementReport semt.019.001.12

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / SecuritiesSettlementTransactionAllegementReport semt.019.001.12.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1378** SecuritiesSettlementTransactionAllegementReport semt.019.001.12

**P1379** Description

**P1380** On the 15 January 2019, the account servicer , Dresdner Bank London (DRESGB2L) sends to its customer Dresdner Bank Frankfurt (DRESDEFF) a Securities Settlement Transaction Allegement Report (semt.019.001.06).

**P1381** Business Data

**P1382** General Details

**P1383** Number of Pages: 1

**P1384** Report Number: 021

**P1385** Statement Date: 15/01/2019

**P1386** Frequency: weekly

**P1387** Activity Indicator: true

**P1388** Safekeeping Account: 222s

**P1389** Allegement details

**P1390** Securities Movement Type: delivery: free

**P1391** Trade Date: 13/01/2019

**P1392** Settlement Date: 15/01/2019

**P1393** Financial Instrument: GB0000054321

**P1394** Account Owner Transaction Id: FRTJ123DEL1

**P1395** Expected Settlement Date: 18/01/2019

**P1396** Effective Settlement Date: 15/01/2019

**P1397** Settlement Quantity: face amount 10,000

**P1398** Securities Transaction Type: trade

**P1399** Delivering Party 1 (the agent of the counterparty): Crest account 123

**P1400** Delivering Party 2: DRESDEFF (Dresdner Bank Frankfurt

**P1401** Delivering Party 3: MGTCDE55 (JP Morgan Investment GmbH, Frankfurt

**P1402** Receiving Depository: CRSTGB22

**P1403** Receiving Party 1: CREST 456

**P1404** Receiving Party 2: CFPIDEFF (Commerz Financial Products GmbH, Frankfurt)

**P1405** Message Instance

**P1406** <SctiesSttlmTxAllgmtRpt>

**P1407** 	<Pgntn>

**P1408** 		<PgNb>1</PgNb>

**P1409** 		<LastPgInd>true</LastPgInd>

**P1410** 	</Pgntn>

**P1411** 	<StmtGnlDtls>

**P1412** 		<RptNb>

**P1413** 			<Shrt>021</Shrt>

**P1414** 		</RptNb>

**P1415** 		<StmtDtTm>

**P1416** 			<Dt>2019-01-15</Dt>

**P1417** 		</StmtDtTm>

**P1418** 		<Frqcy>

**P1419** 			<Cd>WEEK</Cd>

**P1420** 		</Frqcy>

**P1421** 		<ActvtyInd>true</ActvtyInd>

**P1422** 	</StmtGnlDtls>

**P1423** 	<SfkpgAcct>

**P1424** 		<Id>222S</Id>

**P1425** 	</SfkpgAcct>

**P1426** 	<AllgmtDtls>

**P1427** 		<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P1428** 		<Pmt>FREE</Pmt>

**P1429** 		<TradDt>

**P1430** 			<Dt>

**P1431** 				<Dt>2019-01-13</Dt>

**P1432** 			</Dt>

**P1433** 		</TradDt>

**P1434** 		<SttlmDt>

**P1435** 			<Dt>

**P1436** 				<Dt>2019-01-15</Dt>

**P1437** 			</Dt>

**P1438** 		</SttlmDt>

**P1439** 		<FinInstrmId>

**P1440** 			<ISIN>GB0000054321</ISIN>

**P1441** 			</FinInstrmId>

**P1442** 		<QtyAndAcctDtls>

**P1443** 			<SttlmQty>

**P1444** 				<FaceAmt>10000</FaceAmt>

**P1445** 			</SttlmQty>

**P1446** 		</QtyAndAcctDtls>

**P1447** 		<SttlmParams>

**P1448** 			<SctiesTxTp>

**P1449** 				<Cd>TRAD</Cd>

**P1450** 			</SctiesTxTp>

**P1451** 		</SttlmParams>

**P1452** 		<DlvrgSttlmPties>

**P1453** 			<Dpstry>

**P1454** 				<Id>

**P1455** 					<AnyBIC>CRSTGB22</AnyBIC>

**P1456** 				</Id>

**P1457** 			</Dpstry>

**P1458** 			<Pty1>

**P1459** 				<Id>

**P1460** 					<PrtryId>

**P1461** 						<Id>456</Id>

**P1462** 						<Issr>CRST</Issr>

**P1463** 					</PrtryId>

**P1464** 				</Id>

**P1465** 			</Pty1>

**P1466** 			<Pty2>

**P1467** 				<Id>

**P1468** 					<AnyBIC>CPFIDEFF</AnyBIC>

**P1469** 				</Id>

**P1470** 			</Pty2>

**P1471** 		</DlvrgSttlmPties>

**P1472** 		<RcvgSttlmPties>

**P1473** 			<Pty1>

**P1474** 				<Id>

**P1475** 					<PrtryId>

**P1476** 						<Id>123</Id>

**P1477** 						<Issr>CRST</Issr>

**P1478** 					</PrtryId>

**P1479** 				</Id>

**P1480** 			</Pty1>

**P1481** 			<Pty2>

**P1482** 				<Id>

**P1483** 					<AnyBIC>DRESDEFF</AnyBIC>

**P1484** 				</Id>

**P1485** 			</Pty2>

**P1486** 			<Pty3>

**P1487** 				<Id>

**P1488** 					<AnyBIC>MGTCDE55</AnyBIC>

**P1489** 				</Id>

**P1490** 				<SfkpgAcct>

**P1491** 					<Id>111S</Id>

**P1492** 				</SfkpgAcct>

**P1493** 			</Pty3>

**P1494** 		</RcvgSttlmPties>

**P1495** 	</AllgmtDtls>

**P1496** </SctiesSttlmTxAllgmtRpt>

