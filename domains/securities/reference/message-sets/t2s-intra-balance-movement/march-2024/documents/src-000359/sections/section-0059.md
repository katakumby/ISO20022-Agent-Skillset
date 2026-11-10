---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Pending Report - camt.085.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Pending Report - camt.085.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Pending Report - camt.085.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1560** Intra-balance Movement Pending Report - camt.085.001

**P1561** Description

**P1562** This example shows an Intra-Balance Movement Pending Report for the dedicated cash account ‘9000000456’ (a delta intraday report in this case). The report contains 30 movements pending as of 15h00 on the current business day, the 15th of January 2015.

**P1563** Message instance

**P1564** <Document>

**P1565**        <IntraBalMvmntPdgRpt>

**P1566** 			<Id>

**P1567** 			<Id>NONREF</Id>

**P1568** 		</Id>

**P1569** 		<Pgntn>

**P1570** 			<PgNb>1</PgNb>

**P1571** 			<LastPgInd>true</LastPgInd>

**P1572** 		</Pgntn>

**P1573** 		<RptGnlDtls>

**P1574** 			<RptId>RID0PDR0050</RptId>

**P1575** 			<RptDtTm>

**P1576** 				<DtTm>2015-01-17T15:00:25</DtTm>

**P1577** 			</RptDtTm>

**P1578** 			<Frqcy>

**P1579** 				<Cd>DAIL</Cd>

**P1580** 			</Frqcy>

**P1581** 			<UpdTp>

**P1582** 				<Cd>DELT</Cd>

**P1583** 			</UpdTp>

**P1584** 			<ActvtyInd>true</ActvtyInd>

**P1585** 		</RptGnlDtls>

**P1586** 		<CshAcct>

**P1587** 			<Id>

**P1588** 				<Othr>

**P1589** 					<Id>9000000456</Id>

**P1590** 				</Othr>

**P1591** 			</Id>

**P1592** 		</CshAcct>

**P1593** 		<CshAcctOwnr>

**P1594** 			<Id>

**P1595** 				<Id>

**P1596** 					<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1597** 				</Id>

**P1598** 			</Id>

**P1599** 			<RspnsblPtyId>

**P1600** 				<Id>

**P1601** 					<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1602** 				</Id>

**P1603** 			</RspnsblPtyId>

**P1604** 		</CshAcctOwnr>

**P1605** 		<Mvmnts>

**P1606** 			<Mvmnt>

**P1607** 				<StsAndRsn>

**P1608** 					<PrcgSts>

**P1609** 						<AckdAccptd>

**P1610** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1611** 						</AckdAccptd>

**P1612** 					</PrcgSts>

**P1613** 				</StsAndRsn>

**P1614** 				<AcctOwnrTxId>ACCTOWNREF907</AcctOwnrTxId>

**P1615** 				<MktInfrstrctrTxId>T2SREF00010952</MktInfrstrctrTxId>

**P1616** 				<BalFr>

**P1617** 					<Tp>

**P1618** 						<Prtry>

**P1619** 							<Id>DLVR</Id>

**P1620** 							<Issr>T2S</Issr>

**P1621** 							<SchmeNm>RT</SchmeNm>

**P1622** 						</Prtry>

**P1623** 					</Tp>

**P1624** 				</BalFr>

**P1625** 				<BalTo>

**P1626** 					<Tp>

**P1627** 						<Prtry>

**P1628** 							<Id>RSV9</Id>

**P1629** 							<Issr>T2S</Issr>

**P1630** 							<SchmeNm>RT</SchmeNm>

**P1631** 						</Prtry>

**P1632** 					</Tp>

**P1633** 				</BalTo>

**P1634** 				<SttlmAmt>

**P1635** 					<AmtWthCcy Ccy="EUR">23000</AmtWthCcy>

**P1636** 				</SttlmAmt>

**P1637** 				<IntnddSttlmDt>

**P1638** 					<Dt>2015-01-20</Dt>

**P1639** 				</IntnddSttlmDt>

**P1640** 				<StsDt>2015-01-15T14:10:45</StsDt>

**P1641** 				<CshSubBalId>

**P1642** 					<Id>700234</Id>

**P1643** 				</CshSubBalId>

