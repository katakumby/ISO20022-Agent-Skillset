---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Fund Cash Forecast ", "FundEstimatedCashForecastReport camt.040.001.04 – 1"]
content_origin: "source-transcription"
---

# FundEstimatedCashForecastReport camt.040.001.04 – 1

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Fund Cash Forecast  / FundEstimatedCashForecastReport camt.040.001.04 – 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1784** FundEstimatedCashForecastReport camt.040.001.04 – 1

**P1785** Description

**P1786** A FundEstimatedCashForecastReport message is sent to report the cash-flow movements of financial instrument ISIN SG1234567890, fund name ABC, for trade date 9 January 2015. 

**P1787** As it is an estimated cash forecast report, the estimated amounts are based on the price of the previous trade date, 08 January 2015. This report does not contain an exceptional net cash flow.

**P1788** The cash-in flows for settlement date 12 January 2015 are the result of the subscription to 2,000 units for an estimated total cash-in amount of SGD 40,000. 

**P1789** The cash-out flows for settlement date 12 January 2015 are the result of the redemption of 500 units for an estimated total cash-out amount of SGD 10,000. 

**P1790** The estimated net cash amount coming into the fund is SGD 30,000.

**P1791** Message Instance

**P1792** <FndEstmtdCshFcstRpt>

**P1793** 	<MsgId>

**P1794** 		<Id>123DA5409</Id>

**P1795** 		<CreDtTm>2015-01-08T16:45:00</CreDtTm>

**P1796** 	</MsgId>

**P1797** 	<MsgPgntn>

**P1798** 		<PgNb>1</PgNb>

**P1799** 		<LastPgInd>true</LastPgInd>

**P1800** 	</MsgPgntn>

**P1801** 	<EstmtdFndCshFcstDtls>

**P1802** 		<Id>FCF0002</Id>

**P1803** 		<TradDtTm>

**P1804** 			<Dt>2015-01-09</Dt>

**P1805** 		</TradDtTm>

**P1806** 		<PrvsTradDtTm>

**P1807** 			<Dt>2015-01-08</Dt>

**P1808** 		</PrvsTradDtTm>

**P1809** 		<FinInstrmDtls>

**P1810** 			<Id>

**P1811** 				<ISIN>SG1234567890</ISIN>

**P1812** 			</Id>

**P1813** 		<Nm>Fund ABC</Nm>

**P1814** 			<DualFndInd>false</DualFndInd>

**P1815** 		</FinInstrmDtls>

**P1816** 		<XcptnlNetCshFlowInd>false</XcptnlNetCshFlowInd>

**P1817** 		<EstmtdCshInFcstDtls>

**P1818** 			<CshSttlmDt>2015-01-12</CshSttlmDt>

**P1819** 			<SubTtlAmt Ccy="SGD">40000</SubTtlAmt>

**P1820** 			<SubTtlUnitsNb>

**P1821** 				<Unit>2000</Unit>

**P1822** 			</SubTtlUnitsNb>

**P1823** 		</EstmtdCshInFcstDtls>

**P1824** 		<EstmtdCshOutFcstDtls>

**P1825** 			<CshSttlmDt>2015-01-12</CshSttlmDt>

**P1826** 			<SubTtlAmt Ccy="SGD">10000</SubTtlAmt>

**P1827** 			<SubTtlUnitsNb>

**P1828** 				<Unit>500</Unit>

**P1829** 			</SubTtlUnitsNb>

**P1830** 		</EstmtdCshOutFcstDtls>

**P1831** 		<EstmtdNetCshFcstDtls>

**P1832** 			<CshSttlmDt>2015-01-12</CshSttlmDt>

**P1833** 			<NetAmt Ccy="SGD">30000</NetAmt>

**P1834** 			<NetUnitsNb>

**P1835** 				<Unit>1500</Unit>

**P1836** 			</NetUnitsNb>

**P1837** 			<FlowDrctn>INCG</FlowDrctn>

**P1838** 		</EstmtdNetCshFcstDtls>

**P1839** 	</EstmtdFndCshFcstDtls>

**P1840** </FndEstmtdCshFcstRpt>

