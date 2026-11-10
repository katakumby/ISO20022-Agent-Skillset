---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FinancialInstitutionCreditTransfer pacs.009.001.13 - 2", "First FinancialInstitutionCreditTransfer"]
content_origin: "source-transcription"
---

# First FinancialInstitutionCreditTransfer

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / FinancialInstitutionCreditTransfer pacs.009.001.13 - 2 / First FinancialInstitutionCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2205** First FinancialInstitutionCreditTransfer

**P2206** Description 

**P2207** On 20 October 2015, AAAAFRPP agrees on a foreign exchange deal with BBBBITTT: 100 million SEK is sold against 10,621,575.00 EUR (exchange rate 9.4148). The deal is confirmed with common reference BBBBTT4148AAAAPP.

**P2208** On the same day AAAAFRPP sends a FinancialInstitutionCreditTransfer message to its SEK correspondent CCCCSESS. They instruct CCCCSESS to debit their account 123456789 with value date 22 October 2015 to pay 100 million SEK to BBBBITTT.

**P2209** BBBBITTT has communicated the following settlement instructions: the SEK amount is to be credited to the SEK sub- account of their account 995566ZZ876 with DDDDLULL. DDDDLULL owns a SEK account 24538877443 with FFFF Bank (FFFFSESS).

**P2210** Business Data 

**P2211** The first FinancialInstitutionCreditTransfer message, from AAAAFRPP to CCCCSESS:

[T43 - complete table](../tables/tbl-0043.md)

**P2212** Message Instance

**P2213** <FICdtTrf>

**P2214** 	<GrpHdr>

**P2215** 		<MsgId>AAAA/151020-SEK/005</MsgId>

**P2216** 		<CreDtTm>2015-10-20T11:03:00</CreDtTm>

**P2217** 		<NbOfTxs>1</NbOfTxs>

**P2218** 		<SttlmInf>

**P2219** 			<SttlmMtd>INDA</SttlmMtd>

**P2220** 			<SttlmAcct>

**P2221** 				<Id>

**P2222** 					<Othr>

**P2223** 						<Id>123456789</Id>

**P2224** 					</Othr>

**P2225** 				</Id>

**P2226** 			</SttlmAcct>

**P2227** 		</SttlmInf>

**P2228** 		<InstgAgt>

**P2229** 			<FinInstnId>

**P2230** 				<BICFI>AAAAFRPP</BICFI>

**P2231** 			</FinInstnId>

**P2232** 		</InstgAgt>

**P2233** 		<InstdAgt>

**P2234** 			<FinInstnId>

**P2235** 				<BICFI>CCCCSESS</BICFI>

**P2236** 			</FinInstnId>

**P2237** 		</InstdAgt>

**P2238** 	</GrpHdr>

**P2239** 	<CdtTrfTxInf>

**P2240** 		<PmtId>

**P2241** 			<InstrId>AAAA/151020-SEK/005/1</InstrId>

**P2242** 			<EndToEndId>BBBBTT4148AAAAPP</EndToEndId>

**P2243** 			<TxId>AAAA/151020-SEK/005/1</TxId>

**P2244** 		</PmtId>

**P2245** 		<IntrBkSttlmAmt Ccy="SEK">100000000</IntrBkSttlmAmt>

**P2246** 		<IntrBkSttlmDt>2015-10-22</IntrBkSttlmDt>

**P2247** 		<IntrmyAgt1>

**P2248** 			<FinInstnId>

**P2249** 				<BICFI>FFFFSESS</BICFI>

**P2250** 			</FinInstnId>

**P2251** 		</IntrmyAgt1>

**P2252** 		<Dbtr>

**P2253** 			<FinInstnId>

**P2254** 				<BICFI>AAAAFRPP</BICFI>

**P2255** 			</FinInstnId>

**P2256** 		</Dbtr>

**P2257** 		<CdtrAgt>

**P2258** 			<FinInstnId>

**P2259** 				<BICFI>DDDDLULL</BICFI>

**P2260** 			</FinInstnId>

**P2261** 		</CdtrAgt>

**P2262** 		<CdtrAgtAcct>

**P2263** 			<Id>

**P2264** 				<Othr>

**P2265** 					<Id>24538877443</Id>

**P2266** 				</Othr>

**P2267** 			</Id>

**P2268** 		</CdtrAgtAcct>

**P2269** 		<Cdtr>

**P2270** 			<FinInstnId>

**P2271** 				<BICFI>BBBBITTT</BICFI>

**P2272** 			</FinInstnId>

**P2273** 		</Cdtr>

**P2274** 		<CdtrAcct>

**P2275** 			<Id>

**P2276** 				<Othr>

**P2277** 					<Id>995566ZZ876</Id>

**P2278** 				</Othr>

**P2279** 			</Id>

**P2280** 			<Ccy>SEK</Ccy>

**P2281** 		</CdtrAcct>

**P2282** 	</CdtTrfTxInf>

**P2283** </FICdtTrf>

