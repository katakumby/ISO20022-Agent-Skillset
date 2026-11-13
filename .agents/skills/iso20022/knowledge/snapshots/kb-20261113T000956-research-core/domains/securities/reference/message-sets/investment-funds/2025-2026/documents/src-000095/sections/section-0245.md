---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Subscription ", "SubscriptionOrderConfirmation setr.012.001.06"]
content_origin: "source-transcription"
---

# SubscriptionOrderConfirmation setr.012.001.06

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Subscription  / SubscriptionOrderConfirmation setr.012.001.06.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3304** SubscriptionOrderConfirmation setr.012.001.06

**P3305** Description

**P3306** A SubscriptionOrderConfirmation message is sent for investment account 33333333 to confirm the execution of a subscription order.

**P3307** The confirmation message contains one order execution. It is the execution of an order with order reference Order 1 and with deal reference Deal 1. This execution is for financial instrument ISIN BE1234567890.

**P3308** The gross amount is EUR 5000. The front-end charge applied is EUR 100 (a discount of 3% on the standard charge of 5%). The net amount (price x quantity) is EUR 4900. The price (NAVL) is EUR 40 per unit, equating to 122.5 units. The total fees for the transaction is EUR 100.

**P3309** The trade date for this execution is 03 January 2026. This execution is cum dividend. The order was fully executed, and there is no physical delivery of the units.

**P3310** Message Instance

**P3311** <SbcptOrdrConf>

**P3312** 	<MsgId>

**P3313** 		<Id>S00</Id>

**P3314** 		<CreDtTm>2026-01-05T09:30:00</CreDtTm>

**P3315** 	</MsgId>

**P3316** 	<MltplExctnDtls>

**P3317** 		<InvstmtAcctDtls>

**P3318** 			<AcctId>33333333</AcctId>

**P3319** 		</InvstmtAcctDtls>

**P3320** 		<IndvExctnDtls>

**P3321** 			<OrdrRef> Order 1</OrdrRef>

**P3322** 			<DealRef>Deal 1</DealRef>

**P3323** 			<FinInstrmDtls>

**P3324** 				<Id>

**P3325** 					<ISIN>BE1234567890</ISIN>

**P3326** 				</Id>

**P3327** 			</FinInstrmDtls>

**P3328** 			<UnitsNb>122.5</UnitsNb>

**P3329** 			<NetAmt Ccy="EUR">4900</NetAmt>

**P3330** 			<GrssAmt Ccy="EUR">5000</GrssAmt>

**P3331** 			<TradDtTm>

**P3332** 				<Dt>2026-01-03</Dt>

**P3333** 			</TradDtTm>

**P3334** 			<DealgPricDtls>

**P3335** 				<Tp>

**P3336** 					<Cd>NAVL</Cd>

**P3337** 				</Tp>

**P3338** 				<Val>

**P3339** 					<Amt Ccy="EUR">40</Amt>

**P3340** 				</Val>

**P3341** 			</DealgPricDtls>

**P3342** 			<SttlmAmt Ccy="EUR">4900</SttlmAmt>

**P3343** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P3344** 			<CumDvddInd>true</CumDvddInd>

**P3345** 			<TxOvrhd>

**P3346** 				<TtlFees Ccy="EUR">100</TtlFees>

**P3347** 				<IndvFee>

**P3348** 					<Tp>

**P3349** 						<Cd>FEND</Cd>

**P3350** 					</Tp>

**P3351** 					<StdRate>5</StdRate>

**P3352** 					<DscntDtls>

**P3353** 						<Rate>3</Rate>

**P3354** 					</DscntDtls>

**P3355** 					<ApldAmt Ccy="EUR">100</ApldAmt>

**P3356** 					<ApldRate>2</ApldRate>

**P3357** 					<InftvInd>false</InftvInd>

**P3358** 				</IndvFee>

**P3359** 			</TxOvrhd>

**P3360** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3361** 		</IndvExctnDtls>

**P3362** 	</MltplExctnDtls>

**P3363** </SbcptOrdrConf>

