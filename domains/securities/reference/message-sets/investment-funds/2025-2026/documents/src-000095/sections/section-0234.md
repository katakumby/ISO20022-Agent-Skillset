---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Redemption", "RedemptionOrder setr.004.001.05 (2)"]
content_origin: "source-transcription"
---

# RedemptionOrder setr.004.001.05 (2)

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Order and Confirmation / Redemption / RedemptionOrder setr.004.001.05 (2).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2864** RedemptionOrder setr.004.001.05 (2)

**P2865** Description

**P2866** A RedemptionOrder message is sent for investment account 36-96XYZ. It contains 2 individual orders.

**P2867** Order 1

**P2868** The first individual order has order reference REF A and is for financial instrument ISIN IE0000012345. The net amount of 3000 EUR is to be redeemed.

**P2869** Order 2

**P2870** The second individual order has order reference REF B and is for financial instrument ISIN IE0000078910. The net amount of 2000 EUR is to be redeemed. The back-end charge rate is 10 percent, the commercial agreement COMAGR4582.

**P2871** There will be no physical delivery. A copy of the message will be sent to a third party, BDAPIEXX.

**P2872** Message Instance

**P2873** <RedOrdr>

**P2874** 	<MsgId>

**P2875** 		<Id>R0005</Id>

**P2876** 		<CreDtTm>2026-01-02T09:30:30</CreDtTm>

**P2877** 	</MsgId>

**P2878** 	<MltplOrdrDtls>

**P2879** 		<InvstmtAcctDtls>

**P2880** 			<AcctId>36-96XYZ</AcctId>	

**P2881** 		</InvstmtAcctDtls>

**P2882** 		<IndvOrdrDtls>

**P2883** 			<OrdrRef>REF A</OrdrRef>

**P2884** 			<FinInstrmDtls>

**P2885** 				<Id>

**P2886** 					<ISIN>IE0000012345</ISIN>

**P2887** 				</Id>

**P2888** 			</FinInstrmDtls>

**P2889** 			<AmtOrUnitsOrPctg>

**P2890** 				<NetAmt Ccy="EUR">3000</NetAmt>

**P2891** 			</AmtOrUnitsOrPctg>

**P2892** 			<PhysDlvryInd>false</PhysDlvryInd>

**P2893** 		</IndvOrdrDtls>

**P2894** 		<IndvOrdrDtls>

**P2895** 			<OrdrRef>REF B</OrdrRef>

**P2896** 			<FinInstrmDtls>

**P2897** 				<Id>

**P2898** 					<ISIN>IE0000078910</ISIN>

**P2899** 				</Id>

**P2900** 			</FinInstrmDtls>

**P2901** 			<AmtOrUnitsOrPctg>

**P2902** 				<NetAmt Ccy="EUR">2000</NetAmt>

**P2903** 			</AmtOrUnitsOrPctg>

**P2904** 			<TxOvrhd>

**P2905** 				<ComrclAgrmtRef>COMAGR4582</ComrclAgrmtRef>

**P2906** 				<IndvFee>

**P2907** 					<Tp>

**P2908** 						<Cd>BEND</Cd>

**P2909** 					</Tp>

**P2910** 					<StdRate>10</StdRate>

**P2911** 				</IndvFee>

**P2912** 			</TxOvrhd>

**P2913** 			<PhysDlvryInd>false</PhysDlvryInd>

**P2914** 		</IndvOrdrDtls>

**P2915** 	</MltplOrdrDtls>

**P2916** 	<CpyDtls>

**P2917** 		<CpyInd>true</CpyInd>

**P2918** 		<OrgnlRcvr>BDAPIEXX</OrgnlRcvr>

**P2919** 	</CpyDtls>

**P2920** </RedOrdr>

