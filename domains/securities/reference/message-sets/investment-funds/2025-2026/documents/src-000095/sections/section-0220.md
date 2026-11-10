---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Fund Cash Forecast ", "FundDetailedConfirmedCashForecastReport camt.043.001.04 – By Currency"]
content_origin: "source-transcription"
---

# FundDetailedConfirmedCashForecastReport camt.043.001.04 – By Currency

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Fund Cash Forecast  / FundDetailedConfirmedCashForecastReport camt.043.001.04 – By Currency.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2138** FundDetailedConfirmedCashForecastReport camt.043.001.04 – By Currency

**P2139** Description

**P2140** A FundDetailedConfirmedCashForecastReport message is sent to report the cash flow movements of financial instrument ISIN DE1234567890 for trade date 15 January 2015. This report contains an exceptional net cash flow. In this report, the cash flows are sorted by currency.

**P2141** MOVEMENTS IN USD

**P2142** The cash-in flows in USD for settlement date 19 January 202015 are the result of orders for 150 units for a total cash-in amount of USD 15,000. The 150 units can be broken down as follows: 90 units are the result of a switch-in. The original order was placed as units. The remaining 60 units are the result of a subscription. The original order was placed as units.

**P2143** The cash-out flows in USD for settlement date 19 January 2015 are the result of orders redeeming 80 units for a total cash-out amount of USD 8,000. The 80 units can be broken down as follows: 30 units are the result of a switch-out. The remaining 50 units are the result of a redemption.

**P2144** MOVEMENTS IN EUR

**P2145** The cash-in flows in EUR for settlement date 19 January 2015 are the result of orders for 2,000,000 units for a total cash-in amount of EUR 200,000,000. This is regarded as an exceptional cash-in movement. The 2,000,000 units can be broken down as follows: 500,000 units are the result of a subscription and the original order was placed as units. The remaining 1,500,000 units are the result of a subscription and the original order was placed as cash.

**P2146** The cash-out flows in EUR for settlement date 19 January 2015 are the result of orders redeeming 10,000 units for a total cash-out amount of EUR 10,000,000. This is regarded as an exceptional cash-in movement. The 10,000 units can be broken down as follows: 2,000 are the result of a switch-out. The remaining 8,000 units are the result of a redemption.

**P2147** Message Instance

**P2148** <FndDtldConfdCshFcstRpt>

**P2149** 	<MsgId>

**P2150** 		<Id>44FA34195</Id>

**P2151** 		<CreDtTm>2015-01-15T17:00:00</CreDtTm>

**P2152** 	</MsgId>

**P2153** 	<MsgPgntn>

**P2154** 		<PgNb>1</PgNb>

**P2155** 		<LastPgInd>true</LastPgInd>

**P2156** 	</MsgPgntn>

**P2157** 	<FndCshFcstDtls>

**P2158** 		<Id>FCF010</Id>

**P2159** 		<TradDtTm>

**P2160** 			<Dt>2015-01-15</Dt>

**P2161** 		</TradDtTm>

**P2162** 		<FinInstrmDtls>

**P2163** 			<Id>

**P2164** 				<ISIN>DE1234567890</ISIN>

**P2165** 			</Id>

**P2166** 			<DualFndInd>false</DualFndInd>

**P2167** 		</FinInstrmDtls>

**P2168** 		<XcptnlNetCshFlowInd>false</XcptnlNetCshFlowInd>

**P2169** 		<BrkdwnByCcy>

**P2170** 				<Ccy>USD</Ccy>

**P2171** 				<CshOutFcst>

**P2172** 					<CshSttlmDt>2015-01-19</CshSttlmDt>

**P2173** 					<SubTtlAmt Ccy="USD">8000</SubTtlAmt>

**P2174** 					<SubTtlUnitsNb>

**P2175** 						<Unit>80</Unit>

**P2176** 					</SubTtlUnitsNb>

**P2177** 					<XcptnlCshFlowInd>false</XcptnlCshFlowInd>

**P2178** 					<CshOutBrkdwnDtls>

**P2179** 						<UnitsNb>

**P2180** 							<Unit>30</Unit>

**P2181** 						</UnitsNb>

**P2182** 						<InvstmtFndTxOutTp>

**P2183** 							<Cd>SWIO</Cd>

**P2184** 						</InvstmtFndTxOutTp>

**P2185** 						<OrgnlOrdrQtyTp>

**P2186** 							<Cd>UNIT</Cd>

**P2187** 						</OrgnlOrdrQtyTp>

**P2188** 					</CshOutBrkdwnDtls>

**P2189** 					<CshOutBrkdwnDtls>

**P2190** 						<UnitsNb>

**P2191** 							<Unit>50</Unit>

**P2192** 						</UnitsNb>

**P2193** 						<InvstmtFndTxOutTp>

**P2194** 							<Cd>REDM</Cd>

**P2195** 						</InvstmtFndTxOutTp>

**P2196** 						<OrgnlOrdrQtyTp>

**P2197** 							<Cd>UNIT</Cd>

**P2198** 						</OrgnlOrdrQtyTp>

**P2199** 					</CshOutBrkdwnDtls>

**P2200** 				</CshOutFcst>

**P2201** 				<CshInFcst>

**P2202** 					<CshSttlmDt>2015-01-19</CshSttlmDt>

