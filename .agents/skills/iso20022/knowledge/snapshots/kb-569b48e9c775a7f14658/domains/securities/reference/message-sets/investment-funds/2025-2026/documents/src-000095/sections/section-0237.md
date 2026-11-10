---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Redemption", "RedemptionOrderConfirmation setr.006.001.06 - Amendment"]
content_origin: "source-transcription"
---

# RedemptionOrderConfirmation setr.006.001.06 - Amendment

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Redemption / RedemptionOrderConfirmation setr.006.001.06 - Amendment.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2978** RedemptionOrderConfirmation setr.006.001.06 - Amendment

**P2979** Description

**P2980** The RedemptionOrderConfirmation message is sent as an amendment to the previously sent confirmation above. The AmendmentIndicator is present with the value 'true'. The price, which was previously NAVL EUR 20, is now NAVL EUR 25 and the number of units has been adjusted accordingly.

**P2981** Message Instance

**P2982** <RedOrdrConf>

**P2983** 	<MsgId>

**P2984** 		<Id>R0008</Id>

**P2985** 		<CreDtTm>2026-01-05T09:40:30</CreDtTm>

**P2986** 	</MsgId>

**P2987** 	<MltplExctnDtls>

**P2988** 		<AmdmntInd>true</AmdmntInd>

**P2989** 		<InvstmtAcctDtls>

**P2990** 			<AcctId>78-89ABCD</AcctId>	

**P2991** 		</InvstmtAcctDtls>

**P2992** 		<IndvExctnDtls>

**P2993** 			<OrdrRef>KL67TRE54</OrdrRef>

**P2994** 			<DealRef>ZERER6</DealRef>

**P2995** 			<FinInstrmDtls>

**P2996** 				<Id>

**P2997** 					<ISIN>IE9876543210</ISIN>

**P2998** 				</Id>

**P2999** 			</FinInstrmDtls>

**P3000** 			<UnitsNb>200</UnitsNb>

**P3001** 			<GrssAmt Ccy="EUR">5000</GrssAmt>

**P3002** 			<TradDtTm>

**P3003** 				<Dt>2017-01-03</Dt>

**P3004** 			</TradDtTm>

**P3005** 			<DealgPricDtls>

**P3006** 				<Tp>

**P3007** 					<Cd>NAVL</Cd>

**P3008** 				</Tp>

**P3009** 				<Val>

**P3010** 					<Amt Ccy="EUR">20</Amt>

**P3011** 				</Val>

**P3012** 			</DealgPricDtls>

**P3013** 			<SttlmAmt Ccy="GBP">5000</SttlmAmt>

**P3014** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P3015** 			<CumDvddInd>false</CumDvddInd>

**P3016** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3017** 		</IndvExctnDtls>

**P3018** 	</MltplExctnDtls>

**P3019** </RedOrdrConf>

