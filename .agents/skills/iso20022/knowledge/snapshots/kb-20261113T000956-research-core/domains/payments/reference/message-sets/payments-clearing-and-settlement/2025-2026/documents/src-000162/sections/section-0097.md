---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FinancialInstitutionCreditTransfer pacs.009.001.13 - 1", "First FinancialInstitutionCreditTransfer"]
content_origin: "source-transcription"
---

# First FinancialInstitutionCreditTransfer

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / FinancialInstitutionCreditTransfer pacs.009.001.13 - 1 / First FinancialInstitutionCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2030** First FinancialInstitutionCreditTransfer

**P2031** Description 

**P2032** Under business example 1 of the FIToFICustomerCreditTransfer, BBBB Bank, New York (BBBBUS33) sent an FIToFICustomerCreditTransfer message to AAAA Bank (AAAAGB2L) using the cover method as BBBB Bank does not have a JPY account relationship with AAAA Bank. BBBB Bank uses CCCC Bank, Tokyo as its correspondent. AAAA Bank uses AAAA Bank, Tokyo (AAAAJPJT) as its JPY correspondent.  Immediately after sending the FIToFICustomerCreditTransfer to AAAA Bank, BBBB Bank sends its correspondent CCCC Bank a FinancialInstitutionCreditTransfer message to cover the customer payment.

**P2033** Business Data 

**P2034** FinancialInstitutionCreditTransfer from BBBB Bank to CCCC Bank:

[T41 - complete table](../tables/tbl-0041.md)

**P2035** Message Instance

**P2036** <FICdtTrf>

**P2037** 	<GrpHdr>

**P2038** 		<MsgId>BBBB/150928-FICT/JPY/430</MsgId>

**P2039** 		<CreDtTm>2015-09-28T16:00:00</CreDtTm>

**P2040** 		<NbOfTxs>1</NbOfTxs>

**P2041** 		<SttlmInf>

**P2042** 			<SttlmMtd>INDA</SttlmMtd>

**P2043** 		</SttlmInf>

**P2044** 		<InstgAgt>

**P2045** 			<FinInstnId>

**P2046** 				<BICFI>BBBBUS33</BICFI>

**P2047** 			</FinInstnId>

**P2048** 		</InstgAgt>

**P2049** 		<InstdAgt>

**P2050** 			<FinInstnId>

**P2051** 				<BICFI>CCCCJPJT</BICFI>

**P2052** 			</FinInstnId>

**P2053** 		</InstdAgt>

**P2054** 	</GrpHdr>

**P2055** 	<CdtTrfTxInf>

**P2056** 		<PmtId>

**P2057** 			<InstrId>BBBB/150928-FICT/JPY/430/1</InstrId>

**P2058** 			<EndToEndId>ABC/4562/2015-09-08</EndToEndId>

**P2059** 			<TxId>BBBB/150928-CCT/123/1</TxId>

**P2060** 		</PmtId>

**P2061** 		<IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>

**P2062** 		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>

**P2063** 		<Dbtr>

**P2064** 			<FinInstnId>

**P2065** 				<BICFI>BBBBUS33</BICFI>

**P2066** 			</FinInstnId>

**P2067** 		</Dbtr>

**P2068** 		<CdtrAgt>

**P2069** 			<FinInstnId>

**P2070** 				<BICFI>AAAAJPJT</BICFI>

**P2071** 			</FinInstnId>

**P2072** 		</CdtrAgt>

**P2073** 		<Cdtr>

**P2074** 			<FinInstnId>

**P2075** 				<BICFI>AAAAGB2L</BICFI>

**P2076** 			</FinInstnId>

**P2077** 		</Cdtr>

**P2078** 		<UndrlygCstmrCdtTrf>

**P2079** 			<InitgPty>

**P2080** 				<Nm>ABC Corporation</Nm>

**P2081** 				<PstlAdr>

**P2082** 					<StrtNm>Times Square</StrtNm>

**P2083** 					<BldgNb>7</BldgNb>

**P2084** 					<PstCd>NY 10036</PstCd>

**P2085** 					<TwnNm>New York</TwnNm>

**P2086** 					<Ctry>US</Ctry>

**P2087** 				</PstlAdr>

**P2088** 			</InitgPty>

**P2089** 			<Dbtr>

**P2090** 				<Nm>ABC Corporation</Nm>

**P2091** 				<PstlAdr>

**P2092** 					<StrtNm>Times Square</StrtNm>

**P2093** 					<BldgNb>7</BldgNb>

**P2094** 					<PstCd>NY 10036</PstCd>

**P2095** 					<TwnNm>New York</TwnNm>

**P2096** 					<Ctry>US</Ctry>

**P2097** 				</PstlAdr>

**P2098** 			</Dbtr>

**P2099** 				<DbtrAgt>

**P2100** 				<FinInstnId>

**P2101** 					<BICFI>BBBBUS33</BICFI>

**P2102** 				</FinInstnId>

**P2103** 			</DbtrAgt>

**P2104** 			<CdtrAgt>

**P2105** 				<FinInstnId>

**P2106** 					<BICFI>AAAAGB2L</BICFI>

**P2107** 				</FinInstnId>

**P2108** 			</CdtrAgt>

**P2109** 			<Cdtr>

**P2110** 				<Nm>DEF Electronics</Nm>

**P2111** 				<PstlAdr>

**P2112** 					<StrtNm>Mark Lane</StrtNm>

**P2113** 					<BldgNb>55</BldgNb>

**P2114** 					<PstCd>EC3RZNE</PstCd>

**P2115** 					<TwnNm>London</TwnNm>

**P2116** 					<Ctry>GB</Ctry>

**P2117** 					<AdrLine>Corn Exchange 5th Floor</AdrLine>

**P2118** 				</PstlAdr>

**P2119** 			</Cdtr>

**P2120** 			<CdtrAcct>

**P2121** 				<Id>

**P2122** 					<Othr>

**P2123** 						<Id>29683707994815</Id>

**P2124** 					</Othr>

**P2125** 				</Id>

**P2126** 			</CdtrAcct>

**P2127** 			<RmtInf>

**P2128** 				<Strd>

**P2129** 					<RfrdDocInf>

**P2130** 						<Tp>

**P2131** 							<CdOrPrtry>

**P2132** 								<Cd>CINV</Cd>

**P2133** 							</CdOrPrtry>

**P2134** 						</Tp>

**P2135** 						<Nb>4562</Nb>

**P2136** 						<RltdDt>

**P2137** 						<Tp>

**P2138** 							<Cd>INDA</Cd>

**P2139** 						</Tp>

**P2140** 						<Dt>2015-09-08</Dt>									

**P2141** 						</RltdDt>							

**P2142** 						</RfrdDocInf>

**P2143** 				</Strd>

**P2144** 			</RmtInf>

**P2145** 		</UndrlygCstmrCdtTrf>

**P2146** 	</CdtTrfTxInf>

**P2147** </FICdtTrf>

