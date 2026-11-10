---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Business Examples", "CorporateActionInstructionStatementReport seev.042.00x.14"]
content_origin: "source-transcription"
---

# CorporateActionInstructionStatementReport seev.042.00x.14

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Business Examples / CorporateActionInstructionStatementReport seev.042.00x.14.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1682** CorporateActionInstructionStatementReport seev.042.00x.14

**P1683** Description

**P1684** This example describes a CorporateActionStatementReport sent by an account servicer. It contains reporting information about 2 corporate action events for a single safekeeping account. The information reported on the 2 corporate action events is the total eligible balance, the uninstructed balance and the breakdown of the instructed balance per option.

**P1685** The CorporateActionStatementReport message is sent on 20 September 2010 to the account owner and reports only on the missing instructions for a single account but for 2 corporate action events that were announced between the 15 August 2010 and the 20 September 2010. This message is part of a daily statement report and consists of a full report (as opposed to reporting only changes from the previous report).

**P1686** The first corporate action event is a distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares, cash. 

**P1687** The second corporate action event is early redemption of a security, at the election of the holder, subject to the terms and conditions of the issue

**P1688** Business Data

**P1689** Issues names

**P1690** For the dividend option: Glaxo Holdings - ISIN GB0007123466

**P1691** For the early bond redemption: Nat West Variable Rate Capital Notes due 30 September 2010 - ISIN GB0037583977

**P1692** Instructions status

**P1693** For the dividend option, the total eligible balance is 80.000 units of which 50.000 are uninstructed and 30.000 have been instructed on option 2 (securities).

**P1694** For the early bond redemption, the total eligible balance is an amount of 20.000.000 of which 150.000.000 are uninstructed and 50.000.000 have been instructed on option 1 (cash).

**P1695** Relative dates

**P1696** For the dividend option, Dividend payment date - 02 October 2010 and Response deadline date - 23 September 2010.

**P1697** For the early bond redemption, redemption date - 30 September 2010 and Response deadline date - 26 September 2010.

**P1698** Transaction description

**P1699** The safekeeping account is 98-0112441-05.

**P1700** For the dividend option event, the total eligible balance is 80.000 units and 30.000 units have been instructed for option 2 (securities) whilst 50.000 units are still uninstructed. The response deadline set by the account servicer is 23 September 2010 at 17h00.

**P1701** For the early bond redemption, the total eligible balance is an amount of 20.000.000 and 5.000.000 have been instructed for option 1 (cash) whilst 15.000.000 are still uninstructed. The response deadline set by the account servicer is 26 September 2010 at 17h00.

**P1702** Message Instance (with application header)

**P1703** <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02" xmlns:n1="http://www.w3.org/2000/09/xmldsig#">

**P1704** 	<Fr>

**P1705** 		<FIId>

**P1706** 			<FinInstnId>

**P1707** 				<BICFI>ABCDBEBBXXX</BICFI>

**P1708** 			</FinInstnId>

**P1709** 		</FIId>

**P1710** 	</Fr>

**P1711** 	<To>

**P1712** 		<FIId>

**P1713** 			<FinInstnId>

**P1714** 				<BICFI>WXYZFRPP666</BICFI>

**P1715** 			</FinInstnId>

**P1716** 		</FIId>

**P1717** 	</To>

**P1718** 	<BizMsgIdr>LOCCUS0000000345</BizMsgIdr>

**P1719** 	<MsgDefIdr>seev.042.001.14</MsgDefIdr>

**P1720** 	<CreDt>2010-09-20T17:30:00Z</CreDt>

**P1721** </AppHdr>

**P1722** <Document xmlns="urn:iso:std:iso:20022:tech:xsd:seev.042.001.14" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

**P1723** <CorpActnInstrStmtRpt>

**P1724** 	<Pgntn>

**P1725** 		<PgNb>1</PgNb>

**P1726** 		<LastPgInd>true</LastPgInd>

**P1727** 	</Pgntn>

**P1728** 	<StmtGnlDtls>

**P1729** 		<StmtTp>MISS</StmtTp>

**P1730** 		<RptgTp>SAME</RptgTp>

