---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FinancialInstitutionDirectDebit pacs.010.001.06 "]
content_origin: "source-transcription"
---

# FinancialInstitutionDirectDebit pacs.010.001.06 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / FinancialInstitutionDirectDebit pacs.010.001.06 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2418** FinancialInstitutionDirectDebit pacs.010.001.06 

**P2419** Description

**P2420** Bank MMMM instructs Bank NNNN to debit the account of Bank PPPP for 2500 EUR and Bank OOOO for 5000 EUR in favour of its account at Bank QQQQ with value date 21 November 2015. 

**P2421** Business Data 

**P2422** The FinancialInstitutionDirectDebit message, from Bank MMMMBEBB to Bank NNNNDEFF:

[T46 - complete table](../tables/tbl-0046.md)

**P2424** Message Instance

**P2425** <FIDrctDbt>

**P2426** 	<GrpHdr>

**P2427** 		<MsgId>MMMM/151121 PPPP_OOOO_EUR</MsgId>

**P2428** 		<CreDtTm>2015-11-20T16:00:00</CreDtTm>

**P2429** 		<NbOfTxs>2</NbOfTxs>

**P2430** 		<InstgAgt>

**P2431** 			<FinInstnId>

**P2432** 				<BICFI>MMMMBEBB</BICFI>

**P2433** 			</FinInstnId>

**P2434** 		</InstgAgt>

**P2435** 		<InstdAgt>

**P2436** 			<FinInstnId>

**P2437** 				<BICFI>NNNNDEFF</BICFI>

**P2438** 			</FinInstnId>

**P2439** 		</InstdAgt>

**P2440** 	</GrpHdr>

**P2441** 	<CdtInstr>

**P2442** 		<CdtId>MMMM/151121 PPPP_OOOO_EUR_7500</CdtId>

**P2443** 		<BtchBookg>true</BtchBookg>

**P2444** 		<CdtrAgt>

**P2445** 			<FinInstnId>

**P2446** 				<BICFI>QQQQFRPP</BICFI>

**P2447** 			</FinInstnId>

**P2448** 		</CdtrAgt>

**P2449** 		<CdtrAgtAcct>

**P2450** 			<Id>

**P2451** 				<IBAN>DE89370400440532013000</IBAN>

**P2452** 			</Id>

**P2453** 		</CdtrAgtAcct>

**P2454** 		<Cdtr>

**P2455** 				<FinInstnId>

**P2456** 					<BICFI>MMMMBEBB</BICFI>

**P2457** 				</FinInstnId>

**P2458** 		</Cdtr>

**P2459** 		<CdtrAcct>

**P2460** 			<Id>

**P2461** 				<IBAN>FR1420041010050500013M02606</IBAN>

**P2462** 			</Id>

**P2463** 		</CdtrAcct>

**P2464** 		<DrctDbtTxInf>

**P2465** 			<PmtId>

**P2466** 				<InstrId>MMMM/151121 PPPP_OOOO_EUR_2500</InstrId>

**P2467** 				<EndToEndId>REFERENCE0001</EndToEndId>

**P2468** 				<TxId>PPPP _2500</TxId>

**P2469** 			</PmtId>

**P2470** 			<IntrBkSttlmAmt Ccy="EUR">2500</IntrBkSttlmAmt>

**P2471** 			<IntrBkSttlmDt>2015-11-21</IntrBkSttlmDt>

**P2472** 			<Dbtr>

**P2473** 				<FinInstnId>

**P2474** 					<BICFI>PPPPDKKK</BICFI>

**P2475** 				</FinInstnId>

**P2476** 			</Dbtr>

**P2477** 			<DbtrAgt>

**P2478** 				<FinInstnId>

**P2479** 					<BICFI>NNNNDEFF</BICFI>

**P2480** 				</FinInstnId>

**P2481** 			</DbtrAgt>

**P2482** 		</DrctDbtTxInf>

**P2483** 		<DrctDbtTxInf>

**P2484** 			<PmtId>

**P2485** 				<InstrId>MMMM/151121 PPPP_OOOO_EUR_5000</InstrId>

**P2486** 				<EndToEndId>REFERENCE0002</EndToEndId>

**P2487** 				<TxId>OOOO_5000</TxId>

**P2488** 			</PmtId>

**P2489** 			<IntrBkSttlmAmt Ccy="EUR">5000</IntrBkSttlmAmt>

**P2490** 			<IntrBkSttlmDt>2015-11-21</IntrBkSttlmDt>

**P2491** 			<Dbtr>

**P2492** 				<FinInstnId>

**P2493** 					<BICFI>OOOOATWW</BICFI>

**P2494** 				</FinInstnId>

**P2495** 			</Dbtr>

**P2496** 			<DbtrAgt>

**P2497** 				<FinInstnId>

**P2498** 						<BICFI>NNNNDEFF</BICFI>

**P2499** 				</FinInstnId>

**P2500** 			</DbtrAgt>

**P2501** 		</DrctDbtTxInf>

**P2502** 	</CdtInstr>

**P2503** </FIDrctDbt>

