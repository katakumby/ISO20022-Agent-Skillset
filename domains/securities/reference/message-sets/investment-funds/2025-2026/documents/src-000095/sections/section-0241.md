---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Order and Confirmation", "Subscription ", "SubscriptionBulkOrderConfirmation setr.009.001.05"]
content_origin: "source-transcription"
---

# SubscriptionBulkOrderConfirmation setr.009.001.05

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Order and Confirmation / Subscription  / SubscriptionBulkOrderConfirmation setr.009.001.05.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P3081** SubscriptionBulkOrderConfirmation setr.009.001.05

**P3082** Description

**P3083** A SubscriptionBulkOrderConfirmation is sent for financial instrument ISIN LU8888888888. It contains two order executions.

**P3084** Confirmation 1

**P3085** The first execution is for an order with order reference 123-1 and deal reference 123-1/001. It is for account 11111111. For this account, EUR 500 have been invested, corresponding to 50 units subscribed at an NAV price of EUR 10.

**P3086** The trade date for this execution is 03 January 2026. The execution is cum dividend. The original order was executed fully. A front-end charge of EUR 5 has been levied. There will not be a physical delivery for this execution. The settlement and custody details indicates that the place of settlement will be SICVFRPP and the delivery agent details will be Euroclear France participant scheme 068. 

**P3087** Confirmation 2

**P3088** The second execution is for an order with order reference 123-2 and deal reference 123-2/002. It is for account 22222222. For this account, GBP 200 have been invested, corresponding to EUR 300 at an exchange rate of 1.5. It corresponds to 30 units subscribed at an NAV price of EUR 10.

**P3089** The trade date for this execution is 03 January 2026. The execution is made cum dividend. The original order was executed fully. There will not be a physical delivery for this execution. The settlement and custody details indicates that the place of settlement will be SICVFRPP and the delivery agent details will be Euroclear France participant scheme 068.

**P3090** Message Instance

**P3091** <SbcptBlkOrdrConf>

**P3092** 	<MsgId>

**P3093** 		<Id>S003</Id>

**P3094** 		<CreDtTm>2026-01-05T09:30:30</CreDtTm>

**P3095** 	</MsgId>

**P3096** 	<BlkExctnDtls>

**P3097** 		<FinInstrmDtls>

**P3098** 			<Id>

**P3099** 				<ISIN>LU8888888888</ISIN>

**P3100** 			</Id>

**P3101** 		</FinInstrmDtls>

**P3102** 		<IndvExctnDtls>

**P3103** 			<OrdrRef>123-1</OrdrRef>

**P3104** 			<DealRef>123-1/001</DealRef>

**P3105** 			<InvstmtAcctDtls>

**P3106** 				<AcctId>11111111</AcctId>

**P3107** 			</InvstmtAcctDtls>

**P3108** 			<UnitsNb>50</UnitsNb>

**P3109** 			<TradDtTm>

**P3110** 				<Dt>2017-01-03</Dt>

**P3111** 			</TradDtTm>

**P3112** 			<DealgPricDtls>

**P3113** 				<Tp>

**P3114** 					<Cd>NAVL</Cd>

**P3115** 				</Tp>

**P3116** 				<Val>

**P3117** 					<Amt Ccy="EUR">10</Amt>

**P3118** 				</Val>

**P3119** 			</DealgPricDtls>

**P3120** 			<SttlmAmt Ccy="EUR">500</SttlmAmt>

**P3121** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P3122** 			<CumDvddInd>true</CumDvddInd>

**P3123** 			<TxOvrhd>

**P3124** 				<IndvFee>

**P3125** 					<Tp>

**P3126** 						<Cd>FEND</Cd>

**P3127** 					</Tp>

**P3128** 					<StdAmt Ccy="EUR">5</StdAmt>

**P3129** 					<InftvInd>false</InftvInd>

**P3130** 				</IndvFee>

**P3131** 			</TxOvrhd>

**P3132** 			<SttlmAndCtdyDtls>

**P3133** 				<SttlmPlc>

**P3134** 				<Pty>

**P3135** 					<AnyBIC>SICVFRPP</AnyBIC>

**P3136** 				</Pty>

**P3137** 				</SttlmPlc>

**P3138** 				<DlvrgSdDtls>

**P3139** 					<DlvrgAgtDtls>

**P3140** 						<PtyId>

**P3141** 							<Pty>

**P3142** 								<PrtryId>

**P3143** 									<Id>068</Id>

**P3144** 									<SchmeNm>Participant</SchmeNm>

**P3145** 									<Issr>Euroclear France</Issr>

**P3146** 								</PrtryId>

**P3147** 							</Pty>

**P3148** 						</PtyId>

**P3149** 					</DlvrgAgtDtls>

**P3150** 				</DlvrgSdDtls>

**P3151** 			</SttlmAndCtdyDtls>

**P3152** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3153** 		</IndvExctnDtls>

**P3154** 		<IndvExctnDtls>

**P3155** 			<OrdrRef>123-2</OrdrRef>

**P3156** 			<DealRef>123-2/002</DealRef>

**P3157** 			<InvstmtAcctDtls>

**P3158** 				<AcctId>22222222</AcctId>

**P3159** 			</InvstmtAcctDtls>

**P3160** 			<UnitsNb>30</UnitsNb>

**P3161** 			<TradDtTm>

**P3162** 				<Dt>2017-01-03</Dt>

**P3163** 			</TradDtTm>

**P3164** 			<DealgPricDtls>

**P3165** 				<Tp>

**P3166** 					<Cd>NAVL</Cd>

**P3167** 				</Tp>

**P3168** 				<Val>

**P3169** 					<Amt Ccy="EUR">10</Amt>

**P3170** 				</Val>

**P3171** 			</DealgPricDtls>

**P3172** 			<SttlmAmt Ccy="EUR">300</SttlmAmt>

**P3173** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P3174** 			<CumDvddInd>true</CumDvddInd>

**P3175** 			<FXDtls>

**P3176** 				<ToAmt Ccy="GBP">200</ToAmt>

**P3177** 				<FrAmt Ccy="EUR">300</FrAmt>

**P3178** 				<UnitCcy>GBP</UnitCcy>

**P3179** 				<QtdCcy>EUR</QtdCcy>

**P3180** 				<XchgRate>1.5</XchgRate>

**P3181** 			</FXDtls>

**P3182** 			<SttlmAndCtdyDtls>

**P3183** 				<SttlmPlc>

**P3184** 				<Pty>

**P3185** 					<AnyBIC>SICVFRPP</AnyBIC>

**P3186** 				</Pty>

**P3187** 				</SttlmPlc>

**P3188** 				<DlvrgSdDtls>

**P3189** 					<DlvrgAgtDtls>

**P3190** 						<PtyId>

**P3191** 							<Pty>

**P3192** 								<PrtryId>

**P3193** 									<Id>068</Id>

**P3194** 									<Issr>Euroclear France</Issr>

**P3195** 							</PrtryId>

**P3196** 						</Pty>

**P3197** 					</PtyId>					

**P3198** 					</DlvrgAgtDtls>

**P3199** 				</DlvrgSdDtls>

**P3200** 			</SttlmAndCtdyDtls>

**P3201** 			<PhysDlvryInd>false</PhysDlvryInd>

**P3202** 		</IndvExctnDtls>

**P3203** 	</BlkExctnDtls>

**P3204** </SbcptBlkOrdrConf>