**P1644** 				<Prty>

**P1645** 					<Nmrc>0004</Nmrc>

**P1646** 				</Prty>

**P1647** 				<MsgOrgtr>

**P1648** 				<Id>

**P1649** 					<Id>

**P1650** 						<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1651** 					</Id>

**P1652** 				</Id>

**P1653** 				<RspnsblPtyId>

**P1654** 					<Id>

**P1655** 						<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1656** 					</Id>

**P1657** 				</RspnsblPtyId>

**P1658** 				</MsgOrgtr>

**P1659** 				<CreDtTm>2015-01-15T10:01:12</CreDtTm>

**P1660** 			</Mvmnt>

**P1661** 			<Mvmnt>

**P1662** 				<StsAndRsn>

**P1663** 					<PrcgSts>

**P1664** 						<AckdAccptd>

**P1665** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1666** 						</AckdAccptd>

**P1667** 					</PrcgSts>

**P1668** 				</StsAndRsn>

**P1669** 				<AcctOwnrTxId>ACCTOWNREF856</AcctOwnrTxId>

**P1670** 				<MktInfrstrctrTxId>T2SREF00011734</MktInfrstrctrTxId>

**P1671** 				<BalFr>

**P1672** 					<Tp>

**P1673** 						<Prtry>

**P1674** 							<Id>DLVR</Id>

**P1675** 							<Issr>T2S</Issr>

**P1676** 							<SchmeNm>RT</SchmeNm>

**P1677** 						</Prtry>

**P1678** 					</Tp>

**P1679** 				</BalFr>

**P1680** 				<BalTo>

**P1681** 					<Tp>

**P1682** 						<Prtry>

**P1683** 							<Id>BLK2</Id>

**P1684** 							<Issr>T2S</Issr>

**P1685** 							<SchmeNm>RT</SchmeNm>

**P1686** 						</Prtry>

**P1687** 					</Tp>

**P1688** 				</BalTo>

**P1689** 				<SttlmAmt>

**P1690** 					<AmtWthCcy Ccy="EUR">145000</AmtWthCcy>

**P1691** 				</SttlmAmt>

**P1692** 				<IntnddSttlmDt>

**P1693** 					<Dt>2015-01-21</Dt>

**P1694** 				</IntnddSttlmDt>

**P1695** 				<StsDt>2015-01-16T16:20:34</StsDt>

**P1696** 				<CshSubBalId>

**P1697** 					<Id>856765</Id>

**P1698** 				</CshSubBalId>

**P1699** 				<Prty>

**P1700** 					<Nmrc>0004</Nmrc>

**P1701** 				</Prty>

**P1702** 				<MsgOrgtr>

**P1703** 				<Id>

**P1704** 					<Id>

**P1705** 						<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1706** 					</Id>

**P1707** 				</Id>

**P1708** 				<RspnsblPtyId>

**P1709** 					<Id>

**P1710** 						<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1711** 					</Id>

**P1712** 				</RspnsblPtyId>

**P1713** 				</MsgOrgtr>

**P1714** 				<CreDtTm>2015-01-16T10:01:12</CreDtTm>

**P1715** 			</Mvmnt>

**P1716** 			<Mvmnt>

**P1717** 				<StsAndRsn>

**P1718** 					<PrcgSts>

**P1719** 						<AckdAccptd>

**P1720** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1721** 						</AckdAccptd>

**P1722** 					</PrcgSts>

**P1723** 				</StsAndRsn>

**P1724** 				<AcctOwnrTxId>ACCTOWNREF123</AcctOwnrTxId>

**P1725** 				<MktInfrstrctrTxId>T2SREF00008952</MktInfrstrctrTxId>

**P1726** 				<BalFr>

**P1727** 					<Tp>

**P1728** 						<Prtry>

**P1729** 							<Id>DLVR</Id>

**P1730** 							<Issr>T2S</Issr>

**P1731** 							<SchmeNm>RT</SchmeNm>

**P1732** 						</Prtry>

**P1733** 					</Tp>

**P1734** 				</BalFr>

**P1735** 				<BalTo>

**P1736** 					<Tp>

**P1737** 						<Prtry>

**P1738** 							<Id>RSV9</Id>

