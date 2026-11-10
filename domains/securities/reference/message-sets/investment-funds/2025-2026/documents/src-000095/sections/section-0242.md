---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Subscription ", "SubscriptionOrder setr.010.001.05 (1)"]
content_origin: "source-transcription"
---

# SubscriptionOrder setr.010.001.05 (1)

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Order and Confirmation / Subscription  / SubscriptionOrder setr.010.001.05 (1).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3205** SubscriptionOrder setr.010.001.05 (1)

**P3206** Description

**P3207** A SubscriptionOrder message is sent for investment account 33333333. It contains one order.

**P3208** The individual order has order reference Order 1 and is for financial instrument ISIN BE1234567890. 

**P3209** EUR 5,000 is to be invested in the referenced financial instrument, this amount includes any charges.

**P3210** A discount of 3% to the standard front-end change of 5% has been agreed,. 

**P3211** Message Instance

**P3212** <SbcptOrdr>

**P3213** 	<MsgId>

**P3214** 		<Id>S0004</Id>

**P3215** 		<CreDtTm>2026-01-02T09:30:30</CreDtTm>

**P3216** 	</MsgId>

**P3217** 	<MltplOrdrDtls>

**P3218** 		<InvstmtAcctDtls>

**P3219** 			<AcctId>33333333</AcctId>

**P3220** 		</InvstmtAcctDtls>

**P3221** 		<IndvOrdrDtls>

**P3222** 			<OrdrRef>Order 1</OrdrRef>

**P3223** 			<FinInstrmDtls>

**P3224** 				<Id>

**P3225** 					<ISIN>BE1234567890</ISIN>

**P3226** 				</Id>

**P3227** 			</FinInstrmDtls>

**P3228** 			<AmtOrUnits>

**P3229** 				<GrssAmt Ccy="EUR">5000</GrssAmt>

**P3230** 			</AmtOrUnits>

**P3231** 			<TxOvrhd>

**P3232** 					<IndvFee>

**P3233** 						<Tp>

**P3234** 							<Cd>FEND</Cd>

**P3235** 						</Tp>

**P3236** 						<StdRate>5</StdRate>

**P3237** 						<DscntDtls>

**P3238** 							<Rate>3</Rate>

**P3239** 						</DscntDtls>

**P3240** 						<ReqdRate>2</ReqdRate>

**P3241** 					</IndvFee>

**P3242** 			</TxOvrhd>

**P3243** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3244** 		</IndvOrdrDtls>

**P3245** 	</MltplOrdrDtls>

**P3246** </SbcptOrdr>

