---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 1", "Second FIToFICustomerCreditTransfer"]
content_origin: "source-transcription"
---

# Second FIToFICustomerCreditTransfer

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / FIToFICustomerCreditTransfer pacs.008.001.14 - 1 / Second FIToFICustomerCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1393** Second FIToFICustomerCreditTransfer

**P1394** Business Data 

**P1395** The second FIToFICustomerCreditTransfer, from BBBBUS33 to EEEEDEFF:

[T36 - complete table](../tables/tbl-0036.md)

**P1396** Message Instance

**P1397** <FIToFICstmrCdtTrf>

**P1398** 	<GrpHdr>

**P1399** 		<MsgId>BBBB/150928-CT/EUR/912</MsgId>

**P1400** 		<CreDtTm>2015-09-28T16:01:00</CreDtTm>

**P1401** 		<NbOfTxs>2</NbOfTxs>

**P1402** 		<TtlIntrBkSttlmAmt Ccy="EUR">504500</TtlIntrBkSttlmAmt>

**P1403** 		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>

**P1404** 		<SttlmInf>

**P1405** 			<SttlmMtd>INDA</SttlmMtd>

**P1406** 			<SttlmAcct>

**P1407** 				<Id>

**P1408** 					<Othr>

**P1409** 						<Id>29314569847</Id>

**P1410** 					</Othr>

**P1411** 				</Id>

**P1412** 			</SttlmAcct>

**P1413** 		</SttlmInf>

**P1414** 		<InstgAgt>

**P1415** 			<FinInstnId>

**P1416** 				<BICFI>BBBBUS33</BICFI>

**P1417** 			</FinInstnId>

**P1418** 		</InstgAgt>

**P1419** 		<InstdAgt>

**P1420** 			<FinInstnId>

**P1421** 				<BICFI>EEEEDEFF</BICFI>

**P1422** 			</FinInstnId>

**P1423** 		</InstdAgt>

**P1424** 	</GrpHdr>

**P1425** 	<CdtTrfTxInf>

**P1426** 		<PmtId>

**P1427** 			<InstrId>BBBB/150928-CCT/EUR/912/1</InstrId>

**P1428** 			<EndToEndId>ABC/ABC-13679/2015-09-15</EndToEndId>

**P1429** 			<TxId>BBBB/150928-CCT/EUR/912/1</TxId>

**P1430** 		</PmtId>

**P1431** 		<PmtTpInf>

**P1432** 			<InstrPrty>NORM</InstrPrty>

**P1433** 		</PmtTpInf>

**P1434** 		<IntrBkSttlmAmt Ccy="EUR">499500</IntrBkSttlmAmt>

**P1435** 		<InstdAmt Ccy="EUR">500000</InstdAmt>

**P1436** 		<ChrgBr>CRED</ChrgBr>

**P1437** 		<ChrgsInf>

**P1438** 			<Amt Ccy="EUR">500</Amt>

**P1439** 			<Agt>

**P1440** 				<FinInstnId>

**P1441** 					<BICFI>BBBBUS33</BICFI>

**P1442** 				</FinInstnId>

**P1443** 			</Agt>

**P1444** 		</ChrgsInf>

**P1445** 		<Dbtr>

**P1446** 			<Nm>ABC Corporation</Nm>

**P1447** 			<PstlAdr>

**P1448** 				<StrtNm>Times Square</StrtNm>

**P1449** 				<BldgNb>7</BldgNb>

**P1450** 				<PstCd>NY 10036</PstCd>

**P1451** 				<TwnNm>New York</TwnNm>

**P1452** 				<Ctry>US</Ctry>

**P1453** 			</PstlAdr>

**P1454** 		</Dbtr>

**P1455** 		<DbtrAcct>

**P1456** 			<Id>

**P1457** 				<Othr>

**P1458** 					<Id>00125574999</Id>

**P1459** 				</Othr>

**P1460** 			</Id>

**P1461** 		</DbtrAcct>

**P1462** 		<DbtrAgt>

**P1463** 			<FinInstnId>

**P1464** 					<BICFI>BBBBUS33</BICFI>

**P1465** 			</FinInstnId>

**P1466** 		</DbtrAgt>

**P1467** 		<CdtrAgt>

**P1468** 			<FinInstnId>

**P1469** 				<BICFI>DDDDBEBB</BICFI>

**P1470** 			</FinInstnId>

**P1471** 		</CdtrAgt>

**P1472** 		<Cdtr>

**P1473** 			<Nm>GHI Semiconductors</Nm>

**P1474** 			<PstlAdr>

**P1475** 				<StrtNm>Avenue Brugmann</StrtNm>

