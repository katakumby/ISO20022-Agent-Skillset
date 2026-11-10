---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Subscription ", "SubscriptionBulkOrder setr.007.001.05"]
content_origin: "source-transcription"
---

# SubscriptionBulkOrder setr.007.001.05

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Order and Confirmation / Subscription  / SubscriptionBulkOrder setr.007.001.05.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3021** SubscriptionBulkOrder setr.007.001.05

**P3022** Description

**P3023** A SubscriptionBulkOrder message is sent for financial instrument ISIN LU8888888888. It contains two orders.

**P3024** Order 1

**P3025** The first individual order, order reference 123-1, is for account 11111111. For this account, EUR 500 net is to be invested. There will be no physical delivery.

**P3026** Order 2

**P3027** The second individual order, order reference 123-2, is for account22222222. For this account, GBP 200 net is to be invested. There will be no physical delivery. The requested settlement currency for all the orders in the message is EUR, even though for one of the orders, the ordered amount is in GBP.

**P3028** Message Instance

**P3029** <SbcptBlkOrdr>

**P3030** 	<MsgId>

**P3031** 		<Id>S0001</Id>

**P3032** 		<CreDtTm>2026-01-05T09:30:30</CreDtTm>

**P3033** 	</MsgId>

**P3034** 	<BlkOrdrDtls>

**P3035** 		<FinInstrmDtls>

**P3036** 			<Id>

**P3037** 				<ISIN>LU8888888888</ISIN>

**P3038** 			</Id>

**P3039** 		</FinInstrmDtls>

**P3040** 		<IndvOrdrDtls>

**P3041** 			<OrdrRef>123-1</OrdrRef>

**P3042** 			<AmtOrUnits>

**P3043** 				<NetAmt Ccy="EUR">500</NetAmt>

**P3044** 			</AmtOrUnits>

**P3045** 			<InvstmtAcctDtls>

**P3046** 				<AcctId>11111111</AcctId>

**P3047** 			</InvstmtAcctDtls>

**P3048** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3049** 		</IndvOrdrDtls>

**P3050** 		<IndvOrdrDtls>

**P3051** 			<OrdrRef>123-2</OrdrRef>

**P3052** 			<AmtOrUnits>

**P3053** 				<NetAmt Ccy="GBP">200</NetAmt>

**P3054** 			</AmtOrUnits>

**P3055** 			<InvstmtAcctDtls>

**P3056** 				<AcctId>22222222</AcctId>

**P3057** 			</InvstmtAcctDtls>

**P3058** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3059** 		</IndvOrdrDtls>

**P3060** 		<ReqdSttlmCcy>EUR</ReqdSttlmCcy> 

**P3061** 	</BlkOrdrDtls>

**P3062** </SbcptBlkOrdr>

