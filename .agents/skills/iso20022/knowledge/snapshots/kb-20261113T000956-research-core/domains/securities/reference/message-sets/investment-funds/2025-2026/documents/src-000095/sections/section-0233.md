---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Redemption", "RedemptionOrder setr.004.001.05 (1)"]
content_origin: "source-transcription"
---

# RedemptionOrder setr.004.001.05 (1)

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Redemption / RedemptionOrder setr.004.001.05 (1).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2836** RedemptionOrder setr.004.001.05 (1)

**P2837** Description

**P2838** A RedemptionOrder message is sent for investment account 78-89ABCD. It contains one order. The individual order has order reference KL67TRE54 and is for financial instrument ISIN IE9876543210. The amount (gross) of 5000 EUR is to be redeemed.

**P2839** There will be no physical delivery.

**P2840** Message Instance

**P2841** <RedOrdr>

**P2842** 	<MsgId>

**P2843** 		<Id>R0004</Id>

**P2844** 		<CreDtTm>2026-01-02T09:30:30</CreDtTm>

**P2845** 	</MsgId>

**P2846** 	<MltplOrdrDtls>

**P2847** 		<InvstmtAcctDtls>

**P2848** 			<AcctId>78-89ABCD</AcctId>

**P2849** 		</InvstmtAcctDtls>

**P2850** 		<IndvOrdrDtls>

**P2851** 			<OrdrRef>KL67TRE54</OrdrRef>

**P2852** 			<FinInstrmDtls>

**P2853** 				<Id>

**P2854** 					<ISIN>IE9876543210</ISIN>

**P2855** 				</Id>

**P2856** 			</FinInstrmDtls>

**P2857** 			<AmtOrUnitsOrPctg>

**P2858** 				<GrssAmt Ccy="EUR">5000</GrssAmt>

**P2859** 			</AmtOrUnitsOrPctg>

**P2860** 			<PhysDlvryInd>false</PhysDlvryInd>

**P2861** 		</IndvOrdrDtls>

**P2862** 	</MltplOrdrDtls>

**P2863** </RedOrdr>

