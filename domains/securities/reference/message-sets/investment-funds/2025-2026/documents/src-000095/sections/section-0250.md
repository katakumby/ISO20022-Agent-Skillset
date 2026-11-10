---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Switch", "SwitchOrder setr.013.001.05"]
content_origin: "source-transcription"
---

# SwitchOrder setr.013.001.05

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Order and Confirmation / Switch / SwitchOrder setr.013.001.05.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3530** SwitchOrder setr.013.001.05

**P3531** Description

**P3532** A SwitchOrder message is sent for investment account11111111.

**P3533** This order has order reference Order 1.

**P3534** The redemption leg indicates that EUR 500 worth of financial instrument ISIN IT1111111111 is to be redeemed. There is no physical delivery for this leg.

**P3535** The subscription leg indicates that 100 percent of the redeemed total amount must be subscribed to financial instrument ISIN IT2222222222. There is no physical delivery for this leg.

**P3536** In addition, the switch order specifies that an additional EUR 200 must be invested.

**P3537** Message Instance

**P3538** <SwtchOrdr>

**P3539** 	<MsgId>

**P3540** 		<Id>SW0001</Id>

**P3541** 		<CreDtTm>2026-01-03T09:30:30</CreDtTm>

**P3542** 	</MsgId>

**P3543** 	<SwtchOrdrDtls>

**P3544** 		<OrdrRef>Order 1</OrdrRef>

**P3545** 		<InvstmtAcctDtls>

**P3546** 			<AcctId>11111111</AcctId>

**P3547** 		</InvstmtAcctDtls>

**P3548** 		<AddtlAmt>

**P3549** 			<AddtlCshIn Ccy="EUR">200</AddtlCshIn>

**P3550** 		</AddtlAmt>

**P3551** 		<RedLegDtls>

**P3552** 			<LegId>1</LegId>

**P3553** 			<FinInstrmDtls>

**P3554** 				<Id>

**P3555** 					<ISIN>IT1111111111</ISIN>

**P3556** 				</Id>

**P3557** 			</FinInstrmDtls>

**P3558** 			<FinInstrmQtyChc>

**P3559** 				<NetAmt Ccy="EUR">500</NetAmt>

**P3560** 			</FinInstrmQtyChc>

**P3561** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3562** 		</RedLegDtls>

**P3563** 		<SbcptLegDtls>

**P3564** 			<LegId>2</LegId>

**P3565** 			<FinInstrmDtls>

**P3566** 				<Id>

**P3567** 					<ISIN>IT2222222222</ISIN>

**P3568** 				</Id>

**P3569** 			</FinInstrmDtls>

**P3570** 			<FinInstrmQtyChc>

**P3571** 				<PctgOfTtlRedAmt>100</PctgOfTtlRedAmt>

**P3572** 			</FinInstrmQtyChc>

**P3573** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3574** 		</SbcptLegDtls>

**P3575** 	</SwtchOrdrDtls>

**P3576** </SwtchOrdr>

