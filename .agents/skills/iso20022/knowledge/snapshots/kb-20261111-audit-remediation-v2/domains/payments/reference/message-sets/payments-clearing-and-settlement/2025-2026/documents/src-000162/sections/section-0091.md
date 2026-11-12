---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 1", "Third FIToFICustomerCreditTransfer"]
content_origin: "source-transcription"
---

# Third FIToFICustomerCreditTransfer

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / FIToFICustomerCreditTransfer pacs.008.001.14 - 1 / Third FIToFICustomerCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1568** Third FIToFICustomerCreditTransfer

**P1569** Business Data 

**P1570** The third FIToFICustomerCreditTransfer, from BBBBUS33 to BBBBUS66:

[T37 - complete table](../tables/tbl-0037.md)

**P1571** Message Instance

**P1572** <FIToFICstmrCdtTrf>

**P1573** 	<GrpHdr>

**P1574** 		<MsgId>BBBB/150928-CCT/USD/897</MsgId>

**P1575** 		<CreDtTm>2015-09-28T16:02:00</CreDtTm>

**P1576** 		<NbOfTxs>1</NbOfTxs>

**P1577** 		<TtlIntrBkSttlmAmt Ccy="USD">1000000</TtlIntrBkSttlmAmt>

**P1578** 		<IntrBkSttlmDt>2015-06-29</IntrBkSttlmDt>

**P1579** 		<SttlmInf>

**P1580** 			<SttlmMtd>INDA</SttlmMtd>

**P1581** 		</SttlmInf>

**P1582** 		<InstgAgt>

**P1583** 			<FinInstnId>

**P1584** 				<BICFI>BBBBUS33</BICFI>

**P1585** 			</FinInstnId>

**P1586** 		</InstgAgt>

**P1587** 		<InstdAgt>

**P1588** 			<FinInstnId>

**P1589** 				<BICFI>BBBBUS66</BICFI>

**P1590** 			</FinInstnId>

**P1591** 		</InstdAgt>

**P1592** 	</GrpHdr>

**P1593** 	<CdtTrfTxInf>

**P1594** 		<PmtId>

**P1595** 			<InstrId>ABC/150928/CCT001/3</InstrId>

**P1596** 			<EndToEndId>ABC/987-AC/2015-09-27</EndToEndId>

**P1597** 			<TxId>BBBB/150928-CCT/USD/897</TxId>

**P1598** 		</PmtId>

**P1599** 		<PmtTpInf>

**P1600** 			<InstrPrty>NORM</InstrPrty>

**P1601** 		</PmtTpInf>

**P1602** 		<IntrBkSttlmAmt Ccy="USD">1000000</IntrBkSttlmAmt>

**P1603** 		<ChrgBr>SHAR</ChrgBr>

**P1604** 		<Dbtr>

**P1605** 			<Nm>ABC Corporation</Nm>

**P1606** 			<PstlAdr>

**P1607** 				<StrtNm>Times Square</StrtNm>

**P1608** 				<BldgNb>7</BldgNb>

**P1609** 				<PstCd>NY 10036</PstCd>

**P1610** 				<TwnNm>New York</TwnNm>

**P1611** 				<Ctry>US</Ctry>

**P1612** 			</PstlAdr>

**P1613** 		</Dbtr>

**P1614** 		<DbtrAcct>

**P1615** 			<Id>

**P1616** 				<Othr>

**P1617** 					<Id>00125574999</Id>

**P1618** 				</Othr>

**P1619** 			</Id>

**P1620** 		</DbtrAcct>

**P1621** 		<DbtrAgt>

**P1622** 			<FinInstnId>

**P1623** 				<BICFI>BBBBUS33</BICFI>

**P1624** 			</FinInstnId>

**P1625** 		</DbtrAgt>

**P1626** 		<CdtrAgt>

**P1627** 			<FinInstnId>

**P1628** 				<BICFI>BBBBUS66</BICFI>

**P1629** 			</FinInstnId>

**P1630** 		</CdtrAgt>

**P1631** 		<Cdtr>

**P1632** 			<Nm>ABC Corporation</Nm>

**P1633** 			<PstlAdr>

**P1634** 				<Dept>Treasury Department</Dept>

**P1635** 				<StrtNm>Bush Street</StrtNm>

**P1636** 				<BldgNb>13</BldgNb>

**P1637** 				<PstCd>CA 94108</PstCd>

**P1638** 				<TwnNm>San Francisco</TwnNm>

**P1639** 				<Ctry>US</Ctry>

**P1640** 			</PstlAdr>

**P1641** 		</Cdtr>

**P1642** 		<CdtrAcct>

**P1643** 			<Id>

**P1644** 				<Othr>

**P1645** 					<Id>4895623</Id>

**P1646** 				</Othr>

**P1647** 			</Id>

**P1648** 		</CdtrAcct>

**P1649** 		<Purp>

**P1650** 			<Cd>INTC</Cd>

**P1651** 		</Purp>

**P1652** 		<RmtInf>

**P1653** 			<Strd>

**P1654** 				<RfrdDocInf>

**P1655** 					<Tp>

**P1656** 						<CdOrPrtry>

**P1657** 							<Cd>CINV</Cd>

**P1658** 						</CdOrPrtry>

**P1659** 					</Tp>

**P1660** 					<Nb>987-AC</Nb>

**P1661** 					<RltdDt>

**P1662** 					<Tp>

**P1663** 						<Cd>INDA</Cd>

**P1664** 					</Tp>

**P1665** 					<Dt>2015-09-27</Dt>									

**P1666** 					</RltdDt>					

**P1667** 				</RfrdDocInf>

**P1668** 			</Strd>

**P1669** 		</RmtInf>

**P1670** 	</CdtTrfTxInf>

**P1671** </FIToFICstmrCdtTrf>

