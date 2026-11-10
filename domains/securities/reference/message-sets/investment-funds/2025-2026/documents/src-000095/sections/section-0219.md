---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Fund Cash Forecast ", "FundDetailedEstimatedCashForecastReport camt.042.001.04 – By Country"]
content_origin: "source-transcription"
---

# FundDetailedEstimatedCashForecastReport camt.042.001.04 – By Country

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Fund Cash Forecast  / FundDetailedEstimatedCashForecastReport camt.042.001.04 – By Country.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2009** FundDetailedEstimatedCashForecastReport camt.042.001.04 – By Country

**P2010** Description

**P2011** A FundDetailedEstimatedCashForecastReport message is sent to report the cash-flow movements of financial instrument ISIN BE1234567890 for trade date 16 January 2015. As it is an estimated cash flow report, the estimated amounts are based on the price of the previous trade date, 15 January 2015. This report does not contain an exceptional net cash flow. In this report, the cash forecasts are sorted by country.

**P2012** CASH MOVEMENTS FOR BELGIUM

**P2013** The cash-in flows from Belgium for settlement date 19 January 2015 are the result of switch and subscription orders for 1,000 units for an estimated total cash-in amount of EUR 1,000,000. The 1000 units are broken down as follows: 600 units were the result of a switch-in and the original switch order was placed as units. The remaining 400 units were the result of a subscription and the original subscription order was placed as an amount of money.

**P2014** The cash-out flows from Belgium for settlement date 19 January 2015 are the result of switch and redemption orders for 1,450 units for an estimated total cash-out amount of EUR 1,450,000. The 1,450 units are broken down as follows: 1000 units were the result of a switch-out. The remaining 450 units were the result of a redemption.

**P2015** CASH MOVEMENTS FOR LUXEMBOURG

**P2016** The cash-in flows from Luxembourg for settlement date 19 January 2015 are the result of switch and subscription orders for 80,000 units for an estimated total cash-in amount of EUR 80,000,000. The amount of EUR 80,000,000 are broken down as follows: EUR 70,000,000 comes from subscriptions, the original order was placed as cash. The remaining EUR 10,000,000 comes from switch-in orders, the original order was placed as cash.

**P2017** The cash-out flows from Luxembourg for settlement date 19 January 2015 are the result of the redemption of 25,000 units for an estimated total cash-out amount of EUR 25,000,000.

**P2018** Message Instance

**P2019** <FndDtldEstmtdCshFcstRpt>

**P2020** 	<MsgId>

**P2021** 		<Id>87AC543</Id>

**P2022** 		<CreDtTm>2015-01-16T16:50:00</CreDtTm>

**P2023** 	</MsgId>

**P2024** 	<MsgPgntn>

**P2025** 		<PgNb>1</PgNb>

**P2026** 		<LastPgInd>true</LastPgInd>

**P2027** 	</MsgPgntn>

**P2028** 	<EstmtdFndCshFcstDtls>

**P2029** 		<Id>FCF0008</Id>

**P2030** 		<TradDtTm>

**P2031** 			<Dt>2015-01-16</Dt>

**P2032** 		</TradDtTm>

**P2033** 		<FinInstrmDtls>

**P2034** 			<Id>

**P2035** 				<ISIN>BE1234567890</ISIN>

**P2036** 			</Id>

**P2037** 			<DualFndInd>false</DualFndInd>

**P2038** 		</FinInstrmDtls>

**P2039** 		<XcptnlNetCshFlowInd>false</XcptnlNetCshFlowInd>

**P2040** 	<BrkdwnByCtry>

**P2041** 		<Ctry>BE</Ctry>

**P2042** 			<CshInFcst>

**P2043** 				<CshSttlmDt>2015-01-19</CshSttlmDt>

**P2044** 				<SubTtlAmt Ccy="EUR">1000000</SubTtlAmt>

**P2045** 				<SubTtlUnitsNb>

**P2046** 					<Unit>1000</Unit>

**P2047** 				</SubTtlUnitsNb>

**P2048** 				<CshInBrkdwnDtls>

**P2049** 					<UnitsNb>

**P2050** 						<Unit>600</Unit>

**P2051** 					</UnitsNb>

**P2052** 					<InvstmtFndTxInTp>

**P2053** 						<Cd>SWII</Cd>

**P2054** 					</InvstmtFndTxInTp>

**P2055** 					<OrgnlOrdrQtyTp>

**P2056** 						<Cd>UNIT</Cd>

**P2057** 					</OrgnlOrdrQtyTp>

