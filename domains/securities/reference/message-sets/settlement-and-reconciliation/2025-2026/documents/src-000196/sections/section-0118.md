---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesTransactionCancellationRequestStatusAdvice sese.027.001.09"]
content_origin: "source-transcription"
---

# SecuritiesTransactionCancellationRequestStatusAdvice sese.027.001.09

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesTransactionCancellationRequestStatusAdvice sese.027.001.09.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2138** SecuritiesTransactionCancellationRequestStatusAdvice sese.027.001.09

**P2139** Description

**P2140** On the 08 January 2019, the account servicer, Dresdner Bank London (DRESGB2L), informs the account owner Dresdner Bank Frankfurt (DRESDEFF) of the status for the cancellation request previously sent for a transaction. This is done through a SecuritiesTransactionCancellationRequestStatusAdvice (sese.027.001.05)

**P2141** Business Data

**P2142** Cancellation Request Reference: FRTJ123DEL2CANC

**P2143** Account Owner Transaction Identification: FRTJ123DEL2

**P2144** Securities Movement Type: Delivery

**P2145** Payment: against payment

**P2146** Processing Status: repair

**P2147** Reason: received too late

**P2148** Safekeeping Account: 222S

**P2149** Financial Instrument: BE0123456789

**P2150** Message Instance

**P2151** <SctiesTxCxlReqStsAdvc>

**P2152** 	<CxlReqRef>

**P2153** 		<Id>FRTJ123DEL2CANC</Id>

**P2154** 	</CxlReqRef>

**P2155** 	<TxId>

**P2156** 		<AcctOwnrTxId>

**P2157** 			<SctiesSttlmTxId>

**P2158** 				<TxId>FRTJ123DEL2</TxId>

**P2159** 				<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P2160** 				<Pmt>APMT</Pmt>

**P2161** 			</SctiesSttlmTxId>

**P2162** 		</AcctOwnrTxId>

**P2163** 	</TxId>

**P2164** 	<PrcgSts>

**P2165** 		<Rpr>

**P2166** 			<Rsn>

**P2167** 				<Cd>

**P2168** 					<Cd>LATE</Cd>

**P2169** 				</Cd>

**P2170** 			</Rsn>

**P2171** 		</Rpr>

**P2172** 	</PrcgSts>

**P2173** 	<TxDtls>

**P2174** 		<SfkpgAcct>

**P2175** 			<Id>222S</Id>

**P2176** 		</SfkpgAcct>

**P2177** 		<FinInstrmId>

**P2178** 			<ISIN>BE0123456789</ISIN>

**P2179** 			<Desc>Belgium Company XYZ </Desc>

**P2180** 		</FinInstrmId>

**P2181** 		<SttlmQty>

**P2182** 			<Qty>

**P2183** 				<FaceAmt>5000000</FaceAmt>

**P2184** 			</Qty>

**P2185** 		</SttlmQty>

**P2186** 		<SttlmAmt>

**P2187** 			<Amt Ccy="EUR">5057200</Amt>

**P2188** 			<CdtDbtInd>CRDT</CdtDbtInd>

**P2189** 		</SttlmAmt>

**P2190** 		<TradDt>

**P2191** 			<Dt>

**P2192** 				<Dt>2019-01-05</Dt>

**P2193** 			</Dt>

**P2194** 		</TradDt>

**P2195** 		<SttlmDt>

**P2196** 			<Dt>

**P2197** 				<Dt>2019-01-08</Dt>

**P2198** 			</Dt>

**P2199** 		</SttlmDt>

**P2200** 		<RcvgSttlmPties>

**P2201** 			<Dpstry>

**P2202** 				<Id>

**P2203** 					<AnyBIC>NBBEBEBB</AnyBIC>

**P2204** 				</Id>

**P2205** 			</Dpstry>

**P2206** 			<Pty1>

**P2207** 				<Id>

**P2208** 					<AnyBIC>CITIBEBB</AnyBIC>

**P2209** 				</Id>

**P2210** 			</Pty1>

**P2211** 			<Pty2>

**P2212** 				<Id>

**P2213** 					<AnyBIC>CFPIDEFF</AnyBIC>

**P2214** 				</Id>

**P2215** 				<SfkpgAcct>

**P2216** 					<Id>321654</Id>

**P2217** 				</SfkpgAcct>

**P2218** 			</Pty2>

**P2219** 		</RcvgSttlmPties>

**P2220** 	</TxDtls>

**P2221** </SctiesTxCxlReqStsAdvc>

