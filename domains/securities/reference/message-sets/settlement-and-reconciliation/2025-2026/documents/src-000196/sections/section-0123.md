---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesSettlementTransactionGenerationNotification sese.032.001.13"]
content_origin: "source-transcription"
---

# SecuritiesSettlementTransactionGenerationNotification sese.032.001.13

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesSettlementTransactionGenerationNotification sese.032.001.13.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2451** SecuritiesSettlementTransactionGenerationNotification sese.032.001.13

**P2452** Description

**P2453** On the 09 January 2019, Dresdner Bank London (DRESGB2L) informs its customer, Dresdner Bank Frankfurt (DRESDEFF), that a deliver versus payment has been auto-generated for account 222S following a corporate action event. This is done through the SecuritiesSettlementTransactionGeneration Notification (sese.032.001.07).

**P2454** Business Data

**P2455** Account Owner Transaction Id: FRTJ123DEL2

**P2456** Securities Movement Type: delivery

**P2457** Payment: against payment

**P2458** Corporate Action Event Id: 4578965478

**P2459** Trade Date: 05/01/2019

**P2460** Effective Settlement Date: 08/01/2019

**P2461** Deal price: par value

**P2462** Rate: 101.002

**P2463** Financial Instrument and Description: BE0123456789 Belgium Company

**P2464** XYZ

**P2465** Quantity: face amount 5,500,000

**P2466** Safekeeping Account: 222S

**P2467** Securities Transaction Type: trade

**P2468** Receiving Depository: NBBEBEBB (National bank of Belgium)

**P2469** Receiving Settlement Parties1: CITIBEBB (Citibank)

**P2470** Receiving Settlement Parties2: CFPIDEFF (Commerz Financial Products

**P2471** GmbH, Frankfurt) account 321654

**P2472** Settlement Amount: EUR 50,850,000 credit

**P2473** Generated Reason: transformation following a corporate action

**P2474** Message Instance

**P2475** <SctiesSttlmTxGnrtnNtfctn>

**P2476** 	<TxIdDtls>

**P2477** 		<AcctOwnrTxId>FRTJ123DEL2</AcctOwnrTxId>

**P2478** 		<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P2479** 		<Pmt>APMT</Pmt>

**P2480** 		<CorpActnEvtId>4578965478</CorpActnEvtId>

**P2481** 	</TxIdDtls>

**P2482** 	<TradDtls>

**P2483** 		<TradDt>

**P2484** 			<Dt>

**P2485** 				<Dt>2019-01-05</Dt>

**P2486** 			</Dt>

**P2487** 		</TradDt>

**P2488** 		<SttlmDt>

**P2489** 			<Dt>

**P2490** 				<Dt>2019-01-08</Dt>

**P2491** 			</Dt>

**P2492** 		</SttlmDt>

**P2493** 		<DealPric>

**P2494** 			<Tp>

**P2495** 				<ValTp>PARV</ValTp>

**P2496** 			</Tp>

**P2497** 			<Val>

**P2498** 				<Rate>101.002</Rate>

**P2499** 			</Val>

**P2500** 		</DealPric>

**P2501** 	</TradDtls>

**P2502** 	<FinInstrmId>

**P2503** 		<ISIN>BE0987654321</ISIN>

**P2504** 		<Desc>Belgium Company ZYX</Desc>

**P2505** 	</FinInstrmId>

**P2506** 	<QtyAndAcctDtls>

**P2507** 		<SttlmQty>

**P2508** 			<Qty>

**P2509** 				<FaceAmt>5500000</FaceAmt>

**P2510** 			</Qty>

**P2511** 		</SttlmQty>

**P2512** 		<SfkpgAcct>

**P2513** 			<Id>222S</Id>

**P2514** 		</SfkpgAcct>

**P2515** 	</QtyAndAcctDtls>

**P2516** 	<SttlmParams>

**P2517** 		<SctiesTxTp>

**P2518** 			<Cd>TRAD</Cd>

**P2519** 		</SctiesTxTp>

**P2520** 	</SttlmParams>

**P2521** 	<RcvgSttlmPties>

**P2522** 		<Dpstry>

**P2523** 			<Id>

**P2524** 				<AnyBIC>NBBEBEBB</AnyBIC>

**P2525** 			</Id>

**P2526** 		</Dpstry>

**P2527** 		<Pty1>

**P2528** 			<Id>

**P2529** 				<AnyBIC>CITIBEBB</AnyBIC>

**P2530** 			</Id>

**P2531** 		</Pty1>

**P2532** 		<Pty2>

**P2533** 			<Id>

**P2534** 				<AnyBIC>CFPIDEFF</AnyBIC>

**P2535** 			</Id>

**P2536** 			<SfkpgAcct>

**P2537** 				<Id>321654</Id>

**P2538** 			</SfkpgAcct>

**P2539** 		</Pty2>

**P2540** 	</RcvgSttlmPties>

**P2541** 	<SttlmAmt>

**P2542** 		<AcrdIntrstInd>true</AcrdIntrstInd>

**P2543** 		<Amt Ccy="EUR">50850000</Amt>

**P2544** 		<CdtDbtInd>CRDT</CdtDbtInd>

**P2545** 	</SttlmAmt>

**P2546** 	<GnrtdRsn>

**P2547** 		<Cd>

**P2548** 			<Cd>TRAN</Cd>

**P2549** 		</Cd>

**P2550** 	</GnrtdRsn>

**P2551** </SctiesSttlmTxGnrtnNtfctn>