**P1739** 							<Issr>T2S</Issr>

**P1740** 							<SchmeNm>RT</SchmeNm>

**P1741** 						</Prtry>

**P1742** 					</Tp>

**P1743** 				</BalTo>

**P1744** 				<SttlmAmt>

**P1745** 					<AmtWthCcy Ccy="EUR">12000</AmtWthCcy>

**P1746** 				</SttlmAmt>

**P1747** 				<IntnddSttlmDt>

**P1748** 					<Dt>2015-01-20</Dt>

**P1749** 				</IntnddSttlmDt>

**P1750** 				<StsDt>2015-01-16T10:20:15</StsDt>

**P1751** 				<CshSubBalId>

**P1752** 					<Id>700234</Id>

**P1753** 				</CshSubBalId>

**P1754** 				<Prty>

**P1755** 					<Nmrc>0003</Nmrc>

**P1756** 				</Prty>

**P1757** 				<MsgOrgtr>

**P1758** 				<Id>

**P1759** 					<Id>

**P1760** 						<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1761** 					</Id>

**P1762** 				</Id>

**P1763** 				<RspnsblPtyId>

**P1764** 					<Id>

**P1765** 						<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1766** 					</Id>

**P1767** 				</RspnsblPtyId>

**P1768** 				</MsgOrgtr>

**P1769** 				<CreDtTm>2015-01-16T12:51:41</CreDtTm>

**P1770** 			</Mvmnt>

**P1771** 			<Mvmnt>

**P1772** 				<StsAndRsn>

**P1773** 					<PrcgSts>

**P1774** 						<AckdAccptd>

**P1775** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1776** 						</AckdAccptd>

**P1777** 					</PrcgSts>

**P1778** 				</StsAndRsn>

**P1779** 				<AcctOwnrTxId>ACCTOWNREF114</AcctOwnrTxId>

**P1780** 				<MktInfrstrctrTxId>T2SREF00007563</MktInfrstrctrTxId>

**P1781** 				<BalFr>

**P1782** 					<Tp>

**P1783** 						<Prtry>

**P1784** 							<Id>DLVR</Id>

**P1785** 							<Issr>T2S</Issr>

**P1786** 							<SchmeNm>RT</SchmeNm>

**P1787** 						</Prtry>

**P1788** 					</Tp>

**P1789** 				</BalFr>

**P1790** 				<BalTo>

**P1791** 					<Tp>

**P1792** 						<Prtry>

**P1793** 							<Id>BLK7</Id>

**P1794** 							<Issr>T2S</Issr>

**P1795** 							<SchmeNm>RT</SchmeNm>

**P1796** 						</Prtry>

**P1797** 					</Tp>

**P1798** 				</BalTo>

**P1799** 				<SttlmAmt>

**P1800** 					<AmtWthCcy Ccy="EUR">55000</AmtWthCcy>

**P1801** 				</SttlmAmt>

**P1802** 				<IntnddSttlmDt>

**P1803** 					<Dt>2015-01-24</Dt>

**P1804** 				</IntnddSttlmDt>

**P1805** 				<StsDt>2015-01-17T13:43:48</StsDt>

**P1806** 				<CshSubBalId>

**P1807** 					<Id>886723</Id>

**P1808** 				</CshSubBalId>

**P1809** 				<Prty>

**P1810** 					<Nmrc>0004</Nmrc>

**P1811** 				</Prty>

**P1812** 				<MsgOrgtr>

**P1813** 				<Id>

**P1814** 					<Id>

**P1815** 						<AnyBIC>PRYBFRPPXXX</AnyBIC>

**P1816** 					</Id>

**P1817** 				</Id>

**P1818** 				<RspnsblPtyId>

**P1819** 					<Id>

**P1820** 						<AnyBIC>CSDBFRPPXXX</AnyBIC>

**P1821** 					</Id>

**P1822** 				</RspnsblPtyId>

**P1823** 				</MsgOrgtr>

**P1824** 				<CreDtTm>2015-01-17T11:22:52</CreDtTm>

**P1825** 			</Mvmnt>

**P1826** 		</Mvmnts>

**P1827** 	</IntraBalMvmntPdgRpt>

**P1828** </Document>