**P2058** 				</CshInBrkdwnDtls>

**P2059** 				<CshInBrkdwnDtls>

**P2060** 					<UnitsNb>

**P2061** 						<Unit>400</Unit>

**P2062** 					</UnitsNb>

**P2063** 					<InvstmtFndTxInTp>

**P2064** 						<Cd>SUBS</Cd>

**P2065** 					</InvstmtFndTxInTp>

**P2066** 					<OrgnlOrdrQtyTp>

**P2067** 						<Cd>CASH</Cd>

**P2068** 					</OrgnlOrdrQtyTp>

**P2069** 				</CshInBrkdwnDtls>

**P2070** 			</CshInFcst>

**P2071** 			<CshOutFcst>

**P2072** 				<CshSttlmDt>2015-01-19</CshSttlmDt>

**P2073** 				<SubTtlAmt Ccy="EUR">1450000</SubTtlAmt>

**P2074** 				<SubTtlUnitsNb>

**P2075** 					<Unit>1450</Unit>

**P2076** 				</SubTtlUnitsNb>

**P2077** 				<CshOutBrkdwnDtls>

**P2078** 					<UnitsNb>

**P2079** 						<Unit>1000</Unit>

**P2080** 					</UnitsNb>

**P2081** 					<InvstmtFndTxOutTp>

**P2082** 						<Cd>SWIO</Cd>

**P2083** 					</InvstmtFndTxOutTp>

**P2084** 					<OrgnlOrdrQtyTp>

**P2085** 						<Cd>UNIT</Cd>

**P2086** 					</OrgnlOrdrQtyTp>

**P2087** 				</CshOutBrkdwnDtls>

**P2088** 				<CshOutBrkdwnDtls>

**P2089** 					<UnitsNb>

**P2090** 						<Unit>450</Unit>

**P2091** 					</UnitsNb>

**P2092** 					<InvstmtFndTxOutTp>

**P2093** 						<Cd>REDM</Cd>

**P2094** 					</InvstmtFndTxOutTp>

**P2095** 					<OrgnlOrdrQtyTp>

**P2096** 						<Cd>UNIT</Cd>

**P2097** 					</OrgnlOrdrQtyTp>

**P2098** 				</CshOutBrkdwnDtls>

**P2099** 			</CshOutFcst>

**P2100** 		</BrkdwnByCtry>

**P2101** 		<BrkdwnByCtry>

**P2102** 			<Ctry>LU</Ctry>

**P2103** 			<CshInFcst>

**P2104** 				<CshSttlmDt>2015-01-19</CshSttlmDt>

**P2105** 				<SubTtlAmt Ccy="EUR">80000000</SubTtlAmt>

**P2106** 				<SubTtlUnitsNb>

**P2107** 					<Unit>80000</Unit>

**P2108** 				</SubTtlUnitsNb>

**P2109** 				<CshInBrkdwnDtls>

**P2110** 					<Amt Ccy="EUR">70000000</Amt>

**P2111** 					<InvstmtFndTxInTp>

**P2112** 						<Cd>SUBS</Cd>

**P2113** 					</InvstmtFndTxInTp>

**P2114** 					<OrgnlOrdrQtyTp>

**P2115** 						<Cd>CASH</Cd>

**P2116** 					</OrgnlOrdrQtyTp>

**P2117** 				</CshInBrkdwnDtls>

**P2118** 				<CshInBrkdwnDtls>

**P2119** 					<Amt Ccy="EUR">10000000</Amt>

**P2120** 					<InvstmtFndTxInTp>

**P2121** 						<Cd>SWII</Cd>

**P2122** 					</InvstmtFndTxInTp>

**P2123** 					<OrgnlOrdrQtyTp>

**P2124** 						<Cd>CASH</Cd>

**P2125** 					</OrgnlOrdrQtyTp>

**P2126** 				</CshInBrkdwnDtls>

**P2127** 			</CshInFcst>

**P2128** 			<CshOutFcst>

**P2129** 				<CshSttlmDt>2015-01-19</CshSttlmDt>

**P2130** 				<SubTtlAmt Ccy="EUR">25000000</SubTtlAmt>

**P2131** 				<SubTtlUnitsNb>

**P2132** 					<Unit>25000</Unit>

**P2133** 				</SubTtlUnitsNb>

**P2134** 			</CshOutFcst>

**P2135** 		</BrkdwnByCtry>

**P2136** 	</EstmtdFndCshFcstDtls>

**P2137** </FndDtldEstmtdCshFcstRpt>

