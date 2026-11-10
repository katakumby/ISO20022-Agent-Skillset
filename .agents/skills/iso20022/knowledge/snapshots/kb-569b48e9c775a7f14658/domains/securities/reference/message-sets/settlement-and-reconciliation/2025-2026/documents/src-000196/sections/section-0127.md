---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesFinancingModificationInstruction sese.036.001.10"]
content_origin: "source-transcription"
---

# SecuritiesFinancingModificationInstruction sese.036.001.10

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / SecuritiesFinancingModificationInstruction sese.036.001.10.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2795** SecuritiesFinancingModificationInstruction sese.036.001.10

**P2796** Description

**P2797** On the 05 March 2019 a securities financing instructing party, Dresdner Bank Frankfurt (DRESDEFF) instructs their global custodian (securities financing servicing party), Bank of New York Mellon S.A. Brussels (IRVTBEBB) to do a repurchase call in order to modify the termination date and amount of the repurchase agreement. This is done with the SecuritiesFinancingModificationInstruction(sese.036.001.06).

**P2798** Business Data

**P2799** Account Owner Transaction Identification: REPOINSTR123

**P2800** Securities Financing Transaction Type: repurchase agreement

**P2801** Payment: against payment

**P2802** Modification Type: repurchase call

**P2803** Trade Date: 05/03/2019

**P2804** Opening Settlement Date: 08/03/2019

**P2805** Financial Instrument: FR0000294034

**P2806** Quantity: face amount 100,050,000

**P2807** Safekeeping Account: 111111111

**P2808** Securities Financing Trade Identification: REPO12345

**P2809** Termination Date: 29/03/2019

**P2810** Termination Transaction Amount: EUR 9,920,000

**P2811** Receiving Depository: NCSDXX21

**P2812** Receiving Party 1: SUBCYY34

**P2813** Receiving Party 2: BUYRGB22

**P2814** Opening Settlement Amount: EUR 9,900,000 credit

**P2815** Message Instance

**P2816** <SctiesFincgModInstr>

**P2817** 	<TxTpAndModAddtlParams>

**P2818** 		<AcctOwnrTxId>REPOINSTR123</AcctOwnrTxId>

**P2819** 		<SctiesFincgTxTp>REPU</SctiesFincgTxTp>

**P2820** 		<Pmt>APMT</Pmt>

**P2821** 		<ModTp>

**P2822** 			<Cd>CALL</Cd>

**P2823** 		</ModTp>

**P2824** 	</TxTpAndModAddtlParams>

**P2825** 	<TradDtls>

**P2826** 		<TradDt>

**P2827** 			<Dt>2019-03-05</Dt>

**P2828** 		</TradDt>

**P2829** 		<OpngSttlmDt>

**P2830** 			<Dt>2019-03-08</Dt>

**P2831** 		</OpngSttlmDt>

**P2832** 	</TradDtls>

**P2833** 	<FinInstrmId>

**P2834** 		<ISIN>FR0000294034</ISIN>

**P2835** 		</FinInstrmId>

**P2836** 	<QtyAndAcctDtls>

**P2837** 		<SttlmQty>

**P2838** 			<FaceAmt>100050000</FaceAmt>

**P2839** 		</SttlmQty>

**P2840** 		<SfkpgAcct>

**P2841** 			<Id>111111111</Id>

**P2842** 		</SfkpgAcct>

**P2843** 	</QtyAndAcctDtls>

**P2844** 	<SctiesFincgAddtlDtls>

**P2845** 		<SctiesFincgTradId>REPO12345</SctiesFincgTradId>

**P2846** 		<TermntnDt>

**P2847** 			<Dt>

**P2848** 				<Dt>2019-03-29</Dt>

**P2849** 			</Dt>

**P2850** 		</TermntnDt>

**P2851** 		<TermntnTxAmt>

**P2852** 			<Amt Ccy="EUR">9920000</Amt>

**P2853** 		</TermntnTxAmt>

**P2854** 	</SctiesFincgAddtlDtls>

**P2855** 	<RcvgSttlmPties>

**P2856** 		<Dpstry>

**P2857** 			<Id>

**P2858** 				<AnyBIC>NCSDXX21</AnyBIC>

**P2859** 			</Id>

**P2860** 		</Dpstry>

**P2861** 		<Pty1>

**P2862** 			<Id>

**P2863** 				<AnyBIC>SUBCYY34</AnyBIC>

**P2864** 				</Id>

**P2865** 		</Pty1>

**P2866** 		<Pty2>

**P2867** 			<Id>

**P2868** 				<AnyBIC>BUYRGB22</AnyBIC>

**P2869** 			</Id>

**P2870** 		</Pty2>

**P2871** 	</RcvgSttlmPties>

**P2872** 		<OpngSttlmAmt>

**P2873** 		<Amt Ccy="EUR">9900000</Amt>

**P2874** 	</OpngSttlmAmt>

**P2875** </SctiesFincgModInstr>

