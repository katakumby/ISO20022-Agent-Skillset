---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Subscription ", "SubscriptionOrder setr.010.001.05 (3) Hedge Fund "]
content_origin: "source-transcription"
---

# SubscriptionOrder setr.010.001.05 (3) Hedge Fund 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Subscription  / SubscriptionOrder setr.010.001.05 (3) Hedge Fund .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3422** SubscriptionOrder setr.010.001.05 (3) Hedge Fund 

**P3423** Description

**P3424** A SubscriptionOrder message is sent for investment account 44444444, the beneficial owner reference is 444444. The order, reference Order HF-001, is an instruction to subscribe EUR 50,000 to 9-Theta Hedge Fund, class A (Identification 12345678, GA). A special agreement is in place that means the fee is waived and reference is made to the side letter. The total settlement amount is to be EUR 50,000.

**P3425** The cash will be settled on 4 January 2026. There will be no physical delivery.

**P3426** Message Instance

**P3427** <SbcptOrdr>

**P3428** 	<MsgId>

**P3429** 		<Id>HF-0325-DA</Id>

**P3430** 		<CreDtTm>2026-01-04T09:30:00</CreDtTm>

**P3431** 	</MsgId>

**P3432** 	<MltplOrdrDtls>

**P3433** 		<InvstmtAcctDtls>

**P3434** 			<AcctId>1111111111</AcctId>

**P3435** 			<AcctDsgnt>444444</AcctDsgnt>

**P3436** 		</InvstmtAcctDtls>

**P3437** 		<IndvOrdrDtls>

**P3438** 			<OrdrRef>Order HF-001</OrdrRef>

**P3439** 			<FinInstrmDtls>

**P3440** 				<Id>

**P3441** 					<OthrPrtryId>

**P3442** 						<Id>12345678</Id>

**P3443** 						<IdSrc>

**P3444** 							<Prtry>GA</Prtry>

**P3445** 						</IdSrc>

**P3446** 					</OthrPrtryId>

**P3447** 				</Id>

**P3448** 				<Nm>9-Theta Hedge Fund</Nm>

**P3449** 				<ClssTp>Class A</ClssTp>

**P3450** 			</FinInstrmDtls>

**P3451** 			<AmtOrUnits>

**P3452** 				<GrssAmt Ccy="EUR">50000</GrssAmt>

**P3453** 			</AmtOrUnits>

**P3454** 			<SttlmAmt Ccy="EUR">50000</SttlmAmt>

**P3455** 			<CshSttlmDt>2026-01-04</CshSttlmDt>

**P3456** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3457** 			<OrdrWvrDtls>

**P3458** 				<OrdrWvrRsn>

**P3459** 					<Cd>COMW</Cd>

**P3460** 				</OrdrWvrRsn>

**P3461** 				<InfVal>SIDELETTER</InfVal>

**P3462** 			</OrdrWvrDtls>

**P3463** 		</IndvOrdrDtls>

**P3464** 	</MltplOrdrDtls>

**P3465** </SbcptOrdr>

