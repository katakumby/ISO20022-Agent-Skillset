---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesFinancingInstruction sese.033.001.13"]
content_origin: "source-transcription"
---

# SecuritiesFinancingInstruction sese.033.001.13

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesFinancingInstruction sese.033.001.13.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2552** SecuritiesFinancingInstruction sese.033.001.13

**P2553** Description

**P2554** On the 05 March 2019 a securities financing instructing party, Dresdner Bank Frankfurt (DRESDEFF) instructs their global custodian (securities financing servicing party), Bank of New York Mellon S.A. Brussels (IRVTBEBB ) to do a repurchase agreement. This is done with the SecuritiesFinancingInstruction (sese.033.001.07).

**P2555** Business Data

**P2556** Transaction Identification: REPOINSTR123

**P2557** Securities Financing Transaction Type: repurchase agreement

**P2558** Payment: against payment

**P2559** Trade Date: 05/03/2019

**P2560** Opening Settlement Date: 08/03/2019

**P2561** Financial Instrument: FR0000294034

**P2562** Quantity: face amount 100,050,000 Safekeeping Account: 111111111

**P2563** Securities Financing Trade Identification: REPO12345

**P2564** Termination Date: 15/03/2019

**P2565** Termination Transaction Amount: EUR 9,910,780

**P2566** Receiving Depository: NCSDXX21

**P2567** Receiving Party 1: SUBCYY34

**P2568** Receiving Party 2: BUYRGB22

**P2569** Opening Settlement Amount: EUR 9,900,000 credit

**P2570** Message Instance

**P2571** <SctiesFincgInstr>

**P2572** 	<TxId>REPOINSTR123</TxId>

**P2573** 	<TxTpAndAddtlParams>

**P2574** 		<SctiesFincgTxTp>REPU</SctiesFincgTxTp>

**P2575** 		<Pmt>APMT</Pmt>

**P2576** 	</TxTpAndAddtlParams>

**P2577** 	<TradDtls>

**P2578** 		<TradDt>

**P2579** 			<Dt>

**P2580** 				<Dt>2019-03-05</Dt>

**P2581** 			</Dt>

**P2582** 		</TradDt>

**P2583** 		<OpngSttlmDt>

**P2584** 			<Dt>2019-03-08</Dt>

**P2585** 		</OpngSttlmDt>

**P2586** 	</TradDtls>

**P2587** 	<FinInstrmId>

**P2588** 		<ISIN>FR0000294034</ISIN>

**P2589** 		</FinInstrmId>

**P2590** 	<QtyAndAcctDtls>

**P2591** 		<SttlmQty>

**P2592** 			<Qty>

**P2593** 				<FaceAmt>100050000</FaceAmt>

**P2594** 			</Qty>

**P2595** 		</SttlmQty>

**P2596** 		<SfkpgAcct>

**P2597** 			<Id>111111111</Id>

**P2598** 		</SfkpgAcct>

**P2599** 	</QtyAndAcctDtls>

**P2600** 	<SctiesFincgDtls>

**P2601** 		<SctiesFincgTradId>REPO12345</SctiesFincgTradId>

**P2602** 		<TermntnDt>

**P2603** 			<Dt>

**P2604** 				<Dt>2019-03-15</Dt>

**P2605** 			</Dt>

**P2606** 		</TermntnDt>

**P2607** 		<TermntnTxAmt>

**P2608** 			<Amt Ccy="EUR">9910780</Amt>

**P2609** 		</TermntnTxAmt>

**P2610** 	</SctiesFincgDtls>

**P2611** 	<RcvgSttlmPties>

**P2612** 		<Dpstry>

**P2613** 			<Id>

**P2614** 				<AnyBIC>NCSDXX21</AnyBIC>

**P2615** 			</Id>

**P2616** 		</Dpstry>

**P2617** 		<Pty1>

**P2618** 			<Id>

**P2619** 				<AnyBIC>SUBCYY34</AnyBIC>

**P2620** 			</Id>

**P2621** 		</Pty1>

**P2622** 		<Pty2>

**P2623** 			<Id>

**P2624** 				<AnyBIC>BUYRGB22</AnyBIC>

**P2625** 			</Id>

**P2626** 		</Pty2>

**P2627** 	</RcvgSttlmPties>

**P2628** 	<OpngSttlmAmt>

**P2629** 		<Amt Ccy="EUR">9900000</Amt>

**P2630** 		<CdtDbtInd>CRDT</CdtDbtInd>

**P2631** 	</OpngSttlmAmt>

**P2632** </SctiesFincgInstr>

