---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionAllegementNotification sese.028.001.12"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionAllegementNotification sese.028.001.12

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / SecuritiesSettlementTransactionAllegementNotification sese.028.001.12.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2222** SecuritiesSettlementTransactionAllegementNotification sese.028.001.12

**P2223** Description

**P2224** On the 08 January 2019, Dresdner Bank London (DRESGB2L) advises its customer Dresdner Bank Frankfurt (DRESDEFF) that counterparty has alleged a settlement instruction, and that they could not find the corresponding instruction. This is done through a SecuritiesSettlementTransactionAllegement Notification (sese.028.001.06).

**P2225** Business Data

**P2226** Transaction identification: A4321BCD1SA1

**P2227** Securities Movement Type: delivery

**P2228** Payment: free

**P2229** Trade Date: 05/01/2019

**P2230** Settlement Date: 08/01/2019

**P2231** Financial Instrument: GB0000054321

**P2232** Quantity: unit 10,000

**P2233** Safekeeping Account: 222S

**P2234** Securities Transaction Type: trade

**P2235** Delivering Depository: CRSTGB22 (CREST)

**P2236** Delivering Party 1: CREST account 456

**P2237** Delivering Party 2: CPFIDEFF (Commerz Financial Products, GmbH, Frankfurt)

**P2238** Receiving Party1: CREST account 123

**P2239** Receiving Party 2: MGTCDE55 (JP Morgan Investment GmbH, Frankfurt)

**P2240** Message Instance

**P2241** <SctiesSttlmTxAllgmtNtfctn>

**P2242** 	<TxId>A4321BCD1SA1</TxId>

**P2243** 	<SttlmTpAndAddtlParams>

**P2244** 		<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P2245** 		<Pmt>FREE</Pmt>

**P2246** 	</SttlmTpAndAddtlParams>

**P2247** 	<TradDtls>

**P2248** 		<TradDt>

**P2249** 			<Dt>

**P2250** 				<Dt>2019-01-05</Dt>

**P2251** 			</Dt>

**P2252** 		</TradDt>

**P2253** 		<SttlmDt>

**P2254** 			<Dt>

**P2255** 			<Dt>2019-01-08</Dt>

**P2256** 			</Dt>

**P2257** 		</SttlmDt>

**P2258** 	</TradDtls>

**P2259** 	<FinInstrmId>

**P2260** 		<ISIN>GB0000054321</ISIN>

**P2261** 		</FinInstrmId>

**P2262** 	<QtyAndAcctDtls>

**P2263** 		<SttlmQty>

**P2264** 			<Unit>10000</Unit>

**P2265** 		</SttlmQty>

**P2266** 		<SfkpgAcct>

**P2267** 			<Id>222S</Id>

**P2268** 		</SfkpgAcct>

**P2269** 	</QtyAndAcctDtls>

**P2270** 	<SttlmParams>

**P2271** 		<SctiesTxTp>

**P2272** 			<Cd>TRAD</Cd>

**P2273** 		</SctiesTxTp>

**P2274** 	</SttlmParams>

**P2275** 	<DlvrgSttlmPties>

**P2276** 		<Dpstry>

**P2277** 			<Id>

**P2278** 				<AnyBIC>CRSTGB22</AnyBIC>

**P2279** 			</Id>

**P2280** 		</Dpstry>

**P2281** 		<Pty1>

**P2282** 			<Id>

**P2283** 				<PrtryId>

**P2284** 					<Id>456</Id>

**P2285** 					<Issr>CRST</Issr>

**P2286** 				</PrtryId>

**P2287** 			</Id>

**P2288** 		</Pty1>

**P2289** 		<Pty2>

**P2290** 			<Id>

**P2291** 				<AnyBIC>CPFIDEFF</AnyBIC>

**P2292** 			</Id>

**P2293** 		</Pty2>

**P2294** 	</DlvrgSttlmPties>

**P2295** 	<RcvgSttlmPties>

**P2296** 		<Pty1>

**P2297** 			<Id>

**P2298** 				<PrtryId>

**P2299** 					<Id>123</Id>

**P2300** 					<Issr>CRST</Issr>

**P2301** 				</PrtryId>

**P2302** 			</Id>

**P2303** 		</Pty1>

**P2304** 		<Pty2>

**P2305** 			<Id>

**P2306** 				<AnyBIC>MGTCDE55</AnyBIC>

**P2307** 			</Id>

**P2308** 			<SfkpgAcct>

**P2309** 				<Id>111S</Id>

**P2310** 			</SfkpgAcct>

**P2311** 		</Pty2>

**P2312** 	</RcvgSttlmPties>

**P2313** </SctiesSttlmTxAllgmtNtfctn>

