---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 2", "Second FIToFICustomerCreditTransfer"]
content_origin: "source-transcription"
---

# Second FIToFICustomerCreditTransfer

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / FIToFICustomerCreditTransfer pacs.008.001.14 - 2 / Second FIToFICustomerCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1908** Second FIToFICustomerCreditTransfer

**P1909** Description

**P1910** On receipt of the payment instruction, BBBB Bank debits AAAA Bank account, deducts its processing charges and sends an FIToFICustomerCreditTransfer to CCCC Bank, Dublin across the Irish RTGS system.

**P1911** Business Data 

**P1912** The second FIToFICustomerCreditTransfer, sent by BBBB Bank to CCCC Bank:

[T40 - complete table](../tables/tbl-0040.md)

**P1913** Message Instance

**P1914** <FIToFICstmrCdtTrf>

**P1915** 	<GrpHdr>

**P1916** 		<MsgId>BBBB/151109-CBJO56</MsgId>

**P1917** 		<CreDtTm>2015-11-09T10:13:00</CreDtTm>

**P1918** 		<NbOfTxs>1</NbOfTxs>

**P1919** 		<SttlmInf>

**P1920** 			<SttlmMtd>CLRG</SttlmMtd>

**P1921** 			<ClrSys>

**P1922** 				<Prtry>CBJ</Prtry>

**P1923** 			</ClrSys>

**P1924** 		</SttlmInf>

**P1925** 		<InstgAgt>

**P1926** 			<FinInstnId>

**P1927** 				<BICFI>BBBBIE2D</BICFI>

**P1928** 			</FinInstnId>

**P1929** 		</InstgAgt>

**P1930** 		<InstdAgt>

**P1931** 			<FinInstnId>

**P1932** 				<BICFI>CCCCIE2D</BICFI>

**P1933** 			</FinInstnId>

**P1934** 		</InstdAgt>

**P1935** 	</GrpHdr>

**P1936** 	<CdtTrfTxInf>

**P1937** 		<PmtId>

**P1938** 			<InstrId>BBBB/151109/-CBJ056/1</InstrId>

**P1939** 			<EndToEndId>CROPS/SX-25T/2015-10-13</EndToEndId>

**P1940** 			<TxId>AAAA/151109-CCT/EUR/443/1</TxId>

**P1941** 		</PmtId>

**P1942** 		<IntrBkSttlmAmt Ccy="EUR">74900</IntrBkSttlmAmt>

**P1943** 		<IntrBkSttlmDt>2015-11-09</IntrBkSttlmDt>

**P1944** 		<InstdAmt Ccy="EUR">75000</InstdAmt>

**P1945** 		<ChrgBr>SHAR</ChrgBr>

**P1946** 		<ChrgsInf>

**P1947** 			<Amt Ccy="EUR">100</Amt>

**P1948** 			<Agt>

**P1949** 				<FinInstnId>

**P1950** 					<BICFI>BBBBIE2D</BICFI>

**P1951** 				</FinInstnId>

**P1952** 			</Agt>

**P1953** 		</ChrgsInf>

**P1954** 		<UltmtDbtr>

**P1955** 			<Nm>Biogenetics - CROPS</Nm>

**P1956** 			<PstlAdr>

**P1957** 				<StrtNm>Growth Street</StrtNm>

**P1958** 				<BldgNb>17</BldgNb>

**P1959** 				<PstCd>G5 OTW</PstCd>

**P1960** 				<TwnNm>Glasgow</TwnNm>

**P1961** 				<Ctry>GB</Ctry>

**P1962** 			</PstlAdr>

**P1963** 		</UltmtDbtr>

**P1964** 		<Dbtr>

**P1965** 			<Nm>Biogenetics - HQ</Nm>

**P1966** 			<PstlAdr>

**P1967** 				<StrtNm>Corn Street</StrtNm>

**P1968** 				<BldgNb>13</BldgNb>

**P1969** 				<PstCd>W6 8DR</PstCd>

**P1970** 				<TwnNm>London</TwnNm>

**P1971** 				<Ctry>GB</Ctry>

**P1972** 			</PstlAdr>

**P1973** 		</Dbtr>

**P1974** 		<DbtrAcct>

**P1975** 			<Id>

**P1976** 				<Othr>

**P1977** 					<Id>46373892034012</Id>

**P1978** 				</Othr>

**P1979** 			</Id>

**P1980** 		</DbtrAcct>

**P1981** 		<DbtrAgt>

**P1982** 			<FinInstnId>

**P1983** 				<BICFI>AAAAGB2L</BICFI>

**P1984** 			</FinInstnId>

**P1985** 		</DbtrAgt>

**P1986** 		<CdtrAgt>

**P1987** 			<FinInstnId>

**P1988** 				<BICFI>CCCCIE2D</BICFI>

**P1989** 			</FinInstnId>

**P1990** 		</CdtrAgt>

**P1991** 		<Cdtr>

**P1992** 			<Nm>Seed Inc.</Nm>

**P1993** 			<PstlAdr>

**P1994** 				<StrtNm>Grain Lane</StrtNm>

**P1995** 				<BldgNb>27</BldgNb>

**P1996** 				<TwnNm>Dublin</TwnNm>

**P1997** 				<Ctry>IE</Ctry>

**P1998** 			</PstlAdr>

**P1999** 		</Cdtr>

**P2000** 		<CdtrAcct>

**P2001** 			<Id>

**P2002** 				<IBAN>IE29CCCC93115212345678</IBAN>

**P2003** 			</Id>

**P2004** 		</CdtrAcct>

**P2005** 		<Purp>

**P2006** 			<Cd>GDDS</Cd>

**P2007** 		</Purp>

**P2008** 		<RmtInf>

**P2009** 			<Strd>

**P2010** 				<RfrdDocInf>

**P2011** 					<Tp>

**P2012** 						<CdOrPrtry>

**P2013** 							<Cd>CINV</Cd>

**P2014** 						</CdOrPrtry>

**P2015** 					</Tp>

**P2016** 					<Nb>SX-25T</Nb>

**P2017** 					<RltdDt>

**P2018** 					<Tp>

**P2019** 						<Cd>INDA</Cd>

**P2020** 					</Tp>

**P2021** 					<Dt>2015-10-13</Dt>									

**P2022** 					</RltdDt>						

**P2023** 				</RfrdDocInf>

**P2024** 			</Strd>

**P2025** 		</RmtInf>

**P2026** 	</CdtTrfTxInf>

**P2027** </FIToFICstmrCdtTrf>