**P2203** 					<SubTtlAmt Ccy="USD">15000</SubTtlAmt>

**P2204** 					<SubTtlUnitsNb>

**P2205** 						<Unit>150</Unit>

**P2206** 					</SubTtlUnitsNb>

**P2207** 					<XcptnlCshFlowInd>false</XcptnlCshFlowInd>

**P2208** 					<CshInBrkdwnDtls>

**P2209** 						<UnitsNb>

**P2210** 							<Unit>90</Unit>

**P2211** 						</UnitsNb>

**P2212** 						<InvstmtFndTxInTp>

**P2213** 							<Cd>SWII</Cd>

**P2214** 						</InvstmtFndTxInTp>

**P2215** 						<OrgnlOrdrQtyTp>

**P2216** 							<Cd>UNIT</Cd>

**P2217** 						</OrgnlOrdrQtyTp>

**P2218** 					</CshInBrkdwnDtls>

**P2219** 					<CshInBrkdwnDtls>

**P2220** 						<UnitsNb>

**P2221** 							<Unit>60</Unit>

**P2222** 						</UnitsNb>

**P2223** 						<InvstmtFndTxInTp>

**P2224** 							<Cd>SUBS</Cd>

**P2225** 						</InvstmtFndTxInTp>

**P2226** 						<OrgnlOrdrQtyTp>

**P2227** 							<Cd>UNIT</Cd>

**P2228** 						</OrgnlOrdrQtyTp>

**P2229** 					</CshInBrkdwnDtls>

**P2230** 				</CshInFcst>

**P2231** 		</BrkdwnByCcy>

**P2232** 		<BrkdwnByCcy>

**P2233** 			<Ccy>EUR</Ccy>

**P2234** 			<CshOutFcst>

**P2235** 			<CshSttlmDt>2015-01-19</CshSttlmDt>

**P2236** 			<SubTtlAmt Ccy="EUR">10000000</SubTtlAmt>

**P2237** 			<SubTtlUnitsNb>

**P2238** 				<Unit>10000</Unit>

**P2239** 			</SubTtlUnitsNb>

**P2240** 			<XcptnlCshFlowInd>true</XcptnlCshFlowInd>

**P2241** 			<CshOutBrkdwnDtls>

**P2242** 				<UnitsNb>

**P2243** 					<Unit>2000</Unit>

**P2244** 				</UnitsNb>

**P2245** 				<InvstmtFndTxOutTp>

**P2246** 					<Cd>SWIO</Cd>

**P2247** 				</InvstmtFndTxOutTp>

**P2248** 				<OrgnlOrdrQtyTp>

**P2249** 					<Cd>UNIT</Cd>

**P2250** 				</OrgnlOrdrQtyTp>

**P2251** 				</CshOutBrkdwnDtls>

**P2252** 				<CshOutBrkdwnDtls>

**P2253** 					<UnitsNb>

**P2254** 						<Unit>8000</Unit>

**P2255** 					</UnitsNb>

**P2256** 					<InvstmtFndTxOutTp>

**P2257** 						<Cd>REDM</Cd>

**P2258** 					</InvstmtFndTxOutTp>

**P2259** 					<OrgnlOrdrQtyTp>

**P2260** 						<Cd>UNIT</Cd>

**P2261** 					</OrgnlOrdrQtyTp>

**P2262** 				</CshOutBrkdwnDtls>

**P2263** 			</CshOutFcst>

**P2264** 			<CshInFcst>

**P2265** 				<CshSttlmDt>2015-01-19</CshSttlmDt>

**P2266** 				<SubTtlAmt Ccy="EUR">200000000</SubTtlAmt>

**P2267** 				<SubTtlUnitsNb>

**P2268** 					<Unit>2000000</Unit>

**P2269** 				</SubTtlUnitsNb>

**P2270** 				<XcptnlCshFlowInd>true</XcptnlCshFlowInd>

**P2271** 				<CshInBrkdwnDtls>

**P2272** 					<UnitsNb>

**P2273** 						<Unit>500000</Unit>

**P2274** 					</UnitsNb>

**P2275** 					<InvstmtFndTxInTp>

**P2276** 						<Cd>SUBS</Cd>

**P2277** 					</InvstmtFndTxInTp>

**P2278** 					<OrgnlOrdrQtyTp>

**P2279** 						<Cd>UNIT</Cd>

**P2280** 					</OrgnlOrdrQtyTp>

**P2281** 				</CshInBrkdwnDtls>

**P2282** 				<CshInBrkdwnDtls>

**P2283** 					<UnitsNb>

**P2284** 						<Unit>150000</Unit>

**P2285** 					</UnitsNb>

**P2286** 					<InvstmtFndTxInTp>

**P2287** 						<Cd>SUBS</Cd>

**P2288** 					</InvstmtFndTxInTp>

**P2289** 					<OrgnlOrdrQtyTp>

**P2290** 						<Cd>CASH</Cd>

**P2291** 					</OrgnlOrdrQtyTp>

**P2292** 				</CshInBrkdwnDtls>

**P2293** 			</CshInFcst>

**P2294** 		</BrkdwnByCcy>

**P2295** 	</FndCshFcstDtls>

**P2296** </FndDtldConfdCshFcstRpt>

