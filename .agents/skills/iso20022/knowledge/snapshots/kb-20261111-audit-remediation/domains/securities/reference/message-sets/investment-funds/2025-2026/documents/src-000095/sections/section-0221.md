---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Fund Cash Forecast ", "FundDetailedConfirmedCashForecastReport camt.043.001.04 – By Party"]
content_origin: "source-transcription"
---

# FundDetailedConfirmedCashForecastReport camt.043.001.04 – By Party

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Fund Cash Forecast  / FundDetailedConfirmedCashForecastReport camt.043.001.04 – By Party.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P2297** FundDetailedConfirmedCashForecastReport camt.043.001.04 – By Party

**P2298** Description

**P2299** A FundDetailedConfirmedCashForecastReport message is sent to report the cash-flow movements of financial instrument ISIN FR1234567890 for trade date 29 January 2015. As it is a confirmed cash flow report, the amounts are based on the price of the trade date. This report does not contain an exceptional net cash flow. In this report, the cash forecasts are sorted by party.

**P2300** CASH MOVEMENTS FOR PEFILULL:

**P2301** The cash-in flows from PEFILULL for settlement date 3 February 2015 are the result of switch and subscription orders for 1,000 units for a total cash-in amount of EUR 1,000,000. The 1000 units are broken down as follows: 600 units were the result of a switch-in and the original switch order was placed as units. The remaining 400 units were the result of a subscription and the original subscription order was placed as an amount of money.

**P2302** The cash-out flows from PEFILULL for settlement date 3 February 2015 are the result of switch and redemption orders for 1,450 units for a total cash-out amount of EUR 1,450,000. The 1,450 units are broken down as follows: 1000 units were the result of a switch-out and the original switch order was placed as cash. The remaining 450 units were the result of a redemption and the original order was placed as cash.

**P2303** CASH MOVEMENTS FOR BDAPLULL:

**P2304** The cash-in flows from BDAPLULL for settlement date 3 February 2015 are the result of switch and subscription orders for 80,000 units for a total cash-in amount of EUR 80,000,000. The amount of EUR 80,000,000 are broken down as follows: EUR 70,000,000 comes from subscriptions, , the original order was placed as cash. The remaining EUR 10,000,000 comes from switch-in orders, the original order was placed as cash.

**P2305** The cash-out flows from BDAPLULL for settlement date 3 February 2015 are the result of the redemption of 25,000 units for an estimated total cash-out amount of EUR 25,000,000.

**P2306** Message Instance

**P2307** <FndDtldConfdCshFcstRpt>

**P2308** 	<MsgId>

**P2309** 		<Id>56DA7623</Id>

**P2310** 		<CreDtTm>2015-01-29T16:55:30</CreDtTm>

**P2311** 	</MsgId>

**P2312** 	<MsgPgntn>

**P2313** 		<PgNb>1</PgNb>

**P2314** 		<LastPgInd>true</LastPgInd>

**P2315** 	</MsgPgntn>

**P2316** 	<FndCshFcstDtls>

**P2317** 		<Id>FCF012</Id>

**P2318** 		<TradDtTm>

**P2319** 			<Dt>2015-01-29</Dt>

**P2320** 		</TradDtTm>

**P2321** 		<FinInstrmDtls>

**P2322** 			<Id>

**P2323** 				<ISIN>FR1234567890</ISIN>

**P2324** 			</Id>

**P2325** 			<DualFndInd>false</DualFndInd>

**P2326** 		</FinInstrmDtls>

**P2327** 		<XcptnlNetCshFlowInd>false</XcptnlNetCshFlowInd>

**P2328** 		<BrkdwnByPty>

**P2329** 			<Pty>

**P2330** 				<OwnrId>

**P2331** 					<BICOrBEI>PEFILULL</BICOrBEI>

**P2332** 				</OwnrId>

**P2333** 			</Pty>

**P2334** 			<CshInFcst>

**P2335** 				<CshSttlmDt>2015-02-03</CshSttlmDt>

**P2336** 				<SubTtlAmt Ccy="EUR">1000000</SubTtlAmt>

**P2337** 				<SubTtlUnitsNb>

**P2338** 					<Unit>1000</Unit>

**P2339** 				</SubTtlUnitsNb>

**P2340** 				<CshInBrkdwnDtls>

**P2341** 					<UnitsNb>

**P2342** 						<Unit>600</Unit>

**P2343** 					</UnitsNb>

**P2344** 					<InvstmtFndTxInTp>

**P2345** 						<Cd>SWII</Cd>

**P2346** 					</InvstmtFndTxInTp>

**P2347** 					<OrgnlOrdrQtyTp>

**P2348** 						<Cd>UNIT</Cd>

