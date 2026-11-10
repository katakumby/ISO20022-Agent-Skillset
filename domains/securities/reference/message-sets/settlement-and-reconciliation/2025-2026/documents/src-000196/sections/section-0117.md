---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionReversalAdvice sese.026.001.12"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionReversalAdvice sese.026.001.12

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesSettlementTransactionReversalAdvice sese.026.001.12.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2044** SecuritiesSettlementTransactionReversalAdvice sese.026.001.12

**P2045** Description

**P2046** On the 09 January 2019, Dresdner Bank London (DRESGB2L) informs its customer, Dresdner Bank Frankfurt (DRESDEFF). that the a previously confirmed movement of securities is reversed. This is done with the SecuritiesSettlementTransactionReversalAdvice (sese.026.001.06).

**P2047** Business Data

**P2048** Account Owner Transaction Id: FRTJ123DEL2

**P2049** Securities Movement Type: delivery

**P2050** Payment: against payment

**P2051** Confirmation reference previously sent: D9876XYZD2

**P2052** Trade Date: 05/01/2019

**P2053** Effective Settlement Date: 08/01/2019

**P2054** Deal price: par value

**P2055** Rate: 101.002

**P2056** Financial Instrument and Description: BE0123456789 Belgium Company XYZ

**P2057** Quantity: face amount 5,000,000

**P2058** Safekeeping Account: 222S

**P2059** Securities Transaction Type: trade

**P2060** Receiving Depository: NBBEBEBB (National bank of Belgium)

**P2061** Receiving Settlement Parties1: CITIBEBB (Citibank)

**P2062** Receiving Settlement Parties2: CFPIDEFF (Commerz account 321654)

**P2063** Message Instance

**P2064** <SctiesSttlmTxRvslAdvc>

**P2065** <TxIdDtls>

**P2066** 	<AcctOwnrTxId>FRTJ123DEL2</AcctOwnrTxId>

**P2067** 		<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P2068** 		<Pmt>APMT</Pmt>

**P2069** 	</TxIdDtls>

**P2070** 	<ConfRef>

**P2071** 		<Id>D9876XYZD2</Id>

**P2072** 	</ConfRef>

**P2073** 	<TradDtls>

**P2074** 		<TradDt>

**P2075** 			<Dt>

**P2076** 				<Dt>2019-01-05</Dt>

**P2077** 			</Dt>

**P2078** 		</TradDt>

**P2079** 		<FctvSttlmDt>

**P2080** 			<Dt>

**P2081** 				<Dt>2019-01-08</Dt>

**P2082** 			</Dt>

**P2083** 		</FctvSttlmDt>

**P2084** 		<DealPric>

**P2085** 			<Tp>

**P2086** 				<ValTp>PARV</ValTp>

**P2087** 			</Tp>

**P2088** 			<Val>

**P2089** 				<Rate>101.002</Rate>

**P2090** 			</Val>

**P2091** 		</DealPric>

**P2092** 	</TradDtls>

**P2093** 	<FinInstrmId>

**P2094** 		<ISIN>BE0123456789</ISIN>

**P2095** 		<Desc>Belgium Company XYZ</Desc>

**P2096** 	</FinInstrmId>

**P2097** 	<QtyAndAcctDtls>

**P2098** 		<SttldQty>

**P2099** 			<Qty>

**P2100** 				<FaceAmt>5000000</FaceAmt>

**P2101** 			</Qty>

**P2102** 		</SttldQty>

**P2103** 		<SfkpgAcct>

**P2104** 			<Id>222S</Id>

**P2105** 		</SfkpgAcct>

**P2106** 	</QtyAndAcctDtls>

**P2107** 	<SttlmParams>

**P2108** 		<SctiesTxTp>

**P2109** 			<Cd>TRAD</Cd>

**P2110** 		</SctiesTxTp>

**P2111** 	</SttlmParams>

**P2112** 	<RcvgSttlmPties>

**P2113** 		<Dpstry>

**P2114** 			<Id>

**P2115** 				<AnyBIC>NBBEBEBB</AnyBIC>

**P2116** 			</Id>

**P2117** 		</Dpstry>

**P2118** 		<Pty1>

**P2119** 			<Id>

**P2120** 				<AnyBIC>CITIBEBB</AnyBIC>

**P2121** 			</Id>

**P2122** 		</Pty1>

**P2123** 		<Pty2>

**P2124** 			<Id>

**P2125** 				<AnyBIC>CFPIDEFF</AnyBIC>

**P2126** 			</Id>

**P2127** 			<SfkpgAcct>

**P2128** 				<Id>321654</Id>

**P2129** 			</SfkpgAcct>

**P2130** 		</Pty2>

**P2131** 	</RcvgSttlmPties>

**P2132** 	<SttldAmt>

**P2133** 		<AcrdIntrstInd>true</AcrdIntrstInd>

**P2134** 		<Amt Ccy="EUR">5057200</Amt>

**P2135** 		<CdtDbtInd>CRDT</CdtDbtInd>

**P2136** 	</SttldAmt>

**P2137** </SctiesSttlmTxRvslAdvc>

