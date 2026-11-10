---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Subscription ", "SubscriptionOrderConfirmation setr.012.001.06 (3) Hedge Fund"]
content_origin: "source-transcription"
---

# SubscriptionOrderConfirmation setr.012.001.06 (3) Hedge Fund

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Order and Confirmation / Subscription  / SubscriptionOrderConfirmation setr.012.001.06 (3) Hedge Fund.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3466** SubscriptionOrderConfirmation setr.012.001.06 (3) Hedge Fund

**P3467** Description

**P3468** A SubscriptionOrderConfirmation message is sent for investment account 44444444, beneficial owner reference 444444, to confirm the execution of a subscription order.

**P3469** The confirmation message contains one order execution. It is the execution of an order with order reference Order HF-001 and with deal reference Deal HF-001-01. This execution is for 9-Theta Hedge Fund, class A (Identification 12345678, GA). The series is identified as Series 42.

**P3470** The trade date is 8 February 2026.

**P3471** EUR 50,000 was subscribed at a price of EUR 100, with the creation of 500 units. The settlement amount is EUR 50,000. It is confirmed that the fees are waived.

**P3472** It is confirmed the cash was/is to be settled on 4 January 2026. There will be no physical delivery.

**P3473** Message Instance

**P3474** <SbcptOrdrConf>

**P3475** 	<MsgId>

**P3476** 		<Id>EX-0056</Id>

**P3477** 		<CreDtTm>2026-01-08T09:00:00</CreDtTm>

**P3478** 	</MsgId>

**P3479** 	<MltplExctnDtls>

**P3480** 		<InvstmtAcctDtls>

**P3481** 			<AcctId>1111111111</AcctId>

**P3482** 			<AcctDsgnt>444444</AcctDsgnt>

**P3483** 		</InvstmtAcctDtls>

**P3484** 		<IndvExctnDtls>

**P3485** 			<OrdrRef>Order HF-001</OrdrRef>

**P3486** 			<DealRef>Deal HF-001-01</DealRef>

**P3487** 			<FinInstrmDtls>

**P3488** 				<Id>

**P3489** 					<OthrPrtryId>

**P3490** 						<Id>12345678</Id>

**P3491** 						<IdSrc>

**P3492** 							<Prtry>GA</Prtry>

**P3493** 						</IdSrc>

**P3494** 					</OthrPrtryId>

**P3495** 				</Id>

**P3496** 					<Nm>9-Theta Hedge Fund</Nm>

**P3497** 				<ClssTp>Class A</ClssTp>

**P3498** 				<SrsId>

**P3499** 			<SrsNm>Series 42</SrsNm>

**P3500** 				</SrsId>

**P3501** 				</FinInstrmDtls>

**P3502** 		<UnitsNb>500</UnitsNb>

**P3503** 				<GrssAmt Ccy="EUR">50000</GrssAmt>

**P3504** 			<TradDtTm>

**P3505** 				<Dt>2026-01-08</Dt>

**P3506** 			</TradDtTm>

**P3507** 			<DealgPricDtls>

**P3508** 				<Tp>

**P3509** 					<Cd>NAVL</Cd>

**P3510** 				</Tp>

**P3511** 				<Val>

**P3512** 					<Amt Ccy="EUR">100</Amt>

**P3513** 				</Val>

**P3514** 			</DealgPricDtls>

**P3515** 			<SttlmAmt Ccy="EUR">50000</SttlmAmt>

**P3516** 			<CshSttlmDt>2026-02-08</CshSttlmDt>

**P3517** 			<PrtlyExctdInd>true</PrtlyExctdInd>

**P3518** 			<CumDvddInd>false</CumDvddInd>

**P3519** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3520** 			<OrdrWvrDtls>

**P3521** 				<OrdrWvrRsn>

**P3522** 					<Cd>COMW</Cd>

**P3523** 				</OrdrWvrRsn>

**P3524** 				<InfVal>SIDELETTER</InfVal>

**P3525** 			</OrdrWvrDtls>

**P3526** 		</IndvExctnDtls>

**P3527** 	</MltplExctnDtls>

**P3528** </SbcptOrdrConf>