**P1476** 				<BldgNb>415</BldgNb>

**P1477** 				<PstCd>1180</PstCd>

**P1478** 				<TwnNm>Brussels</TwnNm>

**P1479** 				<Ctry>BE</Ctry>

**P1480** 			</PstlAdr>

**P1481** 		</Cdtr>

**P1482** 		<CdtrAcct>

**P1483** 			<Id>

**P1484** 				<IBAN>BE30001216371411</IBAN>

**P1485** 			</Id>

**P1486** 		</CdtrAcct>

**P1487** 		<Purp>

**P1488** 			<Cd>GDDS</Cd>

**P1489** 		</Purp>

**P1490** 		<RmtInf>

**P1491** 			<Strd>

**P1492** 				<RfrdDocInf>

**P1493** 					<Tp>

**P1494** 						<CdOrPrtry>

**P1495** 							<Cd>CINV</Cd>

**P1496** 						</CdOrPrtry>

**P1497** 					</Tp>

**P1498** 					<Nb>ABC-13679</Nb>

**P1499** 					<RltdDt>

**P1500** 					<Tp>

**P1501** 						<Cd>INDA</Cd>

**P1502** 					</Tp>

**P1503** 					<Dt>2015-09-15</Dt>									

**P1504** 					</RltdDt>		

**P1505** 				</RfrdDocInf>

**P1506** 			</Strd>

**P1507** 		</RmtInf>

**P1508** 	</CdtTrfTxInf>

**P1509** 	<CdtTrfTxInf>

**P1510** 		<PmtId>

**P1511** 			<InstrId>BBBB/150928-CCT/EUR/912/2</InstrId>

**P1512** 			<EndToEndId>BBBB/150928-ZZ/JO/164794</EndToEndId>

**P1513** 			<TxId>BBBB/150928-CCT/EUR/912/2</TxId>

**P1514** 		</PmtId>

**P1515** 		<PmtTpInf>

**P1516** 			<InstrPrty>NORM</InstrPrty>

**P1517** 		</PmtTpInf>

**P1518** 		<IntrBkSttlmAmt Ccy="EUR">5000</IntrBkSttlmAmt>

**P1519** 		<ChrgBr>SHAR</ChrgBr>

**P1520** 		<Dbtr>

**P1521** 			<Nm>Mr. Jones</Nm>

**P1522** 			<PstlAdr>

**P1523** 				<StrtNm>16th Street</StrtNm>

**P1524** 				<BldgNb>30</BldgNb>

**P1525** 				<PstCd>NY10023</PstCd>

**P1526** 				<TwnNm>New York</TwnNm>

**P1527** 				<Ctry>US</Ctry>

**P1528** 			</PstlAdr>

**P1529** 		</Dbtr>

**P1530** 		<DbtrAcct>

**P1531** 			<Id>

**P1532** 				<Othr>

**P1533** 					<Id>00125583145</Id>

**P1534** 				</Othr>

**P1535** 			</Id>

**P1536** 		</DbtrAcct>

**P1537** 		<DbtrAgt>

**P1538** 			<FinInstnId>

**P1539** 				<BICFI>BBBBUS33</BICFI>

**P1540** 			</FinInstnId>

**P1541** 		</DbtrAgt>

**P1542** 		<CdtrAgt>

**P1543** 			<FinInstnId>

**P1544** 				<BICFI>EEEEDEFF</BICFI>

**P1545** 			</FinInstnId>

**P1546** 		</CdtrAgt>

**P1547** 		<Cdtr>

**P1548** 			<Nm>ZZ Insurances</Nm>

**P1549** 			<PstlAdr>

**P1550** 				<StrtNm>Friedrich-Ebert-Anlage</StrtNm>

**P1551** 				<BldgNb>2-14</BldgNb>

**P1552** 				<PstCd>D-60 325</PstCd>

**P1553** 				<TwnNm>Frankfurt am Main</TwnNm>

**P1554** 				<Ctry>DE</Ctry>

**P1555** 				<AdrLine>City Haus 1 10th Floor</AdrLine>

**P1556** 			</PstlAdr>

**P1557** 		</Cdtr>

**P1558** 		<CdtrAcct>

**P1559** 			<Id>

**P1560** 				<IBAN>DE89370400440532014000</IBAN>

**P1561** 			</Id>

**P1562** 		</CdtrAcct>

**P1563** 		<RmtInf>

**P1564** 			<Ustrd>Contract ZZ/JO/164794</Ustrd>

**P1565** 		</RmtInf>

**P1566** 	</CdtTrfTxInf>

**P1567** </FIToFICstmrCdtTrf>

