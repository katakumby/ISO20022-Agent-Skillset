---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Redemption", "RedemptionBulkOrderConfirmation setr.003.001.05"]
content_origin: "source-transcription"
---

# RedemptionBulkOrderConfirmation setr.003.001.05

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Order and Confirmation / Redemption / RedemptionBulkOrderConfirmation setr.003.001.05.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2754** RedemptionBulkOrderConfirmation setr.003.001.05

**P2755** Description

**P2756** A RedemptionBulkOrderConfirmation message is sent for financial instrument ISIN FR1234567890. The confirmation message contains two order executions.

**P2757** Order 1

**P2758** The first execution is for an order with order reference 1111 and deal reference 1111-0001. It is for account 001-56576576. For this account, 100 units have been redeemed at a NAV price of EUR 10 per unit for an amount of EUR 1000. The trade date for this execution is 03 January 2026. This execution is made ex dividend. It is not a partial execution of the original order. There will not be a physical delivery for this execution.

**P2759** Order 2

**P2760** The second execution is for an order with order reference 2222 and deal reference 2222-0001. It is for account 007-23415354. For this account, 50 units have been redeemed at a NAV price of EUR 10 per unit for an amount of EUR 500. The trade date for this execution is 03 January 2026. For this execution, a commission of EUR 30 applies. The beneficiary of this commission is the party DISTFRPP. The settlement amount is EUR 470.This execution is made ex dividend. It is not a partial execution of the original order. There will not be a physical delivery for this execution.

**P2761** Message Instance

**P2762** <RedBlkOrdrConf>

**P2763** 	<MsgId>

**P2764** 		<Id>R0003</Id>

**P2765** 		<CreDtTm>2026-01-05T09:30:30</CreDtTm>

**P2766** 	</MsgId>

**P2767** 	<BlkExctnDtls>

**P2768** 		<FinInstrmDtls>

**P2769** 			<Id>

**P2770** 				<ISIN>FR1234567890</ISIN>

**P2771** 			</Id>

**P2772** 		</FinInstrmDtls>

**P2773** 		<IndvExctnDtls>

**P2774** 			<OrdrRef>1111</OrdrRef>

**P2775** 			<DealRef>1111-0001</DealRef>

**P2776** 			<UnitsNb>100</UnitsNb>

**P2777** 			<InvstmtAcctDtls>

**P2778** 				<AcctId>001-56576576</AcctId>

**P2779** 			</InvstmtAcctDtls>

**P2780** 			<TradDtTm>

**P2781** 				<Dt>2026-01-03</Dt>

**P2782** 			</TradDtTm>

**P2783** 			<SttlmAmt Ccy="EUR">1000</SttlmAmt>

**P2784** 			<DealgPricDtls>

**P2785** 				<Tp>

**P2786** 					<Cd>NAVL</Cd>

**P2787** 				</Tp>

**P2788** 				<Val>

**P2789** 					<Amt Ccy="EUR">58.90</Amt>

**P2790** 				</Val>

**P2791** 			</DealgPricDtls>

**P2792** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P2793** 			<CumDvddInd>false</CumDvddInd>

**P2794** 			<PhysDlvryInd>false</PhysDlvryInd>

**P2795** 		</IndvExctnDtls>

**P2796** 		<IndvExctnDtls>

**P2797** 			<OrdrRef>2222</OrdrRef>

**P2798** 			<DealRef>2222-0001</DealRef>

**P2799** 			<UnitsNb>50</UnitsNb>

**P2800** 			<InvstmtAcctDtls>

**P2801** 				<AcctId>007-23415354</AcctId>

**P2802** 			</InvstmtAcctDtls>

**P2803** 			<GrssAmt Ccy="EUR">500</GrssAmt>

**P2804** 			<TradDtTm>

**P2805** 				<Dt>2017-01-03</Dt>

**P2806** 			</TradDtTm>

**P2807** 			<SttlmAmt Ccy="EUR">570</SttlmAmt>

**P2808** 			<DealgPricDtls>

**P2809** 				<Tp>

**P2810** 					<Cd>NAVL</Cd>

**P2811** 				</Tp>

**P2812** 				<Val>

**P2813** 					<Amt Ccy="EUR">10</Amt>

**P2814** 				</Val>

**P2815** 			</DealgPricDtls>

**P2816** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P2817** 			<CumDvddInd>false</CumDvddInd>

**P2818** 			<TxOvrhd>

**P2819** 				<IndvFee>

**P2820** 					<Tp>

**P2821** 						<Cd>COMM</Cd>

**P2822** 					</Tp>

**P2823** 					<ApldAmt Ccy="EUR">30</ApldAmt>

**P2824** 					<RcptId>

**P2825** 						<Pty>

**P2826** 							<AnyBIC>DISTFRPP</AnyBIC>

**P2827** 						</Pty>

**P2828** 					</RcptId>

**P2829** 					<InftvInd>false</InftvInd>

**P2830** 				</IndvFee>

**P2831** 			</TxOvrhd>

**P2832** 			<PhysDlvryInd>false</PhysDlvryInd>

**P2833** 		</IndvExctnDtls>

**P2834** 	</BlkExctnDtls>

**P2835** </RedBlkOrdrConf>

