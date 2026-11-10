---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Fund Cash Forecast ", "FundConfirmedCashForecastReport camt.041.001.04 – 2"]
content_origin: "source-transcription"
---

# FundConfirmedCashForecastReport camt.041.001.04 – 2

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Fund Cash Forecast  / FundConfirmedCashForecastReport camt.041.001.04 – 2.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1973** FundConfirmedCashForecastReport camt.041.001.04 – 2

**P1974** Description

**P1975** A FundConfirmedCashForecastReport message is sent to report the cash-flow movements of two funds. 

**P1976** Fund 1	

**P1977** ‘AB Ethical Fund’, for trade date 3 March 2015. The currency of the fund is USD. The total NAV is USD 3,000,000. The previous total NAV is USD 2,080,000.

**P1978** Fund 2	

**P1979** ‘Green Fund’, for trade date 4 March 2015. The currency of the fund is EUR. The total NAV is EUR 2,500,000. The previous total NAV is EUR 1,900,000

**P1980** Message Instance

**P1981** <FndConfdCshFcstRpt>

**P1982** 	<MsgId>

**P1983** 		<Id>32DC34C</Id>

**P1984** 		<CreDtTm>2015-03-05T09:30:10</CreDtTm>

**P1985** 	</MsgId>

**P1986** 	<MsgPgntn>

**P1987** 		<PgNb>1</PgNb>

**P1988** 		<LastPgInd>true</LastPgInd>

**P1989** 	</MsgPgntn>

**P1990** 	<FndOrSubFndDtls>

**P1991** 		<Nm>AB Ethical Fund</Nm>

**P1992** 		<Ccy>USD</Ccy>

**P1993** 		<TradDtTm>

**P1994** 			<Dt>2015-03-03</Dt>

**P1995** 		</TradDtTm>

**P1996** 		<TtlNAV Ccy="USD">3000000</TtlNAV>

**P1997** 		<PrvsTtlNAV Ccy="USD">2080000</PrvsTtlNAV>

**P1998** 	</FndOrSubFndDtls>

**P1999** 	<FndOrSubFndDtls>

**P2000** 		<Nm>Green Fund</Nm>

**P2001** 		<Ccy>EUR</Ccy>

**P2002** 		<TradDtTm>

**P2003** 			<Dt>2015-03-04</Dt>

**P2004** 		</TradDtTm>

**P2005** 		<TtlNAV Ccy="EUR">2500000</TtlNAV>

**P2006** 		<PrvsTtlNAV Ccy="EUR">1900000</PrvsTtlNAV>

**P2007** 	</FndOrSubFndDtls>

**P2008** </FndConfdCshFcstRpt>

