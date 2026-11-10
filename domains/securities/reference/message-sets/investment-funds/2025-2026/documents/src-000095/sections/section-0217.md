---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Fund Cash Forecast ", "FundConfirmedCashForecastReport camt.041.001.04 – 1"]
content_origin: "source-transcription"
---

# FundConfirmedCashForecastReport camt.041.001.04 – 1

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Fund Cash Forecast  / FundConfirmedCashForecastReport camt.041.001.04 – 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1924** FundConfirmedCashForecastReport camt.041.001.04 – 1

**P1925** Description

**P1926** A FundConfirmedCashForecastReport message is sent to report the cash-flow movements of financial instrument ISIN US1234567890, for trade date 16 January 2015. This report does not contain an exceptional net cash flow.

**P1927** The cash-in flows for settlement date 19 January 2015 are the result of the subscription to 1,000 units for a total cash-in amount of USD 10,000. 

**P1928** The cash-out flows for settlement date 19 January 2015 are the result of the redemption of 1,100 units for a total cash-out amount of USD 11,000.

**P1929** The estimated net cash amount going out of the fund is USD 1,000.

**P1930** Message Instance

**P1931** <FndConfdCshFcstRpt>

**P1932** 	<MsgId>

**P1933** 		<Id>22FB5436</Id>

**P1934** 		<CreDtTm>2015-01-16T16:45:00</CreDtTm>

**P1935** 	</MsgId>

**P1936** 	<MsgPgntn>

**P1937** 		<PgNb>1</PgNb>

**P1938** 		<LastPgInd>true</LastPgInd>

**P1939** 	</MsgPgntn>

**P1940** 	<FndCshFcstDtls>

**P1941** 		<Id>FCF0006</Id>

**P1942** 		<TradDtTm>

**P1943** 			<Dt>2015-01-16</Dt>

**P1944** 		</TradDtTm>

**P1945** 		<FinInstrmDtls>

**P1946** 			<Id>

**P1947** 				<ISIN>US1234567890</ISIN>

**P1948** 			</Id>

**P1949** 			<DualFndInd>false</DualFndInd>

**P1950** 		</FinInstrmDtls>

**P1951** 		<XcptnlNetCshFlowInd>false</XcptnlNetCshFlowInd>

**P1952** 		<CshInFcstDtls>

**P1953** 			<CshSttlmDt>2015-01-19</CshSttlmDt>

**P1954** 			<SubTtlAmt Ccy="USD">10000</SubTtlAmt>

**P1955** 			<SubTtlUnitsNb>

**P1956** 				<Unit>1000</Unit>

**P1957** 			</SubTtlUnitsNb>

**P1958** 		</CshInFcstDtls>

**P1959** 		<CshOutFcstDtls>

**P1960** 			<CshSttlmDt>2015-01-19</CshSttlmDt>

**P1961** 			<SubTtlAmt Ccy="USD">11000</SubTtlAmt>

**P1962** 			<SubTtlUnitsNb>

**P1963** 				<Unit>1100</Unit>

**P1964** 			</SubTtlUnitsNb>

**P1965** 		</CshOutFcstDtls>

**P1966** 		<NetCshFcstDtls>

**P1967** 			<CshSttlmDt>2015-01-19</CshSttlmDt>

**P1968** 			<NetAmt Ccy="USD">1000</NetAmt>

**P1969** 			<FlowDrctn>OUTG</FlowDrctn>

**P1970** 		</NetCshFcstDtls>

**P1971** 	</FndCshFcstDtls>

**P1972** </FndConfdCshFcstRpt>

