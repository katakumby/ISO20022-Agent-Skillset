---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Subscription ", "SubscriptionOrderConfirmation setr.012.001.06 - Amendment"]
content_origin: "source-transcription"
---

# SubscriptionOrderConfirmation setr.012.001.06 - Amendment

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Subscription  / SubscriptionOrderConfirmation setr.012.001.06 - Amendment.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3364** SubscriptionOrderConfirmation setr.012.001.06 - Amendment

**P3365** Description

**P3366** The SubscriptionOrderConfirmation message is sent as an amendment to the previously sent confirmation above. The AmendmentIndicator is present with the value 'true'. The price, which was previously NAVL EUR 40, is now NAVL EUR 35 and the number of units has been adjusted accordingly.

**P3367** Message Instance

**P3368** <SbcptOrdrConf>

**P3369** 	<MsgId>

**P3370** 		<Id>S008</Id>

**P3371** 		<CreDtTm>2026-01-05T09:40:00</CreDtTm>

**P3372** 	</MsgId>

**P3373** 	<MltplExctnDtls>

**P3374** 		<AmdmntInd>true</AmdmntInd>

**P3375** 		<InvstmtAcctDtls>

**P3376** 			<AcctId>33333333</AcctId>

**P3377** 		</InvstmtAcctDtls>

**P3378** 		<IndvExctnDtls>

**P3379** 			<OrdrRef>Order 1</OrdrRef>

**P3380** 			<DealRef>Deal 1</DealRef>

**P3381** 			<FinInstrmDtls>

**P3382** 				<Id>

**P3383** 					<ISIN>BE1234567890</ISIN>

**P3384** 				</Id>

**P3385** 			</FinInstrmDtls>

**P3386** 			<UnitsNb>140</UnitsNb>

**P3387** 			<NetAmt Ccy="EUR">4900</NetAmt>

**P3388** 			<GrssAmt Ccy="EUR">5000</GrssAmt>

**P3389** 			<TradDtTm>

**P3390** 				<Dt>2026-01-03</Dt>

**P3391** 			</TradDtTm>

**P3392** 			<DealgPricDtls>

**P3393** 			<Tp>

**P3394** 				<Cd>NAVL</Cd>

**P3395** 			</Tp>

**P3396** 				<Val>

**P3397** 					<Amt Ccy="EUR">35</Amt>

**P3398** 				</Val>

**P3399** 			</DealgPricDtls>

**P3400** 			<SttlmAmt Ccy="EUR">4900</SttlmAmt>

**P3401** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P3402** 			<CumDvddInd>true</CumDvddInd>

**P3403** 			<TxOvrhd>

**P3404** 				<TtlFees Ccy="EUR">100</TtlFees>

**P3405** 				<IndvFee>

**P3406** 					<Tp>

**P3407** 						<Cd>FEND</Cd>

**P3408** 					</Tp>

**P3409** 					<StdRate>5</StdRate>

**P3410** 					<DscntDtls>

**P3411** 							<Rate>3</Rate>

**P3412** 					</DscntDtls>

**P3413** 					<ApldAmt Ccy="EUR">100</ApldAmt>

**P3414** 					<ApldRate>2</ApldRate>

**P3415** 					<InftvInd>false</InftvInd>

**P3416** 				</IndvFee>

**P3417** 			</TxOvrhd>

**P3418** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3419** 		</IndvExctnDtls>

**P3420** 	</MltplExctnDtls>

**P3421** </SbcptOrdrConf>