**P1731** 		<StmtId>ST20100920-1</StmtId>

**P1732** 		<RptNb>1</RptNb>

**P1733** 		<StmtDtTm>

**P1734** 			<DtTm>2010-09-20T17:00:00</DtTm>

**P1735** 		</StmtDtTm>

**P1736** 		<Frqcy>

**P1737** 			<Cd>DAIL</Cd>

**P1738** 		</Frqcy>

**P1739** 		<UpdTp>

**P1740** 			<Cd>COMP</Cd>

**P1741** 		</UpdTp>

**P1742** 	<ActvtyInd>true</ActvtyInd>

**P1743** 		<NtfctnDdlnPrd>

**P1744** 			<Dt>

**P1745** 				<FrDt>2010-08-15</FrDt>

**P1746** 				<ToDt>2010-09-19</ToDt>

**P1747** 			</Dt>

**P1748** 		</NtfctnDdlnPrd>

**P1749** 	</StmtGnlDtls>

**P1750** 	<AcctAndStmtDtls>

**P1751** 		<SfkpgAcct>98-0112441-05</SfkpgAcct>

**P1752** 		<CorpActnEvtAndBal>

**P1753** 			<GnlInf>

**P1754** 				<CorpActnEvtId>DIVGLAX123</CorpActnEvtId>

**P1755** 				<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1756** 				<EvtTp>

**P1757** 					<Cd>DVOP</Cd>

**P1758** 				</EvtTp>

**P1759** 				<MndtryVlntryEvtTp>

**P1760** 					<Cd>CHOS</Cd>

**P1761** 				</MndtryVlntryEvtTp>

**P1762** 				<LastNtfctnId>

**P1763** 					<Id>1997189-012</Id>

**P1764** 				</LastNtfctnId>

**P1765** 			</GnlInf>

**P1766** 			<UndrlygScty>

**P1767** 				<ISIN>GB0007123466</ISIN>

**P1768** 				<Desc>GLAXO HOLDINGS</Desc>

**P1769** 			</UndrlygScty>

**P1770** 			<Bal>

**P1771** 				<TtlElgblBal>

**P1772** 					<QtyChc>

**P1773** 						<SgndQty>

**P1774** 							<ShrtLngPos>LONG</ShrtLngPos>

**P1775** 							<Qty>

**P1776** 								<Unit>80000</Unit>

**P1777** 							</Qty>

**P1778** 						</SgndQty>

**P1779** 					</QtyChc>

**P1780** 				</TtlElgblBal>

**P1781** 				<UinstdBal>

**P1782** 					<Bal>

**P1783** 						<ShrtLngPos>LONG</ShrtLngPos>

**P1784** 						<QtyChc>

**P1785** 							<Qty>

**P1786** 								<Unit>50000</Unit>

**P1787** 							</Qty>

**P1788** 						</QtyChc>

**P1789** 					</Bal>

**P1790** 				</UinstdBal>

**P1791** 				<TtlInstdBalDtls>

**P1792** 					<TtlInstdBal>

**P1793** 						<Bal>

**P1794** 							<ShrtLngPos>LONG</ShrtLngPos>

**P1795** 							<QtyChc>

**P1796** 								<Qty>

**P1797** 									<Unit>30000</Unit>

**P1798** 								</Qty>

**P1799** 							</QtyChc>

**P1800** 						</Bal>

**P1801** 					</TtlInstdBal>

**P1802** 					<OptnDtls>

**P1803** 						<OptnNb>002</OptnNb>

**P1804** 						<OptnTp>

**P1805** 							<Cd>SECU</Cd>

**P1806** 						</OptnTp>

**P1807** 						<InstdBal>

**P1808** 							<Bal>

**P1809** 							  <ShrtLngPos>LONG</ShrtLngPos>

**P1810** 								<QtyChc>

**P1811** 									<Qty>

**P1812** 									  <Unit>3000</Unit>

**P1813** 									</Qty>

**P1814** 								</QtyChc>

**P1815** 							</Bal>

**P1816** 						</InstdBal>

**P1817** 						<EvtDdlns>

**P1818** 							<RspnDdln>

