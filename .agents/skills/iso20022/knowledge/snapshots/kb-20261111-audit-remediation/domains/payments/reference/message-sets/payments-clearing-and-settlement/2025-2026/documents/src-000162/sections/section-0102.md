---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FinancialInstitutionCreditTransfer pacs.009.001.13 - 2", "Third FinancialInstitutionCreditTransfer"]
content_origin: "source-transcription"
---

# Third FinancialInstitutionCreditTransfer

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / FinancialInstitutionCreditTransfer pacs.009.001.13 - 2 / Third FinancialInstitutionCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2352** Third FinancialInstitutionCreditTransfer

**P2353** Description

**P2354** FFFF sends a FinancialInstitutionCreditTransfer to the next party which is the creditor agent DDDD, Luxemburg, for whom they service a SEK account. On receipt, DDDD will credit the SEK account of its client BBBBITTT.

**P2355** Business Data 

**P2356** The third FinancialInstitutionCreditTransfer message, from FFFFSESS to DDDDLULL:

[T45 - complete table](../tables/tbl-0045.md)

**P2357** Message Instance

**P2358** <FICdtTrf>

**P2359** 	<GrpHdr>

**P2360** 		<MsgId>FFFF/151022-SEK/110</MsgId>

**P2361** 		<CreDtTm>2015-10-22T10:11:00</CreDtTm>

**P2362** 		<NbOfTxs>1</NbOfTxs>

**P2363** 		<SttlmInf>

**P2364** 			<SttlmMtd>INGA</SttlmMtd>

**P2365** 			<SttlmAcct>

**P2366** 				<Id>

**P2367** 					<Othr>

**P2368** 						<Id>245388877443</Id>

**P2369** 					</Othr>

**P2370** 				</Id>

**P2371** 			</SttlmAcct>

**P2372** 		</SttlmInf>

**P2373** 		<InstgAgt>

**P2374** 			<FinInstnId>

**P2375** 				<BICFI>FFFFSESS</BICFI>

**P2376** 			</FinInstnId>

**P2377** 		</InstgAgt>

**P2378** 		<InstdAgt>

**P2379** 			<FinInstnId>

**P2380** 				<BICFI>DDDDLULL</BICFI>

**P2381** 			</FinInstnId>

**P2382** 		</InstdAgt>

**P2383** 	</GrpHdr>

**P2384** 	<CdtTrfTxInf>

**P2385** 		<PmtId>

**P2386** 			<InstrId>FFFF/151022-SEK/110/1</InstrId>

**P2387** 			<EndToEndId>BBBBTT4148AAAAPP</EndToEndId>

**P2388** 			<TxId>AAAA/151020-SEK/005/1</TxId>

**P2389** 		</PmtId>

**P2390** 		<IntrBkSttlmAmt Ccy="SEK">100000000</IntrBkSttlmAmt>

**P2391** 		<IntrBkSttlmDt>2015-10-22</IntrBkSttlmDt>

**P2392** 		<Dbtr>

**P2393** 			<FinInstnId>

**P2394** 				<BICFI>AAAAFRPP</BICFI>

**P2395** 			</FinInstnId>

**P2396** 		</Dbtr>

**P2397** 		<DbtrAgt>

**P2398** 			<FinInstnId>

**P2399** 				<BICFI>CCCCSESS</BICFI>

**P2400** 			</FinInstnId>

**P2401** 		</DbtrAgt>

**P2402** 		<Cdtr>

**P2403** 			<FinInstnId>

**P2404** 				<BICFI>BBBBITTT</BICFI>

**P2405** 			</FinInstnId>

**P2406** 		</Cdtr>

**P2407** 		<CdtrAcct>

**P2408** 			<Id>

**P2409** 				<Othr>

**P2410** 					<Id>995566ZZ876</Id>

**P2411** 				</Othr>

**P2412** 			</Id>

**P2413** 			<Ccy>SEK</Ccy>

**P2414** 		</CdtrAcct>

**P2415** 	</CdtTrfTxInf>

**P2416** </FICdtTrf>

**P2417**   


