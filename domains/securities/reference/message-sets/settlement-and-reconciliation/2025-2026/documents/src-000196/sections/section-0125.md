---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesFinancingStatusAdvice sese.034.001.11"]
content_origin: "source-transcription"
---

# SecuritiesFinancingStatusAdvice sese.034.001.11

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesFinancingStatusAdvice sese.034.001.11.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2633** SecuritiesFinancingStatusAdvice sese.034.001.11

**P2634** Description

**P2635** On the 06 March 2019 the securities financing servicing party Bank of New York Mellon S.A. Brussels (IRVTBEBB), provides a status on the repurchase agreement to the securities financing instructing party, Dresdner Bank Frankfurt (DRESDEFF). This is done through a SecuritiesFinancingStatusAdvice (sese.034.001.07).

**P2636** Business Data

**P2637** Account Owner Transaction Identification: REPOINSTR123

**P2638** Matching Status: unmatched

**P2639** Reason: depository does not match

**P2640** Securities Financing Trade Identification: REPO12345

**P2641** Safekeeping Account: 111111111

**P2642** Financial Instrument: FR0000294034

**P2643** Quantity: face amount 100,050,000

**P2644** Opening Settlement Amount: EUR 9,900,000 credit

**P2645** Termination Transaction Amount: EUR 9,910,780

**P2646** Opening Settlement Date: 08/03/2019

**P2647** Termination Date: 15/03/2019

**P2648** Trade Date: 05/03/2019

**P2649** Securities Financing Transaction Type: repurchase agreement

**P2650** Payment: against payment

**P2651** Message Instance

**P2652** <SctiesFincgStsAdvc>

**P2653** 	<TxId>

**P2654** 		<AcctOwnrTxId>REPOINSTR123</AcctOwnrTxId>

**P2655** 	</TxId>

**P2656** 	<MtchgSts>

**P2657** 		<Umtchd>

**P2658** 			<Rsn>

**P2659** 				<Cd>

**P2660** 					<Cd>DEPT</Cd>

**P2661** 				</Cd>

**P2662** 			</Rsn>

**P2663** 		</Umtchd>

**P2664** 	</MtchgSts>

**P2665** 	<TxDtls>

**P2666** 		<SctiesFincgTradId>REPO12345</SctiesFincgTradId>

**P2667** 		<SfkpgAcct>

**P2668** 			<Id>111111111</Id>

**P2669** 		</SfkpgAcct>

**P2670** 		<FinInstrmId>

**P2671** 			<ISIN>FR0000294034</ISIN>

**P2672** 			</FinInstrmId>

**P2673** 		<SttlmQty>

**P2674** 			<Qty>

**P2675** 				<FaceAmt>100050000</FaceAmt>

**P2676** 			</Qty>

**P2677** 		</SttlmQty>

**P2678** 		<OpngSttlmAmt>

**P2679** 			<Amt Ccy="EUR">9900000</Amt>

**P2680** 			<CdtDbtInd>CRDT</CdtDbtInd>

**P2681** 		</OpngSttlmAmt>

**P2682** 		<TermntnTxAmt>

**P2683** 			<Amt Ccy="EUR">9910780</Amt>

**P2684** 		</TermntnTxAmt>

**P2685** 		<OpngSttlmDt>

**P2686** 			<Dt>

**P2687** 				<Dt>2019-03-08</Dt>

**P2688** 			</Dt>

**P2689** 		</OpngSttlmDt>

**P2690** 		<TermntnDt>

**P2691** 			<Dt>

**P2692** 				<Dt>2019-03-15</Dt>

**P2693** 			</Dt>

**P2694** 		</TermntnDt>

**P2695** 		<TradDt>

**P2696** 			<Dt>

**P2697** 				<Dt>2019-03-05</Dt>

**P2698** 			</Dt>

**P2699** 		</TradDt>

**P2700** 		<SctiesFincgTxTp>REPU</SctiesFincgTxTp>

**P2701** 		<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P2702** 		<Pmt>APMT</Pmt>

**P2703** 	</TxDtls>

**P2704** </SctiesFincgStsAdvc>

