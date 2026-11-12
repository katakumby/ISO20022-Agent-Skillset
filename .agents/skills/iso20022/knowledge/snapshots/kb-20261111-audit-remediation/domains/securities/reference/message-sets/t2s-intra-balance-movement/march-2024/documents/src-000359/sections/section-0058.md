---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Posting Report - camt.084.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Posting Report - camt.084.001

Source: [src-000359](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Posting Report - camt.084.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1379** Intra-balance Movement Posting Report - camt.084.001

**P1380** Description

**P1381** This example shows an Intra-Balance Movement Posting Report for the dedicated cash account ‘9000000456’ (a complete daily report in this case). The report contains 28 movements settled on the current business day, the 15th of January 2015.

**P1382** Message instance

**P1383** <Document>

**P1384**        <IntraBalMvmntPstngRpt>

**P1385** 		<Id>

**P1386** 			<Id>NONREF</Id>

**P1387** 		</Id>

**P1388** 		<Pgntn>

**P1389**                      <PgNb>1</PgNb>

**P1390**                      <LastPgInd>true</LastPgInd>

**P1391** 		</Pgntn>

**P1392** 		<RptGnlDtls>

**P1393** 		        <RptId>RID0PTR0010</RptId>

**P1394** 		        <RptDtTm>

**P1395** 		        	<DtTm>2015-01-15T19:42:01</DtTm>

**P1396** 		        </RptDtTm>

**P1397** 		        <RptPrd>

**P1398** 		        	<FrDtTmToDtTm>

**P1399** 		        		<FrDtTm>2015-01-15T00:00:01</FrDtTm>

**P1400** 		        		<ToDtTm>2015-01-15T18:00:00</ToDtTm>

**P1401** 		        	</FrDtTmToDtTm>

**P1402** 		        </RptPrd>

**P1403** 		        <Frqcy>

**P1404** 		        	<Cd>DAIL</Cd>

**P1405** 		        </Frqcy>

**P1406** 		        <UpdTp>

**P1407** 		        	<Cd>COMP</Cd>

**P1408** 		        </UpdTp>

**P1409** 		        	<ActvtyInd>true</ActvtyInd>

**P1410** 		</RptGnlDtls>

**P1411** 		<CshAcct>

**P1412** 		        <Id>

**P1413** 		        	<Othr>

**P1414** 		        		<Id>9000000456</Id>

**P1415** 		        	</Othr>

**P1416** 		        </Id>

**P1417** 		</CshAcct>

**P1418** 		<CshAcctOwnr>

**P1419** 			<Id>

**P1420** 				<Id>

**P1421** 					<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1422** 				</Id>

**P1423** 			</Id>

**P1424** 			<RspnsblPtyId>

**P1425** 				<Id>

**P1426** 					<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1427** 				</Id>

**P1428** 			</RspnsblPtyId>

**P1429** 		</CshAcctOwnr>

**P1430** 		<SubBal>

**P1431** 			<BalFr>

**P1432** 				<Tp>

**P1433** 					<Prtry>

**P1434** 						<Id>DLVR</Id>

**P1435** 						<Issr>T2S</Issr>

**P1436** 						<SchmeNm>RT</SchmeNm>

**P1437** 					</Prtry>

**P1438** 				</Tp>

**P1439** 			</BalFr>

**P1440** 			<Mvmnt>

**P1441** 				<AcctOwnrTxId>ACCTOWNREF055</AcctOwnrTxId>

**P1442** 				<MktInfrstrctrTxId>T2SREF00009532</MktInfrstrctrTxId>

**P1443** 				<BalTo>

**P1444** 					<Tp>

**P1445** 						<Prtry>

**P1446** 							<Id>BLK1</Id>

**P1447** 							<Issr>T2S</Issr>

**P1448** 							<SchmeNm>RT</SchmeNm>

**P1449** 						</Prtry>

**P1450** 					</Tp>

**P1451** 				</BalTo>

**P1452** 				<SttldAmt>

**P1453** 					<AmtWthCcy Ccy="EUR">100000</AmtWthCcy>

**P1454** 				</SttldAmt>

**P1455** 				<FctvSttlmDt>

**P1456** 					<Dt>2015-01-15</Dt>

**P1457** 				</FctvSttlmDt>

**P1458** 				<StsDt>2015-01-15T14:10:45</StsDt>

**P1459** 				<CshSubBalId>

**P1460** 					<Id>567459</Id>

**P1461** 				</CshSubBalId>

**P1462** 				<Prty>

**P1463** 					<Nmrc>0002</Nmrc>

**P1464** 				</Prty>

**P1465** 				<MsgOrgtr>

**P1466** 					<Id>

**P1467** 						<Id>

**P1468** 							<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1469** 						</Id>

**P1470** 					</Id>

**P1471** 					<RspnsblPtyId>

**P1472** 						<Id>

**P1473** 							<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1474** 						</Id>

**P1475** 					</RspnsblPtyId>

**P1476** 				</MsgOrgtr>

**P1477** 					<CreDtTm>2015-01-09T11:20:23</CreDtTm>

**P1478** 			</Mvmnt>

**P1479** 			<Mvmnt>

**P1480** 				<AcctOwnrTxId>ACCTOWNREF129</AcctOwnrTxId>

**P1481** 				<MktInfrstrctrTxId>T2SREF00015261</MktInfrstrctrTxId>

**P1482** 				<BalTo>

**P1483** 					<Tp>

**P1484** 						<Prtry>

**P1485** 							<Id>BLK1</Id>

**P1486** 							<Issr>T2S</Issr>

**P1487** 							<SchmeNm>RT</SchmeNm>

**P1488** 						</Prtry>

**P1489** 					</Tp>

**P1490** 				</BalTo>

**P1491** 				<SttldAmt>

**P1492** 					<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P1493** 				</SttldAmt>

**P1494** 				<FctvSttlmDt>

**P1495** 					<Dt>2015-01-15</Dt>

**P1496** 				</FctvSttlmDt>

**P1497** 				<StsDt>2015-01-15T15:30:30</StsDt>

**P1498** 				<CshSubBalId>

**P1499** 					<Id>567459</Id>

**P1500** 				</CshSubBalId>

**P1501** 				<Prty>

**P1502** 					<Nmrc>0002</Nmrc>

**P1503** 				</Prty>

**P1504** 				<MsgOrgtr>

**P1505** 					<Id>

**P1506** 						<Id>

**P1507** 							<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1508** 						</Id>

**P1509** 					</Id>

**P1510** 					<RspnsblPtyId>

**P1511** 						<Id>

**P1512** 							<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1513** 						</Id>

**P1514** 					</RspnsblPtyId>

**P1515** 				</MsgOrgtr>

**P1516** 				<CreDtTm>2015-01-09T11:20:12</CreDtTm>

**P1517** 			</Mvmnt>

**P1518** 			<Mvmnt>

**P1519** 				<AcctOwnrTxId>ACCTOWNREF075</AcctOwnrTxId>

**P1520** 				<MktInfrstrctrTxId>T2SREF000011015</MktInfrstrctrTxId>

**P1521** 				<BalTo>

**P1522** 					<Tp>

**P1523** 						<Prtry>

**P1524** 							<Id>RSV4</Id>

**P1525** 							<Issr>T2S</Issr>

**P1526** 							<SchmeNm>RT</SchmeNm>

**P1527** 						</Prtry>

**P1528** 					</Tp>

**P1529** 				</BalTo>

**P1530** 				<SttldAmt>

**P1531** 					<AmtWthCcy Ccy="EUR">75000</AmtWthCcy>

**P1532** 				</SttldAmt>

**P1533** 				<FctvSttlmDt>

**P1534** 					<Dt>2015-01-15</Dt>

**P1535** 				</FctvSttlmDt>

**P1536** 				<StsDt>2015-01-15T14:59:12</StsDt>

**P1537** 				<CshSubBalId>

**P1538** 					<Id>567459</Id>

**P1539** 				</CshSubBalId>

**P1540** 				<Prty>

**P1541** 					<Nmrc>0002</Nmrc>

**P1542** 				</Prty>

**P1543** 				<MsgOrgtr>

**P1544** 					<Id>

**P1545** 						<Id>

**P1546** 							<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1547** 						</Id>

**P1548** 					</Id>

**P1549** 					<RspnsblPtyId>

**P1550** 						<Id>

**P1551** 							<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1552** 						</Id>

**P1553** 					</RspnsblPtyId>

**P1554** 				</MsgOrgtr>

**P1555** 				<CreDtTm>2015-01-13T12:40:23</CreDtTm>

**P1556** 			</Mvmnt>

**P1557** 		</SubBal>

**P1558** 	</IntraBalMvmntPstngRpt>

**P1559** </Document>

