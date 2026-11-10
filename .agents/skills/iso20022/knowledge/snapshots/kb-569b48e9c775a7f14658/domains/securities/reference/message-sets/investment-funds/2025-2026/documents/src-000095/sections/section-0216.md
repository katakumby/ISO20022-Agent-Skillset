---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Fund Cash Forecast ", "FundEstimatedCashForecastReport camt.040.001.04 – 2"]
content_origin: "source-transcription"
---

# FundEstimatedCashForecastReport camt.040.001.04 – 2

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Fund Cash Forecast  / FundEstimatedCashForecastReport camt.040.001.04 – 2.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1841** FundEstimatedCashForecastReport camt.040.001.04 – 2

**P1842** Description

**P1843** A FundDetailedEstimatedCashForecastReport message is sent to report the cash-flow movements of share class ISIN LU1234567890 of the fund ‘AB Ethical Fund’. The currency of the share class is EUR. The currency of the fund is USD. The estimated total NAV of the fund is USD 3,000,000. The cash flow as an estimated percentage of the total NAV of the main fund is 0.03%.

**P1844** As the report is an estimated report, the cash amounts are based on the price of the previous trade date, 16 January 2015. The next trade date is 23 January 2015. 

**P1845** The estimated total NAV of the share class is EUR 2,000,000. 

**P1846** The price (of the previous trade date) is EUR 10.

**P1847** The cash flow as an estimated percentage of the total NAV of the share class is 0.35%.

**P1848** Cash–In Details

**P1849** The cash-in for settlement date 20 January 2015 is EUR 7,000 and the number of units is 700. The estimated amount of cash expected from orders placed in units is EUR 2000 and the estimated amount of cash from orders placed in cash is EUR 5000.

**P1850** Cash-Out Details

**P1851** The cash-out for settlement date 20 January 2015 is EUR 2,500 and the number of units is 250.

**P1852** Net Details

**P1853** The estimated net cash amount coming into the fund, for settlement date 20 January 2015, is EUR 3,500 and the net number of units is 350. 

**P1854** Message Instance

**P1855** <FndEstmtdCshFcstRpt>

**P1856** 	<MsgId>

**P1857** 		<Id>412AC7676</Id>

**P1858** 		<CreDtTm>2015-01-19T11:30:00</CreDtTm>

**P1859** 	</MsgId>

**P1860** 	<MsgPgntn>

**P1861** 		<PgNb>1</PgNb>

**P1862** 		<LastPgInd>true</LastPgInd>

**P1863** 	</MsgPgntn>

**P1864** 	<FndOrSubFndDtls>

**P1865** 		<Nm>AB Ethical Fund</Nm>

**P1866** 		<Ccy>USD</Ccy>

**P1867** 		<EstmtdTtlNAV Ccy="USD">3000000</EstmtdTtlNAV>

**P1868** 		<EstmtdPctgOfFndTtlNAV>0.03</EstmtdPctgOfFndTtlNAV>

**P1869** 	</FndOrSubFndDtls>

**P1870** 	<EstmtdFndCshFcstDtls>

**P1871** 		<Id>FCF0004</Id>

**P1872** 		<TradDtTm>

**P1873** 			<Dt>2015-01-23</Dt>

**P1874** 		</TradDtTm>

**P1875** 		<PrvsTradDtTm>

**P1876** 			<Dt>2015-01-16</Dt>

**P1877** 		</PrvsTradDtTm>

**P1878** 		<FinInstrmDtls>

**P1879** 			<Id>

**P1880** 				<ISIN>LU1234567890</ISIN>

**P1881** 			</Id>

**P1882** 			<DualFndInd>true</DualFndInd>

**P1883** 		</FinInstrmDtls>

**P1884** 		<EstmtdTtlNAV Ccy="EUR">2000000</EstmtdTtlNAV>

**P1885** 		<InvstmtCcy>EUR</InvstmtCcy>

**P1886** 		<XcptnlNetCshFlowInd>true</XcptnlNetCshFlowInd>

**P1887** 		<Pric>

**P1888** 			<PricTp>

**P1889** 				<Cd>NAVL</Cd>

**P1890** 			</PricTp>

**P1891** 			<Val>

**P1892** 				<Amt Ccy="EUR">10</Amt>

**P1893** 			</Val>

**P1894** 		</Pric>

**P1895** 		<EstmtdPctgOfShrClssTtlNAV>0.35</EstmtdPctgOfShrClssTtlNAV>

**P1896** 		<EstmtdCshInFcstDtls>

**P1897** 			<CshSttlmDt>2015-01-20</CshSttlmDt>

**P1898** 			<SubTtlAmt Ccy="EUR">7000</SubTtlAmt>

**P1899** 			<SubTtlUnitsNb>

**P1900** 				<Unit>700</Unit>

**P1901** 			</SubTtlUnitsNb>

**P1902** 			<AddtlBal>

**P1903** 				<TtlCshFrUnitOrdrs Ccy="EUR">2000</TtlCshFrUnitOrdrs>

**P1904** 				<TtlCshFrCshOrdrs Ccy="EUR">5000</TtlCshFrCshOrdrs>

**P1905** 			</AddtlBal>

**P1906** 		</EstmtdCshInFcstDtls>

**P1907** 		<EstmtdCshOutFcstDtls>

**P1908** 			<CshSttlmDt>2015-01-20</CshSttlmDt>

**P1909** 			<SubTtlAmt Ccy="EUR">2500</SubTtlAmt>

**P1910** 			<SubTtlUnitsNb>

**P1911** 				<Unit>250</Unit>

**P1912** 			</SubTtlUnitsNb>

**P1913** 		</EstmtdCshOutFcstDtls>

**P1914** 		<EstmtdNetCshFcstDtls>

**P1915** 			<CshSttlmDt>2015-01-20</CshSttlmDt>

**P1916** 			<NetAmt Ccy="EUR">3500</NetAmt>

**P1917** 			<NetUnitsNb>

**P1918** 				<Unit>350</Unit>

**P1919** 			</NetUnitsNb>

**P1920** 			<FlowDrctn>INCG</FlowDrctn>

**P1921** 		</EstmtdNetCshFcstDtls>

**P1922** 	</EstmtdFndCshFcstDtls>

**P1923** </FndEstmtdCshFcstRpt>

