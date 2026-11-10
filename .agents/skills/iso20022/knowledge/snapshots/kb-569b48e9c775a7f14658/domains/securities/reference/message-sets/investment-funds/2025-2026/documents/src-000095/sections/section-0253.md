---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Switch", "SwitchOrderConfirmation setr.015.001.05 - Amendment "]
content_origin: "source-transcription"
---

# SwitchOrderConfirmation setr.015.001.05 - Amendment 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Order and Confirmation / Switch / SwitchOrderConfirmation setr.015.001.05 - Amendment .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3659** SwitchOrderConfirmation setr.015.001.05 - Amendment 

**P3660** Description

**P3661** The SwitchOrderConfirmation message is sent as an amendment to the previously sent confirmation above. The AmendmentIndicator is present with the value 'true'. On the redemption, the price, which was previously NAVL EUR 20, is now NAVL EUR 15 and the subscription leg has been adjusted accordingly, in that EUR 575 is now available for the subscription.

**P3662** Message Instance

**P3663** <SwtchOrdrConf>

**P3664** 	<MsgId>

**P3665** 		<Id>SW0004</Id>

**P3666** 		<CreDtTm>2026-01-03T09:55:30</CreDtTm>

**P3667** 	</MsgId>

**P3668** 	<SwtchExctnDtls>

**P3669** 		<AmdmntInd>true</AmdmntInd>

**P3670** 		<DealRef>Deal 1</DealRef>

**P3671** 		<OrdrRef>Order 1</OrdrRef>

**P3672** 			<InvstmtAcctDtls>

**P3673** 			<AcctId>11111111	</AcctId>

**P3674** 		</InvstmtAcctDtls>

**P3675** 		<AddtlAmt>

**P3676** 			<AddtlCshIn Ccy="EUR">200</AddtlCshIn>

**P3677** 		</AddtlAmt>

**P3678** 		<RedLegDtls>

**P3679** 			<LegId>1</LegId>

**P3680** 			<FinInstrmDtls>

**P3681** 				<Id>

**P3682** 					<ISIN>IT1111111111</ISIN>

**P3683** 				</Id>

**P3684** 			</FinInstrmDtls>

**P3685** 			<UnitsNb>25</UnitsNb>

**P3686** 			<TradDtTm>

**P3687** 				<Dt>2026-01-03</Dt>

**P3688** 			</TradDtTm>

**P3689** 			<PricDtls>

**P3690** 				<Tp>

**P3691** 					<Cd>SWIC</Cd>

**P3692** 				</Tp>

**P3693** 				<Val>

**P3694** 					<Amt Ccy="EUR">15</Amt>

**P3695** 				</Val>

**P3696** 			</PricDtls>

**P3697** 			<CumDvddInd>true</CumDvddInd>

**P3698** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3699** 		</RedLegDtls>

**P3700** 		<SbcptLegDtls>

**P3701** 			<LegId>2</LegId>

**P3702** 			<FinInstrmDtls>

**P3703** 				<Id>

**P3704** 					<ISIN>IT2222222222</ISIN>

**P3705** 				</Id>

**P3706** 			</FinInstrmDtls>

**P3707** 			<UnitsNb>82</UnitsNb>

**P3708** 			<NetAmt Ccy="EUR">575</NetAmt>

**P3709** 			<TradDtTm>

**P3710** 				<Dt>2017-01-03</Dt>

**P3711** 			</TradDtTm>

**P3712** 			<PricDtls>

**P3713** 				<Tp>

**P3714** 					<Cd>SWIC</Cd>

**P3715** 				</Tp>

**P3716** 				<Val>

**P3717** 					<Amt Ccy="EUR">7</Amt>

**P3718** 				</Val>

**P3719** 			</PricDtls>

**P3720** 			<CumDvddInd>true</CumDvddInd>

**P3721** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3722** 		</SbcptLegDtls>

**P3723** 	</SwtchExctnDtls>

**P3724** </SwtchOrdrConf>