**P1819** 								<Dt>

**P1820** 									<DtTm>2010-09-23T17:00:00</DtTm>

**P1821** 								</Dt>

**P1822** 							</RspnDdln>

**P1823** 						</EvtDdlns>

**P1824** 					</OptnDtls>

**P1825** 				</TtlInstdBalDtls>

**P1826** 			</Bal>

**P1827** 		</CorpActnEvtAndBal>

**P1828** 		<CorpActnEvtAndBal>

**P1829** 			<GnlInf>

**P1830** 				<CorpActnEvtId>BPT3437592</CorpActnEvtId>

**P1831** 				<OffclCorpActnEvtId>BI01593212345</OffclCorpActnEvtId>

**P1832** 				<EvtTp>

**P1833** 					<Cd>BPUT</Cd>

**P1834** 				</EvtTp>

**P1835** 				<MndtryVlntryEvtTp>

**P1836** 					<Cd>VOLU</Cd>

**P1837** 				</MndtryVlntryEvtTp>

**P1838** 				<LastNtfctnId>

**P1839** 					<Id>201067839055</Id>

**P1840** 				</LastNtfctnId>

**P1841** 			</GnlInf>

**P1842** 			<UndrlygScty>

**P1843** 				<ISIN>GB0037583977</ISIN>

**P1844** 				<Desc>NATWEST VAR NOTE 2010</Desc>

**P1845** 			</UndrlygScty>

**P1846** 			<Bal>

**P1847** 				<TtlElgblBal>

**P1848** 					<QtyChc>

**P1849** 						<SgndQty>

**P1850** 							<ShrtLngPos>LONG</ShrtLngPos>

**P1851** 							<Qty>

**P1852** 							  <FaceAmt>20000000</FaceAmt>

**P1853** 							</Qty>

**P1854** 						</SgndQty>

**P1855** 					</QtyChc>

**P1856** 				</TtlElgblBal>

**P1857** 				<UinstdBal>

**P1858** 					<Bal>

**P1859** 						<ShrtLngPos>LONG</ShrtLngPos>

**P1860** 						<QtyChc>

**P1861** 							<Qty>

**P1862** 							    <FaceAmt>15000000</FaceAmt>

**P1863** 							</Qty>

**P1864** 						</QtyChc>

**P1865** 					</Bal>

**P1866** 				</UinstdBal>

**P1867** 				<TtlInstdBalDtls>

**P1868** 					<TtlInstdBal>

**P1869** 						<Bal>

**P1870** 							<ShrtLngPos>LONG</ShrtLngPos>

**P1871** 							<QtyChc>

**P1872** 								<Qty>

**P1873** 							      <FaceAmt>5000000</FaceAmt>

**P1874** 								</Qty>

**P1875** 							</QtyChc>

**P1876** 						</Bal>

**P1877** 					</TtlInstdBal>

**P1878** 					<OptnDtls>

**P1879** 						<OptnNb>001</OptnNb>

**P1880** 						<OptnTp>

**P1881** 							<Cd>CASH</Cd>

**P1882** 						</OptnTp>

**P1883** 						<InstdBal>

**P1884** 							<Bal>

**P1885** 							 	<ShrtLngPos>LONG</ShrtLngPos>

**P1886** 								<QtyChc>

**P1887** 									<Qty>

**P1888** 					              	    	<FaceAmt>5000000</FaceAmt>

**P1889** 									</Qty>

**P1890** 								</QtyChc>

**P1891** 							</Bal>

**P1892** 						</InstdBal>

**P1893** 						<EvtDdlns>2010-09-23T17:00:00

**P1894** 							<RspnDdln>

**P1895** 								<DtTm>2010-09-26T17:00:00</DtTm>

**P1896** 							</RspnDdln>

**P1897** 						</EvtDdlns>

**P1898** 					</OptnDtls>

**P1899** 				</TtlInstdBalDtls>

**P1900** 			</Bal>

**P1901** 		</CorpActnEvtAndBal>

**P1902** 	</AcctAndStmtDtls>

**P1903** </CorpActnInstrStmtRpt>

**P1904** </Document>

**P1907**   


