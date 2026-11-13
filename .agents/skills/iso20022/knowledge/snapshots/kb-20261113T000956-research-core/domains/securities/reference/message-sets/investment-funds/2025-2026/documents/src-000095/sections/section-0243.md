---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Subscription ", "SubscriptionOrder setr.010.001.05 (2)"]
content_origin: "source-transcription"
---

# SubscriptionOrder setr.010.001.05 (2)

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Subscription  / SubscriptionOrder setr.010.001.05 (2).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3247** SubscriptionOrder setr.010.001.05 (2)

**P3248** Description

**P3249** A SubscriptionOrder message is sent for investment account 44444444. It contains instructions for two individual orders.

**P3250** Order 1

**P3251** The individual order, order reference Order 1, is for financial instrument ISIN BE1111111111. EUR 500 is to be invested in the referenced financial instrument.

**P3252** Order 2

**P3253** The individual order, order reference Order 2, is for financial instrument ISIN BE1234567890. EUR 800 is to be invested in the referenced financial instrument.

**P3254** There will be no physical delivery.

**P3255** Message Instance

**P3256** <SbcptOrdr>

**P3257** 	<MsgId>

**P3258** 		<Id>S0005</Id>

**P3259** 		<CreDtTm>2026-01-02T09:30:30</CreDtTm>

**P3260** 	</MsgId>

**P3261** 	<MltplOrdrDtls>

**P3262** 		<InvstmtAcctDtls>

**P3263** 			<AcctId>44444444</AcctId>

**P3264** 		</InvstmtAcctDtls>

**P3265** 		<IndvOrdrDtls>

**P3266** 			<OrdrRef>Order 1</OrdrRef>

**P3267** 			<FinInstrmDtls>

**P3268** 				<Id>

**P3269** 					<ISIN>BE1111111111</ISIN>

**P3270** 				</Id>

**P3271** 			</FinInstrmDtls>

**P3272** 			<AmtOrUnits>

**P3273** 				<NetAmt Ccy="EUR">500</NetAmt>

**P3274** 			</AmtOrUnits>

**P3275** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3276** 		</IndvOrdrDtls>

**P3277** 		<IndvOrdrDtls>

**P3278** 			<OrdrRef>Order 2</OrdrRef>

**P3279** 			<FinInstrmDtls>

**P3280** 				<Id>

**P3281** 					<ISIN>BE1234567890</ISIN>

**P3282** 				</Id>

**P3283** 			</FinInstrmDtls>

**P3284** 			<AmtOrUnits>

**P3285** 				<NetAmt Ccy="EUR">800</NetAmt>

**P3286** 			</AmtOrUnits>

**P3287** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3288** 		</IndvOrdrDtls>

**P3289** 	</MltplOrdrDtls>

**P3290** </SbcptOrdr>

