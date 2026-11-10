---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Redemption", "RedemptionOrderConfirmation setr.006.001.06"]
content_origin: "source-transcription"
---

# RedemptionOrderConfirmation setr.006.001.06

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Redemption / RedemptionOrderConfirmation setr.006.001.06.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2934** RedemptionOrderConfirmation setr.006.001.06

**P2935** Description

**P2936** A RedemptionOrderConfirmation message is sent for investment account 78-89ABCD.

**P2937** The confirmation message contains one execution. It is the execution of an order with order reference KL67TRE54 and deal reference ZERER6. This execution is for financial instrument ISIN IE9876543210.

**P2938** A gross amount of EUR 5000 has been redeemed at an NAVL price of EUR 20 per unit, equating to 250 units.

**P2939** The trade date for this execution is 03 January 26. This execution is made cum dividend. The order was fully executed, and there is no physical delivery of the units.

**P2940** Message Instance

**P2941** <RedOrdrConf>

**P2942** 	<MsgId>

**P2943** 		<Id>R0007</Id>

**P2944** 		<CreDtTm>2026-01-05T09:30:30</CreDtTm>

**P2945** 	</MsgId>

**P2946** 	<MltplExctnDtls>

**P2947** 		<InvstmtAcctDtls>

**P2948** 			<AcctId>78-89ABCD</AcctId>	

**P2949** 		</InvstmtAcctDtls>

**P2950** 		<IndvExctnDtls>

**P2951** 			<OrdrRef>KL67TRE54</OrdrRef>

**P2952** 			<DealRef>ZERER6</DealRef>

**P2953** 			<FinInstrmDtls>

**P2954** 				<Id>

**P2955** 					<ISIN>IE9876543210</ISIN>

**P2956** 				</Id>

**P2957** 			</FinInstrmDtls>

**P2958** 			<UnitsNb>250</UnitsNb>

**P2959** 			<GrssAmt Ccy="EUR">5000</GrssAmt>

**P2960** 			<TradDtTm>

**P2961** 				<Dt>2017-01-03</Dt>

**P2962** 			</TradDtTm>

**P2963** 			<DealgPricDtls>

**P2964** 				<Tp>

**P2965** 					<Cd>NAVL</Cd>

**P2966** 				</Tp>

**P2967** 				<Val>

**P2968** 					<Amt Ccy="EUR">20</Amt>

**P2969** 				</Val>

**P2970** 			</DealgPricDtls>

**P2971** 			<SttlmAmt Ccy="GBP">5000</SttlmAmt>

**P2972** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P2973** 			<CumDvddInd>false</CumDvddInd>

**P2974** 			<PhysDlvryInd>false</PhysDlvryInd>

**P2975** 		</IndvExctnDtls>

**P2976** 	</MltplExctnDtls>

**P2977** </RedOrdrConf>

