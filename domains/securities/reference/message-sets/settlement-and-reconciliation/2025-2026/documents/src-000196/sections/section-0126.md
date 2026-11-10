---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesFinancingConfirmation sese.035.001.13"]
content_origin: "source-transcription"
---

# SecuritiesFinancingConfirmation sese.035.001.13

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesFinancingConfirmation sese.035.001.13.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2705** SecuritiesFinancingConfirmation sese.035.001.13

**P2706** Description

**P2707** On the 08 March 2019 the securities financing servicing party Bank of New York Mellon S.A. Brussels (IRVTBEBB), informs the securities financing instructing party, Dresdner Bank Frankfurt (DRESDEFF) that the opening leg of the repurchase agreement has settled. This is done through a SecuritiesFinancingConfirmation (sese.035.001.07).

**P2708** Business Data

**P2709** Account Owner Transaction Identification: REPOINSTR123

**P2710** Securities Financing Transaction Type: repurchase Agreement

**P2711** Payment: against payment

**P2712** Trade Date: 05/03/2019

**P2713** Settlement Date: 08/03/2019

**P2714** Financial Instrument: FR0000294034

**P2715** Quantity: face amount 100,050,000 

**P2716** Safekeeping Account: 111111111

**P2717** Securities Financing Trade Identification: REPO12345

**P2718** Termination Date: 15/03/2019

**P2719** Termination Transaction Amount: EUR 9,910,780

**P2720** Receiving Depository: NCSDXX21

**P2721** Receiving Party 1: SUBCYY34

**P2722** Receiving Party 2: BUYRGB22

**P2723** Settled Amount: EUR 9,900,000 credit

**P2724** Message Instance

**P2725** <SctiesFincgConf>

**P2726** 	<TxIdDtls>

**P2727** 		<AcctOwnrTxId>REPOINSTR123</AcctOwnrTxId>

**P2728** 		<SctiesFincgTxTp>REPU</SctiesFincgTxTp>

**P2729** 		<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P2730** 		<Pmt>APMT</Pmt>

**P2731** 	</TxIdDtls>

**P2732** 	<TradDtls>

**P2733** 		<TradDt>

**P2734** 			<Dt>

**P2735** 				<Dt>2019-03-05</Dt>

**P2736** 			</Dt>

**P2737** 		</TradDt>

**P2738** 		<SttlmDt>

**P2739** 			<Dt>

**P2740** 				<Dt>2019-03-08</Dt>

**P2741** 			</Dt>

**P2742** 		</SttlmDt>

**P2743** 		<FctvSttlmDt>

**P2744** 			<Dt>

**P2745** 				<Dt>2019-03-08</Dt>

**P2746** 			</Dt>

**P2747** 		</FctvSttlmDt>

**P2748** 	</TradDtls>

**P2749** 	<FinInstrmId>

**P2750** 		<ISIN>FR0000294034</ISIN>

**P2751** 		</FinInstrmId>

**P2752** 	<QtyAndAcctDtls>

**P2753** 		<SttldQty>

**P2754** 			<Qty>

**P2755** 				<FaceAmt>100050000</FaceAmt>

**P2756** 			</Qty>

**P2757** 		</SttldQty>

**P2758** 		<SfkpgAcct>

**P2759** 			<Id>111111111</Id>

**P2760** 		</SfkpgAcct>

**P2761** 	</QtyAndAcctDtls>

**P2762** 	<SctiesFincgDtls>

**P2763** 		<SctiesFincgTradId>REPO12345</SctiesFincgTradId>

**P2764** 		<TermntnDt>

**P2765** 			<Dt>

**P2766** 				<Dt>2019-03-15</Dt>

**P2767** 			</Dt>

**P2768** 		</TermntnDt>

**P2769** 		<TermntnTxAmt>

**P2770** 			<Amt Ccy="EUR">9910780</Amt>

**P2771** 		</TermntnTxAmt>

**P2772** 	</SctiesFincgDtls>

**P2773** 	<RcvgSttlmPties>

**P2774** 		<Dpstry>

**P2775** 			<Id>

**P2776** 				<AnyBIC>NCSDXX21</AnyBIC>

**P2777** 			</Id>

**P2778** 		</Dpstry>

**P2779** 		<Pty1>

**P2780** 			<Id>

**P2781** 				<AnyBIC>SUBCYY34</AnyBIC>

**P2782** 			</Id>

**P2783** 		</Pty1>

**P2784** 		<Pty2>

**P2785** 		<Id>

**P2786** 				<AnyBIC>BUYRGB22</AnyBIC>

**P2787** 			</Id>

**P2788** 		</Pty2>

**P2789** 	</RcvgSttlmPties>

**P2790** 	<SttldAmt>

**P2791** 		<Amt Ccy="EUR">9900000</Amt>

**P2792** 		<CdtDbtInd>CRDT</CdtDbtInd>

**P2793** 	</SttldAmt>

**P2794** </SctiesFincgConf>

