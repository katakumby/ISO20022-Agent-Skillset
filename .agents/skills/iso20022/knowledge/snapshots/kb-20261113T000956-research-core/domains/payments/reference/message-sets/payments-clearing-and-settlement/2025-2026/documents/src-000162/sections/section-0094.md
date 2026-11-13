---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 2", "First FIToFICustomerCreditTransfer"]
content_origin: "source-transcription"
---

# First FIToFICustomerCreditTransfer

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / FIToFICustomerCreditTransfer pacs.008.001.14 - 2 / First FIToFICustomerCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1796** First FIToFICustomerCreditTransfer

**P1797** Description 

**P1798** Biogenetics-Crops, Glasgow, subsidiary of Biogenetics HQ, London, has received an invoice with number SX-25T, dated 13 October 2010 from Seed Inc., Dublin: 75 thousand EUR needs to be paid to the account of Seed Inc. IE29CCCC93115212345678 held at CCCC Bank, Dublin (CCCCIE2D). Transaction charges for the payment are shared between Biogenetics and Seed Inc.

**P1799** The payment of all Biogenetics invoices is centralised at Biogenetics HQ. It assigns reference CROPS/SX-25T/

**P1800** 2015-10-13 to the payment order and passes it on to AAAA Bank (AAAAGB2L) where it holds the account

**P1801** 46373892034012. AAAA Bank sends the payment to its correspondent BBBB Bank in Dublin (BBBBIE2D).

**P1802** Business Data 

**P1803** The first FIToFICustomerCreditTransfer, sent by AAAA Bank to BBBB Bank:

[T39 - complete table](../tables/tbl-0039.md)

**P1804** Message Instance

**P1805** <FIToFICstmrCdtTrf>

**P1806** 	<GrpHdr>

**P1807** 		<MsgId>AAAA/151109-CCT/EUR/443</MsgId>

**P1808** 		<CreDtTm>2015-11-09T10:09:13</CreDtTm>

**P1809** 		<NbOfTxs>1</NbOfTxs>

**P1810** 		<SttlmInf>

**P1811** 			<SttlmMtd>INDA</SttlmMtd>

**P1812** 		</SttlmInf>

**P1813** 		<InstgAgt>

**P1814** 			<FinInstnId>

**P1815** 				<BICFI>AAAAGB2L</BICFI>

**P1816** 			</FinInstnId>

**P1817** 		</InstgAgt>

**P1818** 		<InstdAgt>

**P1819** 			<FinInstnId>

**P1820** 				<BICFI>BBBBIE2D</BICFI>

**P1821** 			</FinInstnId>

**P1822** 		</InstdAgt>

**P1823** 	</GrpHdr>

**P1824** 	<CdtTrfTxInf>

**P1825** 		<PmtId>

**P1826** 			<InstrId>AAAA/151109-CCT/EUR/443/1</InstrId>

**P1827** 			<EndToEndId>CROPS/SX-25T/2015-10-13</EndToEndId>

**P1828** 			<TxId>AAAA/151109-CCT/EUR/443/1</TxId>

**P1829** 		</PmtId>

**P1830** 		<IntrBkSttlmAmt Ccy="EUR">750000</IntrBkSttlmAmt>

**P1831** 		<IntrBkSttlmDt>2015-11-09</IntrBkSttlmDt>

**P1832** 		<InstdAmt Ccy="EUR">75000</InstdAmt>

**P1833** 		<ChrgBr>SHAR</ChrgBr>

**P1834** 		<UltmtDbtr>

**P1835** 			<Nm>Biogenetics - CROPS</Nm>

**P1836** 			<PstlAdr>

**P1837** 				<StrtNm>Growth Street</StrtNm>

**P1838** 				<BldgNb>17</BldgNb>

**P1839** 				<PstCd>G5 OTW</PstCd>

**P1840** 				<TwnNm>Glasgow</TwnNm>

**P1841** 				<Ctry>GB</Ctry>

**P1842** 			</PstlAdr>

**P1843** 		</UltmtDbtr>

**P1844** 		<Dbtr>

**P1845** 			<Nm>Biogenetics - HQ</Nm>

**P1846** 			<PstlAdr>

**P1847** 				<StrtNm>Corn Street</StrtNm>

**P1848** 				<BldgNb>13</BldgNb>

**P1849** 				<PstCd>W6 8DR</PstCd>

**P1850** 				<TwnNm>London</TwnNm>

**P1851** 				<Ctry>GB</Ctry>

**P1852** 			</PstlAdr>

**P1853** 		</Dbtr>

**P1854** 		<DbtrAcct>

**P1855** 			<Id>

**P1856** 				<Othr>

**P1857** 					<Id>46373892034012</Id>

**P1858** 				</Othr>

**P1859** 			</Id>

**P1860** 		</DbtrAcct>

**P1861** 		<DbtrAgt>

**P1862** 			<FinInstnId>

**P1863** 				<BICFI>AAAAGB2L</BICFI>

**P1864** 			</FinInstnId>

**P1865** 		</DbtrAgt>

**P1866** 		<CdtrAgt>

**P1867** 			<FinInstnId>

**P1868** 				<BICFI>CCCCIE2D</BICFI>

**P1869** 			</FinInstnId>

**P1870** 		</CdtrAgt>

**P1871** 		<Cdtr>

**P1872** 			<Nm>Seed Inc.</Nm>

**P1873** 			<PstlAdr>

**P1874** 				<StrtNm>Grain Lane</StrtNm>

**P1875** 				<BldgNb>27</BldgNb>

**P1876** 				<TwnNm>Dublin</TwnNm>

**P1877** 				<Ctry>IE</Ctry>

**P1878** 			</PstlAdr>

**P1879** 		</Cdtr>

**P1880** 		<CdtrAcct>

**P1881** 			<Id>

**P1882** 				<IBAN>IE29CCCC93115212345678</IBAN>

**P1883** 			</Id>

**P1884** 		</CdtrAcct>

**P1885** 		<Purp>

**P1886** 			<Cd>GDDS</Cd>

**P1887** 		</Purp>

**P1888** 		<RmtInf>

**P1889** 			<Strd>

**P1890** 				<RfrdDocInf>

**P1891** 					<Tp>

**P1892** 						<CdOrPrtry>

**P1893** 							<Cd>CINV</Cd>

**P1894** 						</CdOrPrtry>

**P1895** 					</Tp>

**P1896** 					<Nb>SX-25T</Nb>

**P1897** 					<RltdDt>

**P1898** 					<Tp>

**P1899** 						<Cd>INDA</Cd>

**P1900** 					</Tp>

**P1901** 					<Dt>2015-10-13</Dt>									

**P1902** 					</RltdDt>					

**P1903** 				</RfrdDocInf>

**P1904** 			</Strd>

**P1905** 		</RmtInf>

**P1906** 	</CdtTrfTxInf>

**P1907** </FIToFICstmrCdtTrf>