**P2349** 					</OrgnlOrdrQtyTp>

**P2350** 				</CshInBrkdwnDtls>

**P2351** 				<CshInBrkdwnDtls>

**P2352** 					<UnitsNb>

**P2353** 						<Unit>400</Unit>

**P2354** 					</UnitsNb>

**P2355** 					<InvstmtFndTxInTp>

**P2356** 						<Cd>SUBS</Cd>

**P2357** 					</InvstmtFndTxInTp>

**P2358** 					<OrgnlOrdrQtyTp>

**P2359** 						<Cd>CASH</Cd>

**P2360** 					</OrgnlOrdrQtyTp>

**P2361** 				</CshInBrkdwnDtls>

**P2362** 			</CshInFcst>

**P2363** 			<CshOutFcst>

**P2364** 				<CshSttlmDt>2015-02-03</CshSttlmDt>

**P2365** 				<SubTtlAmt Ccy="EUR">1450000</SubTtlAmt>

**P2366** 				<SubTtlUnitsNb>

**P2367** 					<Unit>1450</Unit>

**P2368** 				</SubTtlUnitsNb>

**P2369** 				<CshOutBrkdwnDtls>

**P2370** 					<UnitsNb>

**P2371** 						<Unit>1000</Unit>

**P2372** 					</UnitsNb>

**P2373** 					<InvstmtFndTxOutTp>

**P2374** 						<Cd>SWIO</Cd>

**P2375** 					</InvstmtFndTxOutTp>

**P2376** 					<OrgnlOrdrQtyTp>

**P2377** 						<Cd>CASH</Cd>

**P2378** 					</OrgnlOrdrQtyTp>

**P2379** 				</CshOutBrkdwnDtls>

**P2380** 				<CshOutBrkdwnDtls>

**P2381** 					<UnitsNb>

**P2382** 						<Unit>450</Unit>

**P2383** 					</UnitsNb>

**P2384** 					<InvstmtFndTxOutTp>

**P2385** 						<Cd>REDM</Cd>

**P2386** 					</InvstmtFndTxOutTp>

**P2387** 					<OrgnlOrdrQtyTp>

**P2388** 						<Cd>CASH</Cd>

**P2389** 					</OrgnlOrdrQtyTp>

**P2390** 				</CshOutBrkdwnDtls>

**P2391** 			</CshOutFcst>

**P2392** 		</BrkdwnByPty>

**P2393** 			<BrkdwnByPty>

**P2394** 				<Pty>

**P2395** 					<OwnrId>

**P2396** 						<BICOrBEI>BDAPLULL</BICOrBEI>

**P2397** 					</OwnrId>

**P2398** 				</Pty>

**P2399** 				<CshInFcst>

**P2400** 					<CshSttlmDt>2015-02-03</CshSttlmDt>

**P2401** 					<SubTtlAmt Ccy="EUR">80000000</SubTtlAmt>

**P2402** 					<SubTtlUnitsNb>

**P2403** 						<Unit>80000</Unit>

**P2404** 					</SubTtlUnitsNb>

**P2405** 					<CshInBrkdwnDtls>

**P2406** 						<Amt Ccy="EUR">70000000</Amt>

**P2407** 						<InvstmtFndTxInTp>

**P2408** 							<Cd>SUBS</Cd>

**P2409** 						</InvstmtFndTxInTp>

**P2410** 						<OrgnlOrdrQtyTp>

**P2411** 							<Cd>CASH</Cd>

**P2412** 						</OrgnlOrdrQtyTp>

**P2413** 					</CshInBrkdwnDtls>

**P2414** 					<CshInBrkdwnDtls>

**P2415** 						<Amt Ccy="EUR">10000000</Amt>

**P2416** 						<InvstmtFndTxInTp>

**P2417** 							<Cd>SWII</Cd>

**P2418** 						</InvstmtFndTxInTp>

**P2419** 						<OrgnlOrdrQtyTp>

**P2420** 							<Cd>CASH</Cd>

**P2421** 						</OrgnlOrdrQtyTp>

**P2422** 					</CshInBrkdwnDtls>

**P2423** 				</CshInFcst>

**P2424** 				<CshOutFcst>

**P2425** 					<CshSttlmDt>2015-02-03</CshSttlmDt>

**P2426** 					<SubTtlAmt Ccy="EUR">25000000</SubTtlAmt>

**P2427** 					<SubTtlUnitsNb>

**P2428** 						<Unit>25000</Unit>

**P2429** 					</SubTtlUnitsNb>

**P2430** 				</CshOutFcst>

**P2431** 			</BrkdwnByPty>

**P2432** 	</FndCshFcstDtls>

**P2433** </FndDtldConfdCshFcstRpt>

