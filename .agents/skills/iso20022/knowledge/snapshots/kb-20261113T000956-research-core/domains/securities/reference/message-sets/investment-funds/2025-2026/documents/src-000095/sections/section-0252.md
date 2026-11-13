---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Switch", "SwitchOrderConfirmation setr.015.001.05"]
content_origin: "source-transcription"
---

# SwitchOrderConfirmation setr.015.001.05

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Switch / SwitchOrderConfirmation setr.015.001.05.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3591** SwitchOrderConfirmation setr.015.001.05

**P3592** Description

**P3593** A SwitchOrderConfirmation message is sent for investment account 11111111to confirm the execution of a switch order.

**P3594** This order has order reference Order 1 and deal reference Deal 1.

**P3595** The redemption leg indicates that 25 units of financial instrument ISIN IT1111111111, worth EUR 500 have been redeemed at a switch price of EUR 20 per unit. There is no physical delivery for this leg.

**P3596** The subscription leg indicates that 100 units of financial instrument ISIN IT2222222222 have been subscribed to at EUR 7 per unit for an amount of EUR 700 (The amount derived from the redemption is EUR 500 and EUR 200 has been added as instructed in the order). There is no physical delivery for this leg.

**P3597** Message Instance

**P3598** <SwtchOrdrConf>

**P3599** 	<MsgId>

**P3600** 		<Id>SW0003</Id>

**P3601** 		<CreDtTm>2026-01-03T09:30:30</CreDtTm>

**P3602** 	</MsgId>

**P3603** 	<SwtchExctnDtls>

**P3604** 		<DealRef>Deal 1</DealRef>

**P3605** 		<OrdrRef>Order 1</OrdrRef>

**P3606** 		<InvstmtAcctDtls>

**P3607** 			<AcctId>11111111	</AcctId>

**P3608** 		</InvstmtAcctDtls>

**P3609** 		<AddtlAmt>

**P3610** 			<AddtlCshIn Ccy="EUR">200</AddtlCshIn>

**P3611** 		</AddtlAmt>

**P3612** 		<RedLegDtls>

**P3613** 			<LegId>1</LegId>

**P3614** 			<FinInstrmDtls>

**P3615** 				<Id>

**P3616** 					<ISIN>IT1111111111</ISIN>

**P3617** 				</Id>

**P3618** 			</FinInstrmDtls>

**P3619** 			<UnitsNb>25</UnitsNb>

**P3620** 			<TradDtTm>

**P3621** 				<Dt>2026-01-03</Dt>

**P3622** 			</TradDtTm>

**P3623** 			<PricDtls>

**P3624** 				<Tp>

**P3625** 					<Cd>SWIC</Cd>

**P3626** 				</Tp>

**P3627** 				<Val>

**P3628** 					<Amt Ccy="EUR">20</Amt>

**P3629** 				</Val>

**P3630** 			</PricDtls>

**P3631** 			<CumDvddInd>true</CumDvddInd>

**P3632** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3633** 		</RedLegDtls>

**P3634** 		<SbcptLegDtls>

**P3635** 			<LegId>2</LegId>

**P3636** 			<FinInstrmDtls>

**P3637** 				<Id>

**P3638** 					<ISIN>IT2222222222</ISIN>

**P3639** 				</Id>

**P3640** 			</FinInstrmDtls>

**P3641** 			<UnitsNb>100</UnitsNb>

**P3642** 			<NetAmt Ccy="EUR">700</NetAmt>

**P3643** 			<TradDtTm>

**P3644** 				<Dt>2026-01-03</Dt>

**P3645** 			</TradDtTm>

**P3646** 			<PricDtls>

**P3647** 				<Tp>

**P3648** 					<Cd>SWIC</Cd>

**P3649** 				</Tp>

**P3650** 				<Val>

**P3651** 					<Amt Ccy="EUR">7</Amt>

**P3652** 				</Val>

**P3653** 			</PricDtls>

**P3654** 			<CumDvddInd>true</CumDvddInd>

**P3655** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3656** 		</SbcptLegDtls>

**P3657** 	</SwtchExctnDtls>

**P3658** </SwtchOrdrConf>

